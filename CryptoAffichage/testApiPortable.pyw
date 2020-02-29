from tkinter import *
import urllib
import urllib3
from PIL import Image, ImageTk
import requests
import json
import time
from bs4 import BeautifulSoup

#http = urllib3.PoolManager()
#url = 'http://www.thefamouspeople.com/singers.php'
#response = http.request('GET', url)
#soup = BeautifulSoup(response.data)
#ou 
#curl



#http = urllib3.PoolManager()
#url = 'https://www.tradingview.com/x/Hmrc5gN2/'
#response = http.request('GET', url)
#soup = BeautifulSoup(response.data)


def creationDeLaFenetre(root,couleur):
	root.title('Cours du Dogecoin')
	if "black" in couleur :
		couleur = '#%02x%02x%02x' % (0,0,0)
	else : 
		couleur = '#%02x%02x%02x' % (255,255,255)
	root.configure(bg=couleur)
def center_window(width=300, height=200):
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	root.geometry('%dx%d+%d+%d' % (width, height, x, y))
def affichageDes3StatistiquesTemps(variablePrixEnTempReel,pourcentageChangementDeLHeure,pourcentageChangementDes24h,pourcentageChangementDes7d):
	affichageVariablePrixEnTempReel = Label(root, text="Prix actuel: " + variablePrixEnTempReel + "€")
	affichageVariablePrixEnTempReel.configure(background="black")
	affichageVariablePrixEnTempReel.configure(foreground="white")
	affichageVariablePrixEnTempReel.pack()
	affichagePourcentageChangementDeLHeure = Label(root, text="Changement de l'heure: " + pourcentageChangementDeLHeure +"%")
	affichagePourcentageChangementDeLHeure.configure(background="black")
	affichagePourcentageChangementDeLHeure.configure(foreground="white")
	affichagePourcentageChangementDeLHeure.pack()
	affichagePourcentageChangementDes24h = Label(root, text="Changement dans les 24h: " + pourcentageChangementDes24h +"%")
	affichagePourcentageChangementDes24h.configure(background="black")
	affichagePourcentageChangementDes24h.configure(foreground="white")
	affichagePourcentageChangementDes24h.pack()
	affichagePourcentageChangementDes7d = Label(root, text="Changement dans les 7 jours: " + pourcentageChangementDes7d +"%")
	affichagePourcentageChangementDes7d.configure(background="black")
	affichagePourcentageChangementDes7d.configure(foreground="white")
	affichagePourcentageChangementDes7d.pack()
def affichage(crypto):
	destroyAllButNotImageAndButton()
	response = requests.get("https://api.coinmarketcap.com/v1/ticker/"+ crypto +"/?convert=EUR")
	responseEnJson= response.json()
	print(responseEnJson)
	creationDeLaFenetre(root,"black")
	variablePrixEnTempReel = responseEnJson[0]["price_eur"][:-5]
	pourcentageChangementDeLHeure = responseEnJson[0]["percent_change_1h"]
	pourcentageChangementDes24h = responseEnJson[0]["percent_change_24h"]
	pourcentageChangementDes7d = responseEnJson[0]["percent_change_7d"]
	#variablePrixEnTempReel = "0"
	#pourcentageChangementDeLHeure = "0"
	#pourcentageChangementDes24h = "0"
	#pourcentageChangementDes7d = "0"
	#ajoutImageChart si c'est un nouveau jour, Jour a rajouter dans le fichier
	#ajoutImageChart("images/Dogecoin/chart.jpeg")
	
	affichageDes3StatistiquesTemps(variablePrixEnTempReel,pourcentageChangementDeLHeure,pourcentageChangementDes24h,pourcentageChangementDes7d)
	if(boutonExiste != True):
		buttonChangement()
def affichageElementBTC():
	affichage("bitcoin")
	destroySpecifyButtonAndReconstruct("BTC","nouveau")
def affichageElementETH():
	affichage("ethereum")
	destroySpecifyButtonAndReconstruct("ETH","nouveau")
def affichageElementDGE():
	affichage("dogecoin")
	destroySpecifyButtonAndReconstruct("DGE","nouveau")
def affichageElementIOTA():
	affichage("iota")
	destroySpecifyButtonAndReconstruct("IOTA","nouveau")
