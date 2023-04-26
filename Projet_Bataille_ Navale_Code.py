#Constantes
N=10
COLONNES=[str(i) for i in range(N)]
LIGNES = [' '] + list(map(chr, range(97, 107)))
DICT_LIGNES_INT = {LIGNES[i]:i-1 for i in range(len(LIGNES))}
VIDE = '.'
EAU='o'
TOUCHE='x'
BATEAU='#'
DETRUIT='@'
NOMS=['Transporteur','Cuirass´e','Croiseur','Sous-marin','Destructeur']
TAILLES=[5,4,3,3,2]

# Modules importés:
import re
import random
from random import randint


# I) Carte et tir:

# 1) Création d'une matrice NxN
def create_grid():
    M=[]
     #Rajout des lignes
    for i in range(N):
        M.append([])
        #Rajout des colonnes
        for j in range(N):
            M[i].append(VIDE)
    return M

# 2)
def plot_grid(M):
    s=" "
    #On rajoute la première ligne (0,1,...,9)
    for x in COLONNES:
        s+=x+" "
    s+="\n"
    #On rajoute les lignes
    for i in range(N):
        #On commence les lignes par les valeurs de LIGNES (a,b,c,...,j)
        s+=LIGNES[i+1]+" "
        for j in range(N):
            s+=M[i][j]+" "
        s+="\n"
    return s   

# 3)
def tir(p,M,flotte):
    x,y=p[0],p[1]
    #On teste si la case a été déjà attaqué 
    while M[x][y]==EAU or M[x][y]==TOUCHE or M[x][y]==DETRUIT:
        s=input("\nCette case a déjà été attaquée !\nSaisir une autre posistion(lettre chiffre): \n")
        newPose=pos_from_string(s)
        x,y=newPose[0],newPose[1]
    #Si il y a un bateau sur la case:
    if presence_bateau(p,flotte):
        #Si oui
        #On change la case
        M[x][y]=TOUCHE
        #On incrémente le nombre de cases touchées
        flotte[id_bateau_at_pos(p,flotte)]["Cases touchées"]+=1
        #On teste si toutes les cases sont touchées:
        if flotte[id_bateau_at_pos(p,flotte)]["Cases touchées"]==flotte[id_bateau_at_pos(p,flotte)]["Taille"]:
            #Si oui on l'annonce
            print("Touché Coulé !\t%s a été détruit\n"%flotte[id_bateau_at_pos(p,flotte)]["Nom"])
            #Et on change toutes les cases du bateau dans la matrice en DETRUIT
            for pos in flotte[id_bateau_at_pos(p,flotte)]["Positions"]:
                M[pos[0]][pos[1]]=DETRUIT
            #On enleve le bateau de la flotte
            flotte.remove(flotte[id_bateau_at_pos(p,flotte)])
        else:
            #Si non:
            print("Touché ! en {0}\n".format(p))
        return True
    else:
        print("Manqué ! (en {0})\n".format(p))
        M[x][y]=EAU
        return False

# 4)

def random_position():
    return (randint(0,N-1),randint(0,N-1))

# 5)
 
# map1= create_grid()
# a=1
# flotte=[]
# while a==1:
#     print(plot_grid(map1))
#     pos=random_position()
#     print(pos)
#     tir(map1,pos_from_string(pos),flotte)
#     a=int(input("1 continuer, 0 arreter: "))

# 6)
def pos_from_string(s):
    #initialisation
    lettres="abcdefghij"
    lignes=''
    colonnes=0
    #On vérifie que le paramètre est conforme
    while s not in re.findall(r"[a-j]\s*[0-9]",s):
        s=input("Donner une position avec dans l'odre:\n-une lettre en minuscule entre a et j\n-un chiffre entre 0 et 9\n")
    #On identifie dans s l'entier de la colonne
    for x in s:
        if x.isdigit():
            colonnes=int(x)
    #On identifie dans s la lettre de la ligne
    for x in s:
        if x in lettres:
            lignes=lettres.index(x)
    return (lignes, colonnes)

#print(plot_grid(tir(tir(create_grid(),(9,9)),pos_from_string(""))))

# 7) Dans la fonction pos_from_string()
# 8) Dans la fonction tir()

    
# II) La flotte:x

