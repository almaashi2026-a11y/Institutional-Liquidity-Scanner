from flask import Flask, request, jsonify

# يجب أن يكون هذا السطر هو الأساس في تعريف التطبيق
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "السيرفر يعمل يا عبد الرحمن!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # استقبال البيانات من TradingView
    data = request.json
    print(f"بيانات مستلمة: {data}")
    return jsonify({"status": "received"}), 200

# لا تقم بإضافة if __name__ == '__main__':
