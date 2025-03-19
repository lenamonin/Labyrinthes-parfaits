import matplotlib.pyplot as plt
class Case:
    """Classe définissant une case à l'aide de bouléen pour la présence des murs"""
    def __init__(self,l,c):
        self._bas=True  #attribut indiquant la présence (True) ou non (False) du mur bas
        self._haut=True  #attribut indiquant la présence (True) ou non (False) du mur haut
        self._gauche=True  #attribut indiquant la présence (True) ou non (False) du mur gauche
        self._droite=True  #attribut indiquant la présence (True) ou non (False) du mur droit
        self._posL=l #indice de la ligne de la case dans le labyrinthe
        self._posC=c #indice de la colonne de la case dans le labyrinthe
        self._visit=False # indique si la case à été visité ou non, utilisé pour la création du labyrinthe parfait
        
       
    #méthodes pour retirer les murs, on change juste la valeur de l'attribut correspondant
    def retirer_mur_haut(self):
        self._haut=False
    def retirer_mur_bas(self):
        self._bas=False
    def retirer_mur_droite(self):
        self._droite=False
    def retirer_mur_gauche(self):
        self._gauche=False
        
    #fonction/méthode appelé à l'affichage du labyrinthe
    def afficher(self):
        L=[]#on crée la liste qu'on renvoie à la fin
        #pour chaque mur on renvoie ses indices pour le tracer sur plt.figure() de la fonction afficher du labyrinthe
        #'k' pour le dessiner si il est présent et 'w' pour ne pas le dessiner (dessine le mur en blanc sur fond blanc)
        if self._haut :
            L.append([[self._posC , self._posC+ 1], [self._posL, self._posL], 'k'])
        else:
            L.append([[self._posC , self._posC+ 1], [self._posL, self._posL], 'w'])
        if self._droite:
            L.append([[self._posC+ 1, self._posC+ 1], [self._posL, self._posL+ 1], 'k'])
        else:
            L.append([[self._posC+ 1, self._posC+ 1], [self._posL, self._posL+ 1], 'w'])
        if self._gauche:
            L.append([[self._posC , self._posC], [self._posL, self._posL+ 1], 'k'])
        else:
            L.append([[self._posC, self._posC], [self._posL, self._posL+ 1], 'w'])
        if self._bas:
            L.append([[self._posC, self._posC+ 1] ,[self._posL+ 1, self._posL + 1], 'k'])
        else:
            L.append([[self._posC, self._posC+ 1], [self._posL + 1, self._posL + 1],'w'])
        #on renvoie la liste
        return L
    #méthode/fonction renvoyant les indices des cases voisines
    def voisines(self,m,n):
        L=[]#liste pour stocker les couple d'indices
        #si la ligne est supérieure à 0 on récupère les indices de la case de la ligne du dessus 
        if self._posL>0:
            L.append((self._posL-1,self._posC))
        #si la colonne est supérieure à 0 on récupère les indices de la case de la colonne de gauche 
        if self._posC>0:
            L.append((self._posL,self._posC-1))
        #si la ligne est inférieure au nb de ligne du labyrinthe on récupère les indices de la case de la ligne en dessous
        if self._posL<m:
            L.append((self._posL+1,self._posC))
        #si la colonne est inférieure au nb de colonne du labyrinthe on récupère les indices de la case de la colonne de droite 
        if self._posC<n:
            L.append((self._posL,self._posC+1))
        #on renvoie la liste de couple d'indice
        return L
