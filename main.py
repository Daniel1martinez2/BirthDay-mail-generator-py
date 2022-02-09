from random import choice
import pandas as pd
import datetime as dt
from send_mail import send_mail

#Get the people info from the csv file
people = pd.read_csv("./birthdays.csv")
#Set the letters template list
letters = [
    "./templates/letter_1.txt",
    "./templates/letter_2.txt",
    "./templates/letter_3.txt"
]
today = dt.datetime.now()
today_tuple = (today.month, today.day)
#Get a random letter from the given list
random_letter = choice(letters)
#iterate from the people list

#Other way
data = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in people.iterrows()}
if today_tuple in data:
    birthday_person = data[today_tuple]
    with open( random_letter ) as letter:
            #Replace the current chosen letter name with the actual person name
            letter_str = letter.read().replace("[NAME]", birthday_person["name"])
            #Send the mail
            send_mail(birthday_person["email"], letter_str)