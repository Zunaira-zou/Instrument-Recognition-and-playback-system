# -*- coding: utf-8 -*-
INSTRUMENTS = {
    "guitar": {
        "display_name": "Acoustic Guitar",
        "family": "Strings (Plucked)",
        "origin": "Spain, 16th century (modern form)",
        "description": (
            "The acoustic guitar is a six-stringed instrument played by plucking "
            "or strumming over a hollow wooden resonating body. It is one of the "
            "most widely played instruments in the world, central to folk, "
            "classical, and popular music alike."
        ),
        "fun_fact": "The classical guitar's body shape was standardized by Spanish luthier Antonio de Torres in the 1850s.",
        "play_label": "Strings",
        "play_type": "strings",
        "wave": "sawtooth",
        "decay": 1.8,
        "notes": [
            {"label": "E2 (6th)", "freq": 82.41},
            {"label": "A2 (5th)", "freq": 110.00},
            {"label": "D3 (4th)", "freq": 146.83},
            {"label": "G3 (3rd)", "freq": 196.00},
            {"label": "B3 (2nd)", "freq": 246.94},
            {"label": "E4 (1st)", "freq": 329.63},
        ],
        "imagenet_classes": ["acoustic guitar", "guitar pick", "electric guitar"],
    },
    "violin": {
        "display_name": "Violin",
        "family": "Strings (Bowed)",
        "origin": "Italy, early 16th century",
        "description": (
            "The violin is the smallest and highest-pitched member of the bowed "
            "string family. Played with a horsehair bow drawn across four strings, "
            "it is prized for its expressive, voice-like tone in orchestras and "
            "solo performance."
        ),
        "fun_fact": "Antonio Stradivari's violins, made in the 1600s-1700s, remain among the most valuable instruments ever crafted.",
        "play_label": "Strings",
        "play_type": "strings",
        "wave": "sawtooth",
        "decay": 2.2,
        "notes": [
            {"label": "G3", "freq": 196.00},
            {"label": "D4", "freq": 293.66},
            {"label": "A4", "freq": 440.00},
            {"label": "E5", "freq": 659.25},
        ],
        "imagenet_classes": ["violin", "fiddle"],
    },
    "piano": {
        "display_name": "Piano",
        "family": "Keyboard (Struck Strings)",
        "origin": "Italy, c. 1700 (Bartolomeo Cristofori)",
        "description": (
            "The piano produces sound when felt-covered hammers strike steel "
            "strings, triggered by pressing keys. Its 88-key range gives it "
            "remarkable dynamic and harmonic versatility, anchoring genres from "
            "classical to jazz."
        ),
        "fun_fact": "Cristofori originally called it 'gravicembalo col piano e forte' — harpsichord with soft and loud.",
        "play_label": "Keys",
        "play_type": "keys",
        "wave": "triangle",
        "decay": 1.5,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "D4", "freq": 293.66},
            {"label": "E4", "freq": 329.63},
            {"label": "F4", "freq": 349.23},
            {"label": "G4", "freq": 392.00},
            {"label": "A4", "freq": 440.00},
            {"label": "B4", "freq": 493.88},
            {"label": "C5", "freq": 523.25},
        ],
        "imagenet_classes": ["grand piano", "upright piano"],
    },
    "flute": {
        "display_name": "Flute",
        "family": "Woodwind",
        "origin": "Prehistoric; modern form France, 19th century",
        "description": (
            "The flute is a side-blown woodwind instrument that produces sound as "
            "the player's breath splits across an embouchure hole. Despite the "
            "'wood' in woodwind, modern concert flutes are usually made of metal."
        ),
        "fun_fact": "The oldest known flutes, carved from bird bone and mammoth ivory, are over 40,000 years old.",
        "play_label": "Holes / Keys",
        "play_type": "keys",
        "wave": "sine",
        "decay": 1.0,
        "notes": [
            {"label": "C5", "freq": 523.25},
            {"label": "D5", "freq": 587.33},
            {"label": "E5", "freq": 659.25},
            {"label": "F5", "freq": 698.46},
            {"label": "G5", "freq": 783.99},
            {"label": "A5", "freq": 880.00},
        ],
        "imagenet_classes": ["flute"],
    },
    "trumpet": {
        "display_name": "Trumpet",
        "family": "Brass",
        "origin": "Ancient; modern valved form Germany, 1814",
        "description": (
            "The trumpet is a brass instrument that produces sound via the "
            "buzzing of the player's lips into a mouthpiece, with pitch shaped "
            "by three valves. It has a bright, piercing tone used in orchestras, "
            "jazz, and fanfares."
        ),
        "fun_fact": "Trumpets made from animal horns and conch shells date back over 3,000 years.",
        "play_label": "Valves",
        "play_type": "keys",
        "wave": "square",
        "decay": 0.9,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "E4", "freq": 329.63},
            {"label": "G4", "freq": 392.00},
            {"label": "C5", "freq": 523.25},
        ],
        "imagenet_classes": ["cornet", "trumpet"],
    },
    "saxophone": {
        "display_name": "Saxophone",
        "family": "Woodwind (Single Reed)",
        "origin": "Belgium, 1840s (Adolphe Sax)",
        "description": (
            "The saxophone is a single-reed woodwind made of brass, blending "
            "woodwind fingering with brass-like projection. It became the "
            "defining voice of jazz in the 20th century."
        ),
        "fun_fact": "Adolphe Sax patented the instrument in 1846 hoping to bridge brass and woodwind sections.",
        "play_label": "Keys",
        "play_type": "keys",
        "wave": "sawtooth",
        "decay": 1.1,
        "notes": [
            {"label": "Bb3", "freq": 233.08},
            {"label": "C4", "freq": 261.63},
            {"label": "D4", "freq": 293.66},
            {"label": "F4", "freq": 349.23},
            {"label": "G4", "freq": 392.00},
        ],
        "imagenet_classes": ["sax", "saxophone"],
    },
    "drum": {
        "display_name": "Drum (Snare/Hand Drum)",
        "family": "Percussion (Membranophone)",
        "origin": "Prehistoric, worldwide",
        "description": (
            "Drums are among humanity's oldest instruments — a membrane "
            "stretched over a resonating shell, struck by hand or stick to "
            "produce rhythmic, often pitch-indefinite sound."
        ),
        "fun_fact": "Drums have been used for communication over long distances in many African cultures, encoding language through rhythm.",
        "play_label": "Strike Zones",
        "play_type": "drum",
        "wave": "triangle",
        "decay": 0.3,
        "notes": [
            {"label": "Low Tom", "freq": 100},
            {"label": "Mid Tom", "freq": 150},
            {"label": "High Tom", "freq": 220},
            {"label": "Snare", "freq": 300},
            {"label": "Rim", "freq": 450},
        ],
        "imagenet_classes": ["drum", "steel drum"],
    },
    "cello": {
        "display_name": "Cello",
        "family": "Strings (Bowed)",
        "origin": "Italy, early 16th century",
        "description": (
            "The cello is a large bowed string instrument played upright between "
            "the knees. Tuned an octave below the viola, it spans a wide range and "
            "is celebrated for its warm, rich, voice-like lower register."
        ),
        "fun_fact": "The cello's full name, violoncello, means 'little big viol' in Italian.",
        "play_label": "Strings",
        "play_type": "strings",
        "wave": "sawtooth",
        "decay": 2.4,
        "notes": [
            {"label": "C2", "freq": 65.41},
            {"label": "G2", "freq": 98.00},
            {"label": "D3", "freq": 146.83},
            {"label": "A3", "freq": 220.00},
        ],
        "imagenet_classes": ["cello"],
    },
    "harp": {
        "display_name": "Harp",
        "family": "Strings (Plucked)",
        "origin": "Ancient Egypt/Mesopotamia",
        "description": (
            "The harp consists of a triangular frame with strings of graduated "
            "length stretched across it, plucked directly by the fingers. It "
            "produces a shimmering, resonant tone used in orchestral and folk "
            "traditions worldwide."
        ),
        "fun_fact": "Harps appear in art and artifacts dating back over 5,000 years, making them among the oldest stringed instruments.",
        "play_label": "Strings",
        "play_type": "strings",
        "wave": "sine",
        "decay": 2.6,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "D4", "freq": 293.66},
            {"label": "E4", "freq": 329.63},
            {"label": "G4", "freq": 392.00},
            {"label": "A4", "freq": 440.00},
            {"label": "C5", "freq": 523.25},
        ],
        "imagenet_classes": ["harp"],
    },
    "banjo": {
        "display_name": "Banjo",
        "family": "Strings (Plucked)",
        "origin": "West Africa, brought to the Americas",
        "description": (
            "The banjo has a thin membrane stretched over a circular frame, "
            "topped with a fretted neck and metal strings. Its bright, percussive "
            "twang is a hallmark of bluegrass and American folk music."
        ),
        "fun_fact": "The banjo descends from West African gourd lutes brought to the Americas by enslaved people in the 17th century.",
        "play_label": "Strings",
        "play_type": "strings",
        "wave": "square",
        "decay": 0.8,
        "notes": [
            {"label": "G4 (5th)", "freq": 392.00},
            {"label": "D3 (4th)", "freq": 146.83},
            {"label": "G3 (3rd)", "freq": 196.00},
            {"label": "B3 (2nd)", "freq": 246.94},
            {"label": "D4 (1st)", "freq": 293.66},
        ],
        "imagenet_classes": ["banjo"],
    },
    "accordion": {
        "display_name": "Accordion",
        "family": "Free-Reed (Bellows-driven)",
        "origin": "Germany/Austria, early 19th century",
        "description": (
            "The accordion uses a hand-pumped bellows to push air across metal "
            "reeds, with pitch selected through piano-style keys or buttons. Its "
            "portable, full-bodied sound is central to folk traditions across "
            "Europe and Latin America."
        ),
        "fun_fact": "The accordion was patented in Vienna in 1829 by Cyrill Demian.",
        "play_label": "Keys",
        "play_type": "keys",
        "wave": "sawtooth",
        "decay": 1.3,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "D4", "freq": 293.66},
            {"label": "E4", "freq": 329.63},
            {"label": "F4", "freq": 349.23},
            {"label": "G4", "freq": 392.00},
            {"label": "A4", "freq": 440.00},
        ],
        "imagenet_classes": ["accordion"],
    },
    "harmonica": {
        "display_name": "Harmonica",
        "family": "Free-Reed (Wind)",
        "origin": "Germany, early 19th century",
        "description": (
            "The harmonica is a small handheld free-reed instrument played by "
            "breathing in and out across a row of reed channels. Its compact "
            "design made it a staple of blues, folk, and country music."
        ),
        "fun_fact": "Harmonicas were carried by soldiers in both World Wars for their portability and morale-boosting music.",
        "play_label": "Reed Holes",
        "play_type": "keys",
        "wave": "square",
        "decay": 0.7,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "D4", "freq": 293.66},
            {"label": "E4", "freq": 329.63},
            {"label": "G4", "freq": 392.00},
            {"label": "C5", "freq": 523.25},
        ],
        "imagenet_classes": ["harmonica"],
    },
    "marimba": {
        "display_name": "Marimba",
        "family": "Percussion (Idiophone)",
        "origin": "Africa & Central America",
        "description": (
            "The marimba is a wooden mallet percussion instrument with tuned "
            "bars laid out like a piano keyboard, each suspended over a "
            "resonating tube. Striking the bars with mallets produces a warm, "
            "rounded tone."
        ),
        "fun_fact": "Guatemala officially declared the marimba its national instrument in 1978.",
        "play_label": "Bars",
        "play_type": "keys",
        "wave": "sine",
        "decay": 1.4,
        "notes": [
            {"label": "C4", "freq": 261.63},
            {"label": "E4", "freq": 329.63},
            {"label": "G4", "freq": 392.00},
            {"label": "C5", "freq": 523.25},
            {"label": "E5", "freq": 659.25},
        ],
        "imagenet_classes": ["marimba", "xylophone"],
    },
    "organ": {
        "display_name": "Pipe Organ",
        "family": "Keyboard (Wind)",
        "origin": "Ancient Greece; pipe form Europe, Middle Ages",
        "description": (
            "The pipe organ forces air through ranks of pipes of varying length "
            "and material, controlled by keys and stops. It produces a "
            "majestic, sustained sound long associated with cathedrals and "
            "concert halls."
        ),
        "fun_fact": "The largest pipe organs have over 30,000 individual pipes.",
        "play_label": "Keys",
        "play_type": "keys",
        "wave": "square",
        "decay": 2.0,
        "notes": [
            {"label": "C3", "freq": 130.81},
            {"label": "E3", "freq": 164.81},
            {"label": "G3", "freq": 196.00},
            {"label": "C4", "freq": 261.63},
            {"label": "G4", "freq": 392.00},
        ],
        "imagenet_classes": ["organ", "pipe organ"],
    },
    "maracas": {
        "display_name": "Maracas",
        "family": "Percussion (Idiophone, Shaken)",
        "origin": "Latin America / Caribbean",
        "description": (
            "Maracas are handheld percussion rattles, typically made from a "
            "hollow gourd or shell filled with seeds or beads. Shaken in pairs, "
            "they provide rhythmic texture in Latin American music."
        ),
        "fun_fact": "Traditional maracas were originally made from the dried shells of the higuera tree gourd.",
        "play_label": "Shake Zones",
        "play_type": "drum",
        "wave": "triangle",
        "decay": 0.2,
        "notes": [
            {"label": "Shake Soft", "freq": 800},
            {"label": "Shake Hard", "freq": 1200},
            {"label": "Tap", "freq": 1500},
        ],
        "imagenet_classes": ["maraca"],
    },
}

# Order used for navigation / gallery listing
INSTRUMENT_ORDER = [
    "guitar", "violin", "piano", "flute", "trumpet",
    "saxophone", "drum", "cello", "harp", "banjo",
    "accordion", "harmonica", "marimba", "organ", "maracas",
]
