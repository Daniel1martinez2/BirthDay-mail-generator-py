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
#Get a random letter from the given list
random_letter = choice(letters)
#iterate from the people list
for (index, row) in people.iterrows():
    #Getting the values from each person
    name = row["name"]
    email = row["email"]
    year = row["year"]
    month = row["month"]
    day = row["day"]
    #Construct the date time obj from the given info
    person_b_date =  dt.datetime(year=year, month=month, day=day)
    #Check wether the current date match with the current person bd date
    if person_b_date.weekday() == dt.datetime.now().weekday():
        #Open the letter file
        with open( random_letter ) as letter:
            #Replace the current chosen letter name with the actual person name
            letter_str = letter.read().replace("[NAME]", name)
            #Send the mail
            send_mail(email, letter_str)






