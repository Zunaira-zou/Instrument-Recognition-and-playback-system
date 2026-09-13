(function () {
  const INSTRUMENTS = window.INSTRUMENTS_DATA.reduce((acc, inst) => {
    acc[inst.id] = inst;
    return acc;
  }, {});
  const ORDER = window.INSTRUMENTS_DATA.map((i) => i.id);

  const dropzone = document.getElementById("dropzone");
  const fileInput = document.getElementById("fileInput");
  const previewImage = document.getElementById("previewImage");
  const pedestalEmpty = document.getElementById("pedestalEmpty");

  const curatorIdle = document.getElementById("curatorIdle");
  const curatorLoading = document.getElementById("curatorLoading");
  const curatorResult = document.getElementById("curatorResult");
  const curatorManual = document.getElementById("curatorManual");

  const resultName = document.getElementById("resultName");
  const resultMeta = document.getElementById("resultMeta");
  const resultConfidence = document.getElementById("resultConfidence");
  const resultDesc = document.getElementById("resultDesc");
  const resultFact = document.getElementById("resultFact");
  const goToPlayBtn = document.getElementById("goToPlayBtn");
  const notRightBtn = document.getElementById("notRightBtn");
  const manualGrid = document.getElementById("manualGrid");

  const displayCase = document.getElementById("display-case");
  const caseInstrumentName = document.getElementById("caseInstrumentName");
  const caseInstrumentFamily = document.getElementById("caseInstrumentFamily");
  const caseTitle = document.getElementById("caseTitle");
  const caseSubtitle = document.getElementById("caseSubtitle");
  const placardStrip = document.getElementById("placardStrip");
  const sustainToggle = document.getElementById("sustainToggle");
  const stopAllBtn = document.getElementById("stopAllBtn");

  let currentInstrumentId = null;

  function showPanel(panel) {
    [curatorIdle, curatorLoading, curatorResult, curatorManual].forEach((p) => {
      p.hidden = p !== panel;
    });
  }

  // ----- Manual selection grid -----
  function buildManualGrid() {
    manualGrid.innerHTML = "";
    ORDER.forEach((id) => {
      const inst = INSTRUMENTS[id];
      const btn = document.createElement("button");
      btn.textContent = inst.display_name;
      btn.addEventListener("click", () => {
        showRecognitionResult(id, null);
      });
      manualGrid.appendChild(btn);
    });
  }
  buildManualGrid();

  notRightBtn.addEventListener("click", () => showPanel(curatorManual));

  // ----- Upload handling -----
  dropzone.addEventListener("click", () => fileInput.click());
  dropzone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropzone.classList.add("drag-over");
  });
  dropzone.addEventListener("dragleave", () => dropzone.classList.remove("drag-over"));
  dropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropzone.classList.remove("drag-over");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  });
  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) handleFile(e.target.files[0]);
  });

  function handleFile(file) {
    if (!file.type.startsWith("image/")) {
      alert("Please upload an image file (JPG or PNG).");
      return;
    }
    const url = URL.createObjectURL(file);
    previewImage.src = url;
    previewImage.hidden = false;
    pedestalEmpty.hidden = true;

    showPanel(curatorLoading);

    previewImage.onload = async () => {
      try {
        const { match, predictions } = await Recognition.classify(previewImage);
        if (match) {
          showRecognitionResult(match.instrumentId, match.confidence);
        } else {
          showNoMatch(false);
        }
      } catch (err) {
        console.error("Recognition error:", err);
        showNoMatch(true);
      }
    };
  }

  function showNoMatch(modelFailed) {
    showPanel(curatorManual);
    document.querySelectorAll(".manual-note").forEach((n) => n.remove());
    const note = document.createElement("p");
    note.className = "curator-msg manual-note";
    note.style.marginBottom = "12px";
    note.textContent = modelFailed
      ? "The curator's model couldn't load right now (check your internet connection), so please select the instrument manually:"
      : "We couldn't confidently match that to our collection. Please select the instrument manually:";
    manualGrid.parentElement.insertBefore(note, manualGrid);
  }

  function showRecognitionResult(instrumentId, confidence) {
    const inst = INSTRUMENTS[instrumentId];
    if (!inst) return;
    currentInstrumentId = instrumentId;

    resultName.textContent = inst.display_name;
    resultMeta.textContent = `${inst.family} · ${inst.origin}`;
    resultConfidence.textContent = confidence
      ? `Curator confidence: ${Math.round(confidence * 100)}%`
      : "Selected manually";
    resultDesc.textContent = inst.description;
    resultFact.textContent = `Did you know? ${inst.fun_fact}`;

    showPanel(curatorResult);
    loadDisplayCase(instrumentId);
  }

  goToPlayBtn.addEventListener("click", () => {
    displayCase.scrollIntoView({ behavior: "smooth", block: "start" });
  });

  // ----- Display case / playback -----
  function loadDisplayCase(instrumentId) {
    const inst = INSTRUMENTS[instrumentId];
    if (!inst) return;
    currentInstrumentId = instrumentId;

    displayCase.hidden = false;
    caseTitle.textContent = `${inst.display_name} — Display Case`;
    caseSubtitle.textContent = `Tap each placard to play its ${inst.play_label.toLowerCase()}. ${inst.notes.length} tones available.`;
    caseInstrumentName.textContent = inst.display_name;
    caseInstrumentFamily.textContent = inst.play_label;

    placardStrip.innerHTML = "";
    inst.notes.forEach((note, idx) => {
      const key = document.createElement("button");
      key.className = "note-key";
      key.textContent = note.label;
      key.dataset.idx = idx;

      const voiceKey = `${instrumentId}-${idx}`;

      const triggerStart = (e) => {
        e.preventDefault();
        AudioEngine.playNote(
          voiceKey,
          note.freq,
          inst.wave,
          inst.decay,
          sustainToggle.checked,
          inst.play_type
        );
        key.classList.add("playing");
      };
      const triggerEnd = () => {
        key.classList.remove("playing");
        if (sustainToggle.checked) AudioEngine.stopNote(voiceKey, false);
      };

      key.addEventListener("mousedown", triggerStart);
      key.addEventListener("mouseup", triggerEnd);
      key.addEventListener("mouseleave", triggerEnd);
      key.addEventListener("touchstart", triggerStart, { passive: false });
      key.addEventListener("touchend", triggerEnd);

      placardStrip.appendChild(key);
    });
  }

  stopAllBtn.addEventListener("click", () => {
    AudioEngine.stopAll();
    document.querySelectorAll(".note-key.playing").forEach((k) => k.classList.remove("playing"));
  });

  // ----- Collection grid click -> load straight into display case -----
  document.querySelectorAll(".collection-card").forEach((card) => {
    card.addEventListener("click", () => {
      const id = card.dataset.id;
      showRecognitionResult(id, null);
      displayCase.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // Pre-warm the model in the background so first classification is fast
  Recognition.loadModel().catch((e) => console.warn("Model preload failed:", e));
})();
