from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from os import system

system("cls")

class games(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("game.png"))
        self.setWindowTitle("X va 0 o'yini")
        self.setFixedSize(430, 420)

        self.current_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = []

        button_positions = [
            (30, 20), (155, 20), (280, 20),
            (30, 145), (155, 145), (280, 145),
            (30, 270), (155, 270), (280, 270)
        ]

        for index, (x, y) in enumerate(button_positions):
            button = QPushButton("", self)
            button.setFixedSize(120, 120)
            button.setStyleSheet("font-size:30px")
            button.move(x, y)
            button.clicked.connect(lambda _, idx=index: self.make_move(idx))
            self.buttons.append(button)

        self.show()

    def make_move(self, index):
        row, col = divmod(index, 3)

        if self.board[row][col] == '':
            self.board[row][col] = self.current_turn
            self.buttons[index].setText(self.current_turn)

            if self.check_winner():
                self.show_winner(self.current_turn)
            elif self.check_tie():
                self.show_winner(None)

            self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self):

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def check_tie(self):

        for row in self.board:
            if '' in row:
                return False
        return True

    def show_winner(self, winner):

        if winner:
            QMessageBox.information(self, "O'yin tugadi", f"{winner} yutdi!")
        else:
            QMessageBox.information(self, "O'yin tugadi", "Durang!")
        self.reset_game()

    def reset_game(self):
        self.current_turn = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for button in self.buttons:
            button.setText("")

app = QApplication([])
oyna = games()
app.exec_()
