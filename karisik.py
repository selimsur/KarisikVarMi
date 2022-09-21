# Password Generator for SallaPass

import random
import string
import pyfiglet


ascii_c = pyfiglet.figlet_format("HSS")
print(ascii_c)

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+")

def generate_random_password():
    length = int(input("Enter the length of the password: ")) 
    random.shuffle(characters)  
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))
    
generate_random_password()