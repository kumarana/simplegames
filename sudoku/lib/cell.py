# lib/cell.py

import pygame
from .config import BLACK, GRAY, SELECTED_CELL_COLOR, HIGHLIGHT_COLOR, NUMBER_FONT

class Cell:
    def __init__(self, value, row, col, width, height, editable):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.editable = editable
        self.selected = False
        self.highlighted = False

    def draw(self, win):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap + 60  # Adjust for menu height

        if self.highlighted:
            pygame.draw.rect(win, HIGHLIGHT_COLOR, (x, y, gap, gap))

        if self.selected:
            pygame.draw.rect(win, SELECTED_CELL_COLOR, (x, y, gap, gap))

        if self.value != 0:
            font_color = GRAY if not self.editable else BLACK
            text = NUMBER_FONT.render(str(self.value), True, font_color)
            win.blit(
                text,
                (
                    x + (gap / 2 - text.get_width() / 2),
                    y + (gap / 2 - text.get_height() / 2),
                ),
            )
