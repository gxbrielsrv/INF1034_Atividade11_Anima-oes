import pygame
import sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

frame_atual = 0
tempo_animacao = 0
frame_corrida = 0
tempo_corrida = 0
frame_pulo = 0
tempo_pulo = 0
animando_corrida = False
animando_pulo = False
virado_direita = True
x = 200
y = 300
velocidade = 3

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animações PyGame")

sprites_corrida = pygame.image.load("Knight 2D Pixel Art/Sprites/without_outline/RUN.png")
sprites_pulo = pygame.image.load("Knight 2D Pixel Art/Sprites/without_outline/JUMP.png")

imagens = []
for i in range(8):
    imagens.append(pygame.image.load(f"PNG_sequence/walkL{i+1}.png"))

largura_frame = 95
total_frames_corrida = sprites_corrida.get_width() // largura_frame
total_frames_pulo = sprites_pulo.get_width() // largura_frame

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and not animando_pulo:
                animando_pulo = True
                frame_pulo = 0
                tempo_pulo = 0

    teclas = pygame.key.get_pressed()

    if teclas[K_d]:
        animando_corrida = True
        virado_direita = True
        x += velocidade
    elif teclas[K_a]:
        animando_corrida = True
        virado_direita = False
        x -= velocidade
    else:
        animando_corrida = False

    x = max(0, min(800 - 180, x))
    dt = clock.tick(60)

    if animando_corrida:
        tempo_corrida += dt
        if tempo_corrida >= 100:
            frame_corrida = (frame_corrida + 1) % total_frames_corrida
            tempo_corrida = 0
    else:
        frame_corrida = 0

    tempo_animacao += dt
    if tempo_animacao >= 180:
        frame_atual = (frame_atual + 1) % len(imagens)
        tempo_animacao = 0
    if animando_pulo:
        tempo_pulo += dt
        if tempo_pulo >= 80:
            frame_pulo += 1
            if frame_pulo >= total_frames_pulo:
                frame_pulo = total_frames_pulo - 1
                animando_pulo = False
            tempo_pulo = 0

    tela.fill((255, 255, 255))
    tela.blit(imagens[frame_atual], (0, 0))
    frame = sprites_corrida.subsurface((largura_frame * frame_corrida, 0, largura_frame, 64))
    
    if not virado_direita:
        frame = pygame.transform.flip(frame, True, False)
    frame = pygame.transform.scale(frame, (180, 240))

    if animando_pulo:
        frame_pulo_img = sprites_pulo.subsurface((largura_frame * frame_pulo, 0, largura_frame, 64))
        if not virado_direita:
            frame_pulo_img = pygame.transform.flip(frame_pulo_img, True, False)
        frame_pulo_img = pygame.transform.scale(frame_pulo_img, (180, 240))
        tela.blit(frame_pulo_img, (x, y))
    else:
        tela.blit(frame, (x, y))

    pygame.display.update()