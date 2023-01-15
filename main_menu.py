# здесь подключаются модули
import os

import pygame

import sys

# здесь определяются константы,
# классы и функции
FPS = 60

# здесь происходит инициация,
# создание объектов,
# подключение изображения
pygame.init()
pygame.display.set_mode((1330, 600))
clock = pygame.time.Clock()
screen = pygame.display.get_surface()
surface = pygame.image.load(os.path.join('images', 'fon1.jpg'))
screen.blit(surface, (0, 0))
pygame.display.flip()
# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # change the window screen title
    pygame.display.set_caption('Три в ряд')

    # Create a font file by passing font file
    # and size of the font
    font1 = pygame.font.SysFont('freesanbold.ttf', 25)
    font2 = pygame.font.SysFont('chalkduster.ttf', 40)
    with open('text/rules', encoding="utf-8") as file:
        data = file.read()
        print(data)
    # Render the texts that you want to display
    text1 = font1.render(data, False, (255, 255, 255), (255, 255, 255))
    text2 = font2.render('Удачи!', True, (255, 255, 255))


    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # deactivating the pygame library
                pygame.quit()

                # quitting the program.
                quit()

            # update the display
pygame.display.update()
