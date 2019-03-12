from contextlib import redirect_stdout

name = "Naima"
greeting = ["Bonjour ", "Bonsoir "]
entreprise = "Intuition Factory"







print(greeting[0] + name)
print("J’ai consulté les projets et missions proposés par " + entreprise + \
      " . Ils  m’ont fortement intéressé ainsi que rejoindre la team " + entreprise + ". " \
                                                                                      "Mais je viens de débuter ma mission actuellement, et mon statut de salarié étranger algérien" \
                                                                                      " ne me facilite pas la tâche de changer d’employeur excepté après un an. Donc pour le moment je " \
                                                                                      "ne peux pas être à l'écoute du marché. Mais je voudrais rester en contact avec vous dans le futur pour" \
                                                                                      " de futures opportunités.")
print("Cordialement,")
print("Walid")

with open('help.txt', 'w', encoding="utf-8") as f:
    with redirect_stdout(f):
        print(greeting[0] + name)
        print("J’ai consulté les projets et missions proposés par " + entreprise + \
              " . Ils  m’ont fortement intéressé ainsi que rejoindre la team " +
              entreprise + ". " \
                           "Mais je viens de "
                           "débuter ma mission "
                           "actuellement, "
                           "et mon statut de "
                           "salarié étranger "
                           "algérien" \
                           "ne me facilite pas la "
                           "tâche de changer "
                           "d’employeur excepté "
                           "après un an. Donc pour "
                           "le moment je " \
                           "ne peux pas être à "
                           "l'écoute du marché. "
                           "Mais je voudrais "
                           "rester en contact avec "
                           "vous dans le futur "
                           "pour" \
                           "de futures "
                           "opportunités.")
        print("Cordialement,")
        print("Walid")
