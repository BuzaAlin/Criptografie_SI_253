def este_cheie2_valida(cheie2):
    return cheie2.isalpha() and len(cheie2) >= 7

def litera_la_numar(litera):
    # Convertim literă la poziția din alfabet: A=0, B=1, ..., Z=25
    return ord(litera.upper()) - ord('A')

def shift_litera(litera, shift, operatie):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pozitie = alfabet.index(litera)
    
    if operatie == 'criptare':
        noua_pozitie = (pozitie + shift) % 26
    elif operatie == 'decriptare':
        noua_pozitie = (pozitie - shift) % 26
    else:
        return litera  # în caz de eroare, returnăm litera originală

    return alfabet[noua_pozitie]

def cezar_doua_chei(mesaj, cheie1, cheie2, operatie):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mesaj = mesaj.upper().replace(" ", "")
    cheie2 = cheie2.upper()

    rezultat = ""

    for i, litera in enumerate(mesaj):
        if litera not in alfabet:
            continue  # ignorăm caracterele non-alfabetice

        # Pasul 1: shift cu cheia 1
        litera1 = shift_litera(litera, cheie1, operatie)

        # Pasul 2: shift cu cheia 2, pe baza literei corespunzătoare din cheie
        litera_din_cheie2 = cheie2[i % len(cheie2)]  # repetăm cheia 2 dacă e mai scurtă/daca mesajul e mai lung se repeta ciclic
        shift2 = litera_la_numar(litera_din_cheie2)

        litera2 = shift_litera(litera1, shift2, operatie)

        rezultat += litera2

    return rezultat


# --- Interacțiune cu utilizatorul ---

# Citim cheia 1
cheie1 = int(input("Introdu cheia 1 (număr între 1 și 25): "))
if not (1 <= cheie1 <= 25):
    print("Cheia 1 trebuie să fie între 1 și 25.")
    exit()

# Citim cheia 2
cheie2 = input("Introdu cheia 2 (minim 7 litere, doar A-Z): ")
if not este_cheie2_valida(cheie2):
    print("Cheia 2 trebuie să aibă minim 7 litere și să conțină doar caractere A-Z/a-z.")
    exit()

# Citim mesajul
mesaj = input("Introdu mesajul: ")

# Citim operația
operatie = input("Introdu operația (criptare/decriptare): ").lower()
if operatie not in ['criptare', 'decriptare']:
    print("Operația trebuie să fie 'criptare' sau 'decriptare'.")
    exit()

# Apelăm funcția
rezultat = cezar_doua_chei(mesaj, cheie1, cheie2, operatie)

print("Rezultat:", rezultat)
