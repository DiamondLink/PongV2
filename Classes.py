#-*-coding:UTF-8 -*
import pygame
from pygame.image import *
from pygame.display import *
from pygame.locals import *
from pygame.mixer import *
from tkinter import *
from constantes import *
from random import *
from math import *
import os
import time
pygame.mixer.init()
pygame.init()






class menu:
    def __init__(self):
        self.x=-140
        self.y=randrange(5,613)
        self.difficulté=False
        self.level_ok=False
    
    def afficher_credits(self):
        fenetre.blit(fond,(0,0))
        fenetre.blit(text_credits_un,(250,10))
        fenetre.blit(text_credits_deux,(150,75))
        fenetre.blit(text_credits_trois,(255,150))
        fenetre.blit(text_credits_quatre,(10,200))
        fenetre.blit(text_credits_cinq,(103,233))
        fenetre.blit(text_credits_six,(100,266))
        fenetre.blit(text_credits_sept,(106,299))
        fenetre.blit(text_credits_huit,(101,332))
        fenetre.blit(text_credits_neuf,(150,365))
        fenetre.blit(text_credits_dix,(154,398))
        fenetre.blit(text_credits_onze,(104,431))
        fenetre.blit(text_credits_douze,(100,464))
        fenetre.blit(text_credits_treize,(50,497))
        fenetre.blit(text_credits_quatorze,(65,530))
        
        position_souris=pygame.mouse.get_pos()

        if position_souris[0]>240 and position_souris[0]<394 and position_souris[1]>581 and position_souris[1]<623:
            fenetre.blit(bouton_back_deux,(240,581))
        else:
            fenetre.blit(bouton_back_un,(240,581))




    def animation(self):
        fenetre.blit(fond,(0,0))
        fenetre.blit(palette,(self.x,self.y))
        fenetre.blit(titre,(150,93))

        position_souris=pygame.mouse.get_pos()
        if position_souris[0]>200 and position_souris[0]<450 and position_souris[1]>300 and position_souris[1]<363:
            fenetre.blit(bouton_play_deux,(200,300))
        else:
            fenetre.blit(bouton_play_un,(200,300))


        if position_souris[0]>200 and position_souris[0]<450 and position_souris[1]>363 and position_souris[1]<426:
            fenetre.blit(bouton_shop_deux,(200,363))
        else:
            fenetre.blit(bouton_shop_un,(200,363))


        if position_souris[0]>200 and position_souris[0]<450 and position_souris[1]>426 and position_souris[1]<489:
            fenetre.blit(bouton_quitter_deux,(200,426))
        else:
            fenetre.blit(bouton_quitter_un,(200,426))


        if position_souris[0]>200 and position_souris[0]<450 and position_souris[1]>489 and position_souris[1]<552:
            fenetre.blit(bouton_credits_deux,(200,489))
        else:
            fenetre.blit(bouton_credits_un,(200,489))
  
        self.x+=1
        if self.x==630:
            self.x=-140
            self.y=randrange(5,613)
            if self.y<200 and self.y>85: 
                self.x=629


        fenetre.blit(version_jeu,(285,610))
    
    def play(self):
        fenetre.blit(fond,(0,0))

        position_souris=pygame.mouse.get_pos()

        if position_souris[0]>200 and position_souris[0]<455 and position_souris[1]>235 and position_souris[1]<315:
            fenetre.blit(bouton_againstia_deux,(200,235))
        else:
            fenetre.blit(bouton_againstia_un,(200,235))

        if position_souris[0]>200 and position_souris[0]<455 and position_souris[1]>315 and position_souris[1]<395:
            fenetre.blit(bouton_multiplayer_deux,(200,315))
        else:
            fenetre.blit(bouton_multiplayer_un,(200,315))

        if position_souris[0]>240 and position_souris[0]<394 and position_souris[1]>581 and position_souris[1]<623:
            fenetre.blit(bouton_back_deux,(240,581))
        else:
            fenetre.blit(bouton_back_un,(240,581))

    def play_ia(self):
        fenetre.blit(fond,(0,0))

        position_souris=pygame.mouse.get_pos()

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>10 and position_souris[1]<67:
            fenetre.blit(bouton_beginner_deux,(115,10))
        else:
            fenetre.blit(bouton_beginner_un,(115,10))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>67 and position_souris[1]<124:
            fenetre.blit(bouton_amateur_deux,(115,67))
        else:
            fenetre.blit(bouton_amateur_un,(115,67))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>124 and position_souris[1]<181:
            fenetre.blit(bouton_connoisseur_deux,(115,124))
        else:
            fenetre.blit(bouton_connoisseur_un,(115,124))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>181 and position_souris[1]<238:
            fenetre.blit(bouton_advanced_deux,(115,181))
        else:
            fenetre.blit(bouton_advanced_un,(115,181))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>238 and position_souris[1]<295:
            fenetre.blit(bouton_confirmed_deux,(115,238))
        else:
            fenetre.blit(bouton_confirmed_un,(115,238))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>295 and position_souris[1]<352:
            fenetre.blit(bouton_challenger_deux,(115,295))
        else:
            fenetre.blit(bouton_challenger_un,(115,295))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>352 and position_souris[1]<409:
            fenetre.blit(bouton_expert_deux,(115,352))
        else:
            fenetre.blit(bouton_expert_un,(115,352))
        
        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>409 and position_souris[1]<466:
            fenetre.blit(bouton_master_deux,(115,409))
        else:
            fenetre.blit(bouton_master_un,(115,409))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>466 and position_souris[1]<523:
            fenetre.blit(bouton_champion_deux,(115,466))
        else:
            fenetre.blit(bouton_champion_un,(115,466))

        if position_souris[0]>115 and position_souris[0]<515 and position_souris[1]>523 and position_souris[1]<580:
            fenetre.blit(bouton_extreme_deux,(115,523))
        else:
            fenetre.blit(bouton_extreme_un,(115,523))

        if position_souris[0]>240 and position_souris[0]<394 and position_souris[1]>586 and position_souris[1]<628:
            fenetre.blit(bouton_back_deux,(240,586))
        else:
            fenetre.blit(bouton_back_un,(240,586))

