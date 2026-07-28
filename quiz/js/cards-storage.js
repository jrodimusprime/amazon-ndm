const CardsStorage = (() => {
  const BASE_KEY = 'andm-cards-v1';
  let activeDeck = 'core';

  function storageKey(deckId) {
    const id = deckId || activeDeck || 'core';
    return id === 'core' ? BASE_KEY : `${BASE_KEY}:${id}`;
  }

  function setActiveDeck(deckId) {
    activeDeck = deckId || 'core';
  }

  function getActiveDeck() {
    return activeDeck;
  }

  function load() {
    try {
      return JSON.parse(localStorage.getItem(storageKey()) || '{}');
    } catch {
      return {};
    }
  }

  function save(data) {
    data.updatedAt = Date.now();
    localStorage.setItem(storageKey(), JSON.stringify(data));
  }

  function getState() {
    const data = load();
    return {
      ratings: data.ratings || {},
      mastered: Array.isArray(data.mastered) ? data.mastered : [],
      queue: Array.isArray(data.queue) ? data.queue : null,
      faceMode: data.faceMode === 'answer' ? 'answer' : 'question',
    };
  }

  function setState(partial) {
    const data = load();
    if (partial.ratings !== undefined) data.ratings = partial.ratings;
    if (partial.mastered !== undefined) data.mastered = [...partial.mastered];
    if (partial.queue !== undefined) data.queue = [...partial.queue];
    if (partial.faceMode !== undefined) data.faceMode = partial.faceMode;
    save(data);
  }

  function clearProgress() {
    const faceMode = getState().faceMode;
    localStorage.removeItem(storageKey());
    if (faceMode === 'answer') {
      setState({ faceMode: 'answer', ratings: {}, mastered: [], queue: null });
    }
  }

  return {
    getState,
    setState,
    clearProgress,
    load,
    setActiveDeck,
    getActiveDeck,
    BASE_KEY,
  };
})();
