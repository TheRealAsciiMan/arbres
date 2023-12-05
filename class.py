class Noeud:
    def __init__(self, etiquette:str):
        self.etiquette = etiquette
        self.enfants = []
    def ajoute_un_fils(self, noeud):
        self.enfants.append(noeud)

    def __str__(self):
        if self.enfants==[]:
            return self.etiquette
        else :
            ma_liste = self.etiquette + '('
            for e in self.enfants:
                    ma_liste += ' '
                    ma_liste += e.__str__()
            ma_liste += " )"
            return ma_liste

def hauteur(arbre:None):
    if arbre == None:
        return -1
    else:
        if arbre.enfants == []:
            return 0
        else:
            hauteurs_enfants = []
            for e in arbre.enfants:
                hauteur_enfant = hauteur(e)
                hauteurs_enfants.append(hauteur_enfant)
            return 1 + max(hauteurs_enfants)

def feuilles(arbre:None):
    if arbre == None:
        return -1
    else:
        if arbre.enfants == []:
            return 1
        else:
            noeuds_sans_fils = 0
            for e in arbre.enfants:
                noeud_sans_fils = feuilles(e)
                noeuds_sans_fils += noeud_sans_fils
            return noeuds_sans_fils

def noeuds_internes(arbre:None):
    if arbre == None:
        return -1
    else:
        if arbre.enfants == []:
            return 0
        else:
            noeuds_avec_fils = 1
            for e in arbre.enfants:
                noeuds_avec_fils += noeuds_internes(e)
            return noeuds_avec_fils





n1 = Noeud('Grand-père')
n2 = Noeud('Père')
n3 = Noeud('Tonton')
n4 = Noeud('Moi')
n5 = Noeud('Cousin')
n1.ajoute_un_fils(n2)
n1.ajoute_un_fils(n3)
n2.ajoute_un_fils(n4)
n3.ajoute_un_fils(n5)
print(n1)
print("Nombre de générations :", hauteur(n1))
print("Nombre de personnes sans enfants :", feuilles(n1))
print("Nombre de pères", noeuds_internes(n1))


