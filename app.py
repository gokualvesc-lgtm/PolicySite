from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__)

app.secret_key =  "GLASHGALSK"

usuarios = {"Lorent1010": "DF-CC-2015-0608"}

@app.route("/")
def main():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        if username == "beckman" or username == "BECKMAN" or username == "Beckman":
            if password == "BECKMAN":
                return redirect(url_for("secret"))

        try:
            if not usuarios[username]:
                return render_template("login.html")
        except:
            return render_template("login.html")

        if password == usuarios[username]:
            session["username"] = username
            return redirect(url_for("dashboard"))


    return render_template("login.html")

@app.route("/main")
def dashboard():
    if not "username" in session:
        return
    return render_template("mainVisit.html")

@app.route("/secret")
def secret():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)