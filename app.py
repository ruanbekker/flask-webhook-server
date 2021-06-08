from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    payload = request.get_json(force=True)
    print(payload)
    return jsonify(payload)

@app.route('/health', methods=['GET'])
def main():
    payload = {'status': 'up'}
    return jsonify(payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
