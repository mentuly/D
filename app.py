from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('favorites.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS favorite_colors (id INTEGER PRIMARY KEY, color TEXT)')
    conn.commit()
    conn.close()

def add_favorite_color(color):
    conn = sqlite3.connect('favorites.db')
    c = conn.cursor()
    c.execute('INSERT INTO favorite_colors (color) VALUES (?)', (color,))
    conn.commit()
    conn.close()

def get_favorite_colors():
    conn = sqlite3.connect('favorites.db')
    c = conn.cursor()
    c.execute('SELECT color FROM favorite_colors')
    favorite_colors = [row[0] for row in c.fetchall()]
    conn.close()
    return favorite_colors

@app.route('/')
def index():
    create_table()
    return render_template('index.html')

@app.route('/favorite_color', methods=['POST'])
def favorite_color():
    color = request.form['color']
    add_favorite_color(color)
    return '', 204

@app.route('/favorite_colors')
def favorite_colors():
    colors = get_favorite_colors()
    return {'favorite_colors': colors}

if __name__ == '__main__':
    app.run(debug=True)