class jeu:
    def __init__(self):
        self.x_palette_un=240
        self.x_palette_deux=240
        self.x_balle=300
        self.y_balle=300 
        self.coef_directeur=None
        self.a_function=None
        self.b_function=None

            
    def make_function(self):

        if self.direction_balle==90:
            if randrange(2)==0:
                self.direction_balle=92
            else:
                self.direction_balle=88
        
        self.b_function=tan(radians(self.direction_balle)*self.x_balle)
        self.a_function=(self.y_balle-self.b_function)/self.x_balle



    def afficher(self):
        print(self.x_balle,"    ",self.y_balle,"    ",self.direction_balle,"    ",self.a_function,"     ",self.b_function)
        fenetre.blit(fond,(0,0))
        fenetre.blit(palette,(self.x_palette_un,542))
        fenetre.blit(palette,(self.x_palette_deux,70))
        fenetre.blit(balle,(self.x_balle,self.y_balle))
        
    def animation_play(self):
        fenetre.blit(fond,(0,0))
        fenetre.blit(compteur_3,(280,280))
        son_compteur.play()
        flip()
        time.sleep(1)
        fenetre.blit(fond,(0,0))
        fenetre.blit(compteur_2,(280,280))
        son_compteur.play()
        flip()
        time.sleep(1)
        fenetre.blit(fond,(0,0))
        fenetre.blit(compteur_1,(280,280))
        son_compteur.play()
        flip()
        time.sleep(1)
        fenetre.blit(fond,(0,0))
        fenetre.blit(compteur_go,(180,280))
        son_go.play()
        flip()
        time.sleep(0.6)
        self.x_palette_un=240
        self.x_palette_deux=240
        self.x_balle=300
        self.y_balle=300 
    
    def deplacement_palette_droite(self):
        
        for loop in range(2):
            self.x_palette_un+=1
            fenetre.blit(palette,(self.x_palette_un,542))
            flip()
      


    def deplacement_palette_gauche(self):

        for loop in range(2):
            self.x_palette_un-=1
            fenetre.blit(palette,(self.x_palette_un,542))
            flip()


    def deplacement_balle(self):
  
        if self.direction_balle>90:
            if self.player_side==True:
                self.x_balle+=1
            else:
                self.x_balle-=1
        else:
            if self.player_side==True:
                self.x_balle-=1
            else:
                self.x_balle+=1

        self.y_balle=(self.a_function*self.x_balle)+self.b_function
        self.y_balle=int(self.y_balle)
        self.x_balle=int(self.x_balle)



    def fin_manche(self):
        pass

            







































































































































        
       






    