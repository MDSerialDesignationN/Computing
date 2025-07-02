EINGABE anzahl_runden
richtige_antworten = 0

FÜR RUNDE IN anzahl_runden
    zahl1 = ZUFALLSZAHL(1, 10)
    zahl2 = ZUFALLSZAHL(1, 10)
    ergebnis = zahl1 * zahl2
    
    AUSGABE "Was ist " + zahl1 + " × " + zahl2 + "?"
    EINGABE antwort
    
    WENN antwort = ergebnis DANN
        AUSGABE "Richtig!"
        richtige_antworten = richtige_antworten + 1
    SONST
        AUSGABE "Falsch! Richtige Antwort: " + ergebnis
    ENDE WENN
ENDE SCHLEIFE

AUSGABE "Ergebnis: " + richtige_antworten + " von " + anzahl_runden