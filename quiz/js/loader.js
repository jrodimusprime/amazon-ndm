const QuizLoader = (() => {
  let baseUrl = null;

  function getDataBase() {
    if (baseUrl) return baseUrl;
    const script = document.querySelector('script[src*="quiz/js/loader.js"]');
    if (script && script.src) {
      baseUrl = new URL('quiz/data/', new URL('../..', script.src)).href;
      return baseUrl;
    }
    const path = location.pathname.replace(/\/?index\.html$/, '');
    const prefix = path.endsWith('/') ? path : `${path}/`;
    baseUrl = `${location.origin}${prefix}quiz/data/`;
    return baseUrl;
  }

  let cache = { sections: null, supplemental: {}, allQuestions: null };

  async function fetchJson(path) {
    const res = await fetch(`${getDataBase()}${path}`);
    if (!res.ok) {
      throw new Error(`Failed to load ${path} (${res.status})`);
    }
    return res.json();
  }

  async function loadSections() {
    if (cache.sections) return cache.sections;
    cache.sections = await fetchJson('sections.json');
    return cache.sections;
  }

  async function loadSupplemental(file) {
    if (cache.supplemental[file]) return cache.supplemental[file];
    const data = await fetchJson(file);
    cache.supplemental[file] = data.questions || data;
    return cache.supplemental[file];
  }

  async function getModuleQuestions(moduleId) {
    const config = await loadSections();
    const mod = config.modules.find((m) => m.id === moduleId);
    if (!mod || !mod.dataFile) return [];
    return loadSupplemental(mod.dataFile);
  }

  async function getAllQuestions() {
    if (cache.allQuestions) return cache.allQuestions;
    const config = await loadSections();
    const seen = new Set();
    const all = [];
    for (const mod of config.modules) {
      const qs = await getModuleQuestions(mod.id);
      for (const q of qs) {
        if (!seen.has(q.id)) {
          seen.add(q.id);
          all.push({ ...q, module: q.module || mod.id });
        }
      }
    }
    cache.allQuestions = all;
    return all;
  }

  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  return {
    loadSections,
    getModuleQuestions,
    getAllQuestions,
    shuffle,
    getDataBase,
  };
})();
