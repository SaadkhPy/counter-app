from flask import Flask, jsonify
import redis

# Initialize Flask app
app = Flask(__name__)

# Get Redis connection info from environment variables
r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

# Redis key to store the hit count
HIT_COUNT_KEY = "git_hit_count"

@app.route('/')
def home():
    # Get the current hit count from Redis
    hit_count = r.get(HIT_COUNT_KEY)
    
    if hit_count:
        # Increment the hit count if it exists
        r.incr(HIT_COUNT_KEY)
    else:
        # Set initial value if hit count doesn't exist
        r.set(HIT_COUNT_KEY, 1)
        hit_count = 1
    
    return jsonify({
        'message': 'Welcome to Git Hit Count!',
        'hit_count': hit_count
    })

@app.route('/reset')
def reset_hit_count():
    # Reset the hit count in Redis
    r.set(HIT_COUNT_KEY, 0)
    return jsonify({
        'message': 'Hit count has been reset to 0!',
        'hit_count': 0
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')