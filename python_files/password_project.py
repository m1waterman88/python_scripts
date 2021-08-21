#!/usr/bin/env python3

"""A way to get familiar with Python."""

# very database, much hashed and salted
password = "SecretCode1"
name = "mike".title()

attempt = input("Enter password: ")
attempt_count = 1

while attempt_count < 5:
    if attempt == password:
        print("Welcome, " + name + "!")
        break
    else:
        print("The username and password combination is not recognized")
        attempt_count += 1
        attempt = input("Re-enter Password: ")

if attempt != password and attempt_count >= 5:
    print("Your account has been locked. Please contact your system administrator.")
