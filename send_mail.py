import smtplib
from personal_data import my_email, my_password

def send_mail(person_mail, _message):    
    #Create the connection
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #Call starttls
        connection.starttls()
        #Login
        connection.login(user=my_email, password=my_password)
        #Send the mail
        connection.sendmail(from_addr=my_email, to_addrs=person_mail, msg=f"Subject:HPBD\n\n{_message}")
