from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

app = Flask(__name__)

bootstrap = Bootstrap4(app)


app.config['SECRET_KEY'] = "epppppdkjdndndnmnmdndnjdnejddjj"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Please enter a valid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,
                                                                            message="Password must be at least 8 "
                                                                                    "characters")])
    submit = SubmitField(label="Log In")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        # print(login_form.email.data)
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
