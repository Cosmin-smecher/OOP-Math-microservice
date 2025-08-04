import sqlite3
import json
from datetime import datetime
import os

DB_FILE = 'requests.db'
JSON_FILE = 'log.json'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT NOT NULL,
            parameters TEXT NOT NULL,
            result TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_request_log(operation, parameters, result):
    timestamp = datetime.utcnow().isoformat()

    # --- Salvare în SQLite
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO requests (operation, parameters, result, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (operation, parameters, str(result), timestamp))
    conn.commit()
    conn.close()

    # --- Salvare în JSON
    log_entry = {
        "operation": operation,
        "parameters": parameters,
        "result": result,
        "timestamp": timestamp
    }

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open(JSON_FILE, 'r+') as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
