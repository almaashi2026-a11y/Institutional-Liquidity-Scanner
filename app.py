from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "السيرفر يعمل يا عبد الرحمن! النظام جاهز لاستقبال الإشارات."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("إشارة واردة:", data)
    # هنا سيتم لاحقاً إضافة كود ربط تليجرام
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)
  
