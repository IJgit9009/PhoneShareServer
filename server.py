from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
command = "none"
SECRET = "my_secret_token"

HTML = """
<h1>Phone Control Panel</h1>
<form method="post" action="/send">
    <input type="hidden" name="token" value="my_secret_token">
    <button name="cmd" value="vibrate">VIBRATE</button>
    <button name="cmd" value="flash">FLASH</button>
    <button name="cmd" value="sound">SOUND</button>
</form>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/send", methods=["POST"])
def send():
    global command
    if request.form.get("token") != SECRET:
        return "unauthorized"
    command = request.form["cmd"]
    return redirect("/")

@app.route("/get_command")
def get_command():
    global command
    token = request.args.get("token")
    if token != SECRET:
        return {"command": "none"}

    temp = command
    command = "none"
    return {"command": temp}

app.run(host="0.0.0.0", port=10000)