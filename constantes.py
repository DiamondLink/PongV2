#-*-coding:UTF-8 -*
import pygame
from pygame.image import *
from pygame.display import *
from pygame.locals import *
from pygame.font import *
from tkinter import *
from pygame.mixer import *
from random import *
import os
import time

pygame.mixer.init()
pygame.init()

fenetre_tk=Tk()
variable_tkinter=StringVar()
label_tkinter=Label(fenetre_tk,text="Voulez-vous continer en mode plein écran ?")
case_oui_tkinter=Radiobutton(fenetre_tk,text="oui",variable=variable_tkinter,value="oui")
case_non_tkinter=Radiobutton(fenetre_tk,text="non",variable=variable_tkinter,value="non")
bouton_tkinter=Button(fenetre_tk,text="Ok",command=fenetre_tk.destroy)
label_tkinter.grid(padx=50,pady=50)
case_oui_tkinter.grid(padx=40,pady=40)
case_non_tkinter.grid(padx=40,pady=40)
bouton_tkinter.grid(padx=50,pady=50)
case_non_tkinter.select()
fenetre_tk.mainloop()
variable_tkinter=variable_tkinter.get()
if variable_tkinter=="oui":
    fenetre=set_mode((630,630),FULLSCREEN)
else:
    fenetre=set_mode((630,630),RESIZABLE)


bouton_play_deux=load("sprites//bouton_play_deux.png").convert()
bouton_play_un=load("sprites//bouton_play_un.png").convert()
bouton_shop_un=load("sprites//bouton_shop_un.png").convert()
bouton_shop_deux=load("sprites//bouton_shop_deux.png").convert()
bouton_quitter_un=load("sprites//bouton_quitter_un.png").convert()
bouton_quitter_deux=load("sprites//bouton_quitter_deux.png").convert()
bouton_credits_un=load("sprites//bouton_credits_un.png").convert()
bouton_credits_deux=load("sprites//bouton_credits_deux.png").convert()
bouton_back_un=load("sprites//bouton_back_un.png").convert()
bouton_back_deux=load("sprites//bouton_back_deux.png").convert()
bouton_multiplayer_un=load("sprites//bouton_multiplayer_un.png").convert()
bouton_multiplayer_deux=load("sprites//bouton_multiplayer_deux.png").convert()
bouton_againstia_un=load("sprites//bouton_againstia_un.png").convert()
bouton_againstia_deux=load("sprites//bouton_againstia_deux.png").convert()
bouton_beginner_un=load("sprites//bouton_beginner_un.png").convert()
bouton_beginner_deux=load("sprites//bouton_beginner_deux.png").convert()
bouton_amateur_un=load("sprites//bouton_amateur_un.png").convert()
bouton_amateur_deux=load("sprites//bouton_amateur_deux.png").convert()
bouton_connoisseur_un=load("sprites//bouton_connoisseur_un.png").convert()
bouton_connoisseur_deux=load("sprites//bouton_connoisseur_deux.png").convert()
bouton_advanced_un=load("sprites//bouton_advanced_un.png").convert()
bouton_advanced_deux=load("sprites//bouton_advanced_deux.png").convert()
bouton_confirmed_un=load("sprites//bouton_confirmed_un.png").convert()
bouton_confirmed_deux=load("sprites//bouton_confirmed_deux.png").convert()
bouton_challenger_un=load("sprites//bouton_challenger_un.png").convert()
bouton_challenger_deux=load("sprites//bouton_challenger_deux.png").convert()
bouton_expert_un=load("sprites//bouton_expert_un.png").convert()
bouton_expert_deux=load("sprites//bouton_expert_deux.png").convert()
bouton_master_un=load("sprites//bouton_master_un.png").convert()
bouton_master_deux=load("sprites//bouton_master_deux.png").convert()
bouton_champion_un=load("sprites//bouton_champion_un.png").convert()
bouton_champion_deux=load("sprites//bouton_champion_deux.png").convert()
bouton_extreme_un=load("sprites//bouton_extreme_un.png").convert()
bouton_extreme_deux=load("sprites//bouton_extreme_deux.png").convert()
fond=load("sprites//fond.png").convert()
icone=load("sprites//icone.png").convert()
palette=load("sprites//palette.png").convert()
balle=load("sprites//balle.png").convert_alpha()

set_caption("Pong")
set_icon(icone)

police_blazed=Font("polices//Blazed.ttf",80)
police_fluogums=Font("polices//Fluo_Gums.ttf",20)
police_bigblack_bear=Font("polices//big_black_bear.ttf",16)
police_bigblack_bear_italic=Font("polices//big_black_bear_italic.ttf",16)
text_credits_un=police_fluogums.render("GAME BY :",1,(255,255,255))
text_credits_deux=police_fluogums.render("BAPTISTE VILLENEUVE",1,(255,255,255))
text_credits_trois=police_fluogums.render("SONGS :",1,(255,255,255))
text_credits_quatre=police_fluogums.render("WATERFLAMME - GLORIOUS MORNING",1,(255,255,255))
text_credits_cinq=police_fluogums.render("GEOPLEX - DAYBREAK",1,(255,255,255))
text_credits_six=police_fluogums.render("UNDERTALE - MEGALOVANIA",1,(255,255,255))
text_credits_sept=police_fluogums.render("ELEKTRONOMIA - SKYHIGH",1,(255,255,255))
text_credits_huit=police_fluogums.render("LINDSEY STIRLING - SHADOWS",1,(255,255,255))
text_credits_neuf=police_fluogums.render("ENVY - GRIZZLY",1,(255,255,255))
text_credits_dix=police_fluogums.render("ZLARK - LIGHTER",1,(255,255,255))
text_credits_onze=police_fluogums.render("ALAN WALKER - SPECTRE",1,(255,255,255))
text_credits_douze=police_fluogums.render("ALAN WALKER - FADED",1,(255,255,255))
text_credits_treize=police_fluogums.render("DIFFERENT HEAVEN - NEKOZILLA",1,(255,255,255))
text_credits_quatorze=police_fluogums.render("THE FAT RAT - XENOGENESIS",1,(255,255,255))

compteur_3=police_blazed.render("3",1,(255,255,255))
compteur_2=police_blazed.render("2",1,(255,255,255))
compteur_1=police_blazed.render("1",1,(255,255,255))
compteur_go=police_blazed.render("GO!",1,(255,255,255))

version_jeu=police_bigblack_bear.render(" beta 0.2.2",1,(255,255,255))

son_go=Sound("musics//go.wav")
son_compteur=Sound("musics//compteur.wav")




titre=police_blazed.render("Pong",1,(255,255,255))

repeter_music=999999999
vitesse_balle=5

afficher_menu=True
afficher_credits=False
afficher_play=False
afficher_play_ia=False
afficher_play_ia_deux=False
animation=True









