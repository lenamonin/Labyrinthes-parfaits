from Case import *
from Labyrinthe import *

labyrinthe = Labyrinthe(10,10)
labyrinthe.creation_lab_parfait()


chemin=labyrinthe.methode_main_droite()
labyrinthe.afficher(chemin)

M=labyrinthe.mat_chemin()
M2=labyrinthe.mat_dfs()

chemin2=labyrinthe.chemin(M)
labyrinthe.afficher(chemin2)

chemin3=labyrinthe.chemin(M2)
labyrinthe.afficher(chemin3)


chemin4=labyrinthe.chem_dfs()
labyrinthe.afficher(chemin4)


