import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QLabel,QListWidget,QVBoxLayout,QHBoxLayout
from PySide6.QtCore import QTimer
from settings import *
from PySide6.QtCore import QSize
from entity import Entity
from item import Item
from collections import Counter
from position import Position
from utils import rand_x, rand_y
from game_world import GameWorld

class GameWindow(QWidget):
    def __init__(self, game_world:GameWorld):
        super().__init__()

        self.game_world = game_world
        self.render_frame = 1

        # Создание виджетов
        self.game_map = ButtonGrid(self, map_height,map_width)
        self.tick_label = QLabel("tick: 1")
        self.count_entity = QLabel("count_entity: 0")
        self.count_items = QLabel("count_items: 0")
        self.count_objects = QLabel("count_objects: 0")
        self.entity_list = QListWidget()

        # Вертикальный блок справа
        info_layout = QVBoxLayout()
        info_layout.addWidget(self.tick_label)
        info_layout.addWidget(self.count_entity)
        info_layout.addWidget(self.count_items)
        info_layout.addWidget(self.count_objects)
        info_layout.addWidget(self.entity_list)

        # Главный горизонтальный layout: карта слева, инфо-колонка справа
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.game_map)
        main_layout.addLayout(info_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("Game Window")
                # запускаем таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(100)  # каждые 100 мс
        # self.render()

    def update_game(self):
        self.game_world.update()  # твоя игровая логика
        self.render()
    def render(self):
        self.game_map.clear_all_buttons()
        for i in self.game_world.get_objects():
            pos = i.get_pos()
            self.game_map.set_button_text(pos[1], pos[0], i.render_img)

        type_counts = Counter(type(obj) for obj in self.game_world.get_objects())
        self.tick_label.setText("tick: "+str(self.render_frame))
        self.count_entity.setText("count_entity: "+str(type_counts.get(Entity, 0)))
        self.count_items.setText("count_items: "+str(type_counts.get(Item, 0)))
        self.count_objects.setText("count_objects: "+str(len(self.game_world.get_objects())))
        self.entity_list.clear()
        for i in self.game_world.get_objects():
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = [
            Entity(position=Position(rand_x(),rand_y()),entity_id=1,render_img="@",hp=10,atk=1,stamina=20),
            Entity(position=Position(rand_x(),rand_y()),entity_id=2,render_img="@",hp=10,atk=4,stamina=20),
            Entity(position=Position(rand_x(),rand_y()),entity_id=3,render_img="@",hp=10,atk=1,stamina=20),
            Entity(position=Position(rand_x(),rand_y()),entity_id=4,render_img="@",hp=10,atk=1,stamina=20),
            Entity(position=Position(rand_x(),rand_y()),entity_id=5,render_img="@",hp=10,atk=1,stamina=20),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
            Item(position=Position(rand_x(),rand_y()),render_img="#",name="heal"),
        ]
    world = GameWorld(a)
    window = GameWindow(world)  # 4 строки, 5 столбцов
    window.setWindowTitle("2D Массив кнопок")
    window.show()
    sys.exit(app.exec())
