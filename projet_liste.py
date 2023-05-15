import json
chemin = "./script.json"

liste = True
with open(chemin,"r") as f:
    liste_courses=json.load(f)
while liste == True :
  print("""Choisissez parmi les 5 options suivantes :
 
  1. Ajouter un élément à la liste de courses
  2. Retirer un élément de la liste de courses
  3. Afficher les éléments de la liste de courses
  4. Vider la liste de courses
  5. Quitter le programme""")
  choix = input("Votre choix :")
  if choix == "1" :
     element = input("Entrez le nom d'un élement à ajouter à la liste de courses :")
     liste_courses.append(element)
     print(element, "a été ajouté à votre liste")
  elif choix == "2" :
     element = input("Entrez le nom d'un élement à retirer de la liste de courses :")
     if element in liste_courses:
       liste_courses.remove(element)
       print(element," a été enlevé de votre liste")
     else :
       print("L'élement ",element," n'éxiste pas dans votre liste")
  elif choix == "3" :
    if len(liste_courses)>0 :
      for index, element in enumerate(liste_courses):
        print(index + 1, element)
    else :
      print("Votre liste ne contient aucun élement")
  elif choix == "4" :
    liste_courses=[]
    print("La liste a été vidé de son contenu")
  elif choix == "5" :
    print("Vous êtes sorti du programme")
    with open(chemin,"w") as f:
        json.dump(liste_courses,f,indent=4)
    liste=False
  else :
    print("Jai pas compris, Veuillez cliquer sur 1,2,3,4 ou 5 pour continuer")
