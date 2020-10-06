#!/usr/bin/env python3

"""Display an archived site from the era input."""

import webbrowser

import requests

print("Let's find an old website.")

site = input("Enter a URL: ")
era = input("Type a year, month, and day like 20150613: ")

url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
response = requests.get(url)
data = response.json()

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print(f"Found this copy: {old_site}")
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print(f"Sorry... no luck finding {site}")
