from flask import Flask, render_template, request, redirect
from netmiko_functions import send_command
import time

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def hello ():
    if request.method == "GET":
        return render_template("homepage.html")
    elif request.method == "POST":
        host = request.form["hostname"]
        username = request.form["username"]
        password = request.form["password"]
        command = request.form["command"]
        choosen = request.form["choosen"]

        if choosen == "" and command == "conf t":
            output = "Yetkisiz Erisim"
        elif choosen == "":
            output = send_command(host=host, username=username, password=password, command=command)
        else:
            output = send_command(host=host, username=username, password=password, command=choosen)

        return render_template ("result.html", outp = output)
    else:
        return ""

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


