const Recognition = (() => {
  let model = null;
  let loadingPromise = null;

  // MobileNet returns labels like "acoustic guitar", "violin", "grand piano", etc.
  const LABEL_MAP = {
    "acoustic guitar": "guitar",
    "electric guitar": "guitar",
    "guitar pick": "guitar",
    "banjo": "banjo",
    "violin": "violin",
    "fiddle": "violin",
    "cello": "cello",
    "harp": "harp",
    "grand piano": "piano",
    "upright piano": "piano",
    "piano": "piano",
    "flute": "flute",
    "cornet": "trumpet",
    "trumpet": "trumpet",
    "trombone": "trumpet",
    "french horn": "trumpet",
    "sax": "saxophone",
    "saxophone": "saxophone",
    "drum": "drum",
    "steel drum": "drum",
    "drumstick": "drum",
    "accordion": "accordion",
    "harmonica": "harmonica",
    "mouth organ": "harmonica",
    "marimba": "marimba",
    "xylophone": "marimba",
    "organ": "organ",
    "pipe organ": "organ",
    "maraca": "maracas",
  };

  async function loadModel(onProgress) {
    if (typeof mobilenet === "undefined" || typeof tf === "undefined") {
      throw new Error(
        "Recognition model failed to load (no internet connection to the model CDN). " +
        "Please select your instrument manually below."
      );
    }
    if (model) return model;
    if (loadingPromise) return loadingPromise;
    loadingPromise = mobilenet.load({ version: 2, alpha: 1.0 }).then((m) => {
      model = m;
      return m;
    });
    return loadingPromise;
  }

  function mapPredictionsToInstrument(predictions) {
    // predictions: [{className, probability}, ...] sorted desc
    for (const pred of predictions) {
      const labels = pred.className.split(",").map((s) => s.trim().toLowerCase());
      for (const label of labels) {
        if (LABEL_MAP[label]) {
          return { instrumentId: LABEL_MAP[label], confidence: pred.probability, matchedLabel: label };
        }
      }
      // Fuzzy contains-match as a fallback
      for (const key of Object.keys(LABEL_MAP)) {
        if (labels.some((l) => l.includes(key) || key.includes(l))) {
          return { instrumentId: LABEL_MAP[key], confidence: pred.probability, matchedLabel: key };
        }
      }
    }
    return null;
  }

  async function classify(imgElement) {
    const m = await loadModel();
    const predictions = await m.classify(imgElement, 10);
    const match = mapPredictionsToInstrument(predictions);
    return { match, predictions };
  }

  return { loadModel, classify };
})();
