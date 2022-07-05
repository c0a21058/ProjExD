from tabnanny import check
from telnetlib import BM
from turtle import up
import pygame as pg
import sys
import random

def main():
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("ex04/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, angle =0,scale = 2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400
    
    bom_sfc=pg.Surface((20,20))#Surface
    bom_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bom_sfc,(255,0,0),(10,10),10)
    bomimg_rct=bom_sfc.get_rect()#Rect
    bomimg_rct.centerx=random.randint(0,screen_rct.width)
    bomimg_rct.centery=random.randint(0,screen_rct.height)
    vx,vy=+1,+1#爆弾の座標移動速度


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)


        for event in pg.event.get():
            if event.type==pg.QUIT:return
            
        key_states=pg.key.get_pressed()#辞書
        if key_states[pg.K_UP]==True: 
            tori_rct.centery-=1#y座標を-1

        if key_states[pg.K_DOWN]==True: 
            tori_rct.centery+=1#y座標を+1

        if key_states[pg.K_LEFT]==True: 
            tori_rct.centerx-=1#X座標を-1

        if key_states[pg.K_RIGHT]==True: 
            tori_rct.centerx+=1#x座標を+1

        if check(tori_rct,screen_rct)!=(1,1):#領域外
            if key_states[pg.K_UP]==True:
                 tori_rct.centery+=1#y座標を+1

            if key_states[pg.K_DOWN]==True: 
                tori_rct.centery-=1#y座標を-1

            if key_states[pg.K_LEFT]==True:
                 tori_rct.centerx+=1#X座標を+1

            if key_states[pg.K_RIGHT]==True: 
                tori_rct.centerx-=1#x座標を-1

        screen_sfc.blit(tori_sfc,tori_rct) 
        bomimg_rct.move_ip(vx,vy)

        screen_sfc.blit(bom_sfc,bomimg_rct)

        yoko,tate=check(bomimg_rct,screen_rct)
        vx*=yoko
        vy*=tate

        if tori_rct.colliderect(bomimg_rct):
            return 


    


        pg.display.update()
        clock.tick(1000)
def check(rct,scr_rct):
    '''
    [1]rct:こうかとんor爆弾のrect
    [2]scr_rct:スクリーンのRect
    '''
    yoko,tate=+1,+1#領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right:yoko=-1#領域外
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:tate=-1#領域外
    return yoko,tate



if __name__ =="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()


