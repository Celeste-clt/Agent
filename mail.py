import json
import os

MAIL_FILE = "mails.json"


def creer_mail(destinataire, sujet, contenu):
    mail = {
        "destinataire": destinataire,
        "sujet": sujet,
        "contenu": contenu
    }

    with open(MAIL_FILE, "a", encoding="utf-8") as f:
        json.dump(mail, f, ensure_ascii=False)
        f.write("\n")

    print("Mail enregistré (mails.json)")


def compter_mails():
    if not os.path.exists(MAIL_FILE):
        return 0
    with open(MAIL_FILE, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def lister_mails():
    if not os.path.exists(MAIL_FILE):
        return []
    mails = []
    with open(MAIL_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            mail = json.loads(line)
            mails.append((i, mail))
    return mails


def lire_mail(numero):
    mails = lister_mails()
    for i, mail in mails:
        if i == numero:
            return mail
    return None


def supprimer_mail(numero):
    mails = lister_mails()
    mails_restants = [mail for i, mail in mails if i != numero]
    with open(MAIL_FILE, "w", encoding="utf-8") as f:
        for mail in mails_restants:
            json.dump(mail, f, ensure_ascii=False)
            f.write("\n")
    print(f"Mail {numero} supprimé." if mails_restants else "Aucun mail supprimé.")