# 1)
def nouveau_bateau(flotte, nom, taille, pos, orientation):
    list_pos=[]
    #Tant que l'utilisateur ne rentre pas une orientation conforme
    while (orientation!='h') and (orientation!='v'):
        orientation=input("Vous n'avez pas donné une orientation valide,\nveuillez sélectionner h (horizontale) ou v (verticale): ")
    #Si horizontal, on teste si il y a la place à droite ou à gauche
    if (orientation=='h') and (pos[1]+taille <= N-1):
        for i in range(taille):
            list_pos.append((pos[0],pos[1]+i))
    elif (orientation=='h') and (0 <= pos[1]-taille):
        for i in range(taille):
            list_pos.append((pos[0],pos[1]-i))
    #Si vertical, on teste si il y a la place en haut ou en bas
    if (orientation=='v') and (pos[0]+taille <= N-1):
        for i in range(taille):
            list_pos.append((pos[0]+i,pos[1]))
    elif (orientation=='v') and (0 <= pos[0]-taille):
        for i in range(taille):
            list_pos.append((pos[0]-i,pos[1]))
    flotte.append({"Nom":nom, "Taille":taille,"Positions":list_pos,"Cases touchées":0,"Orientation":orientation})
# flotte=[]
# nouveau_bateau(flotte,"Test",3,(0,0),'h')
# print(flotte)

# 2)
def presence_bateau(pos,flotte):
    #On parcours la flotte
    for bateau in flotte:
        for x in bateau["Positions"]:
            if x==pos:
                return True
    return False

# flotte=[]
# nouveau_bateau(flotte,"test",3,(9,9),"v")

            
# 3)
def plot_flotte_grid(M,flotte):
    s=LIGNES[0]+" "
    for i in range(N):
        s+=COLONNES[i]+" "
    s+="\n"
    for i in range(N):
        #On rajoute les lignes avec au début (a,b,...,j)
        s+=LIGNES[i+1]+" "
        for j in range(N):
            #On navigue dans les bateaux de la flotte:
            if presence_bateau((i,j),flotte):
                #Si elle contient un bateau non touché on attribue à la case le caractère BATEAU
                if M[i][j]!=TOUCHE:
                    s+=BATEAU+" "   
                else:
                    #Sinon on attribue le caractère touché
                    s+=TOUCHE+" "
            else:
                s+=M[i][j]+" "
        s+="\n"      
    return s

# print(plot_flotte_grid(create_grid(),flotte))

# 4)
def input_ajout_bateau(flotte,nom,taille):
    list_pos=[]
    print("\nAjoutons le bateau %s de taille %d à la flotte:\n"%(nom,taille))
    #On demande une position
    pos_string=input("\nDonner une position avec dans l'odre:\n-une lettre en minuscule entre a et j\n-un chiffre entre 0 et 9\n->")
    pos=pos_from_string(pos_string)
    #On demande un orientation
    orientation=''
    while (orientation!='h') and (orientation!='v'):
        orientation=input("\nVeuillez sélectionner une orientation\nh (horizontale) ou v (verticale):\n->")
    #Si horizontal, on teste si il y a la place à droite ou à gauche
    if (orientation=='h') and (pos[1]+taille <= N-1):
        for i in range(taille):
            list_pos.append((pos[0],pos[1]+i))
    elif (orientation=='h') and (0 <= pos[1]-taille):
        for i in range(taille):
            list_pos.append((pos[0],pos[1]-i))
    #Si vertical, on teste si il y a la place en haut ou en bas
    if (orientation=='v') and (pos[0]+taille <= N-1):
        for i in range(taille):
            list_pos.append((pos[0]+i,pos[1]))
    elif (orientation=='v') and (0 <= pos[0]-taille):
        for i in range(taille):
            list_pos.append((pos[0]-i,pos[1]))
    #On teste si les pos sont déjà occupés et recommence si oui
    for pos1 in list_pos:
        for bateau in flotte:
            for pos2 in bateau["Positions"]:
                if pos2==pos1:
                    print("Le bateau que vous avez placé se trouve sur un ou des emplacements déjà occupés({0})\nRecommencer svp:\n".format(pos1))
                    return input_ajout_bateau(flotte,nom,taille)
    flotte.append({"Nom":nom, "Taille":taille,"Positions":list_pos,"Cases touchées":0,"Orientation":orientation})

# flotte=[]
# input_ajout_bateau(flotte,"Titanic",5)
# print(flotte)
# input_ajout_bateau(flotte,"zodiac",5)
# print(plot_flotte_grid(create_grid(),flotte))

# 5) Dans la fonction input_ajout_bateau()

# 6) Déjà fait car on test la position avec le patterne "[a-jA-J]\s*[0-9]" donc il n'y a à priori pas de problème puisqu'on reste dans la boucle while si la lettre n'est pas entre a et j et le chiffre entre 0 et 9. i.e si la position n'est pas dans la grille

# 7) Dans la fonction input_ajout_bateau() à l'aide de presence_bateau()

