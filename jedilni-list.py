# -*- coding: utf-8 -*-

"""
Smartninja Web Development 1 – naloga Jedilni list
Tvoj prijatelj je bil tako zadovoljen s tvojim programom, da je vsem poznanim povedal kako super programer/ka si! Neki lastnik restavracije je tako slišal zate in te nemudoma kontaktiral.
Rad bi namreč imel program, v katerega vneseš dnevni meni: vsako jed posebej ter ceno zanjo. Jedi se nato shranijo v datoteko menu.txt.
"""

dnevni_meni = {}

while True:
    jed = raw_input("Vnesi jed: ")
    cena = raw_input("Vnesi ceno: ")
    dnevni_meni[jed] = cena
#   dnevni_meni.update({jed:cena})
    new = raw_input("Boš vnesel še eno jed in ceno? (da/ne) ")
    if new == "ne":
        break

with open("menu.txt", "w+") as menu_file:
    menu_file.write ("Dnevni meni:\n")
    for jed, cena in dnevni_meni.iteritems():
        menu_file.write("%s: %s \n" %(jed, cena))