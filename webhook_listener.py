from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(filename='webhook_trades.log', level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    signal = data.get('signal')
    symbol = data.get('symbol')
    price = data.get('price')
    time = data.get('time')

    message = f"{signal.upper()} signal for {symbol} at {price} ({time})"
    logging.info(message)
    print("RECEIVED:", message)

    return jsonify({'message': 'Signal received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