# 8)
def init_joueur():
    M=create_grid()
    # s=plot_grid(M)
    flotte=[]
    #Boucle For pour pouvoir placer tous les bateaux:
    for i in range(len(NOMS)):
        input_ajout_bateau(flotte, NOMS[i], TAILLES[i])
    return flotte,M

#print(init_joueur())

# 9)
def init_ia():
    flotte=[]
    m=create_grid()
    map=plot_grid(m)
    s="hv"
    #initialise un premier bateau sinon ajoute deux fois le premier bateau
    nouveau_bateau(flotte, NOMS[0], TAILLES[0],random_position(),random.choice(s))
    for i in range(1,len(NOMS)):
        check1=True
        #Boucle while pour tester des positions pour le bateau jusqu'a ce quon trouve une position qui n'est pas déjà occupée par un autre bateau
        while check1:
            pos=random_position()
            orientation=random.choice(s)
            nouveau_bateau(flotte, NOMS[i], TAILLES[i],pos,orientation)
            check2=0
            for p in flotte[i]["Positions"]:
                if presence_bateau(p, flotte[0:-1]): #[0:-1] Sinon presence_bateau() cherche aussi dans le bateau qu'on vient d'ajouter et vaudra forcement True
                    del flotte[i]
                    check2=1
                    break
            if check2==0:
                check1=False
    return flotte,m

# print(init_ia())
    


# III) Touché Coulé:

# 1)Dans tir
# 2)Dans tir
# 3)
def id_bateau_at_pos(pos,flotte):
    #On parcours la flotte et cherche l'indice
    for i in range(len(flotte)):
        if pos in flotte[i]["Positions"]: #la liste des positions du i-eme bateau
            return i
    return None

# 4)Dans tir
# 5)Dans tir
# 6)

# IV) Intelligence Artificielle et deux joueurs

# 1)
def tour_ia_random(m,flotte):
    pos=random_position()
    x,y=pos[0],pos[1]
    check=True
    #Boucle while infinie jusqu'à ce qu'il touche une case non attaquée
    while check==True:
        pos=random_position()
        x,y=pos[0],pos[1]
        #Si l'on trouve une case Vide ou BATEAU (i.e non touchée), l'IA tire et la boucle while se ferme
        if m[x][y]==VIDE or m[x][y]==BATEAU:
            tir(pos,m,flotte)
            check=False

#2)
def tour_joueur(nom,m,flotte):
    stringPos=input("Donner une position avec dans l'odre:\n-une lettre en minuscule entre a et j\n-un chiffre entre 0 et 9\n")
    pos=pos_from_string(stringPos)
    x,y=pos[0],pos[1]
    check=True
    # Boucle while infinie jusqu'à ce qu'il touche une case dans plot_grid non attaquée
    while check==True:
        # Si l'on trouve une case Vide ou BATEAU (i.e non touchée), le joueur tire et la boucle while se ferme
        if m[x][y]==VIDE or m[x][y]==BATEAU:
            tir(pos,m,flotte)
            check=False
        else:
            print("\n La case a déjà été attaqué\n")
            return tour_joueur(nom,m,flotte)

# 3)
def tour_ia_better_random(m,flotte):
    count=0
    #On compte le nombre de cases touchées
    for L in m:
        count+=L.count(TOUCHE)
    # S'il y a aucune case touchée on lance la fonction tour_ia_random (i.e tir aléatoire pour toucher un bateau)
    if count==0:
        tour_ia_random(m,flotte)
    # Sinon on tire sur un case adjacente:
    else: 
        #On va énumérer les solutions pour la cases adjacente. (ex si la case est au bord, on fait en sorte de ne pas tirer en dehors de la map)
        pos=random_position()
        a=[]
        while m[pos[0]][pos[1]]!=TOUCHE:
            pos=random_position()
        if pos[0]!=0:
            a+= [(-1,0)]
        if pos[0]!=N-1:
            a+=[(1,0)]
        if pos[1]!=0:
            a+=[(0,-1)]
        if pos[1]!=N-1:
            a+=[(0,1)]
        for pos_adj in a:
            if m[pos[0]+pos_adj[0]][pos[1]+pos_adj[1]]!=TOUCHE:
                #Si c'est déjà attaqué on recommence
                return tir((pos[0]+pos_adj[0],pos[1]+pos_adj[1]),m,flotte)
    


# 4)

#On teste si il reste des bateaux dans la flotte
def test_fin_partie(nom,m,flotte,nb_tour):
    if len(flotte)==0:
        print("%s a gagné en %d tours !"%(nom,nb_tour))
        exit()           

