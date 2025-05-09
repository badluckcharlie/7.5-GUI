
import smtplib,ssl
from email.message import EmailMessage




def load_archieve(file):
    archieve = [[], [], []]
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        name, number, email = parts
                        archieve[0].append(name)
                        archieve[1].append(number)
                        archieve[2].append(email)
    except FileNotFoundError:
        print("File not found")
    return archieve

def send_email():
    kellele = input("Kellele: ")
    kiri = "Tere, see on test"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "alexxxey.ivanovvv@gmail.com"
    parool = input("Parool: ")  # "vknn ongl tfdt vuct"
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "Test"
    msg['From'] = kellelt
    msg['To'] = kellele
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellelt, parool)
        server.send_message(msg)
        print("kiri saadetud")
    except Exception as e:
        print("Viga", e)
    finally:
        server.quit()

def add_contact(archieve, name, number, email):
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    archieve[0].append(name)
    archieve[1].append(number)
    archieve[2].append(email)
    return f"The contact '{name}' has been added to the archieve"

def search_contact(archieve, contact):
    contact= input("Enter name/number/email to search")
    if contact in archieve[0]:
        index = archieve[0].index(contact)
    elif contact in archieve[1]:
        index = archieve[1].index(contact)
    elif contact in archieve[2]:
        index = archieve[2].index(contact)
    else:
        return f"'{contact}' is not found."
    
    return (f"Contact found:\n"
            f"Name: {archieve[0][index]}\n"
            f"Number: {archieve[1][index]}\n"
            f"Email: {archieve[2][index]}")

def delete_contact(archieve, name):
    name = input("Enter name to delete: ")
    if name in archieve[0]:
        index = archieve[0].index(name)
        for lst in archieve:
            lst.pop(index)
        return f"The contact '{name}' has been removed from the archieve."
    return f"Contact '{name}' not found."

def change_contact(archieve, name, new_name, new_number, new_email):
    name = input("Enter name of contact to edit: ")
    if name in archieve[0]:
        index = archieve[0].index(name)
        archieve[0][index] = new_name
        archieve[1][index] = new_number
        archieve[2][index] = new_email
        return f"The {name} has been edited."
    else:
        return f"The {name} is not present within the archieve."

def sort_archieve(archieve):
    combined = list(zip(archieve[0], archieve[1], archieve[2]))
    combined.sort()
    for i in range(len(combined)):
        archieve[0][i], archieve[1][i], archieve[2][i] = combined[i]

def show_archieve(archieve):
    for i in range(len(archieve[0])):
        print(f"{archieve[0][i]} - {archieve[1][i]} - {archieve[2][i]}")

def save_archieve(archieve, file):
    with open(file, "w", encoding="utf-8-sig") as f:
        for i in range(len(archieve[0])):
            f.write(f"{archieve[0][i]}|{archieve[1][i]}|{archieve[2][i]}\n")