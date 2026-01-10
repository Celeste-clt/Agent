def ajouter_evenement(date, lieu, titre):
    with open("events.txt", "a", encoding="utf-8") as f:
        f.write(f"{date} | {lieu} | {titre}\n")

    print("Événement ajouté ")
