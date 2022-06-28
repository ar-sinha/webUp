import winsound
import webbrowser
from random import seed
import requests
import time


print("NOTE: Please try to copy and paste the link from the address bar of the browser,\ninstead of typing manually\n")
print("Paste the URL and press enter:\n")
url = input()

while url[:4] != "http":
    print("Invalid URL, please try again\n")
    print("A valid URL shall start with http\n")
    url = input()

print("The program will check for site availability every n seconds\n")
print("Please enter your desired value of interval n")
interval = float(input())

session_obj = requests.Session()
response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})

print("Checking if the site is up\n")
print("This program will beep 3 times and open the URL in a new tab in your default browser, once the site is back\n")

i = 1

while response.status_code != 200 and response.status_code != 400:
    response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})
    print("Trying... [attempt number: " + str(i) + "]")
    i = i+1
    time.sleep(interval)
 
print("\nHurray, the site is back up !")
print("\nOpening the site for you....\n")
webbrowser.open(url)

print("\nSite is now open in a new tab with your default browser\n")

for i in range(3):
    winsound.Beep(440, 500)

print("You can now close this application by pressing Enter key\n")
ex = input()
