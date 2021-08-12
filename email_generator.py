from faker import Faker
import random 

print("Enter the number of emails you want to create: ")
user_input = int(input())

for x in range(user_input):
    fk = Faker()
    first_name = fk.first_name()
    last_name = fk.last_name()

    dot = ["", ".", "_"]
    dt = random.choice(dot)
    emailService = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "me.com", "icloud.com"]
    es = random.choice(emailService)
    randNum = str(random.randint(1, 199))

    email = first_name.lower() + dt + last_name.lower() + randNum + "@" + es

    print(email)


