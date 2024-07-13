import movie_storage
import json
import data_fetcher

def open_and_write_html(html_text):
    with open("_static/index_template.html", "r") as data:
        movies_html = data.read()
        movies_html = movies_html.replace("__TEMPLATE_MOVIE_GRID__", html_text)

    with open("_static/index.html", "w") as new_html:
        new_html.write(movies_html)

def generate_website():
    list_of_movies = movie_storage.get_movies()
    output_text = ''
    for movie in list_of_movies:
        movie_poster = movie["poster_url"]
        movie_name = movie["name"]
        movie_year = movie["year"]
        output_text += '\n<li>\n'
        output_text += '<div class="movie">\n'
        output_text += f'<img class="movie-poster" src="{movie_poster}" alt="image of {movie_name}poster">\n'
        output_text += f'<div class="movie-title"> {movie_name} </div>\n'
        output_text += f'<div class="movie-year"> {movie_year} </div>\n'
        output_text += f'</div>\n'
        output_text += f'</li>'

    open_and_write_html(output_text)
    print("Website was generated successfully")