def affichageElementXRP():
	affichage("ripple")
	destroySpecifyButtonAndReconstruct("XRP","nouveau")
def affichageElementLTC():
	affichage("litecoin")
	destroySpecifyButtonAndReconstruct("LTC","nouveau")
def ajoutImageChart(chemin):
	image = Image.open(chemin)
	image = image.resize((310,310),Image.ANTIALIAS)
	photoImage = ImageTk.PhotoImage(image)
	w=Label(root, image = photoImage)
	w.image = photoImage
	w.configure(background="black")
	w.pack()
def buttonChangement():
	boutonExiste = True
	BTC = Button(root, text="BTC", width=15, command=affichageElementBTC)
	BTC.configure(background="black")
	BTC.configure(foreground="white")
	BTC.pack()
	BTC.place(bordermode=OUTSIDE, height=35, width=50,x=0, y=400)
	ETH = Button(root, text="ETH", width=15, command=affichageElementETH)
	ETH.configure(background="black")
	ETH.configure(foreground="white")
	ETH.pack()
	ETH.place(bordermode=OUTSIDE, height=35, width=50,x=50, y=400)
	DGE = Button(root, text="DGE", width=15, command=affichageElementDGE)
	DGE.configure(background="black")
	DGE.configure(foreground="white")
	DGE.pack()
	DGE.place(bordermode=OUTSIDE, height=35, width=50,x=100, y=400)
	IOTA = Button(root, text="IOTA", width=15, command=affichageElementIOTA)
	IOTA.configure(background="black")
	IOTA.configure(foreground="white")
	IOTA.pack()
	IOTA.place(bordermode=OUTSIDE, height=35, width=50,x=150, y=400)
	XRP = Button(root, text="XRP", width=15, command=affichageElementXRP)
	XRP.configure(background="black")
	XRP.configure(foreground="white")
	XRP.pack()
	XRP.place(bordermode=OUTSIDE, height=35, width=50,x=200, y=400)
	LTC = Button(root, text="LTC", width=15, command=affichageElementLTC)
	LTC.configure(background="black")
	LTC.configure(foreground="white")
	LTC.pack()
	LTC.place(bordermode=OUTSIDE, height=35, width=50,x=251, y=400)
def positionnementEcranEtFixeForeground1366x768():
	tailleEcran = root.winfo_screenheight()
	tailleEcranA = root.winfo_screenwidth()
	root.geometry('300x430+'+str(tailleEcranA-309)+'+'+str(tailleEcran-462))
	root.attributes('-topmost',True)
	root.resizable(width=False, height=False)
def positionnementEcranEtFixeForegroundAutres():
	tailleEcran = root.winfo_screenheight()
	tailleEcranA = root.winfo_screenwidth()
	root.geometry('300x400+'+str(tailleEcranA+965)+'+'+str(tailleEcran-479))
	root.attributes('-topmost',True)
	root.resizable(width=False, height=False)
def connectionErreur():
	creationDeLaFenetre(root,"white")
	imageBlanche = Image.open("images/imageBlanche.jpeg")
	imageBlanche = imageBlanche.resize((310,47),Image.ANTIALIAS)
	photoImageBlanche = ImageTk.PhotoImage(imageBlanche)
	w=Label(root, image = photoImageBlanche)
	w.image = photoImageBlanche
	w.configure(background="white") 
	w.pack()
	
	imageNonConnecte = Image.open("images/-signal-wifi-statusbar-not-connected-26x24px_90160.png")
	imageNonConnecte = imageNonConnecte.resize((250,240),Image.ANTIALIAS)
	photoImageNonConnecte = ImageTk.PhotoImage(imageNonConnecte)
	w=Label(root, image= photoImageNonConnecte)
	w.image = photoImageNonConnecte
	w.configure(background="white")
	w.pack()
	textNonConnecte = Label(root, text="Veuillez vérifier votre connection Internet")
	textNonConnecte.configure(background="white")
	textNonConnecte.pack()
	bouton_reessayer = Button(root, text="Réessayer", command=refresh)
	bouton_reessayer.pack()
	
	raise ConnectionError("Le device n'est pas connecté à Internet.")
	print("Le device n'est pas connecté à Internet.")
	# ici on affiche une fenetre qui ne contient pas les elements et met juste un affichage en mode veuillez verifier votre connection internet
	#La boucle ne fonctionne pas tant qu'il y a l'exception normal
