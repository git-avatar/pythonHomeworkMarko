import random
import math



def pitagor():
    a = float(input('Enter the first cathetus:'))
    b = float(input('Enter the second cathetus:'))
    c_squared = (a**2) + (b**2)
    print(math.sqrt(c_squared))

def get_password():
    chars = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * 0 1 2 3 4 5 6 7 8 9"
    chars_list = chars.split()
    pass_len = int(input('How long do you want your password to be:'))
    password = ""
    for _ in range(0, pass_len):
        pass_char = random.choice(chars_list)
        password = password + pass_char
    return password


def check_password(password):
    if any(letter.islower() for letter in password) and  any(letter.isupper() for letter in password) and  any(letter.isdigit() for letter in password):
        print("Your password is strong!")
    else:
        print('Please make a stronger password!')


def crazy_chess():
    line  = "a b c d e f g h"
    line_list = line.split()
    column = "1 2 3 4 5 6 7 8"
    column_list = column.split()
    rand_line = random.choice(line_list)
    rand_column = random.choice(column_list)
    your_move = rand_line + rand_column
    print("Your move is:",your_move)


def get_marvelmovie():
    movies = ["Iron Man","The Incredible Hulk","Iron Man 2","Captain America: The First Avenger","Thor","The Avengers","Iron Man 3","Thor: The Dark World","Captain America: The Winter Soldier","Guardians of the Galaxy","Avengers: Age of Ultron","Ant-Man","Captain America: Civil War","Doctor Strange","Guardians of the Galaxy: Vol. 2","Spider-Man: Homecoming","Thor: Ragnarök","Black Panther","Avengers: Infinity War","Ant-Man and the Wasp","	Captain Marvel","Avengers: Endgame","Spider-Man: Far from Home","WandaVision(Disney Plus series)","Falcon and the Winter Soldier(Disney Plus series)","	Loki (Disney Plus series)","Black Widow","What If...? (Disney Plus series)","	Shang-Chi and the Legend of the Ten Rings","Eternals","Hawkeye (Disney Plus series)","Spider-Man: No Way Home","Moon Knight (Disney Plus series)","Doctor Strange in the Multiverse of Madness","Ms Marvel"]
    rand_movie = random.choice(movies)
    print("You should check out:", rand_movie)

def calc_velocity():
    distance = float(input('Enter the distance traveled in meters: '))
    time_past = float(input('Enter the time took to pass the distance in seconds:'))
    velocity = distance/time_past
    question = input("Do you want to convert it to km per hour")
    if question.lower() == "yes":
        print((velocity*1000)/3600,"kilometers per hour")
    else:
        print(velocity, "meters per second")