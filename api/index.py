import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# আপনার Replit অ্যাপের URL (যেখানে Vercel ব্যাক-পিং পাঠাবে)
REPLIT_URL = "https://f350b0e7-812c-4340-b11b-06b47a604675-00-10nruw2zh65o5.pike.replit.dev/"

@app.route('/', methods=['GET', 'POST'])
@app.route('/api/ping', methods=['GET', 'POST'])
def ping_back():
    try:
        # Replit-কে ফিরতি পিং পাঠানো হচ্ছে
        print(f"Pinging Replit back at: {REPLIT_URL}")
        response = requests.get(REPLIT_URL, timeout=10)
        
        return jsonify({
            "status": "success",
            "message": "Vercel received ping and pinged Replit back.",
            "replit_status_code": response.status_code
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to ping Replit back.",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
