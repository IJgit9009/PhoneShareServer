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

# 🌐 Главная панель
@app.route("/")
def home():
    return render_template_string(HTML)

# 📤 Отправка команды
@app.route("/send", methods=["POST"])
def send():
    global command

    if request.form.get("token") != SECRET:
        return "unauthorized"

    command = request.form["cmd"]
    return redirect("/")

# 📥 Получение команды (Android)
@app.route("/get_command")
def get_command():
    token = request.args.get("token")

    if token != SECRET:
        return "none"

    return command

# 🧹 Очистка команды (после выполнения на телефоне)
@app.route("/clear", methods=["POST"])
def clear():
    global command
    token = request.args.get("token")

    if token != SECRET:
        return "unauthorized"

    command = "none"
    return "ok"

# 🚀 запуск (локально)
if __name__ == "__main__":
    app.run()