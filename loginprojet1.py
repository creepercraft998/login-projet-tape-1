User_name_confirmation ="william" or "tomy"
User_password_confirmation = "lol" or "tomy"
User_name= input("Quelle est ton nom d'utilisateur:")
User_password=input("Quelle est ton mot de passe:")
if User_name == User_name_confirmation and User_password == User_password_confirmation:
    print("GG!!! Vous êtes connecter a projetlogin.")

    ligne_commande=True
    print("")
    while ligne_commande:
    	menu=input("=> ")
    	if menu=="exit":
    	 	break #brbeak est pour casser la boucle et sortir du programme
    	elif menu=="Concepteur":
    		print("Se programme a été créer par 0°0.")
    	elif menu=="home":
    		continue # pour redémarer la boucle
    	elif menu=="id":
    		print("Votre id est :",User_name_confirmation) #pour afficher le nom du joueur
    	else:
    		print("=> Unvalid command or touch error")

    print("Bonne journer:", User_name_confirmation)
else:
        print("Conection fail.")
