# The Instrument Gallery 🏛️🎻

A museum-themed web app: upload a photo of a musical instrument, an
in-browser AI vision model identifies it, and you can then play its
real notes/strings/keys, synthesized live in your browser.

**15 instruments included:** Acoustic Guitar, Violin, Piano, Flute,
Trumpet, Saxophone, Drum, Cello, Harp, Banjo, Accordion, Harmonica,
Marimba, Pipe Organ, Maracas.

---

##  Important: about "training data" and "sound files"

You asked for a zip with training data and sound files for each
instrument. After looking into it honestly, I built this differently
on purpose, and you should know why before you run it:

1. **No training data is included or needed.** Training an accurate
   image classifier from scratch needs thousands of labeled photos
   per instrument and a GPU — not realistic to hand you in a zip file
   for a 15-class demo. Instead, this app uses **MobileNet**, a
   well-known pretrained image model (via TensorFlow.js), running
   **entirely in your browser**. It already knows what guitars,
   violins, pianos, etc. look like from its original training on
   ImageNet. There's nothing to install or train — it downloads
   automatically from a public CDN the first time you load the page.

2. **No audio sample files are included.** Real instrument recordings
   are copyrighted, so I couldn't legally bundle a sample pack.
   Instead, every note is **synthesized live** using the Web Audio
   API, tuned to the correct real-world frequency for each
   string/key/reed (e.g. a guitar's low E string is tuned to exactly
   82.41 Hz, concert A is 440 Hz, etc.). This means the app works
   **fully offline for sound** and has zero licensing risk.

So instead of a folder of training images and .wav/.mp3 files, what's
in this zip is the actual **application** — code, design, and a
structured database of facts/notes per instrument — which is what
actually makes the upload → recognize → play experience work.

---

## What's in the zip

```
instrument-app/
├── app.py                      # Flask server (routes + JSON API)
├── requirements.txt             # Python dependencies (just Flask)
├── data/
│   └── instruments.py           # The 15-instrument database: names,
│                                 # descriptions, origins, fun facts,
│                                 # and note/frequency tables
├── templates/
│   └── index.html               # The single-page museum gallery UI
├── static/
│   ├── css/style.css            # Museum light theme styling
│   ├── js/
│   │   ├── audio-engine.js      # Web Audio API note synthesizer
│   │   ├── recognition.js       # MobileNet image classification
│   │   └── app.js               # Wires upload → recognition → playback
│   └── images/                  # (empty — no bundled images needed)
└── README.md                    # This file
```

---

## How it works

1. **Upload** — you drag/drop or select a photo of an instrument.
2. **Recognize** — your browser downloads MobileNet (a small pretrained
   vision model, ~16MB, cached after first load) and classifies the
   image locally. The result is mapped from ImageNet's labels (e.g.
   "acoustic guitar", "violin", "cornet") onto our 15-instrument
   collection.
3. **Identify** — the matched instrument's name, family, origin,
   description, and a fun fact are shown on a museum placard.
4. **Play** — scroll down to the "Display Case," where each
   string/key/note is shown as a clickable placard. Clicking/tapping
   one plays that exact pitch using an oscillator tuned to the real
   frequency, shaped with an instrument-appropriate envelope (plucked
   strings decay slowly, drums are short and percussive, etc).

You can also skip the photo entirely and click any instrument
directly in the "Permanent Collection" grid at the bottom of the page.

---

## Requirements

- **Python 3.8+**
- **An internet connection** — required only for:
  - Loading Google Fonts (Fraunces, Inter, Space Mono)
  - Downloading the MobileNet model + TensorFlow.js from a CDN
    (cached by your browser after the first visit)
  - These are loaded via `<script>`/`<link>` tags from
    `cdn.jsdelivr.net` and `fonts.googleapis.com` — no API keys needed.
- A modern browser (Chrome, Firefox, Edge, Safari) with Web Audio API
  support — i.e. basically any browser from the last 8 years.

No GPU, no database, no Docker required.