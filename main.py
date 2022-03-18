from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/BMI_calc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    def __init__(self, email, weight, height):
        self.email = email
        self.height = height
        self.weight = weight


@app.route("/", methods=['GET'])
def index():
    return render_template("data_entry.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email"]
        height = request.form["height"]
        weight = request.form["weight"]

        data1 = Data(email, weight, height)
        send_mail(email, int(height), int(weight))
        try:
            db.session.add(data1)
            db.session.commit()
        except:
            return render_template("data_entry.html", text="We already have a record of this email address")
    return render_template("success.html")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
