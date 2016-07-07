import pygame


data_folder = 'data/'

pics = {}
pics['r'] = pygame.image.load(data_folder+'r-b.png')
pics['n'] = pygame.image.load(data_folder+'n-b.png')
pics['b'] = pygame.image.load(data_folder+'b-b.png')
pics['q'] = pygame.image.load(data_folder+'q-b.png')
pics['k'] = pygame.image.load(data_folder+'k-b.png')
pics['p'] = pygame.image.load(data_folder+'p-b.png')
pics['R'] = pygame.image.load(data_folder+'r-w.png')
pics['N'] = pygame.image.load(data_folder+'n-w.png')
pics['B'] = pygame.image.load(data_folder+'b-w.png')
pics['Q'] = pygame.image.load(data_folder+'q-w.png')
pics['K'] = pygame.image.load(data_folder+'k-w.png')
pics['P'] = pygame.image.load(data_folder+'p-w.png')

DISPLAY = (1000, 320)
scale = 40
pygame.init()
flags = pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode(DISPLAY)
screen = pygame.display.set_mode(DISPLAY, flags)
pygame.display.set_caption("Chesster")


def visualize(board, act1, act2, gap_size, x0, y0,):
    background = pygame.Surface(DISPLAY)
    background.fill(pygame.Color("#000000"))
    text = str(board)
    k = 0
    for i in text:
        if i != '\n' and i != ' ':
            x = k % 8
            y = k / 8
            # drawing board
            rect = pygame.Rect(x*scale+x0, y*scale+y0, scale, scale)
            if (x + y) % 2 == 0:
                clr = pygame.Color(60, 60, 60, 255)
            else:
                clr = pygame.Color(180, 180, 180, 255)
            pygame.draw.rect(screen, clr, rect)
            # drawing figures
            if i != '.':
                screen.blit(pics[i], (x*scale+x0, y*scale+y0))
            k += 1
    k = 0
    if act1:
        for i in act1:
            x = k % 8
            y = k / 8
            # drawing board
            rect = pygame.Rect((x+8)*scale+x0+gap_size, y*scale+y0, scale, scale)
            clr = pygame.Color('#000000')
            clr.hsva = [250*(1-i), 100, 50+50**i, 100]
            pygame.draw.rect(screen, clr, rect)
            # drawing figures
            k += 1
    k = 0
    if act2:
        for i in act2:
            x = k % 8
            y = k / 8
            # drawing board
            rect = pygame.Rect((x+16)*scale+x0+2*gap_size, y*scale+y0, scale, scale)
            clr = pygame.Color('#000000')
            clr.hsva = [250*(1-i), 100, 50+50**i, 100]
            pygame.draw.rect(screen, clr, rect)
            # drawing figures
            k += 1
    pygame.display.update()
    #from time import sleep
    #sleep(10)

