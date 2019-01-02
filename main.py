import pygame
import bricks
import levels


def make_screen():
    screen_size = 1000, 600
    return pygame.display.set_mode(screen_size)


def render_background(screen):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((240, 240, 240))
    screen.blit(background, (0, 0))


def render_level(screen, level):
    brick_map = {
        levels.EMPTY: None,
        levels.WALL: bricks.wall,
        levels.BOX: bricks.box,
        levels.TARGET: bricks.target,
        levels.BOX_ON_TARGET: bricks.player
    }
    elem_width = 50

    # define x,y initial offset
    screen_size = screen.get_size()
    level_size = (len(level[0]) * elem_width), (len(level) * elem_width)
    x_offset = (screen_size[0] - level_size[0]) / 2
    y_offset = (screen_size[1] - level_size[1]) / 2

    y = y_offset
    for line in level:
        x = x_offset
        for elem in line:
            brick = brick_map.get(elem, None)
            if brick is not None:
                screen.blit(brick, (x, y))
            x += elem_width
        y += elem_width


def check_events():
    # user events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)


def main():
    pygame.init()
    pygame.display.set_caption('SOKOBAN')
    clock = pygame.time.Clock()
    screen = make_screen()
    while True:
        clock.tick(60)
        check_events()
        # screen.fill(0)
        render_background(screen)
        render_level(screen, levels.get_level())
        pygame.display.flip()


if __name__ == '__main__':
    main()
