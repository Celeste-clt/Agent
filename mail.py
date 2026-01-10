import json


def creer_mail(destinataire, sujet, contenu):
    mail = {
        "destinataire": destinataire,
        "sujet": sujet,
        "contenu": contenu
    }

    with open("mails.json", "a", encoding="utf-8") as f:
        json.dump(mail, f, ensure_ascii=False)
        f.write("\n")

    print(" Mail enregistré (mails.json)")
