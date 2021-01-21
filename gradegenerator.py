def Average(lst):
    return sum(lst) / len(lst)

def teilbereich(var):
    noten = []
    for x in var.split(","):
        if x[-1] == "+":
            noten.append(int(x[0]) - 0.4)
        elif x[-1] == "-":
            noten.append(int(x[0]) + 0.4)
        else:
            noten.append(int(x))
    durchschnitt = round(Average(noten), 2)
    return durchschnitt


name = str(input("Name: \n")).title()
noten_lesen = input("Gib alle Noten für den Bereich Lesen ein: \n")
noten_su = input("Gib alle Noten für den Bereich Sachunterricht ein: \n")
noten_rs = input("Gib alle Noten für den Bereich Rechtschreibung ein: \n")
noten_s = input("Gib alle Noten für den Bereich Schreiben ein: \n")

lesen_gesamt = teilbereich(noten_lesen)
su_gesamt = teilbereich(noten_su)
rs_gesamt = teilbereich(noten_rs)
s_gesamt = teilbereich(noten_s)
alle = [lesen_gesamt, su_gesamt, rs_gesamt, s_gesamt]
#the factors 8, 6, and 5 reflect the weights of the different subgrades
#change them according to your needs
finale_note = (lesen_gesamt * 8 + su_gesamt * 6 + rs_gesamt * 5 + s_gesamt) / 20
print(f"{name} hat in Deutsch die Note {finale_note} bekommen.")
