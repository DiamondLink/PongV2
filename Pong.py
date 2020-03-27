#-*-coding:UTF-8 -*
import pygame
from pygame.image import *
from pygame.display import *
from pygame.locals import *
from tkinter import *
from pygame.mixer import *
import os
import time
from math import *
from constantes import *
from Classes import *
from random import *


pygame.mixer.init()
pygame.init()

continuer=True
bases=menu()
main=jeu()

music.load("musics//menu_theme.wav")
music.play(repeter_music)
pygame.key.set_repeat(1,1)
while continuer:

    for evenements in pygame.event.get():
        if evenements.type==QUIT:
            continuer=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>200 and evenements.pos[0]<450 and evenements.pos[1]>489 and evenements.pos[1]<552:
            afficher_credits=True
            afficher_menu=False
            bases.level_ok=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>200 and evenements.pos[0]<450 and evenements.pos[1]>426 and evenements.pos[1]<489 and afficher_menu==True:
            continuer=False
            bases.level_ok=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>240 and evenements.pos[0]<394 and evenements.pos[1]>581 and evenements.pos[1]<623 and afficher_credits==True:
            afficher_credits=False
            afficher_menu=True
            bases.level_ok=False
        
        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>200 and evenements.pos[0]<450 and evenements.pos[1]>300 and evenements.pos[1]<363 and afficher_menu==True:
            afficher_play=True
            afficher_menu=False
            afficher_credits=False
            bases.level_ok=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>240 and evenements.pos[0]<394 and evenements.pos[1]>581 and evenements.pos[1]<623 and afficher_play==True:
            afficher_play=False
            afficher_menu=True
            bases.level_ok=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>200 and evenements.pos[0]<455 and evenements.pos[1]>235 and evenements.pos[1]<315 and afficher_play==True:
            afficher_play=False
            afficher_play_ia=True
            bases.level_ok=False

        if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>240 and evenements.pos[0]<394 and evenements.pos[1]>586 and evenements.pos[1]<628 and afficher_play_ia==True:
            afficher_play_ia=False
            afficher_play=True
            bases.level_ok=False


        if afficher_play_ia_deux==True:

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>10 and evenements.pos[1]<67:
                bases.level_ok=True
                bases.difficulté=5
                afficher_play_ia=False
              

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>67 and evenements.pos[1]<124:
                bases.level_ok=True
                bases.difficulté=10
                afficher_play_ia=False
                
            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>124 and evenements.pos[1]<181:
                bases.level_ok=True
                bases.difficulté=20
                afficher_play_ia=False
      

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>181 and evenements.pos[1]<238:
                bases.level_ok=True
                bases.difficulté=25
                afficher_play_ia=False
            

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>238 and evenements.pos[1]<295:
                bases.level_ok=True
                bases.difficulté=35
                afficher_play_ia=False


            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>295 and evenements.pos[1]<352:
                bases.level_ok=True
                bases.difficulté=55
                afficher_play_ia=False
  

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>352 and evenements.pos[1]<409:
                bases.level_ok=True
                bases.difficulté=60
                afficher_play_ia=False
            
        
            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>409 and evenements.pos[1]<466:
                bases.level_ok=True
                bases.difficulté=70
                afficher_play_ia=False
                
            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>466 and evenements.pos[1]<523:
                bases.level_ok=True
                bases.difficulté=90
                afficher_play_ia=False
     

            if evenements.type==MOUSEBUTTONUP and evenements.button==1 and evenements.pos[0]>115 and evenements.pos[0]<515 and evenements.pos[1]>523 and evenements.pos[1]<580:
                bases.level_ok=True
                bases.difficulté=200
                afficher_play_ia=False

        if bases.level_ok==True: 
            if evenements.type==KEYDOWN and evenements.key==K_RIGHT and main.x_palette_un<490:
                main.deplacement_palette_droite()
            if evenements.type==KEYDOWN and evenements.key==K_LEFT and main.x_palette_un>0:
                main.deplacement_palette_gauche()




    if afficher_credits==True:
        bases.afficher_credits()

    if afficher_menu==True:
        bases.animation()
        bases.level_ok=False
        afficher_play=False
        afficher_play_ia=False
        afficher_play_ia_deux=False

    if afficher_play==True:
        bases.play()
        bases.level_ok=False
        afficher_play_ia=False
        afficher_play_ia_deux=False

    if afficher_play_ia==True:
        bases.play_ia()
        afficher_play_ia_deux=True
        bases.level_ok=False

    if bases.level_ok==True:
        if animation==True:
            music.stop()
            main.animation_play()
            animation=False
            main.coef_directeur=randrange(-4)
        
        if main.y_balle==1 or main.y_balle==629:
            main.fin_manche()

            

        main.afficher()
        main.deplacement_balle()

    flip()
