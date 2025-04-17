# import pygame
# import sys
# from collections import Counter
# from ..GameObjects.entity import Entity
# from ..GameObjects.item import Item
# from ..settings import map_width, map_height
# import pygame.freetype
# CELL_SIZE = 20
# INFO_PANEL_WIDTH = 300
# FPS = 60

# class GameRenderer:
#     def __init__(self):
#         pygame.init()
#         self.base_cell_size = CELL_SIZE
#         self.zoom = 1.0
#         self.offset_x = 0
#         self.offset_y = 0

#         self.screen_width = 1200
#         self.screen_height = 800
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_caption("Game Window")
#         self.clock = pygame.time.Clock()
#         # ⬇ ЗАГРУЗИ шрифт emoji
#         # На Windows можно попробовать 'seguiemj.ttf'
#         self.font = pygame.freetype.Font("fonts/NotoColorEmoji-Regular.ttf", 18)
#         self.tick = 1

#     def world_to_screen(self, x, y):
#         screen_x = x * self.base_cell_size * self.zoom + self.offset_x
#         screen_y = y * self.base_cell_size * self.zoom + self.offset_y
#         return int(screen_x), int(screen_y)

#     def draw_grid(self):
#         for y in range(map_height):
#             for x in range(map_width):
#                 screen_x, screen_y = self.world_to_screen(x, y)
#                 size = int(self.base_cell_size * self.zoom)
#                 if 0 <= screen_x < self.screen_width - INFO_PANEL_WIDTH and 0 <= screen_y < self.screen_height:
#                     rect = pygame.Rect(screen_x, screen_y, size, size)
#                     pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

#     def draw_objects(self, game):
#         for obj in game.game_world.get_objects():
#             x, y = obj.get_pos()
#             screen_x, screen_y = self.world_to_screen(x, y)
#             size = int(self.base_cell_size * self.zoom)
#             if isinstance(obj, Entity):
#                 color = (255, 0, 0)
#             elif isinstance(obj, Item):
#                 color = (0, 255, 0)
#             else:
#                 color = (0, 0, 255)

#             rect = pygame.Rect(screen_x, screen_y, size, size)
#             pygame.draw.rect(self.screen, color, rect)

#             if size > 10:
#                 self.font.render_to(self.screen, (screen_x + 2, screen_y + 2), obj.render_img, (0, 0, 0))


#     def draw_info_panel(self, game):
#         panel_x = self.screen_width - INFO_PANEL_WIDTH
#         pygame.draw.rect(self.screen, (30, 30, 30), (panel_x, 0, INFO_PANEL_WIDTH, self.screen_height))

#         objects = game.game_world.get_objects()
#         type_counts = Counter(type(obj) for obj in objects)

#         lines = [
#             f"Tick: {self.tick}",
#             f"Entities: {type_counts.get(Entity, 0)}",
#             f"Items: {type_counts.get(Item, 0)}",
#             f"Total: {len(objects)}",
#             "Entities list:"
#         ]

#         entities = [e for e in objects if isinstance(e, Entity)]
#         lines.extend(str(e) for e in entities[:10])

#         y = 10
#         for line in lines:
#             self.font.render_to(self.screen, (panel_x + 10, y), line, (255, 255, 255))
#             y += 20


#     def handle_zoom(self, event):
#         # Позиция мыши
#         mx, my = pygame.mouse.get_pos()

#         # До масштабирования
#         wx = (mx - self.offset_x) / (self.base_cell_size * self.zoom)
#         wy = (my - self.offset_y) / (self.base_cell_size * self.zoom)

#         # Изменяем масштаб
#         if event.y > 0:
#             self.zoom *= 1.1
#         elif event.y < 0:
#             self.zoom /= 1.1

#         # После масштабирования — пересчитать offset, чтобы "центрировать"
#         new_offset_x = mx - wx * self.base_cell_size * self.zoom
#         new_offset_y = my - wy * self.base_cell_size * self.zoom
#         self.offset_x = new_offset_x
#         self.offset_y = new_offset_y

