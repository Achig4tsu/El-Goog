h1 = ["Arbre","ceriser", "produit","cerise"]
title = ["Cerisier"]
p = ["Arbre", "cerise" , "feuille" , "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "feuille", "branche" , "abruti"]

char = "Arbre qui prodiut feuille  feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille feuille cerise la feuille et la branche branche branche et espece d abruti"
def compteur (char, m ) :
    c = 0
    for i in char.split() :
        if i == m:
            c+=1
    return c
def algo_index (title:list, h1:list, p:list) :
    
    dick = {}
    total = title + h1
    
    for mot in (total + p) :
        if mot in h1 or mot in title :
            dick[mot] = 5
            
        else :
            dick[mot] = 1
    
    for i in dick.keys() :
        if i in p :
            c = compteur(char, i)
            dick[i] += c
    
    return dick

test = algo_index(title,h1,p)
print (test)

