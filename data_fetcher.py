import requests
import json

API_KEY = "fe9cabc7"
def fetch_data(movie_name):
    try:
        url_get = f"http://www.omdbapi.com/?apikey={API_KEY}&"
        params = {
            "t": movie_name
        }
        response_get = requests.get(url_get,params=params)
        if response_get.status_code == requests.codes.ok:
            return json.loads(response_get.text)
        else:
            return response_get.text
    except Exception as e:
        return "Connection Error!"


