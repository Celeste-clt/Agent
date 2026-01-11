import requests
import os
from music import jouer_musique
from add import creer_fichier, modifier_fichier, supprimer_fichier
from agenda import ajouter_evenement
from mail import creer_mail, compter_mails, lister_mails, lire_mail, supprimer_mail

# URL du serveur LLaMA local 
LLAMA_SERVER_URL = "http://127.0.0.1:8080"


# -------- LLaMA --------
def ask_llama(prompt):
    """
    Envoie le prompt au serveur LLaMA et récupère la réponse
    """
    payload = {
        "prompt": prompt,
        "max_tokens": 256
    }
    try:
        response = requests.post(f"{LLAMA_SERVER_URL}/v1/completions", json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["text"].strip()
    except Exception as e:
        print("Erreur LLaMA :", e)
        return ""


def analyser_phrase_ia(phrase):
    """
    Détecte l'action à effectuer.
    Vérification locale avant envoi au modèle LLaMA.
    """
    phrase_lower = phrase.lower()

    # Détection locale prioritaire
    if any(mot in phrase_lower for mot in ["rendez-vous", "événement", "évènements", "date", "anniversaire"]):
        return "evenement"
    if any(mot in phrase_lower for mot in ["musique", "chanson", "écoute"]):
        return "musique"
    if any(mot in phrase_lower for mot in ["mail", "email", "courrier"]):
        return "mail"
    if any(mot in phrase_lower for mot in ["crée", "creer", "nouveau fichier"]):
        return "creer_fichier"
    if any(mot in phrase_lower for mot in ["modifie", "modifier"]):
        return "modifier_fichier"
    if any(mot in phrase_lower for mot in ["supprime", "supprimer"]):
        return "supprimer_fichier"
    if any(mot in phrase_lower for mot in ["quit", "quitte", "au revoir"]):
        return "quit"
    
    # Sinon, renvoyer None pour chat libre
    return None


#  Chat libre
def chat_libre(phrase):
    """
    Utilise LLaMA pour répondre de manière si aucune action n'est détectée.
    """
    prompt = f"L'utilisateur dit : {phrase}\nRéponse"
    reponse = ask_llama(prompt)
    return reponse if reponse else "Désolé, je n'ai pas compris."


# Main 
def main():
    print(" Agent IA lancé. Bonjour je t'écoute !")

    while True:
        phrase = input("> ")
        action = analyser_phrase_ia(phrase)

        # Musique
        if action == "musique":
            fichier = input("Quel fichier audio ? : ")
            chemin = os.path.join("musique", fichier)
            jouer_musique(chemin)

        # Mail
        elif action == "mail":
            print("\nQue veux-tu faire avec les mails ?")
            print("1. Créer un mail")
            print("2. Compter les mails")
            print("3. Lister les mails")
            print("4. Lire un mail")
            print("5. Supprimer un mail")
            choix = input("Choix (1-5) : ")

            if choix == "1":
                destinataire = input("Destinataire : ")
                sujet = input("Sujet : ")
                contenu = input("Contenu : ")
                creer_mail(destinataire, sujet, contenu)

            elif choix == "2":
                nb = compter_mails()
                print(f"Tu as {nb} mail(s).")

            elif choix == "3":
                mails = lister_mails()
                if not mails:
                    print("Aucun mail enregistré.")
                else:
                    for i, mail in mails:
                        print(f"{i}. {mail['sujet']} à {mail['destinataire']}")

            elif choix == "4":
                try:
                    numero = int(input("Numéro du mail à lire : "))
                    mail = lire_mail(numero)
                    if mail:
                        print(f"Mail {numero} - Destinataire : {mail['destinataire']}, Sujet : {mail['sujet']}\nContenu : {mail['contenu']}")
                    else:
                        print("Mail introuvable.")
                except ValueError:
                    print("Numéro invalide.")

            elif choix == "5":
                try:
                    numero = int(input("Numéro du mail à supprimer : "))
                    supprimer_mail(numero)
                except ValueError:
                    print("Numéro invalide.")

            else:
                print("Choix invalide.")

        # Fichier
        elif action == "creer_fichier":
            nom = input("Nom du fichier à créer (ex: test.txt) : ")
            creer_fichier(nom)

        elif action == "modifier_fichier":
            nom = input("Nom du fichier à modifier : ")
            modifier_fichier(nom)

        elif action == "supprimer_fichier":
            nom = input("Nom du fichier à supprimer : ")
            supprimer_fichier(nom)

        # Événement
        elif action == "evenement":
            date = input("Date de l'événement (JJ/MM/AAAA) : ")
            lieu = input("Lieu : ")
            titre = input("Titre : ")
            ajouter_evenement(date, lieu, titre)

        elif action == "quit":
            print("À bientôt !")
            break

        else:
            print(chat_libre(phrase))


if __name__ == "__main__":
    main()
