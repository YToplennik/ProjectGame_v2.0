import sys
import sqlite3
import random
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import tkinter as tk
from tkinter import simpledialog


class Lobby(QMainWindow):
    def __init__(self, con, max_timer):
        super().__init__()
        self.initUI()
        self.con = con
        self.max_timer = max_timer

    def initUI(self):
        uic.loadUi('untitled.ui', self)

        self.btnPlay.clicked.connect(self.openGame)
        self.Exit.clicked.connect(self.close)
        self.btnLiders.clicked.connect(self.Liders)
        self.btnSkins.clicked.connect(self.openSkins)

    def openGame(self):
        self.btnPlay.setEnabled(False)
        ROOT = tk.Tk()

        ROOT.withdraw()
        self.USER_INP = simpledialog.askstring(title="Test",
                                               prompt="Как тебя зовут?:")
        if self.USER_INP:
            self.Game = Game(self.con, self.USER_INP, self.max_timer)
            self.Game.show()
            self.btnPlay.setEnabled(True)
        else:
            self.btnPlay.setEnabled(True)

    def Liders(self):
        self.Liders = Liders()
        self.Liders.show()

    def openSkins(self):
        self.skins = Skins()


class Game(QWidget):
    def __init__(self, coun, user, max_timer):
        super().__init__()
        self.max_timer = max_timer
        self.initUI()
        self.user = user
        self.color_True = (random.choice([255, 0]), 255, random.choice([255, 0]))
        self.hide_buttons_and_connect()
        self.setButtonColorBase()
        self.Gameover_text.hide()
        self.timeBar.setValue(100)
        self.count = coun
        self.count1 = coun

    def hide_buttons_and_connect(self):
        for y in range(4):
            for x in range(4):
                eval('self.gameButton_{}'.format(str(x) + str(y))).hide()

        self.gameButton_40.hide()
        self.gameButton_41.hide()
        self.gameButton_42.hide()
        self.gameButton_True.hide()

        # коннектим неправильные кнопки
        for y in range(4):
            for x in range(4):
                eval('self.gameButton_{}'.format(str(x) + str(y))).clicked.connect(self.FalseButton)

        self.gameButton_40.clicked.connect(self.FalseButton)
        self.gameButton_41.clicked.connect(self.FalseButton)
        self.gameButton_42.clicked.connect(self.FalseButton)

    def setButtonColorBase(self):
        # Устанавливаем цвет кнопок
        for y in range(4):
            for x in range(4):
                eval('self.gameButton_{}'.format(str(x) + str(y))).setStyleSheet('background-color: #FFFFFF')

        self.gameButton_40.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_41.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_42.setStyleSheet('background-color: #FFFFFF')
        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}')

    def setButtonColor(self):
        # for i in range(19):
        #     if self.lvl > i:
        #         b = self.randomColor()
        #         self.gameButton_00.setStyleSheet(f'background-color: rgb{b}')
        #         self.randomFalseText(f'self.gameButton_{}{}', b)
        if self.lvl > 0:
            b = self.randomColor()
            self.gameButton_00.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_00', b)
        if self.lvl > 1:
            b = self.randomColor()
            self.gameButton_01.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_01', b)
        if self.lvl > 2:
            b = self.randomColor()
            self.gameButton_02.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_02', b)
        if self.lvl > 3:
            b = self.randomColor()
            self.gameButton_03.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_03', b)
        if self.lvl > 4:
            b = self.randomColor()
            self.gameButton_10.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_10', b)
        if self.lvl > 5:
            b = self.randomColor()
            self.gameButton_11.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_11', b)
        if self.lvl > 6:
            b = self.randomColor()
            self.gameButton_12.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_12', b)
        if self.lvl > 7:
            b = self.randomColor()
            self.gameButton_13.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_13', b)
        if self.lvl > 8:
            b = self.randomColor()
            self.gameButton_20.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_20', b)
        if self.lvl > 9:
            b = self.randomColor()
            self.gameButton_21.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_21', b)
        if self.lvl > 10:
            b = self.randomColor()
            self.gameButton_22.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_22', b)
        if self.lvl > 11:
            b = self.randomColor()
            self.gameButton_23.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_23', b)
        if self.lvl > 12:
            b = self.randomColor()
            self.gameButton_30.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_30', b)
        if self.lvl > 13:
            b = self.randomColor()
            self.gameButton_31.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_31', b)
        if self.lvl > 14:
            b = self.randomColor()
            self.gameButton_32.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_32', b)
        if self.lvl > 15:
            b = self.randomColor()
            self.gameButton_33.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_33', b)
        if self.lvl > 16:
            b = self.randomColor()
            self.gameButton_40.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_40', b)
        if self.lvl > 17:
            b = self.randomColor()
            self.gameButton_41.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_41', b)
        if self.lvl > 18:
            b = self.randomColor()
            self.gameButton_42.setStyleSheet(f'background-color: rgb{b}')
            self.randomFalseText('self.gameButton_42', b)

    def show_buttons(self):
        for y in range(4):
            for x in range(4):
                eval('self.gameButton_{}'.format(str(x) + str(y))).show()

        self.gameButton_40.show()
        self.gameButton_41.show()
        self.gameButton_42.show()
        self.gameButton_True.show()

        self.StartBtn.hide()
        self.StartBtn.resize(0, 0)

    def initUI(self):
        self.lvl = 0
        uic.loadUi('Game.ui', self)
        self.StartBtn.clicked.connect(self.StartGame)
        self.tab = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButtonTxt)
        self.button_group.addButton(self.radioButtonRGB)
        self.button_group.addButton(self.radioButtonOr)
        self.button_group.buttonClicked.connect(self.radio)
        self.retrybtn.hide()
        self.exitbtn.hide()
        self.retrybtn.clicked.connect(self.retry)
        self.exitbtn.clicked.connect(self.close)

    def StartGame(self):
        self.gameButton_True.clicked.connect(self.TrueButton)
        self.timeText.setText(str(self.count))
        self.radioButtonRGB.hide()
        self.radioButtonTxt.hide()
        self.radioButtonOr.hide()
        self.timeBar.setValue(int(self.count / (self.max_timer / 100)))
        self.game()
        self.show_buttons()
        self.new_lvl()

    def game(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Timeme)
        self.timer.start(1000)

    def randomColor(self):
        return random.choice([255, 0]), random.choice([255, 0]), random.choice([255, 0])

    def Timeme(self):
        if self.count > 1:
            self.count -= 1
            self.timeText.setText(str(self.count))
            self.timeBar.setValue(int(self.count / (self.max_timer / 100)))
            # print(self.count)
        else:
            self.timeText.setText(str(0))
            self.timeBar.setValue(int(0))
            self.endGame()
            # print(self.count - 1)

    def radio(self, button):
        if button.text() == 'Текстовый режим':
            self.rezim = 'txt'
        elif button.text() == 'RGB режим':
            self.rezim = 'rgb'
        elif button.text() == 'Смешанный':
            self.rezim = 'or'
        self.StartBtn.setEnabled(True)

    def randomFalseText(self, a, col):
        flag = True
        while flag:
            g = self.randomColor()
            eval(a).setText(f'{g}')
            if col == (0, 0, 0) or col == (0, 0, 255):
                eval(a).setStyleSheet(f'background-color: rgb{col}; color: white;')
            else:
                eval(a).setStyleSheet(f'background-color: rgb{col}; color: black;')
            if g != col:
                flag = False
        self.rgbInText(g, a)

    def rgbInText(self, g, a):
        if self.rezim == 'txt':
            if g == (0, 0, 0):
                eval(a).setText('Чёрный')
            elif g == (255, 0, 0):
                eval(a).setText('Красный')
            elif g == (0, 255, 0):
                eval(a).setText('Зелёный')
            elif g == (0, 0, 255):
                eval(a).setText('Синий')
            elif g == (255, 0, 255):
                eval(a).setText('Розовый')
            elif g == (0, 255, 255):
                eval(a).setText('Голубой')
            elif g == (255, 255, 255):
                eval(a).setText('Белый')
            elif g == (255, 255, 0):
                eval(a).setText('Жёлтый')
        elif self.rezim == 'rgb':
            if g == (0, 0, 0):
                eval(a).setText('0 0 0')
            elif g == (255, 0, 0):
                eval(a).setText('255 0 0')
            elif g == (0, 255, 0):
                eval(a).setText('0 255 0')
            elif g == (0, 0, 255):
                eval(a).setText('0 0 255')
            elif g == (255, 0, 255):
                eval(a).setText('255 0 255')
            elif g == (0, 255, 255):
                eval(a).setText('0 255 255')
            elif g == (255, 255, 255):
                eval(a).setText('255 255 255')
            elif g == (255, 255, 0):
                eval(a).setText('255 255 0')
        elif self.rezim == 'or':
            if g == (0, 0, 0):
                eval(a).setText(random.choice(['Чёрный', '0, 0, 0']))
            elif g == (255, 0, 0):
                eval(a).setText(random.choice(['Красный', '255, 0, 0']))
            elif g == (0, 255, 0):
                eval(a).setText(random.choice(['Зелёный', '0, 255, 0']))
            elif g == (0, 0, 255):
                eval(a).setText(random.choice(['Синий', '0, 0, 255']))
            elif g == (255, 0, 255):
                eval(a).setText(random.choice(['Розовый', '255, 0, 255']))
            elif g == (0, 255, 255):
                eval(a).setText(random.choice(['Голубой', '0 255 255']))
            elif g == (255, 255, 255):
                eval(a).setText(random.choice(['Белый', '255 255 255']))
            elif g == (255, 255, 0):
                eval(a).setText(random.choice(['Жёлтый', '255, 255, 0']))

    def TrueButton(self):
        if self.count + 5 <= self.max_timer:
            self.count += 5
            self.timeBar.setValue(int(self.count / (self.max_timer / 100)))
            self.timeText.setText(str(self.count))
        else:
            self.count = self.max_timer
            # print('Больше')
            self.timeBar.setValue(int(self.count / (self.max_timer / 100)))
            self.timeText.setText(str(self.count))
        self.lvl_text.setText(str(self.lvl))
        self.new_lvl()

    def new_lvl(self):
        self.lvl += 1
        self.setButtonColor()
        ok = True
        for y in range(4):
            for x in range(5):
                try:
                    # eval('self.gameButton_{}'.format(str(x) + str(y))).setText(str(x) + str(y))

                    while ok:
                        self.rx, self.ry = random.choice(range(0, 4)), random.choice(range(0, 5))
                        if self.tab[self.ry][self.rx] != self.lvl:
                            # print(f'x={self.rx}, y={self.ry}')
                            self.tab[self.ry][self.rx] = self.lvl
                            ok = False
                    eval('self.gameButton_{}'.format(str(x) + str(y))).move(30 + self.rx * 100, 60 + self.ry * 100)
                    ok = True
                # Для True_Button
                except Exception:
                    while ok:
                        self.rx, self.ry = random.choice(range(0, 4)), random.choice(range(0, 5))
                        if self.tab[self.ry][self.rx] != self.lvl:
                            self.tab[self.ry][self.rx] = self.lvl
                            ok = False
                    self.gameButton_True.move(30 + self.rx * 100, 60 + self.ry * 100)
                    self.color_True = (random.choice([255, 0]), random.choice([255, 0]), random.choice([255, 0]))
                    self.gameButton_True.setText(f'{self.color_True}')
                    if self.color_True == (0, 0, 0) or self.color_True == (0, 0, 255):
                        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}; color: white;')
                    else:
                        self.gameButton_True.setStyleSheet(f'background-color: rgb{self.color_True}; color: black;')
                    self.rgbInText(self.color_True, 'self.gameButton_True')

    def FalseButton(self):
        if self.count - 5 > 0:
            self.count -= 5
            self.timeBar.setValue(int(self.count / (self.max_timer / 100)))
            self.timeText.setText(str(self.count))
        else:
            self.endGame()
            self.timeBar.setValue(0)
            self.timeText.setText(str(0))

    def endGame(self):
        self.hide_buttons_and_connect()
        self.Gameover_text.show()
        self.timer.stop()
        a_text = None
        a_rgb = None
        a_smesh = None
        con = sqlite3.connect('BD.sqlite')
        cur = con.cursor()
        name = self.user
        score = self.lvl - 1

        # играл ли вообще:
        # играл ли в текст
        if self.rezim == 'txt':
            result_text = cur.execute(f"""SELECT result FROM players_text WHERE player = '{name}' """)
            for res in result_text:
                for prov in res:
                    self.prov = prov
                a_text = True
        # играл ли в RGB
        if self.rezim == 'rgb':
            result_rgb = cur.execute(f"""SELECT result FROM players_rgb WHERE player = '{name}' """)
            for res in result_rgb:
                for prov in res:
                    self.prov = prov
                a_rgb = True
        # играл ли в smesh
        if self.rezim == 'or':
            result_rgb = cur.execute(f"""SELECT result FROM players_smesh WHERE player = '{name}' """)
            for res in result_rgb:
                for prov in res:
                    self.prov = prov
                a_smesh = True

        # Если новый игрок
        # RGB
        if not a_rgb and self.rezim == 'rgb':
            cur.execute(f'''INSERT INTO players_rgb(player, result) VALUES('{name}', 0)''')
            # print('Добавлен игрок')
        # Text
        if not a_text and self.rezim == 'txt':
            cur.execute(f'''INSERT INTO players_text(player, result) VALUES('{name}', 0)''')
            # print('Добавлен игрок')
        # Smesh
        if not a_smesh and self.rezim == 'or':
            cur.execute(f'''INSERT INTO players_smesh(player, result) VALUES('{name}', 0)''')
            # print('Добавлен игрок')

        if self.rezim == 'txt':
            cur.execute(f'''INSERT INTO all_results(player, result_text) VALUES('{name}', {score})''')
            if not a_text:
                cur.execute(f"""UPDATE players_text SET result = {score} WHERE player = '{name}'""")

            if a_text and self.prov < self.lvl:
                cur.execute(f"""UPDATE players_text SET result = {score} WHERE player = '{name}'""")
                # print('Результат обновлён')
        if self.rezim == 'rgb':
            cur.execute(f'''INSERT INTO all_results(player, result_rgb) VALUES('{name}', {score})''')
            if not a_text:
                cur.execute(f"""UPDATE players_rgb SET result = {score} WHERE player = '{name}'""")

            if a_text and self.prov < self.lvl:
                cur.execute(f"""UPDATE players_rgb SET result = {score} WHERE player = '{name}'""")
                # print('Результат обновлён')
        if self.rezim == 'or':
            cur.execute(f'''INSERT INTO all_results(player, result_smesh) VALUES('{name}', {score})''')
            if not a_text:
                cur.execute(f"""UPDATE players_smesh SET result = {score} WHERE player = '{name}'""")

            if a_text and self.prov < self.lvl:
                cur.execute(f"""UPDATE players_smesh SET result = {score} WHERE player = '{name}'""")
                # print('Результат обновлён')
        con.commit()
        con.close()
        self.exitbtn.show()
        self.retrybtn.show()

    def retry(self):
        # self.initUI()
        # self.color_True = (random.choice([255, 0]), 255, random.choice([255, 0]))
        # self.hide_buttons_and_connect()
        # self.setButtonColorBase()
        # self.Gameover_text.hide()
        # self.timeBar.setValue(100)
        # self.count = self.count1
        # self.radioButtonRGB.show()
        # self.radioButtonTxt.show()
        # self.radioButtonOr.show()
        # self.StartBtn.show()
        # self.exitbtn.hide()
        # self.retrybtn.hide()
        pass


