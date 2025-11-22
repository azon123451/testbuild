#!/usr/bin/env python3
"""
Simple web server to serve the webapp and handle health checks for Scalingo
"""
import os
import json
from pathlib import Path
from flask import Flask, send_from_directory, jsonify

# Create Flask app
app = Flask(__name__, static_folder=None)

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent
WEBAPP_DIR = PROJECT_ROOT / "webapp"

@app.route('/')
def index():
    """Serve the main webapp page"""
    return send_from_directory(WEBAPP_DIR, 'index.html')

@app.route('/catalog.json')
def catalog():
    """Serve the catalog JSON file"""
    return send_from_directory(WEBAPP_DIR, 'catalog.json')

@app.route('/health')
def health():
    """Health check endpoint for Scalingo"""
    return jsonify({"status": "ok", "service": "telegram-bot-webapp"})

# WSGI application for gunicorn
application = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
