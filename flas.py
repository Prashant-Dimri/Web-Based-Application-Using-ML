from flask import Flask, render_template, request
from new import predict_email, predict_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def execute():
    email = request.form['email']
    password = request.form['pass']
    email_prediction = predict_email(email)
    password_prediction = predict_password(password)
    return render_template('index.html', email_prediction=email_prediction, password_prediction=password_prediction)

if __name__ == '__main__':
    app.run(debug=True)
