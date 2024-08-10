import string 
import random

def psw_gen(length,digits,uppercase,lowercase,symbols):
    password = ""
    required_characters = []

    if digits : password +=string.digits
    required_characters.append(random.choice(string.digits))

    if uppercase : password +=string.ascii_uppercase
    required_characters.append(random.choice(string.ascii_uppercase))

    if lowercase : password +=string.ascii_lowercase
    required_characters.append(random.choice(string.ascii_lowercase))

    if symbols : password +=string.punctuation
    required_characters.append(random.choice(string.punctuation))

    if not password:
     return "No characters selected to generate a password."

    final = "".join(random.choice(password) for _ in range(length))
    return final


length = int(input("please enter the number of caractrers:"))
digits = input("Do you want you password to contai  numbers ? (Y/N)").upper()=="Y"
symbols = input("Do you want your password to contain symbols ? (Y/N)").upper()=="Y"
lowercase = input("Do you want your password to include lowercase ? (Y/N)").upper()=="Y"
uppercase = input("Do you want your password to include uppercase ? (Y/N)").upper()=="Y"

final = psw_gen(length,digits,lowercase,uppercase,symbols )

if final : 
   print ( "here's your password ",final)
   
