const CardsLoader = (() => {
  let baseUrl = null;

  function getDataBase() {
    if (baseUrl) return baseUrl;
    const script = document.querySelector('script[src*="quiz/js/cards-loader.js"]');
    if (script && script.src) {
      baseUrl = new URL('quiz/data/', new URL('../..', script.src)).href;
      return baseUrl;
    }
    const path = location.pathname.replace(/\/?index\.html$/, '').replace(/\/cards\/?$/, '/');
    const prefix = path.endsWith('/') ? path : `${path}/`;
    baseUrl = `${location.origin}${prefix}quiz/data/`;
    return baseUrl;
  }

  let cache = { registry: null, decks: {}, allCards: null };

  async function fetchJson(path) {
    const res = await fetch(`${getDataBase()}${path}`);
    if (!res.ok) {
      throw new Error(`Failed to load ${path} (${res.status})`);
    }
    return res.json();
  }

  async function loadRegistry() {
    if (cache.registry) return cache.registry;
    cache.registry = await fetchJson('cards.json');
    return cache.registry;
  }

  async function loadDeck(dataFile) {
    if (cache.decks[dataFile]) return cache.decks[dataFile];
    const data = await fetchJson(dataFile);
    cache.decks[dataFile] = data.cards || data;
    return cache.decks[dataFile];
  }

  function deckIdFromLocation(loc) {
    try {
      const params = new URLSearchParams((loc && loc.search) || '');
      const deck = (params.get('deck') || '').trim();
      return deck || 'core';
    } catch {
      return 'core';
    }
  }

  async function getCardsForDeck(deckId) {
    const registry = await loadRegistry();
    const decks = registry.decks || [];
    const id = deckId || 'core';
    let selected;
    if (id === 'all') {
      selected = decks;
    } else {
      selected = decks.filter((d) => d.id === id);
      if (!selected.length) {
        selected = decks.filter((d) => d.default) ;
      }
      if (!selected.length && decks.length) {
        selected = [decks[0]];
      }
    }
    const seen = new Set();
    const all = [];
    for (const deck of selected) {
      const cards = await loadDeck(deck.dataFile);
      for (const card of cards) {
        if (!card.id || seen.has(card.id)) continue;
        seen.add(card.id);
        all.push({ ...card, deck: card.deck || deck.id });
      }
    }
    return { cards: all, deckId: selected.length === 1 ? selected[0].id : id, title: selected.length === 1 ? selected[0].title : 'All decks' };
  }

  async function getAllCards() {
    if (cache.allCards) return cache.allCards;
    const { cards } = await getCardsForDeck('all');
    cache.allCards = cards;
    return cards;
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
    loadRegistry,
    getAllCards,
    getCardsForDeck,
    deckIdFromLocation,
    shuffle,
    getDataBase,
  };
})();
