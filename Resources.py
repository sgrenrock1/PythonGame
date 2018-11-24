__author__ = 'Steve'
import pygame.image as pgi
RABBIT = {
    "walkRight" : [pgi.load("img/rabRight0.gif"),
                   pgi.load("img/rabRight1.gif"),
                   pgi.load("img/rabRight2.gif"),
                   pgi.load("img/rabRight3.gif"),
                   pgi.load("img/rabRight4.gif"),
                   pgi.load("img/rabRight5.gif"),
                   pgi.load("img/rabRight6.gif"),
                   pgi.load("img/rabRight7.gif")],
    "walkLeft" : [pgi.load("img/rabLeft0.gif"),
                  pgi.load("img/rabLeft1.gif"),
                  pgi.load("img/rabLeft2.gif"),
                  pgi.load("img/rabLeft3.gif"),
                  pgi.load("img/rabLeft4.gif"),
                  pgi.load("img/rabLeft5.gif"),
                  pgi.load("img/rabLeft6.gif"),
                  pgi.load("img/rabLeft7.gif"),],
    "standRight" : [pgi.load("img/standRight.gif")],
    "standLeft" : [pgi.load("img/standLeft.gif"),],
    "attackRight" : [pgi.load("img/attackRight0.gif"),
                     pgi.load("img/attackRight1.gif"),
                     pgi.load("img/attackRight2.gif"),
                     pgi.load("img/attackRight3.gif"),
                     pgi.load("img/attackRight4.gif"),
                     pgi.load("img/attackRight5.gif"),
                     pgi.load("img/attackRight6.gif")],
    "attackLeft" : [pgi.load("img/attackLeft0.gif"),
                    pgi.load("img/attackLeft1.gif"),
                    pgi.load("img/attackLeft2.gif"),
                    pgi.load("img/attackLeft3.gif"),
                    pgi.load("img/attackLeft4.gif"),
                    pgi.load("img/attackLeft5.gif"),
                    pgi.load("img/attackLeft6.gif")],
    "dead" : [pgi.load("img/flowers.gif")]
}

PYTHON = {"moveLeft" : [pgi.load("img/pytemp.gif"),
                        pgi.load("img/pytempfast.gif")],
          "moveRight" : [pgi.load("img/pytemp1.gif"),
                         pgi.load("img/pytempfast1.gif")]}
STAR = {"moveRight" : [pgi.load("img/starRight0.png"),
                      pgi.load("img/starRight1.png"),
                      pgi.load("img/starRight2.png"),
                      pgi.load("img/starRight3.png"),
                      pgi.load("img/starRight4.png")],
        "moveLeft" : [pgi.load("img/starLeft0.png"),
                     pgi.load("img/starLeft1.png"),
                     pgi.load("img/starLeft2.png"),
                     pgi.load("img/starLeft3.png"),
                     pgi.load("img/starLeft4.png")]
}
BG_IMAGES = {"1" : pgi.load("img/bgtest.gif")}
GROUND = {"forest" : pgi.load("img/grass.gif")}
FLOWER = {"forest" : pgi.load("img/flowers.gif")}
BACK_DROP = {"forest" : pgi.load("img/trees.gif")}
GAME_OVER = pgi.load("img/game_over.gif")

