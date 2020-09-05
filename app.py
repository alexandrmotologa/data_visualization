from modules.subscribers.utils import loadSubscribers
from modules.subscribers.email import sendEmail
import re

subscribers = loadSubscribers()


def all_user():
    for i in range(len(subscribers)):
        sendEmail(subscribers[i]['email'], subscribers[i]['name'], 'emailsend@gmail.com', "passemailsend")


def one_user(one):
    for i in range(len(subscribers)):
        if one == subscribers[i]['email']:
            sendEmail(subscribers[i]['email'], subscribers[i]['name'], 'emailsend@gmail.com', "passemailsend")
            print(i)


def user_wth_db():
    em = input("Email: ")
    nm = input("Name: ")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    def check(email):
        if (re.search(regex, email)):
            sendEmail(em, nm, 'emailsend@gmail.com', "passemailsend")
        else:
            print("Invalid Email")
    check(em)


def menu():
    try:
        option = -1
        while option != 0:
            print("######### HI ##########")
            print(">> 1. ALL Email and Name with DB")
            print(">> 2. Send Email for 1 person without DB")
            print(">> 3. Send Email for 1 person with DB")
            print(">> 4. Send Email for ALL Email with DB")
            print("######### END ##########")

            option = int(input())
            if option == 1:
                for i in range(len(subscribers)):
                    print(f"Email: {subscribers[i]['email']:30} Name: {subscribers[i]['name']:30}")
            if option == 2:
                user_wth_db()
            if option == 3:
                one_user(input("Please write email address: "))
            if option == 4:
                all_user()
    except ValueError:
        print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
        menu()
    except KeyError:
        print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
        menu()
    except IndexError:
        print("##### ERROR ##### TRY AGAIN ##### ERROR #####")
        menu()


menu()