#5)
def joueur_vs_ia():
    i=1
    #On demande à l'utilisateur son pseudo
    nom1= input("Joueur 1, choisir un pseudo:\n->")
    print("\nVous allez jouer contre une ia, commencez par placer vos bateaux:\n")
    flotte_joueur,m_joueur=init_joueur()
    flotte_ia,m_ia=init_ia()
    #Boucle while infini qui sera arrété seulement si la flotte du joueur ou de l'IA est totalement détruite
    while i>0:
        #On montre au joueur l'état de son camp
        print(nom1,"Voici l'état de votre camp: ")
        print(plot_flotte_grid(m_joueur,flotte_joueur))
        #On montre au joueur l'état connu du camp adverse
        print("Voici l'état du camp de l'IA selon le retour du radar")
        print(flotte_vu_exterieur(plot_flotte_grid(m_ia,flotte_ia)))

        #Le joueur joue
        tour_joueur("Pierre",m_ia,flotte_ia)
        test_fin_partie("Pierre",m_ia,flotte_ia,i)
        
        #Au tour de l'ia
        print("L'IA joue...\n")
        tour_ia_better_random(m_joueur,flotte_joueur)
        test_fin_partie("IA",m_joueur,flotte_joueur,i)
        
        #Ligne utilisé pour tester le code:
        # print("Etat actuel du camp ia:\n"+plot_flotte_grid(m_ia,flotte_ia))

        i+=1

#joueur_vs_ia()

# 6)

def hide():
    #Pour que le joueur ne voit pas les configurations de l'autre joueur qui vient de jouer
    print("\n"*50)

def flotte_vu_exterieur(s):
    #On va afficher seulement les parties attaqué et non les bateaux pour montrer au joueur où il a déjà attaqué
    s_exte=""
    for c in s:
        if c==BATEAU:
            s_exte+=VIDE
        else:
            s_exte+=c
    return s_exte


def deux_joueurs():
    #Initialise le nbr de tours à 1
    i=1
    print("Vous allez jouer à la bataille navale:\n")

    #Les deux joueurs choisissent leur pseudo:
    nom1= input("Joueur 1, choisir un pseudo:\n->")
    nom2= input("Joueur 2, choisir un pseudo:\n->")
    
    #Joueur 1 place ses bateaux
    print("\n"+nom1, "veuillez placer vos bateaux\n")
    flotte_joueur1,m_joueur1=init_joueur()

    hide()

    #Joueur 2 place ses bateaux
    print("\n"+nom2, "veuillez placer vos bateaux\n")
    flotte_joueur2,m_joueur2=init_joueur()

    hide()

    #Boucle while infini qui sera arrété seulement si la flotte d'un joueur est totalement détruite
    while i>0:
        print(nom1,"Voici l'état de votre camp: ")
        print(plot_flotte_grid(m_joueur1,flotte_joueur1))
        print("Voici l'état du camp de",nom2,"selon le retour du radar")
        print(flotte_vu_exterieur(plot_flotte_grid(m_joueur2,flotte_joueur2)))
        tour_joueur(nom1,m_joueur2,flotte_joueur2)
        test_fin_partie(nom1,m_joueur2,flotte_joueur2,i)

        continuer=""
        while continuer!="o":
            continuer=input("Continuer (tapez 0):\n->")

        hide()

        print(nom2,"Voici l'état de votre camp: ")
        print(plot_flotte_grid(m_joueur2,flotte_joueur2))
        print("Voici l'état du camp de",nom1,"selon le retour du radar:\n")
        print(flotte_vu_exterieur(plot_flotte_grid(m_joueur1,flotte_joueur1)))
        tour_joueur(nom2,m_joueur1,flotte_joueur1)
        test_fin_partie(nom2,m_joueur1,flotte_joueur1,i)

        continuer=""
        while continuer!="o":
            continuer=input("Continuer (tapez 0):\n->")

        hide()
        i+=1

        
# deux_joueurs()


def jouer():
    #On demande 1 ou deux joueur et lance une partie contre une IA si le joueur tape 2 et une partie joueur vs joueur si le joueur tape 2
    print("ok")
    dmd=input("Taper 1 pour jouer contre une IA\nTaper 2 pour joue contre un joueur:\n->")
    while dmd!="1" and dmd!="2":
        dmd=input("Veuillez entrer 1 ou 2\n->")
    if dmd=="2":
        deux_joueurs()
    if dmd=="1":
        joueur_vs_ia()

jouer()


  


# V) Améliorations

# 1) Ajouter des bateaux en diagonales? (cette idée est pas ouf mais au cas où)


