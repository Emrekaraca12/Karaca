# database.py
import psycopg2

def initialize_db():
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            score INTEGER,
            level INTEGER,
            speed INTEGER,
            walls TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE username = %s', (username,))
    user_id = cur.fetchone()
    if user_id is None:
        cur.execute('INSERT INTO users (username) VALUES (%s) RETURNING id', (username,))
        conn.commit()
        user_id = cur.fetchone()[0]
    else:
        user_id = user_id[0]
    cur.close()
    conn.close()
    return user_id

def save_game_state(user_id, score, level, speed, walls):
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    walls_data = ','.join([';'.join(map(str, wall)) for wall in walls])  # Convert list of walls to string
    cur.execute('INSERT INTO user_scores (user_id, score, level, speed, walls) VALUES (%s, %s, %s, %s, %s)',
                (user_id, score, level, speed, walls_data))
    conn.commit()
    cur.close()
    conn.close()

def get_last_game_state(user_id):
    conn = psycopg2.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    cur.execute('''
        SELECT score, level, speed, walls FROM user_scores 
        WHERE user_id = %s 
        ORDER BY id DESC LIMIT 1
    ''', (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        score, level, speed, walls = result
        walls = [tuple(map(int, wall.split(';'))) for wall in walls.split(',')] if walls else []  # Convert string back to list of tuples
        return score, level, speed, walls
    else:
        return None
    
if __name__ == "__main__":
    initialize_db()

