import numpy as np
import pygame
import pygame_menu
import math
import button


# class Personagem:
#     def __init__(self) -> None:
#         pass

#     def poke(self, image):
#         pass




if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("PokeFlappy")
    FPS = 60  # frames por segundo
    scroll_x = 0
    width = 400
    height = 800
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))

    menu = "main"
    volume = 0.4

    #bg
    scene = pygame.image.load("images/background.jpg")
    scene = pygame.transform.scale(scene, (width, height))


    #Botão de play
    play_img = pygame.image.load("images/play2.png").convert_alpha()
    play_size = (240, 160)
    play_img = pygame.transform.scale(play_img, play_size)

    #identificar imagem como botão
    play_button = button.Button(width/4, height/2.8, play_img, 1)

    #botão de options
    options_img = pygame.image.load("images/option3.png").convert_alpha()
    options_size = (100,100)
    options_img = pygame.transform.scale(options_img, options_size)

    #identificar options como botão
    options_button = button.Button(width/20, 685, options_img, 1) \
    

    # botão leaderboards
    lb_img = pygame.image.load("images/leaderboard2.png").convert_alpha()
    lb_size = (90,120)
    lb_img = pygame.transform.scale(lb_img, lb_size)

    #identificar leaderboard como botao
    lb_button = button.Button(width/1.4, 680, lb_img, 1)

    #botão back
    back_img = pygame.image.load("images/back2.png").convert_alpha()
    back_size = (80, 80)
    back_img = pygame.transform.scale(back_img, back_size)

    #identificar back como botao
    back_button = button.Button(1, 1, back_img, 1)

    #botão aumentar volume
    volup_img = pygame.image.load("images/volume_up.png").convert_alpha()
    volup_size = (100,100)
    volup_img = pygame.transform.scale(volup_img, volup_size)

    #identificar imagem como botao
    volup_button = button.Button(300, 350, volup_img, 1)

    #botão diminuir volume
    voldown_img = pygame.image.load("images/volume_down.png").convert_alpha()
    voldown_size = (100,100)
    voldown_img = pygame.transform.scale(voldown_img, voldown_size)

    #identificar imagem como botao
    voldown_button = button.Button(1, 350, voldown_img, 1)





    #musica
    pygame.mixer.music.load("music/music1.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volume)


    game_on = True
    while game_on:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                


        for i in range(0, 2):  # garante que há continuidade na movimentação do cenário
            screen.blit(scene, (i * scene.get_width() + scroll_x, 0))

        scroll_x -= 2
        if (abs(scroll_x) > width):
            scroll_x = 0

        if menu == "main":
            if play_button.draw(screen):
                menu == "play"
            if options_button.draw(screen):
                menu = "options"
            if lb_button.draw(screen):
                menu = "leaderboard"

        if menu == "play":
            pass
        #rodar o jogo aqui

        if menu == "options":
            if back_button.draw(screen):
                menu = "main"
            if volup_button.draw(screen):
                if (volume < 1):
                    volume+=0.2
                    pygame.mixer.music.set_volume(volume)
                else:
                    volume = 1
                    pygame.mixer.music.set_volume(volume)
            if voldown_button.draw(screen):
                if(volume > 0):
                    volume-=0.2
                    pygame.mixer.music.set_volume(volume)
                else:
                    volume=0
                    pygame.mixer.music.set_volume(volume)
                
                
                

        if menu == "leaderboard":
            if back_button.draw(screen):
                menu = "main"
                

        pygame.display.update()
    pygame.quit()
