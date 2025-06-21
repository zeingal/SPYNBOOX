from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_volume', methods=['POST'])
def set_volume():
    volume = request.form['volume']
    device = request.form['device']
    print(f"Set volume {volume} for device {device}")
    return "OK"

@app.route('/set_mode', methods=['POST'])
def set_mode():
    mode = request.form['mode']
    device = request.form['device']
    print(f"Set mode {mode} for device {device}")
    return "OK"

@app.route('/play_test', methods=['POST'])
def play_test():
    device = request.form['device']
    print(f"Play test for device {device}")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