def prog():
	try:
		affichage("dogecoin")
		if root.winfo_screenheight() == 768 and  root.winfo_screenwidth() == 1366 :		
			positionnementEcranEtFixeForeground1366x768()	
		else :
			positionnementEcranEtFixeForegroundAutres()
		#refresh()
		root.mainloop()
	except:
		connectionErreur()
		if root.winfo_screenheight() == 768 and  root.winfo_screenwidth() == 1366 :
			positionnementEcranEtFixeForeground1366x768()		
		else :
			positionnementEcranEtFixeForegroundAutres()
		root.mainloop()
	raise ConnectionError(e, request= print("non"))

def destroyAll():
	boutonExiste = False
	for c in root.winfo_children():
		c.pack_forget()
		c.destroy()

def destroyAllButNotImageAndButton():
	for c in root.winfo_children():
		if(str(c).find("label") != -1):
			if(str(c['text']) != ""):
				c.pack_forget()
				c.destroy()
			
def destroySpecifyButtonAndReconstruct(stringCrypto,choix):
	numeroDuBouton = arrayDesCryptos.index(stringCrypto)
	numeroDuLoopEnCours = 0
	for c in root.winfo_children():
		if(str(c).find("button") != -1):
			if(numeroDuLoopEnCours == numeroDuBouton):
				c.pack_forget()
				c.destroy()
	if(str(choix).find("ancien")):
		boutonRemplacement(numeroDuBouton, "black","white")
	if(str(choix).find("nouveau")):
		boutonRemplacement(numeroDuBouton, "white","black")

def boutonRemplacement(numeroDuBouton, backgroundColor, foregroundColor):
	if(numeroDuBouton == 0):
		BTC = Button(root, text="BTC", width=15, command=affichageElementBTC)
		BTC.configure(background=backgroundColor)
		BTC.configure(foreground=foregroundColor)
		BTC.pack()
		BTC.place(bordermode=OUTSIDE, height=35, width=50,x=0, y=400)
	if(numeroDuBouton == 1):
		ETH = Button(root, text="ETH", width=15, command=affichageElementETH)
		ETH.configure(background=backgroundColor)
		ETH.configure(foreground=foregroundColor)
		ETH.pack()
		ETH.place(bordermode=OUTSIDE, height=35, width=50,x=50, y=400)
	if(numeroDuBouton == 2):
		DGE = Button(root, text="DGE", width=15, command=affichageElementDGE)
		DGE.configure(background=backgroundColor)
		DGE.configure(foreground=foregroundColor)
		DGE.pack()
		DGE.place(bordermode=OUTSIDE, height=35, width=50,x=100, y=400)
	if(numeroDuBouton == 3):
		IOTA = Button(root, text="IOTA", width=15, command=affichageElementIOTA)
		IOTA.configure(background=backgroundColor)
		IOTA.configure(foreground=foregroundColor)
		IOTA.pack()
		IOTA.place(bordermode=OUTSIDE, height=35, width=50,x=150, y=400)
	if(numeroDuBouton == 4):
		XRP = Button(root, text="XRP", width=15, command=affichageElementXRP)
		XRP.configure(background=backgroundColor)
		XRP.configure(foreground=foregroundColor)
		XRP.pack()
		XRP.place(bordermode=OUTSIDE, height=35, width=50,x=200, y=400)
	if(numeroDuBouton == 5):
		LTC = Button(root, text="LTC", width=15, command=affichageElementLTC)
		LTC.configure(background=backgroundColor)
		LTC.configure(foreground=foregroundColor)
		LTC.pack()
		LTC.place(bordermode=OUTSIDE, height=35, width=50,x=251, y=400)
	
root = Tk()
root.iconbitmap(default = "images/Dogecoin/Dogecoin.ico")
boutonExiste= False
arrayDesCryptos = ["BTC","ETH","DGE","IOTA","XRP","LTC"]
prog()


#
#TODO#
#
# A voir : il faut disable le fait que l'on puisse bouger la fenetre
#Effectuer une boucle pour faire un taux de rafraichissement que pour les variablePrixEnTempReels.
#Trouver un moyen de changer l'image (le graph)
#
#Regarder ce que fait le root.destroy // c'est pour faire un close complet de l'appli comme quand on fait un alt-f4