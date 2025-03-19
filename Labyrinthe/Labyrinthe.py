import matplotlib.pyplot as plt
import random
from Case import *
from collections import deque
class Labyrinthe:
    """Classe définissant un labyrinthe """
    def __init__(self,m ,n):
        #liste double permettant de stocker et initialiser chaque case du labyrinthe
        self._graphe_cases = [[Case(i,j) for j in range(n)] for i in range(m)]
        #nb ligne
        self._taille_l=m
        #nb colonne
        self._taille_c=n
    
    #fonctions/méthodes pour retirer les murs des cases pour assurer le bon affichage du labyrinthe
    def retirer_mur_haut(self,i,j):
        #on retire le mur haut de la case d'indice i,j donné en paramètre
        self._graphe_cases[i][j].retirer_mur_haut()
        #si il y a une case au dessus d'elle, on reture son mur bas (le mur bas de la case supérieure)
        if i>0:
            self._graphe_cases[i-1][j].retirer_mur_bas()
    def retirer_mur_bas(self,i,j):
        #on retire le bas haut de la case d'indice i,j donné en paramètre
        self._graphe_cases[i][j].retirer_mur_bas()
        #si il y a une case en dessous d'elle, on reture son mur haut (le mur haut de la case inférieure)
        if i<self._taille_l-1:
            self._graphe_cases[i+1][j].retirer_mur_haut()
    def retirer_mur_droite(self,i,j):
        #on retire le mur droit de la case d'indice i,j donné en paramètre
        self._graphe_cases[i][j].retirer_mur_droite()
        #si il y a une case à droite d'elle, on reture son mur gauche 
        if j<self._taille_c-1:
            self._graphe_cases[i][j+1].retirer_mur_gauche()
    def retirer_mur_gauche(self,i,j):
        #on retire le mur gauche de la case d'indice i,j donné en paramètre
        self._graphe_cases[i][j].retirer_mur_gauche()
        #si il y a une case à gauche d'elle, on reture son mur droit 
        if j>0:
            self._graphe_cases[i][j-1].retirer_mur_droite()
            
    #méthode utilisé dans la création du labyrinthe parfait pour retirer le mur séparant deux cases
    #cette méthode est appelé sur 2 cases voisines
    def retirer_mur(self,case1,case2):
        #si la case2 est sur la ligne supérieure, on retire le mur haut de la case 1 (la méthode appelé retire aussi le mur bas de la case2)
        if case2._posL==case1._posL-1:
            self.retirer_mur_haut(case1._posL,case1._posC)
            
        #si la case2 est sur la ligne inférieure, on retire le mur bas de la case1
        if case2._posL==case1._posL+1:
            self.retirer_mur_bas(case1._posL,case1._posC)
            
        #si la case2 est sur la colonne gauche, on retire le mur gauche de la case1
        if case2._posC==case1._posC-1:
            self.retirer_mur_gauche(case1._posL,case1._posC)
            
        #si la case2 est sur la colonne droite, on retire le mur droit de la case1
        if case2._posC==case1._posC+1:
            self.retirer_mur_droite(case1._posL,case1._posC)
            
    #méthode d'affichage du labyrinthe qui utilise pyplot
    def afficher(self,chemin=None):
        #on crée un espace d'affichage qui fait la taille du labyrinthe (m*n)
        plt.figure(figsize=(self._taille_l, self._taille_c))
        #on appelle la méthode afficher de la classe Case sur chaque case du labyrinthe
        for i in range(len(self._graphe_cases)):
            for j in range(len(self._graphe_cases[i])):
                L=self._graphe_cases[i][j].afficher()
                #récupère les inforamtions données par la méthode afficher et on les affiche gràce a plot
                plt.plot(L[0][0],L[0][1],L[0][2])  #mur du haut
                plt.plot(L[1][0],L[1][1],L[1][2])  #mur de droite
                plt.plot(L[2][0],L[2][1],L[2][2])  #mur de gauche
                plt.plot(L[3][0],L[3][1],L[3][2])  #mur du bas
                if chemin and (i, j) in chemin:
                    plt.plot(j + 0.5, i + 0.5, 'bo') 
        #inverse l'axe des y pour faire correspondre notre affichage avec le système de coordonnées de matplotlib
        plt.gca().invert_yaxis()
        #affiche
        plt.show()
    
    def creation_lab_parfait(self):
        #la méthode utilisée est celle de l'exploration exhaustive
        #liste pour stocker les cases déjà visité pour pouvoir revenir sur nos pas
        cases_visit=[]
        #on ouvre le labyrinthe en haut à gauche (entrée)
        self.retirer_mur_haut(0,0)
        #on ouvre le labyrinthe en bas à droite (sortie)
        self.retirer_mur_bas(self._taille_l-1,self._taille_c-1)
        #on initialise le nombre de murs ouverts à 0
        murs_ouverts=0
        #on doit ouvrir m*n-1 murs pour que le labyrinthe soit parfait (sans compter l'entrée et la sortie)
        murs_max=self._taille_l*self._taille_c-1
        #la case de laquelle on part est choisi arbitrairement, ici on part de l'entrée
        #la variable case_courante sert à savoir dans quelle case on se situe
        case_courante=self._graphe_cases[0][0]
        #on ajoute cette case à la liste des cases visitées
        cases_visit.append(case_courante)#._posL,case_courante._posC))
        #on enregistre que la case sur laquelle on est est visitée
        case_courante._visit=True
        #i est une variable pour retourner sur nos pas dans la liste des cases visitées
        #on l'initialise à -1 pour accéder a la dernière case ajoutée
        i=-1
        #tant qu'il y a moins de murs ouverts que mn-1 on fait :
        while murs_ouverts<murs_max:
            #instruction pour voir si tout marche bien
            #print(f"Iteration {murs_ouverts}: {case_courante._posL}, {case_courante._posC}")
            #on récupère toutes les cases adjacentes à la case courante
            L=case_courante.voisines(self._taille_l-1,self._taille_c-1)
            #on crée une liste pour stocker les cases voisines qui n'ont pas encore été visitées
            CP=[]
            #pour toutes les cases voisines
            for x in L:
                #si elles n'ont pas été visitées
                if self._graphe_cases[x[0]][x[1]]._visit==False:
                    #on les ajoute a la liste
                    CP.append(x)
            # si au moins une case voisines n'a pas été visitée
            if len(CP)>0:
                #on choist aléatoirement une case grâce à son indice dans la liste CP
                #l'indice est choisit entre 0 et le dernier indice
                cc=random.randint(0,len(CP)-1)
                #la case voisine choisit est appelée case2
                #on la récupère avec l'attribut graphe_cases et grace aux indices calculé précedemment
                case2=self._graphe_cases[CP[cc][0]][CP[cc][1]]
                #on retire le mur entre les 2 cases
                self.retirer_mur(case_courante,case2)
                #self._graphe_adj[case_courante._posL][case_courante._posC]=(CP[cc][0],CP[cc][1])
                #la case voisine devient la case courante
                case_courante=case2
                #on ajoute cette nouvelle case à la liste des cases visitées et on la marque comme visitée
                cases_visit.append(case_courante)#._posL,case_courante._posC))
                case_courante._visit=True
                #on incrémente le nombre de murs ouverts
                murs_ouverts+=1
                #on réinitialise l'attribut i
                i=-1
            #si toutes les cases voisines ont déjà été visitées
            else:
                #la case courante devient la case visitée précedemment
                case_courante=cases_visit[i]
                #on décremente l'indice i pour accéder à la case d'encore avant
                #si la nouvelle cases courante n'a aucune voisine non visitée
                i-=1
    #implémentation d'un parcours de labyrinthe via la méthode de la main droite      
    def methode_main_droite(self):
        pos = (0, 0)  # position de départ
        i,j=pos #indice i et j initialisé à 0 , 0
        orientation = "bas" #orientation initiale, initialisé à bas car l'entrée du labyrinthe est en haut à gauche
        #donc on regarde vers le bas
        # liste qui stocke les cases par lesquelles on est passé (on stocke les indices)
        chemin = []
        #on ajoute la première case (ses indices)
        chemin.append(pos)
        #tant qu'on n'est pas à la sortie
        while pos!=(self._taille_l-1,self._taille_c-1):
            #print(pos)
            #pour chaque direction, on regarde si le mur à droite est présent, si il ne l'est pas, on met a jour la position
            #et on incrémente l'indice adéquat
            #si le mur est présent on regarde celui de droite etc..
            if orientation=="bas":
                if not self._graphe_cases[i][j]._gauche:
                    orientation="gauche"
                    j-=1
                elif not self._graphe_cases[i][j]._bas:
                    orientation="bas"
                    i+=1
                elif not self._graphe_cases[i][j]._droite:
                    orientation="droite"
                    j+=1
                else:
                    orientation="haut"
                    i-=1
            elif orientation=="gauche":
                if not self._graphe_cases[i][j]._haut:
                    orientation="haut"
                    i-=1
                elif not self._graphe_cases[i][j]._gauche:
                    orientation="gauche"
                    j-=1
                elif not self._graphe_cases[i][j]._bas:
                    orientation="bas"
                    i+=1
                else:
                    orientation="droite"
                    j+=1
            elif orientation=="haut":
                if not self._graphe_cases[i][j]._droite:
                    orientation="droite"
                    j+=1
                elif not self._graphe_cases[i][j]._haut:
                    orientation="haut"
                    i-=1
                elif not self._graphe_cases[i][j]._gauche:
                    orientation="gauche"
                    j-=1
                else:
                    orientation="bas"
                    i+=1
            elif orientation=="droite":
                if not self._graphe_cases[i][j]._bas:
                    orientation="bas"
                    i+=1
                elif not self._graphe_cases[i][j]._droite:
                    orientation="droite"
                    j+=1
                elif not self._graphe_cases[i][j]._haut:
                    orientation="haut"
                    i-=1
                else:
                    orientation="gauche"
                    j-=1
            #on met à jour la position et on l'ajoute à la liste du parcours
            pos = (i, j)
            chemin.append(pos)
        #on renvoie le chemin parcouru
        return chemin
    
    def cases_voisines(self,i,j):
        L=[]
        if i<self._taille_l-1:
            if not self._graphe_cases[i][j]._bas:
                L.append((i+1,j))
        if i>0:
            if  not self._graphe_cases[i][j]._haut:
                L.append((i-1,j))
        if j<self._taille_c-1:
            if not self._graphe_cases[i][j]._droite:
                L.append((i,j+1))
        if j>0:
            if not self._graphe_cases[i][j]._gauche:
                L.append((i,j-1))
        return L

    #bfs
    def mat_chemin(self):
        #on itialise le tableau des distances avec des très grandes valeurs
        L=[[float('inf')]*self._taille_l for _ in range (self._taille_c)]
        #la distance de la case de départ à elle même est 0
        L[0][0]=0
        #on crée une file pour stocker les voisins
        cases=deque()
        #on ajoute les coordonnées de la première case
        cases.append([0,0])
        #on initialise les indices i et j des lignes et colonnes à 0
        i,j=0,0
        #tant qu'il reste des cases à visiter
        while len(cases)>0 :#and (i<=self._taille_l-1 or j<=self._taille_c-1):
            #on récupère les indices de la derniere case ajoutée à la file
            i,j=cases.popleft()
            #on récupère les cases voisines de la case actuelle
            C=self.cases_voisines(i,j)
            #print(C)
            #pour chaque case dans la liste des cases voisines
            #on regarde si la distance actuelle est supérieure à la nouvelle distance
            #si elle l'est on actualise la distance et on ajoute cette cases à la file
            for x,y in C:
                if L[x][y]>L[i][j]+1:
                    L[x][y]=L[i][j]+1
                    cases.append([x,y])
            #si on arrive à la case de sortie, on sort de la boucle
            if i == self._taille_l - 1 and j == self._taille_c - 1:
                break
        #on renvoie la matrice des tableaux
        return L
    
    #fonction qui renvoie un chemin pour parcourir le labyrinthe
    #M est la matrice de distance
    def chemin(self,M):
        #on récupère la matrice des distances
        M=self.mat_chemin()
        #on crée un tableau pour stocker le chemin
        chemin=[]
        #on initialise les indices i et j aux coordonnées de la sortie
        i,j=self._taille_l - 1,self._taille_c - 1
        #tant qu'on est pas à l'entrée du labyrinthe
        while i!=0 or j!=0:
            #on ajoute la case sur laquelle on est au chemin
            chemin=[(i,j)]+chemin
            #on récupère ses cases voisines
            C=self.cases_voisines(i,j)
            #on initialise la distance minimale à une grande valeur
            distance_min=float('inf')
            #pour chaque case voisine, si la distances est inférieure à la distance min actuelle
            #on actualise la distance min et les indices
            for a,b in C:
                if M[a][b]<distance_min:
                    distance_min=M[a][b]
                    i,j=a,b
        #on ajoute la case d'entrée au chemin 
        chemin=[(0,0)]+chemin
        # on renvoie le chemin
        return chemin
    #creation de la matrice de distance avec dfs au lieu de bfs
    def mat_dfs(self):
        L=[[float('inf')]*self._taille_l for _ in range (self._taille_c)]
        L[0][0]=0
        cases=[]
        cases.append([0,0])
        i,j=0,0
        while len(cases)>0 :#and (i<=self._taille_l-1 or j<=self._taille_c-1):
            i,j=cases.pop()
            C=self.cases_voisines(i,j)
            #print(C)
            for x,y in C:
                if L[x][y]>L[i][j]+1:
                    L[x][y]=L[i][j]+1
                    cases.append([x,y])
            if i == self._taille_l - 1 and j == self._taille_c - 1:
                break
        return L
    
    #parcours du labyrinthe avec dfs (pas efficace)
    def chem_dfs(self):
        chemin=[] #stockage des sommets visités
        vus=[[False]* self._taille_l for _ in range (self._taille_c)] #marquage des sommets visités
        grey=[(0,0)] #pile stockant les voisins des sommets visités
        while len(grey)>0: #tant qu'il reste des voisins non visités
            i,j=grey.pop()#nouveau voisin
            C=self.cases_voisines(i,j)
            if not vus[i][j]:
                chemin.append((i,j))
                vus[i][j]=True
                for x,y in C:
                    if not vus[x][y]: #si pas déjà visité
                        grey.append((x,y)) #ajout à la pile
            if i == self._taille_l - 1 and j == self._taille_c - 1:
                break
        return chemin