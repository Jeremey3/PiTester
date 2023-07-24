import os
import pygame
from moviepy.editor import VideoFileClip

def main():
    # Initialize Pygame
    pygame.init()

    # Set the display to the same resolution as the desktop
    display_info = pygame.display.Info()
    screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

    # Load the video file using moviepy
    video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Testvid.mp4")
    video_clip = VideoFileClip(video_path)

    # Play the video fullscreen
    frame_index = 0
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False

        # Get the current frame from the video clip
        frame = video_clip.get_frame(frame_index / video_clip.fps)
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.scale(frame_surface, (display_info.current_w, display_info.current_h))

        # Blit the current video frame on the screen
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        # Control the frame rate (30 FPS)
        clock.tick(30)

        # Move to the next frame (looping back to the beginning if necessary)
        frame_index = (frame_index + 1) % int(video_clip.fps * video_clip.duration)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
