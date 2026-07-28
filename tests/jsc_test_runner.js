/* Browser mocks + smoke tests for ANDM quiz init (JavaScriptCore). */
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

globalThis.location = { href: `file://${ROOT}index.html`, pathname: '/amazon-ndm/index.html', origin: 'file://', search: '' };

const elements = {};
function makeEl(id) {
  return {
    id,
    textContent: '',
    innerHTML: '',
    className: '',
    classList: {
      _c: new Set(),
      add(...a) { a.forEach((x) => this._c.add(x)); },
      remove(...a) { a.forEach((x) => this._c.delete(x)); },
      toggle(x, force) {
        if (force === true) this._c.add(x);
        else if (force === false) this._c.delete(x);
        else if (this._c.has(x)) this._c.delete(x);
        else this._c.add(x);
      },
    },
    addEventListener() {},
    onclick: null,
    disabled: false,
    dataset: {},
  };
}

globalThis.document = {
  readyState: 'loading',
  getElementById(id) {
    if (!elements[id]) elements[id] = makeEl(id);
    return elements[id];
  },
  addEventListener(event, fn) {
    if (event === 'DOMContentLoaded') fn();
  },
  querySelector(selector) {
    if (selector.includes('quiz/js/loader.js')) {
      return { src: `file://${ROOT}quiz/js/loader.js` };
    }
    return null;
  },
  querySelectorAll() { return []; },
  documentElement: { scrollTop: 0 },
};

globalThis.window = globalThis;
globalThis.fetch = function fetch(url) {
  let path = String(url);
  const marker = 'quiz/data/';
  const idx = path.indexOf(marker);
  if (idx >= 0) {
    path = ROOT + path.slice(idx);
  }
  path = path.replace(/^file:\/\//, '');
  const body = readFile(path);
  return Promise.resolve({
    ok: true,
    status: 200,
    json() { return Promise.resolve(JSON.parse(body)); },
  });
};

function fail(msg) {
  print(`FAIL: ${msg}`);
  quit(1);
}

function assert(cond, msg) {
  if (!cond) fail(msg);
}

load(`${ROOT}quiz/js/loader.js`);
load(`${ROOT}quiz/js/storage.js`);
load(`${ROOT}quiz/js/engine.js`);
load(`${ROOT}quiz/js/format.js`);
load(`${ROOT}quiz/js/ui.js`);
load(`${ROOT}quiz/js/app.js`);

assert(typeof QuizLoader.getAllQuestions === 'function', 'loader');
QuizLoader.getAllQuestions().then((all) => {
  assert(all.length >= 500, `expected >=500 questions, got ${all.length}`);
  QuizEngine.init(all, new Set(['LP-CORE']), new Set(all.filter((q) => q.module === 'LP-CORE').map((q) => q.id)));
  const q = QuizEngine.pickRandom();
  assert(q && q.module === 'LP-CORE', 'engine picks LP-CORE');
  print('PASS: ANDM quiz init smoke tests');
}).catch((err) => fail(err.stack || String(err)));
