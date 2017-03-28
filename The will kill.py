
from gamelib import *

game = Game(1000, 800, "the will to kill")
bk = Image("images\\street2.jpg", game)

gambitwalk = Animation("images//gambit_walkforward ",4,game,frate=5)
gambitstrikehigh = Animation("images//gambit_stickstrikehigh ",10,game,frate=5)
gambitblock = Animation("images//gambit_block 1",8,game,frate=5)
gambitx = 800
gambity = 700
gambitstatus = "stand"

juggernautwalk = Animation("images//juggernaut_walk ",16,game,frate=5) 
juggernautstrike = Animation("images//juggernaut_strike ",9,game,frate=5)
juggernautroundhouse = Animation("images//juggernaut_roundhouse ",6,game,frate=5)
juggernautx = 150
juggernauty = 700
juggernautstatus = "stand"


bk.resizeTo(game.width, game.height)

game.setBackground(bk)


game.drawText("THE WILL TO KILL ",game.width/4 ,game.height/4,Font(red,90,red))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_SPACE)





health=100
while not game.over:
    game.processInput()
    
    bk.draw()
    if keys.Pressed[K_LEFT]:
        gambitstatus = "walkleft"
        gambitx -= 6
    elif keys.Pressed[K_RIGHT]:
        gambitstatus = "walkright"
        gambitx += 6
    elif keys.Pressed[K_o]:
        gambitstatus = "strikehigh"
    elif keys.Pressed[K_p]:
        gambitstatus = "block"
    if not keys.Pressed[K_LEFT] and not keys.Pressed[K_RIGHT] and not keys.Pressed[K_o] and not keys.Pressed[K_p]:
        gambitstatus = "stand"

    
    #gambit Animation Drawing Logic
    if gambitstatus == "walkleft":
        gambitwalk.x = gambitx
        gambitwalk.y = gambity
        gambitwalk.nextFrame()
    elif gambitstatus == "walkright":
        gambitwalk.x = gambitx
        gambitwalk.y = gambity
        gambitwalk.prevFrame()
    elif gambitstatus == "strikehigh":
        gambitstrikehigh.moveTo(gambitx,gambity)
        gambitstrikehigh.draw()
    elif gambitstatus == "block":
        gambitblock.moveTo(gambitx,gambity)
        gambitblock.draw()
    else:  
        gambitwalk.moveTo(gambitx,gambity)
        gambitwalk.draw()





   
    if keys.Pressed[K_a]: 
        juggernautstatus = "walkleft"
        juggernautx -= 6
    elif keys.Pressed[K_s]:
        juggernauttatus = "walkright"
        juggernautx += 6
    elif keys.Pressed[K_q]:
        juggernautstatus = "strike"
    if not keys.Pressed[K_q] and not keys.Pressed[K_a] and not keys.Pressed[K_s]:
        juggernautstatus = "stand"





    #juggernaut Animation Drawing Logic
    if juggernautstatus == "walkleft":
        juggernautwalk.x = juggernautx
        juggernautwalk.y = juggernauty
        juggernautwalk.nextFrame()
    elif  juggernautstatus == "walkright":
        juggernautwalk.x = juggernautx
        juggernautwalk.y = juggernauty
        juggernautwalk.prevFrame()
    elif  juggernautstatus == "strike":
        juggernautstrike.moveTo(juggernautx,juggernauty)
        juggernautstrike.draw()
    elif juggernautstatus == "roundhouse":
        juggernautroundhouse.moveTo(juggernautx,juggernauty)
        juggernautroundhouse.draw()
    else:  
        juggernautwalk.moveTo(juggernautx,juggernauty)
        juggernautwalk.draw()



    if juggernautstrike.collidedWith(gambitwalk):
        gambitwalk.health -= 1
    if gambitstrikehigh.collidedWith(juggernautwalk):
        juggernautwalk.health -= 1
    game.drawText("health: " + str(gambitwalk.health),150,5)
    game.drawText("health: " + str(juggernautwalk.health),800,5)

    if gambitwalk.health <=0 or juggernautwalk.health == 0:

  



        game.over = True
    

    game.update(60)


game.drawText("Game Over",game.width/4,game.height/3,Font(red,90,red))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(red,40,red))

game.update(40)
game.wait(K_ESCAPE)
game.quit()