#     def run(self, game):
#         running = True
#         while running:
#             self.clock.tick(FPS)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 elif event.type == pygame.MOUSEWHEEL:
#                     self.handle_zoom(event)

#             if game.is_over():
#                 game.update()
#                 self.tick += 1

#             self.screen.fill((0, 0, 0))
#             self.draw_grid()
#             self.draw_objects(game)
#             self.draw_info_panel(game)
#             pygame.display.flip()

#         pygame.quit()
import pygame
import sys
from collections import Counter
from ..GameObjects.entity import Entity
from ..GameObjects.item import Item
from ..settings import map_width, map_height

CELL_SIZE = 20
INFO_PANEL_WIDTH = 300
FPS = 60

class GameRenderer:
    def __init__(self):
        pygame.init()
        self.base_cell_size = CELL_SIZE
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0

        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Window")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Segoe UI Emoji", 16)
        self.tick = 1

    def world_to_screen(self, x, y):
        screen_x = x * self.base_cell_size * self.zoom + self.offset_x
        screen_y = y * self.base_cell_size * self.zoom + self.offset_y
        return int(screen_x), int(screen_y)

    def draw_grid(self):
        for y in range(map_height):
            for x in range(map_width):
                screen_x, screen_y = self.world_to_screen(x, y)
                size = int(self.base_cell_size * self.zoom)
                if 0 <= screen_x < self.screen_width - INFO_PANEL_WIDTH and 0 <= screen_y < self.screen_height:
                    rect = pygame.Rect(screen_x, screen_y, size, size)
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def draw_objects(self, game):
        for obj in game.game_world.get_objects():
            x, y = obj.get_pos()
            screen_x, screen_y = self.world_to_screen(x, y)
            size = int(self.base_cell_size * self.zoom)
            if isinstance(obj, Entity):
                color = (255, 0, 0)
            elif isinstance(obj, Item):
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            rect = pygame.Rect(screen_x, screen_y, size, size)
            pygame.draw.rect(self.screen, color, rect)

            if size > 10:
                text = self.font.render(str(obj.render_img), True, (0, 0, 0))
                self.screen.blit(text, (screen_x + 2, screen_y + 2))

    def draw_info_panel(self, game):
        panel_x = self.screen_width - INFO_PANEL_WIDTH
        pygame.draw.rect(self.screen, (30, 30, 30), (panel_x, 0, INFO_PANEL_WIDTH, self.screen_height))

        objects = game.game_world.get_objects()
        type_counts = Counter(type(obj) for obj in objects)

        lines = [
            f"Tick: {self.tick}",
            f"Entities: {type_counts.get(Entity, 0)}",
            f"Items: {type_counts.get(Item, 0)}",
            f"Total: {len(objects)}",
            "Entities list:"
        ]

        entities = [e for e in objects if isinstance(e, Entity)]
        lines.extend(str(e) for e in entities[:10])

        y = 10
        for line in lines:
            text = self.font.render(line, True, (255, 255, 255))
            self.screen.blit(text, (panel_x + 10, y))
            y += 20

    def handle_zoom(self, event):
        # Позиция мыши
        mx, my = pygame.mouse.get_pos()

        # До масштабирования
        wx = (mx - self.offset_x) / (self.base_cell_size * self.zoom)
        wy = (my - self.offset_y) / (self.base_cell_size * self.zoom)

        # Изменяем масштаб
        if event.y > 0:
            self.zoom *= 1.1
        elif event.y < 0:
            self.zoom /= 1.1

        # После масштабирования — пересчитать offset, чтобы "центрировать"
        new_offset_x = mx - wx * self.base_cell_size * self.zoom
        new_offset_y = my - wy * self.base_cell_size * self.zoom
        self.offset_x = new_offset_x
        self.offset_y = new_offset_y

    def run(self, game):
        running = True
        while running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEWHEEL:
                    self.handle_zoom(event)

            if game.is_over():
                game.update()
                self.tick += 1

            self.screen.fill((0, 0, 0))
            self.draw_grid()
            self.draw_objects(game)
            self.draw_info_panel(game)
            pygame.display.flip()

        pygame.quit()
