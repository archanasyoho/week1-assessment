import csv

# 1. Function with *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = salary * rate + sum(extras)
    # Apply the cap if provided
    if "cap" in options:
        total_bonus = min(total_bonus, options["cap"])
    return total_bonus

#print("Bonus:", bonus(50000, 0.1, 1000, 2000, cap=5000))

# 2. Custom Exception
class InvalidSalaryError(Exception):
    pass

# 3. Employee Class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(
                f"Invalid salary: {salary}"
            )
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"{self.name} earns {self.salary}"

# 3. Manager Class

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return (
            f"{self.name} manages "
            f"{self.team_size} employees"
        )

# 4. Create Employee Objects
employee = Employee("Arun", 30000)
manager = Manager("Priya", 60000, 5)
#print(employee.annual_salary())
#print(employee.get_details())
#print(manager.get_details())


# 5. Reading CSV File
with open(r"C:\Users\Admin\Desktop\Training\week1-assessment\data\employee.csv", "r") as file:
    reader= csv.DictReader(file)
    employees=list(reader)

#Convert salary from string to integer
for emp in employees:
    emp['salary']=int(emp['salary']) 


# 6. List Comprehension
# Names with salary above 50000
high_salary_names = [
    emp["name"]
    for emp in employees
    if emp["salary"] > 50000
]
print("Above 50000:", high_salary_names)

# 7. Map and Lambda
# Add 10% raise
raised_salaries = list(
    map(
        lambda emp: emp["salary"] * 1.10,
        employees
    )
)
#print("Raised salaries:", raised_salaries)

# 8. Filter
# Chennai employees
chennai_employees = list(
    filter(
        lambda emp: emp["city"] == "Chennai",
        employees
    )
)
chennai_names = [
    emp["name"] for emp in chennai_employees
]
print("Chennai:", chennai_names)

# 9. Handle Invalid Salary
try:
    employee = Employee("Test", -500)
except InvalidSalaryError as e:
    print("Error:", e)
finally:
    print("Transaction finished")

# 10. For Loop with Continue and Break
salaries = [30000, 0, 45000, 90000, 60000]
for salary in salaries:
    # Skip salary 0
    if salary == 0:
        continue
    # Stop after the first salary above 85000
    if salary > 85000:
        break
    print("Salary:", salary)