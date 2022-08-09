from flask import Flask, redirect, request, render_template
import requests, base64, string, random

client_id = ""
client_secret = ""
client_auth = client_id + ':' + client_secret
client_auth = base64.b64encode(client_auth.encode("utf-8"))
client_auth = client_auth.decode("ascii")

redirect_uri = 'http://localhost:5000/callback'

app = Flask(__name__)

def generateRandomString(N):
  res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
  return res

@app.route('/login', methods=['GET'])
def login():
    state = generateRandomString(16)
    scope = 'user-read-currently-playing'
    redirect_url = f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={scope}&redirect_uri={redirect_uri}&state={state}'
    return redirect(redirect_url)

@app.route('/callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    state = request.args.get('state', '')

    if not state:
        return redirect('/#?error=state_mismatch')
    else:
      url = "https://accounts.spotify.com/api/token"

      payload=f'code={code}&redirect_uri={redirect_uri}&grant_type=authorization_code'
      headers = {
        'Authorization': f'Basic {client_auth}',
        'Content-Type': 'application/x-www-form-urlencoded',
      }

      response = requests.request("POST", url, headers=headers, data=payload).json()
      access_token = response['access_token']
      refresh_token = response['refresh_token']

      with open('token.txt', 'w') as f:
        f.writelines([f'Access Token: {access_token}\n',f'Refresh Token: {refresh_token}'])

    return render_template("success.html")

@app.route('/refreshtoken', methods=['GET'])
def refresh():
  with open('token.txt', 'r') as f:
    lines = f.readlines()
    access_token = lines[0].split('Access Token: ')[1]
    refresh_token = lines[1].split('Refresh Token: ')[1]

  url = "https://accounts.spotify.com/api/token"
  payload=f'grant_type=refresh_token&refresh_token={refresh_token}'
  headers = {
    'Authorization': f'Basic {client_auth}',
    'Content-Type': 'application/x-www-form-urlencoded',
  }

  response = requests.request("POST", url, headers=headers, data=payload).json()
  access_token = response['access_token']
  with open('token.txt', 'w') as f:
    f.writelines([f'Access Token: {access_token}\n',f'Refresh Token: {refresh_token}'])

  return render_template("success.html")

if __name__ == '__main__':
    app.run()