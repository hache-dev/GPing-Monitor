import threading
from flask import Flask, jsonify, render_template, request
from ping3 import ping
import webview
import os

app = Flask(__name__)
HOSTS_FILE = 'hosts.txt'


def read_hosts():
    if not os.path.exists(HOSTS_FILE):
        return []
    with open(HOSTS_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def write_hosts(hosts):
    with open(HOSTS_FILE, 'w') as f:
        f.write('\n'.join(hosts))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ping")
def do_ping():
    host = request.args.get("host")
    if not host:
        return jsonify({"error": "No host provided"}), 400
    latency = ping(host, unit="ms")
    return jsonify({
        "host": host,
        "latency": round(latency, 2) if latency else None
    })


@app.route("/hosts", methods=["GET"])
def get_hosts():
    return jsonify(read_hosts())


@app.route("/add-host", methods=["POST"])
def add_host():
    data = request.get_json()
    host = data.get("host")
    if not host:
        return jsonify({"error": "No host provided"}), 400

    hosts = read_hosts()
    if host not in hosts:
        hosts.append(host)
        write_hosts(hosts)
    return '', 204


@app.route("/remove-host", methods=["POST"])
def remove_host():
    data = request.get_json()
    host = data.get("host")
    if not host:
        return jsonify({"error": "No host provided"}), 400

    hosts = read_hosts()
    if host in hosts:
        hosts.remove(host)
        write_hosts(hosts)
    return '', 204


def run_flask():
    app.run(debug=False, port=5009, threaded=True)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    window = webview.create_window("GPing Monitor", "http://127.0.0.1:5009", maximized=True)
    webview.start(user_agent='GPing Monitor Custom UA')
