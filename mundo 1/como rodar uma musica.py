import pygame

pygame.mixer.init()

pygame.init()

pygame.mixer.music.load('OST.mp3')
pygame.mixer.music.play(loops=0, start=0.0, fade_ms = 0)
pygame.event.wait()
