import smtplib, ssl, os, shutil
from datetime import datetime
from email.message import EmailMessage
from tkinter import END

output_box = None

def set_output_widget(widget):
    global output_box
    output_box = widget

def print_to_output(text):
    if output_box:
        output_box.insert(END, text + "\n")
        output_box.see(END)

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
        print_to_output("File not found")
    return archieve

def save_archieve(archieve, file):
    with open(file, "w", encoding="utf-8") as f:
        for name, number, email in zip(*archieve):
            f.write(f"{name}|{number}|{email}\n")
    print_to_output("Changes saved.")

def add_contact(archieve, name, number, email):
    archieve[0].append(name)
    archieve[1].append(number)
    archieve[2].append(email)
    return f"The contact '{name}' has been added to the archive."

def search_contact(archieve, contact):
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
    if name in archieve[0]:
        index = archieve[0].index(name)
        for lst in archieve:
            lst.pop(index)
        return f"The contact '{name}' has been removed from the archive."
    return f"Contact '{name}' not found."

def change_contact(archieve, name, new_name, new_number, new_email):
    if name in archieve[0]:
        index = archieve[0].index(name)
        archieve[0][index] = new_name
        archieve[1][index] = new_number
        archieve[2][index] = new_email
        return f"The contact '{name}' has been updated."
    return f"The contact '{name}' is not in the archive."

def show_archieve(archieve):
    output_box.delete(1.0, END)
    if not archieve[0]:
        print_to_output("Archive is empty.")
        return
    for i in range(len(archieve[0])):
        print_to_output(f"{i+1}. {archieve[0][i]} | {archieve[1][i]} | {archieve[2][i]}")

def sort_archieve(archieve):
    combined = list(zip(archieve[0], archieve[1], archieve[2]))
    combined.sort()
    for i in range(len(combined)):
        archieve[0][i], archieve[1][i], archieve[2][i] = combined[i]
    print_to_output("Archeive sorted.")




def handle_email_sending(archieve, recipient, password):
    kiri = "Tere, see on test"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "alexxxey.ivanovvv@gmail.com"
    
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "Test"
    msg['From'] = kellelt
    msg['To'] = recipient
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=context)
        server.login(kellelt, password)
        server.send_message(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
    finally:
        server.quit()



def share_contact_by_email(archieve, recipient, password):
    """Send the contact list via email"""
    contact_list = "My Contacts:\n\n" + "\n".join(
        f"{name} | {number} | {email}" 
        for name, number, email in zip(*archieve)
    )
    
    sender_email = "alexxxey.ivanovvv@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    msg = EmailMessage()
    msg.set_content(contact_list)
    msg['Subject'] = "Shared Contact List"
    msg['From'] = sender_email
    msg['To'] = recipient
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        return "Contact list sent successfully!"
    except Exception as e:
        return f"Failed to send contacts: {str(e)}"


def backup_archieve():
    try:
        shutil.copy("archieve.txt", f"archieve_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        print_to_output("Backup created.")
    except:
        print_to_output(f"Backup failed")

def delete_archieve_file():
    try:
        os.remove("archieve.txt")
        print_to_output("Archive file deleted.")
    except:
        print_to_output(f"Error deleting archive:")
