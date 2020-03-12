# _*_ coding: utf-8 _*_

password = "SecretCode1"
name = "mike".title()
attempt = input("Enter password: ")
attempt_count = 1

while attempt_count < 5:
    if attempt == password:
        print("Welcome, " + name + "!")
        break
    elif (attempt != password) and (attempt_count < 5):
        print("The username and password combination is not recognized")
        attempt_count += 1
        attempt = input("Re-enter Password: ")
if (attempt != password) and (attempt_count >= 5):
    print("Your account has been locked. Please contact your system administrator.")


"""
username = "Enter username: ")
password = (SELECT gobtpad_password
            FROM spriden, gobtpad
            WHERE spriden_pidm = gobtpad_pidm
                AND password = gobtpad_third_party_id)
name = (SELECT spriden_first_name
        FROM spriden, gobtpad
        WHERE spriden_pidm = gobtpad_pidm
            AND username = gobtpad_third_party_id)
attempt = input("Enter password: ")
attempt_count = 1

while attempt_count < 5:
    if attempt == password:
        print("Welcome, " + name + "!")
        break
    elif (attempt != password) and (attempt_count < 5):
        print("The username and password combination is not recognized")
        attempt_count += 1
        attempt = input("Re-enter Password: ")
if (attempt != password) and (attempt_count >= 5):
    print("Your account has been locked. Please contact your system administrator.")
"""
