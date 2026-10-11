import pygame
import config


class SnakeGameEnv:
    def __init__(self):
        # 1. אתחול מנוע Pygame
        pygame.init()

        # 2. שמירת ממדי החלון
        self.w = config.WINDOW_WIDTH
        self.h = config.WINDOW_HEIGHT

        # 3. הקמת חלון התצוגה ושמירתו במשתנה של המחלקה
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake AI")

        # 4. שעון לשליטה בקצב הפריימים וגופן להצגת ניקוד
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('arial', 25)

        # 5. איפוס המשחק למצב התחלתי ראשון
        self.reset()

