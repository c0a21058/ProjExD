from tabnanny import check
from telnetlib import BM
from turtle import up
import pygame as pg
import sys
import random

def main():
    tori=""
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("ex04/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    tori_sfc = pg.image.load(f"ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, angle =0,scale = 2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=random.randint(0,screen_rct.width),random.randint(0,screen_rct.height)
    
    bom_sfc=pg.Surface((20,20))#Surface
    bom_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bom_sfc,(255,0,0),(10,10),10)
    bomimg_rct=bom_sfc.get_rect()#Rect
    bomimg_rct.centerx=random.randint(0,screen_rct.width)
    bomimg_rct.centery=random.randint(0,screen_rct.height)
    vx,vy=+1,+1#爆弾の座標移動速度

    nise_bom_sfc1=pg.Surface((20,20))#Surface
    nise_bom_sfc1.set_colorkey((0,0,0))
    pg.draw.circle(nise_bom_sfc1,(255,255,0),(10,10),10)
    nise_bomimg_rct1=nise_bom_sfc1.get_rect()#Rect
    nise_bomimg_rct1.centerx=random.randint(0,screen_rct.width)
    nise_bomimg_rct1.centery=random.randint(0,screen_rct.height)
    vx1,vy1=+1,+1#爆弾の座標移動速度
    
    star_sfc=pg.image.load("ex04/starpng.png")
    star_sfc = pg.transform.rotozoom(star_sfc, angle =0,scale =0.2)
    star_rct=star_sfc.get_rect()
    star_rct.centerx=60
    star_rct.centery=100
    sx,sy=+1,+1#星の座標移動速度

    tori_sfc1 = pg.image.load(f"ex04/fig/7.png")#スターに当たった時にこうかとんを100,100に、目印として表記する
    tori_sfc1 = pg.transform.rotozoom(tori_sfc1, angle =0,scale = 1)
    tori_rct1=tori_sfc1.get_rect()
    tori_rct1.center=100,100

    nise_tori_sfc= pg.image.load(f"ex04/fig/2.png")#にせこうかとんの設定
    nise_tori_sfc = pg.transform.rotozoom(nise_tori_sfc, angle =0,scale = 2.0)
    nise_tori_rct=nise_tori_sfc.get_rect()
    nise_tori_rct.center=random.randint(0,screen_rct.width),random.randint(0,screen_rct.height)

    nise_tori_sfc1= pg.image.load(f"ex04/fig/3.png")#にせこうかとんの設定
    nise_tori_sfc1= pg.transform.rotozoom(nise_tori_sfc1, angle =0,scale = 2.0)
    nise_tori_rct1=nise_tori_sfc1.get_rect()
    nise_tori_rct1.center=random.randint(0,screen_rct.width),random.randint(0,screen_rct.height)



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
        screen_sfc.blit(nise_tori_sfc,nise_tori_rct) 
        screen_sfc.blit(nise_tori_sfc1,nise_tori_rct1) 
        bomimg_rct.move_ip(vx,vy)
        nise_bomimg_rct1.move_ip(vx1,vy1)
        star_rct.move_ip(sx,sy)

        screen_sfc.blit(bom_sfc,bomimg_rct)
        screen_sfc.blit(nise_bom_sfc1,nise_bomimg_rct1)
        screen_sfc.blit(star_sfc,star_rct)

        yoko,tate=check(bomimg_rct,screen_rct)
        vx*=yoko
        vy*=tate

        yoko,tate=check(nise_bomimg_rct1,screen_rct)
        vx1*=yoko
        vy1*=tate

        yoko,tat=check(star_rct,screen_rct)
        sx*=yoko
        sy*=tate
        if tori_rct.colliderect(star_rct):#星に当たると無敵になる
            tori="無敵"
        if tori=="無敵":
            screen_sfc.blit(tori_sfc1,tori_rct1) 

        if tori_rct.colliderect(bomimg_rct):
            if tori=="無敵":
                pass
            elif tori=="":
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


