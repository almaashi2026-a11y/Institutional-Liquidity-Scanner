from flask import Flask

app = Flask(__name__) # هذا هو المتغير الذي يبحث عنه Vercel

@app.route('/')
def home():
    return "السيرفر يعمل يا عبد الرحمن!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # هنا سنضيف لاحقاً كود التعامل مع الإشارات
    return "تم الاستلام", 200

if __name__ == '__main__':
    app.run()
    
