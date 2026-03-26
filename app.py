from flask import Flask, request
import requests
import base64
import os

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

@app.route("/")
def home():
    return "Aspen API running"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    realm_id = request.args.get("realmId")

    auth = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    response = requests.post(
        "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer",
        headers={
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "https://api.aspenaccountingfirm.com/callback"
        }
    )

    return response.json()