class Liders(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('Liders.ui', self)
        con = sqlite3.connect('BD.sqlite')
        cur = con.cursor()
        self.comboBox2.addItems(['Текст', 'RGB', 'Смешанный'])

        list_pl = []
        result_text = cur.execute("""SELECT player FROM players_text""")
        for i in result_text:
            # print(i)
            if i not in list_pl:
                list_pl.append(i)
                self.comboBox.addItems(i)

        result_rgb = cur.execute("""SELECT player FROM players_rgb""")
        for j in result_rgb:
            # print(j)
            if j not in list_pl:
                list_pl.append(j)
                self.comboBox.addItems(j)

        result_smesh = cur.execute("""SELECT player FROM players_smesh""")
        for u in result_smesh:
            # print(u)
            if u not in list_pl:
                list_pl.append(u)
                self.comboBox.addItems(u)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('BD2.sqlite')
        db.open()
        self.model = QSqlTableModel(self, db)
        self.model1 = QSqlTableModel(self, db)
        self.Show.clicked.connect(self.show_pl)
        self.Show_2.clicked.connect(self.obn)

    def obn(self):
        con = sqlite3.connect('BD.sqlite')
        cur = con.cursor()
        con2 = sqlite3.connect('BD2.sqlite')
        cur2 = con2.cursor()
        rez = self.comboBox2.currentText()
        if rez == 'Текст':
            cur2.execute('''DELETE from output''')
            a = cur.execute('''SELECT * FROM players_text ORDER BY result DESC''')
            for i in a:
                cur2.execute(f'''INSERT INTO output(player, result) VALUES('{i[0]}', {i[1]})''')
                con2.commit()
            # print(*cur2.execute('''SELECT * FROM output'''))
            self.model.setTable('output')
            self.model.select()
            self.view.setModel(self.model)
            cur2.execute('''DELETE from output''')
            con2.commit()
            con.close()
            con2.close()
        if rez == 'RGB':
            cur2.execute('''DELETE from output''')
            a = cur.execute('''SELECT * FROM players_rgb ORDER BY result DESC''')
            for i in a:
                cur2.execute(f'''INSERT INTO output(player, result) VALUES('{i[0]}', {i[1]})''')
                con2.commit()
            # print(*cur2.execute('''SELECT * FROM output'''))
            self.model.setTable('output')
            self.model.select()
            self.view.setModel(self.model)
            cur2.execute('''DELETE from output''')
            con2.commit()
            con.close()
            con2.close()
        if rez == 'Смешанный':
            cur2.execute('''DELETE from output''')
            a = cur.execute('''SELECT * FROM players_smesh ORDER BY result DESC''')
            for i in a:
                cur2.execute(f'''INSERT INTO output(player, result) VALUES('{i[0]}', {i[1]})''')
                con2.commit()
            # print(*cur2.execute('''SELECT * FROM output'''))
            self.model.setTable('output')
            self.model.select()
            self.view.setModel(self.model)
            cur2.execute('''DELETE from output''')
            con2.commit()
            con.close()
            con2.close()

    def show_pl(self):
        con = sqlite3.connect('BD.sqlite')
        cur = con.cursor()
        con2 = sqlite3.connect('BD2.sqlite')
        cur2 = con2.cursor()
        rez = self.comboBox.currentText()
        cur2.execute('''DELETE from output''')
        a = cur.execute(f'''SELECT * FROM all_results WHERE player = "{rez}"''')
        for i in a:
            cur2.execute(f'''INSERT INTO output2(player, result_text,  result_rgb, \
                    result_smesh) VALUES('{i[0]}', {i[1]}, {i[2]}, {i[3]})''')
            con2.commit()
        # print(*cur2.execute('''SELECT * FROM output'''))
        self.model1.setTable('output2')
        self.model1.select()
        self.one_pl.setModel(self.model1)
        cur2.execute('''DELETE from output2''')
        con2.commit()
        con.close()
        con2.close()


class Skins(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # В разработке
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex0 = Lobby(20, 66)
    ex0.show()
    sys.exit(app.exec())
