from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    log_request(request)
    return render_template('home.html')

@app.route('/login')
def login():
    log_request(request)
    return render_template('login.html')

def log_request(req):
    data_to_log = {
        'ip_address': req.remote_addr,
        'duration': req.environ.get('REQUEST_TIME', None),
        'timestamp': time.time()
    }
    with open('logs.jsonl', 'a') as f:
        f.write(json.dumps(data_to_log) + '\n')


if __name__ == '__main__':
    app.run(debug=True)