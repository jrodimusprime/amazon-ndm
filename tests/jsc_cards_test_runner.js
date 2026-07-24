/* Queue + engine smoke tests for ANDM flash cards (JavaScriptCore). */
const ROOT = '/Users/jared/code/ANDM/';

if (typeof URL === 'undefined') {
  globalThis.URL = function URL(href, base) {
    const join = (root, rel) => {
      if (rel.startsWith('http://') || rel.startsWith('https://') || rel.startsWith('file://')) {
        return rel;
      }
      const basePath = root.replace(/^file:\/\//, '').replace(/\/[^/]*$/, '/');
      if (rel.startsWith('/')) return `file://${rel}`;
      if (rel === '..') return root.replace(/\/[^/]+\/?$/, '/');
      if (rel === '../..') return root.replace(/\/[^/]+\/?$/, '/').replace(/\/[^/]+\/?$/, '/');
      return `${basePath}${rel}`;
    };
    this.href = base ? join(String(base), String(href)) : String(href);
    this.toString = () => this.href;
  };
  URL.prototype = {};
}

const mockStorage = {};
globalThis.localStorage = {
  getItem(k) { return mockStorage[k] ?? null; },
  setItem(k, v) { mockStorage[k] = v; },
  removeItem(k) { delete mockStorage[k]; },
};

globalThis.location = {
  href: `file://${ROOT}cards/index.html`,
  pathname: '/amazon-ndm/cards/',
  origin: 'file://',
  search: '',
};

globalThis.document = {
  readyState: 'complete',
  getElementById() { return null; },
  addEventListener() {},
  querySelector(selector) {
    if (selector.includes('cards-loader.js')) {
      return { src: `file://${ROOT}quiz/js/cards-loader.js` };
    }
    return null;
  },
  querySelectorAll() { return []; },
};

function fail(msg) {
  print(`FAIL: ${msg}`);
  quit(1);
}

function assert(cond, msg) {
  if (!cond) fail(msg);
}

load(`${ROOT}quiz/js/cards-loader.js`);
load(`${ROOT}quiz/js/cards-storage.js`);
load(`${ROOT}quiz/js/cards-engine.js`);

assert(CardsEngine.insertIndexForRating(10, 1) === 1, 'rating 1');
assert(CardsEngine.insertIndexForRating(10, 3) === 10, 'rating 3');
assert(CardsEngine.insertIndexForRating(10, 4) === null, 'rating 4');

const sample = [
  { id: 'A', deck: 'core', front: 'q1', back: 'a1' },
  { id: 'B', deck: 'core', front: 'q2', back: 'a2' },
  { id: 'C', deck: 'core', front: 'q3', back: 'a3' },
  { id: 'D', deck: 'core', front: 'q4', back: 'a4' },
];
CardsEngine.init(sample);
CardsEngine.advance();
CardsEngine.flip();
CardsEngine.rate(4);
assert(CardsEngine.masteredCount() === 1, 'mastered');
print('PASS cards engine smoke');
