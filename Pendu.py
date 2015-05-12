import time         #importation du module time pour le temps

name = input("Entrer le nom de joueur:")        #on demande le nom au joueur
print ("Salut, " + name, "amusez vous bien !")  #on salue le joueur 
print ("\n")

regles=open("regles.txt")                       #ouvre le fichier contenant les règles
regle=regles.read()                             #on lit le fichier contenant les règles       
regles.close                                    #ferme le fichier contenant les règles
print(regle)                                    #on affiche les règles 

#on attend une 0.5sec
time.sleep(0.5)

print ("Chargement...")
time.sleep(0.5)

def affichemot(mot) : #fonction qui affiche le mot et le nombre d'essai restants
    reponse = ""      #variable de type str vide
    lettres = []      #variable de type list vide
    vies = 7          #nombre d'essai
    q="pendu-7.txt"   #variable str ayant le nom du fichier texte ou figure ler dessin du pendu 
    g=open(q,'r')     #ouvre le fichier dont la variable q porte le nom
    h=g.read()        #h est la variable qui contient le dessin du fichier dont q porte le nom
    while reponse.upper()!=mot.upper()and vies !=0 :
        #tant que la réponse de l'utilisateur(donnée en majuscules) est différente du mot à trouver et le nombre de vie est différents de 0 alors
        reponse = "" #la variable est vide 
        L=input('Entrer une lettre a tester (en minuscule): ') #on demande à l'utilisateur d'insérer une lettre à tester 
        lettres.append(L)                       #on ajoute cette lettres à la liste des lettres deja testé
        print('Lettre entrée: '+L)              #on affich cette lettre 
        vies=nbvies(mot,L,vies)                 #paramètres de la fonction 
        nvies=str(vies)                         #on transforme le nombre d'essais en str
        while len(L)!=1:                        #tant que le caractère saisie n'est pas une seule lettre on revient au debut 
            L=input('Entrer une SEULE lettre a tester: ')#un message d'erreur qui affiche qu'il faut rentrer une seule lettre 
            lettres.append(L)                            #on ajoute cette lettres à la liste des lettres deja testé
        for L in mot:                           #pour toutes lettres dans le mot:        
            if L in lettres :                   #si la lettre entré est dans les lettres deja proposé 
                reponse = reponse + L.upper()   #on ajoute à la réponse affiché la lettre correcte
            elif L=='-':                        #ou si la lettre entré est dans le mot masqué 
                reponse=reponse + L.upper()            #on ajoute à la réponse affiché la lettre correcte 
            else :                              #sinon on laisse le lettre masqué 
                reponse = reponse + "_ "
        q="pendu-"+nvies+".txt"                 #q est la variable qui correspond au nom du fichier et depend du nombre de vie 
        g=open(q,'r')                           #on ouvre le fichier 
        h=g.read()                              #on le lit
        g.close()                               #on le ferme
        print(h)                                #on l'affiche 
        print("Les lettres déja proposées sont:",lettres)        
        print(reponse)                          #on affiche le mot 
        print('Il vous reste '+nvies+' essais\n') #on affiche le nombre d'essais restant 
    if reponse.upper()==mot.upper()and vies !=0 : #si le joueur à afficher le mot correctectement et que le nombre d'erreur est différent de 0 
        print("Vous avez deviné le mot","\'",mot.upper(),"\'","!") #alors on affiche que le joueur a gagné et le mot
        gagne=open("gagne.txt","r")                 #ouvre le fichier gagne.txt qui contient l'image afficher lorsque le joueur gagne
        w=gagne.read()                              #w contient le dessin "gagnant" contenu dans gagne.txt        
        gagne.close()                               #on ferme gagne.txt
        print(w)                                    #on affiche le dessin gagnant
        recommencer=input("Entrer une lettre pour recommencer:") #on propose de rejouer
        if type(recommencer)==str:                               #grâce à cette boucle on peut rejouer directement
                mot=trouvermot()
                affichemot(mot)            
    if reponse.upper()!=mot.upper() and vies ==0:                #mais si le joueur n'y arrive pas alors le joueur a perdu
        print("Perdu le mot à trouver était","\'", mot.upper(),"\'") #on affiche que le joueur a perdu et le mot à trouver
        recommencer=input("Entrer une lettre pour recommencer")   
        if type(recommencer)==str:                              #grâce à cette boucle on peut rejouer directement
                mot=trouvermot()
                affichemot(mot)
            
       

def trouvermot() :                       #fonction chargée de choisir un mot aléatoirement
    import random                        #importe le module random
    f=open('dico.txt','r')               #on ouvre le dictionnaire pour le lire       
    line= random.randrange(0,336531)     #le dico est composée de lignes qui corresponde chacun à un mot donc line est la ligne du mot choisie aléatoirement   
    for n in range (0,line):             #pour n de 0 jusqu'à la ligne du mot
        mot=f.readline().replace('\n','') #lire le mot choisie     
    f.close()                            # on ferme le dico
    return mot                           #on retourne le mot 

def nbvies(mot,L,vies) :                 #fonction paramétrique du nombre d'essais en fonction du nombre d'erreur 
    if L.upper() in mot.upper() :        #si la lettre proposé est dans le mot demandé alors le nombre d'essais reste le meme 
        vies=vies                        #le nombre de vies ne change pas 
    elif len(L)!=1:                      #si le joueur entre plusieurs lettres
        vies=vies                        #le nombre de vies ne change pas              
    else :
        vies=vies-1                      #sinon si on fait une erreur le nombre d'essais diminue de 1
    return vies                          #on retourne le nombre d'essais 



mot=trouvermot()
affichemot(mot)
