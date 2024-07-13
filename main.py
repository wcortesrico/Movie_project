import random
import movie_storage
import data_fetcher

def head_printing():
    print("********** My Movie Database **********")

def menu_printing():
    print("Menu:\n"
          "0. Exit\n"
          "1. List Movies\n"
          "2. Add Movies\n" 
          "3. Delete Movie\n"
          "4. Update Movie\n"
          "5. Stats\n"
          "6. Random Movie\n"
          "7. Search Movie\n"
          "8. Sorted Movie by rating\n"
          "9. Generate website\n"
          )

def bad_input(number):
    #This function determine if the number of the menu is between the range

    if number >= 0 and number <= 9:
        return False
    else:
        return True

def print_list_option():
    #This function print the count of movies and the movie list with each rate
    list_of_movies = movie_storage.get_movies()
    number_total_movies = len(list_of_movies)
    print(f"\n{number_total_movies} movies in total\n")
    for item in list_of_movies:
        movie_name = item["name"]
        movie_rating = item["rating"]
        movie_year = item["year"]
        print(f"{movie_name}  Rating: {movie_rating}  Release year: {movie_year}")


def add_movie():
    movie_found = False
    while movie_found == False:
        new_movie_name = input("\nEnter new movie name ")
        movie_info = data_fetcher.fetch_data(new_movie_name)
        if movie_info == "Connection Error!":
            print(movie_info, "Try again")
        elif "Error" in movie_info.keys():
            print("Movie not Found! Try Again")
        else:
            movie_found = True
            movie_name = movie_info["Title"]
            movie_year = movie_info["Year"]
            movie_rate = float(movie_info["imdbRating"])
            movie_poster = movie_info["Poster"]
            list_of_movies = movie_storage.get_movies()
            list_of_movies.append(
                {"name": movie_name, "rating": movie_rate, "year": movie_year, "poster_url": movie_poster})
            movie_storage.save_movies(list_of_movies)


def delete_movie():
    # This function removes a specific movie by name
    list_of_movies = movie_storage.get_movies()
    removed_item = input("Delete movie: ")
    movie_in_list = False
    for item in list_of_movies:
        if removed_item in item.values():
            movie_in_list = True
            list_of_movies.remove(item)
            break
    if movie_in_list == False:
        print("Movie not in list")

    movie_storage.save_movies(list_of_movies)

def update_movie():
    list_of_movies = movie_storage.get_movies()
    movie_name = input("Enter movie name ")
    for movie in list_of_movies:
        if movie_name in movie.values():
            movie_rate = float(input("Enter new rate "))
            movie["rating"] = movie_rate
        else:
            pass
    movie_storage.save_movies(list_of_movies)

def print_stats():
    list_of_movies = movie_storage.get_movies()
    rating_list = [] #Creating list to store all the ratings to operate them
    for movie in list_of_movies:
        rating_list.append(movie["rating"])
    average_rating = round((sum(rating_list))/len(list_of_movies), 2)
    max_rating = 0 #starting with the minimun posible rating
    for movie in list_of_movies:
        if movie["rating"] > max_rating:
            max_rating = movie["rating"]
            max_movie = movie["name"]
    min_rating = 10 # Starting the rate with the maximum possible rating
    for movie in list_of_movies:
        if movie["rating"] < min_rating:
            min_rating = movie["rating"]
            min_movie = movie["name"]
    print(f"The average rating: {average_rating}")
    print(f"The best movie: {max_movie}, {max_rating}")
    print(f"The worst movie: {min_movie}, {min_rating}")

def print_random_movie():
    list_of_movies = movie_storage.get_movies()
    movie_count = len(list_of_movies)
    random_number = random.randrange(0, movie_count)
    random_movie = list_of_movies[random_number]
    random_movie_name = random_movie["name"]
    random_movie_rating = random_movie["rating"]
    print(f"Your movie for tonight: {random_movie_name}, it's rated {random_movie_rating}")

def print_searching_movie():
    list_of_movies = movie_storage.get_movies()
    name_part = input("Enter part of the movie name: ")
    for movie in list_of_movies:
        if name_part in movie["name"]:
            print(f"{movie["name"]}, {movie["rating"]}")

def print_sorted_movies():
    list_of_movies = movie_storage.get_movies()
    sorted_list = [] #Creating a list to store the movies in order of gratest rating
    while len(list_of_movies) > 0: #This iterate through the list until is empty
        max_rating = 0
        for movie in list_of_movies:
            if movie["rating"] > max_rating:
                max_rating = movie["rating"]
        for movie in list_of_movies:
            if max_rating in movie.values():
                sorted_list.append(movie) #Adding the movie with the greatest rating from the original list
                list_of_movies.remove(movie) #Removing the movie from the original list to iterate the left ones
    print("This are the best ranked movies from best to worst\n")
    for movie in sorted_list:
        print(f"{movie["name"]}: {movie["rating"]}")

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
        movie_rate = movie["rating"]
        output_text += '\n<li>\n'
        output_text += '<div class="movie">\n'
        output_text += f'<img class="movie-poster" src="{movie_poster}" alt="image of {movie_name}poster">\n'
        output_text += f'<div class="movie-title"> {movie_name} </div>\n'
        output_text += f'<div class="movie-year"> {movie_year} </div>\n'
        output_text += f'<div class="movie-year"> Rating: {movie_rate} </div>\n'
        output_text += f'</div>\n'
        output_text += f'</li>'

    open_and_write_html(output_text)
    print("Website was generated successfully")



def main():
    head_printing()
    number_cero = False

    while number_cero == False:
        menu_printing()

        try:
            choice_number = int(input("Enter choice (1-9) "))

            if bad_input(choice_number) == True:
                print("Incorrect Input")
            else:
                pass

            if choice_number == 1:
                print_list_option()
            elif choice_number == 2:
                add_movie()
            elif choice_number == 3:
                delete_movie()
            elif choice_number == 4:
                update_movie()
            elif choice_number == 5:
                print_stats()
            elif choice_number == 6:
                print_random_movie()
            elif choice_number == 7:
                print_searching_movie()
            elif choice_number == 8:
                print_sorted_movies()
            elif choice_number == 9:
                generate_website()
            elif choice_number == 0:
                print("Bye!")
                number_cero = True

        except ValueError as e:
            print("Invalid Input")

        enter = input("\nPress enter to continue")



if __name__ == "__main__":
    main()