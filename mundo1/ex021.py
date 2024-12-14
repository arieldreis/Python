import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('tell-me-the-truth-260010')
pygame.mixer.music.play()
pygame.event.wait()