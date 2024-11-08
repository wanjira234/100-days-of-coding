from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/0e557ce741c2386c8565").json()
MY_EMAIL = "epiphanywanjira@gmail.com"
MY_PASSWORD = "wjaakzqrbfelvxwk"

app = Flask(__name__) 


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New message\n\nName:{name}\n Email: {email}\n phone:{phone}\n Message:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
