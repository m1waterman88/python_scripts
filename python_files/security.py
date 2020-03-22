"""
Security:
    General:
        Put sensitive data in environ vars.
    Type in password (stdin):
        .
"""

from getpass import getpass

username = input("username: ")
# password = input("password: ")
password = getpass("password: ")
print("Logging in...")
