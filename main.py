import pygame
import sys
import quiz

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cool Game Name")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load background image
background_image = pygame.image.load("background.jpg") 

# Create font
font = pygame.font.Font(None, 36)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    submenu()

        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))  # Draw background image

        # Create buttons
        start_button = font.render("Start", True, BLACK)
        start_button_rect = pygame.Rect(300, 280, 200, 60)  # Rectangle dimensions

        # Draw buttons with rounded corners
        pygame.draw.rect(screen, GRAY, start_button_rect, border_radius=10)

        # Calculate centered position for text
        text_x = start_button_rect.x + (start_button_rect.width - start_button.get_width()) // 2
        text_y = start_button_rect.y + (start_button_rect.height - start_button.get_height()) // 2

        screen.blit(start_button, (text_x, text_y))

        pygame.display.flip()

def submenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer_button_rect.collidepoint(event.pos):
                    quiz.start_quiz()  # Start the quiz from the quiz module                elif multiplayer_button_rect.collidepoint(event.pos):
                    print("Multiplayer selected")
                elif options_button_rect.collidepoint(event.pos):
                    print("Options selected")
                

        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))  # Draw background image

        # Create buttons
        button_width = 240  # Adjust button width
        button_height = 60  # Adjust button height

        singleplayer_button = font.render("Singleplayer", True, BLACK)
        multiplayer_button = font.render("Multiplayer", True, BLACK)
        options_button = font.render("Options", True, BLACK)

        singleplayer_button_rect = pygame.Rect(280, 220, button_width, button_height)
        multiplayer_button_rect = pygame.Rect(280, 300, button_width, button_height)
        options_button_rect = pygame.Rect(280, 380, button_width, button_height)

        # Draw buttons with rounded corners
        pygame.draw.rect(screen, GRAY, singleplayer_button_rect, border_radius=10)
        pygame.draw.rect(screen, GRAY, multiplayer_button_rect, border_radius=10)
        pygame.draw.rect(screen, GRAY, options_button_rect, border_radius=10)

        # Calculate centered positions for text
        singleplayer_text_x = singleplayer_button_rect.x + (singleplayer_button_rect.width - singleplayer_button.get_width()) // 2
        singleplayer_text_y = singleplayer_button_rect.y + (singleplayer_button_rect.height - singleplayer_button.get_height()) // 2

        multiplayer_text_x = multiplayer_button_rect.x + (multiplayer_button_rect.width - multiplayer_button.get_width()) // 2
        multiplayer_text_y = multiplayer_button_rect.y + (multiplayer_button_rect.height - multiplayer_button.get_height()) // 2

        options_text_x = options_button_rect.x + (options_button_rect.width - options_button.get_width()) // 2
        options_text_y = options_button_rect.y + (options_button_rect.height - options_button.get_height()) // 2

        screen.blit(singleplayer_button, (singleplayer_text_x, singleplayer_text_y))
        screen.blit(multiplayer_button, (multiplayer_text_x, multiplayer_text_y))
        screen.blit(options_button, (options_text_x, options_text_y))

        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
