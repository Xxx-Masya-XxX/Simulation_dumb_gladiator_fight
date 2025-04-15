import sys
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout,QLabel,QListWidget,QVBoxLayout,QHBoxLayout,QScrollArea,QSizePolicy
from PySide6.QtCore import QTimer
from ..settings import *
from PySide6.QtCore import QSize
from ..GameObjects.entity import Entity
from ..GameObjects.item import Item
from collections import Counter

from ..utils.utils import rand_x, rand_y
from ..Game import Game

class GameWindow(QWidget):
    def __init__(self, game: Game):
        super().__init__()

        self.game = game
        self.render_frame = 1

        # --- Карта и скролл ---
        self.game_map = ButtonGrid(self, map_height, map_width)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.game_map)
        self.scroll_area.setWidgetResizable(True)
        # self.scroll_area.setFixedSize(800, 600)

        # --- Info-панель ---
        self.tick_label = QLabel("tick: 1")
        self.count_entity = QLabel("count_entity: 0")
        self.count_items = QLabel("count_items: 0")
        self.count_objects = QLabel("count_objects: 0")
        self.entity_list = QListWidget()


        # Упаковываем в layout
        info_layout = QVBoxLayout()
        info_layout.addWidget(self.tick_label)
        info_layout.addWidget(self.count_entity)
        info_layout.addWidget(self.count_items)
        info_layout.addWidget(self.count_objects)
        info_layout.addWidget(self.entity_list)

        # Обернём в виджет, чтобы управлять политикой
        info_widget = QWidget()
        info_widget.setLayout(info_layout)
        info_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        info_widget.setFixedWidth(400)  # или другой размер

        # --- Главный layout ---
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.scroll_area, stretch=1)  # растягиваем только карту
        main_layout.addWidget(info_widget)  # инфо-панель не растягиваем

        self.setLayout(main_layout)
        self.setWindowTitle("Game Window")

        # --- Таймер ---
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(100)

    def update_game(self):
        if self.game.is_over():
            self.game.update()  # твоя игровая логика
            self.render()
        else:
            pass
        
    def render(self):
        self.game_map.clear_all_buttons()
        for i in self.game.game_world.get_objects():
            pos = i.get_pos()
            self.game_map.set_button_text(pos[1], pos[0], i.render_img)

        type_counts = Counter(type(obj) for obj in self.game.game_world.get_objects())
        self.tick_label.setText("tick: "+str(self.render_frame))
        self.count_entity.setText("count_entity: "+str(type_counts.get(Entity, 0)))
        self.count_items.setText("count_items: "+str(type_counts.get(Item, 0)))
        self.count_objects.setText("count_objects: "+str(len(self.game.game_world.get_objects())))
        self.entity_list.clear()
        for i in self.game.game_world.get_objects():
            if isinstance(i,Entity):
                self.entity_list.addItem(i.__str__())
        self.render_frame += 1

        ...

class ButtonGrid(QWidget):
    def __init__(self,master, rows, cols):
        super().__init__(master)

        self.rows = rows
        self.cols = cols
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]

        layout = QGridLayout()
        self.setLayout(layout)

        button_size = 20  # Размер стороны квадрата

        for row in range(rows):
            for col in range(cols):
                btn = QPushButton(f" ")
                btn.setFixedSize(QSize(button_size, button_size))  # Квадратные кнопки
                self.buttons[row][col] = btn
                layout.addWidget(btn, row, col)

    def set_button_text(self, row, col, text):
        """Установить текст кнопки по координатам (row, col)."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.buttons[row][col].setText(text)
        else:
            print("Некорректные координаты")
            
    def clear_all_buttons(self):
            """Очистить текст на всех кнопках."""
            for row in range(self.rows):
                for col in range(self.cols):
                    self.buttons[row][col].setText("")
