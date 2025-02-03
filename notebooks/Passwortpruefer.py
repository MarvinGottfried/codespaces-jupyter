def pruefe_eingabe(eingabe):
    pattern = r"^(?=.[A-Z])(?=.[^\w\s])(?=.*[0-9]).{8,16}$"
    if re.fullmatch(pattern, eingabe):
        return "Eingabe ist gültig!"
    else:
        return "Eingabe ist ungültig!"

pruefe_eingabe(input(f"Bitte geben Sie ein Passwort ein, welches folgende Anforderungen erfüllt: \nmind. 1 Großbuchstaben \nmind. 1 Ziffer \nmind. 1 Sonderzeichen \nLänge von 8-16 Zeichen")) 
