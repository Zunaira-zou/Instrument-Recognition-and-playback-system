import json
import os
import sys

from flask import Flask, render_template, jsonify, send_from_directory

sys.path.append(os.path.join(os.path.dirname(__file__), "data"))
from instruments import INSTRUMENTS, INSTRUMENT_ORDER  

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main museum gallery page."""
    ordered = [INSTRUMENTS[key] | {"id": key} for key in INSTRUMENT_ORDER]
    return render_template("index.html", instruments=ordered)


@app.route("/api/instruments")
def api_instruments():
    """Return the full instrument database as JSON (used by the front end
    for recognition-result lookups and the playback UI)."""
    ordered = {key: INSTRUMENTS[key] for key in INSTRUMENT_ORDER}
    return jsonify(ordered)


@app.route("/api/instrument/<instrument_id>")
def api_instrument_single(instrument_id):
    """Return a single instrument's data."""
    instrument = INSTRUMENTS.get(instrument_id)
    if not instrument:
        return jsonify({"error": "Instrument not found"}), 404
    return jsonify(instrument | {"id": instrument_id})


@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok", "instrument_count": len(INSTRUMENTS)})


if __name__ == "__main__":
    print("=" * 60)
    print("  Instrument Gallery — starting server")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host="127.0.0.1", port=5000)
