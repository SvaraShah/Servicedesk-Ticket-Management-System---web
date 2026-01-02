from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def db_conn():
    conn = sqlite3.connect('service_desk.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with db_conn() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tickets
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT, priority TEXT, status TEXT, created_at TEXT)''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tickets', methods=['GET'])
def get_tickets():
    with db_conn() as conn:
        tickets = conn.execute('SELECT * FROM tickets ORDER BY id DESC').fetchall()
        return jsonify([dict(t) for t in tickets])

@app.route('/add_ticket', methods=['POST'])
def add_ticket():
    data = request.json
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with db_conn() as conn:
        conn.execute('INSERT INTO tickets (description, priority, status, created_at) VALUES (?, ?, ?, ?)',
                    (data['description'], data['priority'], 'OPEN', timestamp))
    return jsonify({"message": "Ticket Created"})

@app.route('/resolve/<int:id>', methods=['POST'])
def resolve(id):
    with db_conn() as conn:
        conn.execute('UPDATE tickets SET status = "RESOLVED" WHERE id = ?', (id,))
    return jsonify({"message": "Resolved"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
