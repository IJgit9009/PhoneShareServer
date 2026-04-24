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

# 📤 команда
@app.route("/send", methods=["POST"])
def send_command():
    global command
    command = request.form.get("cmd")
    return redirect("/")

# 📥 получить команду
@app.route("/get_command")
def get_command():
    token = request.args.get("token")

    if token != SECRET:
        return "none"

    return command

# 🧹 очистка (ТОЛЬКО GET чтобы не ломалось)
@app.route("/clear")
def clear():
    global command
    token = request.args.get("token")

    if token == SECRET:
        command = "none"

    return "ok"

if __name__ == "__main__":
    app.run()