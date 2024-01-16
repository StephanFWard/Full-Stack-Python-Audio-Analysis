from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('audio_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audio_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()

# Flask routes
@app.route('/')
def index():
    conn = sqlite3.connect('audio_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM audio_data')
    audio_files = cursor.fetchall()
    conn.close()
    return render_template('index.html', audio_files=audio_files)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file_path = request.form['file_path']
        conn = sqlite3.connect('audio_data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO audio_data (file_path) VALUES (?)', (file_path,))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('upload.html')

# You can implement update and delete routes as needed
# ...

if __name__ == '__main__':
    app.run(debug=True)