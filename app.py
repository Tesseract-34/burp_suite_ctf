from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')

    if username == 'guest' and password == 'guest':
        if role == 'wziej':
            return jsonify({
                "success": True,
                "message": "Welcome, admin!",
                "flag": "flag{I_am_Cicada}"
            })
        else:
            return jsonify({
                "success": True,
                "message": "Logged in as user."
            })
    else:
        return jsonify({
            "success": False,
            "message": "Invalid credentials."
        }), 401

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    print("✅ Server starting at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
