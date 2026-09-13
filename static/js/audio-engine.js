const AudioEngine = (() => {
  let ctx = null;
  const activeVoices = new Map(); // key -> {osc, gain}

  function getCtx() {
    if (!ctx) {
      ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (ctx.state === "suspended") ctx.resume();
    return ctx;
  }

  /**
   * Play a note.
   * @param {string} key      unique id for this voice (e.g. note label)
   * @param {number} freq     frequency in Hz
   * @param {string} wave     oscillator type: sine|square|sawtooth|triangle
   * @param {number} decay    seconds for the note to fade out
   * @param {boolean} sustain if true, note holds until stopNote() is called
   * @param {string} playType "strings" | "keys" | "drum" affects envelope shape
   */
  function playNote(key, freq, wave, decay, sustain, playType) {
    const audioCtx = getCtx();
    stopNote(key, true);

    const osc = audioCtx.createOscillator();
    osc.type = wave || "sine";
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

    const gain = audioCtx.createGain();
    const now = audioCtx.currentTime;

    // Slight harmonic richness via a detuned second oscillator for strings
    let osc2 = null;
    if (playType === "strings") {
      osc2 = audioCtx.createOscillator();
      osc2.type = wave || "sawtooth";
      osc2.frequency.setValueAtTime(freq * 1.004, now);
    }

    const filter = audioCtx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(
      playType === "drum" ? freq * 3 : Math.min(freq * 6, 8000),
      now
    );

    osc.connect(filter);
    if (osc2) osc2.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);

    // Envelope shaping per instrument type
    gain.gain.setValueAtTime(0, now);
    if (playType === "drum") {
      gain.gain.linearRampToValueAtTime(0.55, now + 0.005);
      gain.gain.exponentialRampToValueAtTime(0.001, now + decay);
    } else if (playType === "keys") {
      gain.gain.linearRampToValueAtTime(0.35, now + 0.015);
      gain.gain.exponentialRampToValueAtTime(0.001, now + decay);
    } else {
      // strings — slower attack, longer tail
      gain.gain.linearRampToValueAtTime(0.3, now + 0.04);
      if (!sustain) {
        gain.gain.exponentialRampToValueAtTime(0.001, now + decay);
      }
    }

    osc.start(now);
    if (osc2) osc2.start(now);

    if (!sustain || playType === "drum") {
      const stopTime = now + decay + 0.05;
      osc.stop(stopTime);
      if (osc2) osc2.stop(stopTime);
      setTimeout(() => activeVoices.delete(key), (decay + 0.1) * 1000);
    }

    activeVoices.set(key, { osc, osc2, gain });
  }

  function stopNote(key, immediate) {
    const voice = activeVoices.get(key);
    if (!voice) return;
    const audioCtx = getCtx();
    const now = audioCtx.currentTime;
    const releaseTime = immediate ? 0.03 : 0.25;
    try {
      voice.gain.gain.cancelScheduledValues(now);
      voice.gain.gain.setValueAtTime(voice.gain.gain.value, now);
      voice.gain.gain.exponentialRampToValueAtTime(0.001, now + releaseTime);
      voice.osc.stop(now + releaseTime + 0.02);
      if (voice.osc2) voice.osc2.stop(now + releaseTime + 0.02);
    } catch (e) { /* already stopped */ }
    activeVoices.delete(key);
  }

  function stopAll() {
    for (const key of Array.from(activeVoices.keys())) {
      stopNote(key, false);
    }
  }

  return { playNote, stopNote, stopAll, getCtx };
})();
