from flask import Flask, request, render_template_string

app = Flask(__name__)

command = "none"
SECRET = "my_secret_token"

HTML = """
<h1>Phone Control Panel</h1>

<form action="/send" method="post">
    <button type="submit" name="cmd" value="vibrate">VIBRATE</button>
    <button type="submit" name="cmd" value="flash">FLASH</button>
    <button type="submit" name="cmd" value="sound">SOUND</button>
</form>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/send", methods=["POST"])
def send():
    global command
    command = "vibrate"
    print("BUTTON WORKED")
    return "ok"

@app.route("/get_command")
def get_command():
    global command
    temp = command
    command = "none"
    return temp

if __name__ == "__main__":
    app.run()