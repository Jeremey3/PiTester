import os
import pygame

def main():
    # Initialize Pygame
    pygame.init()

    # Set the display to the same resolution as the desktop
    display_info = pygame.display.Info()
    screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

    # Load the image
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testscreen.png")
    image = pygame.image.load(image_path)

    # Main loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False

        # Scale the image to fit the screen and blit it
        image_surface = pygame.transform.scale(image, (display_info.current_w, display_info.current_h))
        screen.blit(image_surface, (0, 0))

        pygame.display.flip()

        # Control the frame rate (30 FPS)
        clock.tick(30)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

