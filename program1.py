def cezar(mesaj, cheie, operatie):
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rezultat = ''

    for litera in mesaj:                                      # Parcurgem fiecare literă din mesaj
        if litera not in alfabet:                             # Ignorăm caracterele care nu sunt în alfabet
            continue
        pozitie = alfabet.index(litera)                             # Găsim poziția literei în alfabet

        if operatie == 'criptare':                            # Mutăm în față cu cheia (modulo lungimea alfabetului)
            pozitie_noua = (pozitie + cheie) % 26             
        elif operatie == 'decriptare':                        # Mutăm înapoi cu cheia (modulo lungimea alfabetului)
            pozitie_noua = (pozitie - cheie) % 26             
        else:                                                 # Dacă operația nu este validă, returnăm mesajul original
            return mesaj
        
        rezultat += alfabet[pozitie_noua]                     # Adăugăm litera nouă la rezultat

    return rezultat

cheie = int(input("1. Introdu cheia (1-25): "))                  # Citim cheia, transformăm în int și verificăm să fie între 1 și 25

if not (1 <= cheie <= 25):
    print("Cheia trebuie să fie între 1 și 25.")
    exit()

mesaj = input("Introdu mesajul: ").upper()                    # Citim mesajul și îl transformăm în majuscule

operatie = input("Introdu operația (criptare/decriptare): ").lower()             # Citim operația dorită

rezultat = cezar(mesaj, cheie, operatie)                      # Apelăm funcția și afișăm rezultatul

print("Rezultat:", rezultat)
