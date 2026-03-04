import smtplib
import random
from email.mime.text import MIMEText
nadawca = "labaaaaaasd@gmail.com"
haslo = haslo
wszyscy = ["Arek", "Maciek", "Michal", "Alan", "tata", "mama"]
email = ["Arek@gmail.com", "Maciek@gmail.com", "Michal@gmail.com", "alan@gmail.com", "tata@gmail.com", "mama@gmail.com"]


def main():
    wynik = []
    kopia = wszyscy.copy()
    for x in wszyscy:
        prezentowany = losowanie_dla_osoby(x, kopia)    
        if x == "mama" and prezentowany == "mama":
            return main()
        wynik.append(prezentowany)
        kopia.remove(prezentowany)
    rozeslanie(wynik, email)
    
def losowanie_dla_osoby(osoba, osoby):
    prezentowany = random.choice(osoby)
    if osoba != "mama" and osoba == prezentowany:
        return losowanie_dla_osoby(osoba, osoby)
    return prezentowany

def rozeslanie(wynik, email):
    for wybrana, mail in zip(wynik, email):
        msg = MIMEText(f"Osoba która wylosowales na swieta to:{wybrana}")
        msg["Subject"] = "losowanie swiateczne"
        msg["From"] = nadawca 
        msg["To"] = mail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(nadawca, haslo)
            server.send_message(msg)






