import random
import string

def generate_password():

    length = int(input("Enter the length of your password").strip())
    include_upper = input("Do you want to include upper case? (Yes/No)").lower().strip()
    include_special = input("Do you want to include special character? (Yes/No)").lower().strip()
    include_number = input("Do you want to include numbers? (Yes/No)").lower().strip()

    if length<=4:
        print ("Password length should be more than 4")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    number = string.digits if include_number == "yes" else ""

    all_characters = lower+upper+special+number

    password = []

    password.append(random.choice(upper))
    password.append(random.choice(special))
    password.append(random.choice(number))

    remaining_length = length - len(password)

    for _ in range (remaining_length):
        password.append((random.choice(all_characters)))

    random.shuffle(password)
    strong_password = "".join(password)
    return strong_password

new_password = generate_password()
print(new_password)