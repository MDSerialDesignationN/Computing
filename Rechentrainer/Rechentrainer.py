"""
Rechentrainer - Ein einfaches Mathematik-Quiz-Programm.

Dieses Programm erstellt zufällige Multiplikationsaufgaben für den Benutzer
und verfolgt die Anzahl der richtigen Antworten.
"""

import random

# Benutzer nach der gewünschten Anzahl von Runden fragen
rounds = input("Wieviele Runden möchtest du durchgehen?\n")

# Eingabevalidierung: Sicherstellen, dass eine gültige Zahl eingegeben wird
while not rounds.isdigit():
    print("Bitte eine gültige Zahl eingeben.")
    rounds = input("Wieviele Runden möchtest du durchgehen?\n")

# String in Integer konvertieren
rounds = int(rounds)
correct = 0  # Zähler für richtige Antworten

# Hauptschleife für die Quiz-Runden
for i in range(rounds):
    # Zufällige Zahlen zwischen 1 und 10 generieren
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)
    varErg = var1 * var2  # Korrekte Antwort berechnen

    # Benutzer nach der Antwort fragen
    guess = input(f"Was ist {var1} * {var2}?\n")
    
    # Antwort überprüfen und entsprechende Rückmeldung geben
    if not int(guess) == varErg:
        print(f"------ Leider falsch, die richtige Antwort ist {varErg}. ------")
    else: 
        print("------ Richtig! Gut gemacht. ------")
        correct += 1  # Zähler für richtige Antworten erhöhen

# Endergebnis anzeigen
print(f"====== Du hast {correct} von {rounds} richtig beantwortet. ======")
