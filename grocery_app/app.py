from flask import Flask, render_template, request, redirect, session, jsonify
from db_config import get_connection

app = Flask(__name__)
app.secret_key = "secret123"

# Login Page
@app.route('/')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')


# ================= REGISTER =================
@app.route('/register_user', methods=['POST'])
def register_user():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    conn.commit()
    cursor.close()
    conn.close()

    # If request is from Postman (JSON)
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify({"message": "User Registered!"})

    # If from browser form
    return redirect('/')


# ================= LOGIN =================
@app.route('/login_user', methods=['POST'])
def login_user():
    username = request.form.get('username')
    password = request.form.get('password')

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        session['user'] = username

        # Postman response
        if request.headers.get('Content-Type') == 'application/json':
            return jsonify({"message": "Login successful"})

        # Browser redirect
        return redirect('/home')

    else:
        return jsonify({"message": "Invalid Login"}), 401


# ================= HOME =================
@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect('/')


# ================= LOGOUT =================
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)