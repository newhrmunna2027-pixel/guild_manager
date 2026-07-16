import os
import time
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# আপনার Replit অ্যাপের URL
REPLIT_URL = "https://f350b0e7-812c-4340-b11b-06b47a604675-00-10nruw2zh65o5.pike.replit.dev"

@app.route('/', methods=['GET', 'POST'])
@app.route('/api/ping', methods=['GET', 'POST'])
def ping_back():
    start_time = time.time()
    
    # Vercel-এর ১০ সেকেন্ডের লিমিটের মধ্যে নিরাপদ থাকার জন্য আমরা ৮.৫ সেকেন্ড সেট করলাম
    max_duration = 8.5 
    ping_interval = 2.5 # প্রতি ২.৫ সেকেন্ড পর পর Replit-কে পিং করবে
    
    ping_count = 0
    errors = []

    print("Vercel active হয়েছে। Replit-এর সাথে কানেকশন ধরে রাখা হচ্ছে...")

    # যতক্ষণ না ৮.৫ সেকেন্ড পার হচ্ছে, Vercel রান থাকবে এবং Replit-কে পিং করতে থাকবে
    while (time.time() - start_time) < max_duration:
        try:
            print(f"Pinging Replit (Attempt {ping_count + 1})...")
            response = requests.get(REPLIT_URL, timeout=5)
            print(f"Replit Response: {response.status_code}")
            ping_count += 1
        except Exception as e:
            errors.append(str(e))
            print(f"Ping failed: {e}")
        
        # পরবর্তী পিং পাঠানোর আগে বিরতি
        time.sleep(ping_interval)

    # সময় শেষ হওয়ার ঠিক আগে Vercel রেসপন্স রিটার্ন করে শান্তভাবে স্লিপে চলে যাবে
    return jsonify({
        "status": "completed",
        "message": f"Vercel stayed active for {max_duration} seconds before sleep.",
        "total_pings_sent": ping_count,
        "errors": errors
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
