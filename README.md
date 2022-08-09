
# Spotify OAuth Flow

This flask app can be used to fetch access token and refresh token using Spotify O-Auth


## Tech Stack

**Server:** Flask


## PC Requirements

- Python
- Flask

## Setup Spotify Developer Dashboard
- Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and login to your account
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/1.png?raw=true)
- Go to Applications tab and click on "Create An App" button
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/2.png?raw=true)
- Enter App Name and App Description
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/3.png?raw=true)
- Copy Client ID and Client Secret by clicking "Show Client Secret"
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/4.png?raw=true)
- We also need scopes that we later on define in our code, checkout the list of scopes [here](https://developer.spotify.com/documentation/general/guides/authorization/scopes/)


## Run Locally

Clone the project

```bash
  git clone https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask.git
```

Go to the project directory

```bash
  cd Spotify-OAuth-in-Flask
```

Install dependencies

```bash
  pip3 install flask
```

Assign Client ID and Client Secret to respective values of your application
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/ss.png?raw=true)

Assign Scope to respective value, if you need more than one scope, make the string space separated
![alt text](https://github.com/rajatsonibkn2002/Spotify-OAuth-in-Flask/blob/main/images/scopess.png?raw=true)

Start the server

```bash
  python3 flask-app.py
```

## Usage
- Open the endpoint given below, login using spotify to generate an access token and a refresh token(stored in a txt file)
```http://localhost:5000/login```
- If you wanna get a refreshed access token, simply open the below endpoint
```http://localhost:5000/refreshtoken```

## Authors

- [@rajatsonibkn2002](https://www.github.com/rajatsonibkn2002)

