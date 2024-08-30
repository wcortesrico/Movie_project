import json
def get_movies():
    with open("data.json", "r") as data_file:
        movies_list = json.loads(data_file.read())
    return movies_list

def save_movies(movies):
    data_json = json.dumps(movies)
    with open("data.json", "w") as new_file:
        json_file = new_file.write(data_json)

