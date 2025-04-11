import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FPS Display")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройка часов и шрифта
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Основной игровой цикл
def main():
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(BLACK)

        # Получение текущего FPS
        fps = clock.get_fps()

        # Отображение текста с FPS
        fps_text = font.render(f"FPS: {int(fps)}", True, WHITE)
        screen.blit(fps_text, (10, 10))

        # Обновление экрана
        pygame.display.flip()

        # Ограничение FPS (например, до 60)
        clock.tick(60)

# Запуск программы
if __name__ == "__main__":
    main()