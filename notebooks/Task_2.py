import csv
import json
import os
import requests
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("API_KEY")
#print("API key loaded:", api_key is not None)
# 2. Read CSV File
with open(r"C:\Users\Admin\Desktop\Training\week1-assessment\data\employee.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)
print("Rows read:", len(employees))
# 3. Write employees.json
with open("data/employees.json", "w") as file:
    json.dump(employees, file, indent=4)

# 4. Write High Earners CSV
high_earners = [
    emp for emp in employees
    if int(emp["salary"]) > 50000
]
with open("data/high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=employees[0].keys()
    )
    writer.writeheader()
    writer.writerows(high_earners)
print("High earners:", len(high_earners))

# 5. GET API Request
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()
    users = response.json()
    # Print the first user
    for user in users[:1]:

        print(
            user["id"],
            "-",
            user["name"],
            "-",
            user["email"]
        )
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

# 6. Handle 404 Error
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )
    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

# 7. Parse Nested JSON
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()
    users = response.json()
    user_details = []
    for user in users:
        details = {
            "id": user.get("id"),
            "name": user.get("name"),
            "city": user.get("address", {}).get("city"),
            "company": user.get("company", {}).get("name")
        }
        user_details.append(details)
    # Save the extracted information
    with open("data/users.json", "w") as file:
        json.dump(user_details, file, indent=4)
except requests.exceptions.RequestException as e:
    print("API error:", e)