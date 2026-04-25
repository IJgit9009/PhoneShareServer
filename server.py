from flask import Flask, request, render_template_string
import os

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
    cmd = request.form.get("cmd", "none")
    if cmd in ["vibrate", "flash", "sound"]:
        command = cmd
        print(f"Command set: {cmd}")
    return f"ok, cmd={cmd}"

@app.route("/get_command")
def get_command():
    global command
    token = request.args.get("token")
    if token != SECRET:
        return "unauthorized", 403
    
    temp = command
    command = "none"  # сброс после чтения
    return temp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)