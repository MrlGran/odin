from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, wrong1, wrong2, wrong3, right_answer):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

v_line = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
h_line5 = QHBoxLayout()

winner1 = QLabel('Какой национальности не существует?')
h_line1.addWidget(winner1)
v_line.addWidget(
    winner1, alignment = Qt.AlignCenter
)

RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox2 = QGroupBox('Результат теста')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
rbtn_5 = QLabel('Правильно/Неправильно')
rbtn_6 = QLabel('Правильный ответ')
h_line2.addWidget(RadioGroupBox)
h_line2.addWidget(RadioGroupBox2)
RadioGroupBox2.hide()
v_line.addWidget(
    RadioGroupBox, alignment = Qt.AlignCenter
)
v_line.addWidget(
    RadioGroupBox2, alignment = Qt.AlignCenter
)
h_line4.addWidget(rbtn_1)
h_line4.addWidget(rbtn_3)
h_line5.addWidget(rbtn_2)
h_line5.addWidget(rbtn_4)
v_line2.addLayout(h_line4)
v_line2.addLayout(h_line5)
v_line3.addWidget(rbtn_5)

v_line3.addWidget(
    rbtn_6, alignment = Qt.AlignCenter
)
RadioGroupBox.setLayout(v_line2)
RadioGroupBox2.setLayout(v_line3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

winner3 = QPushButton('Ответить')
v_line.addWidget(
    winner3, alignment = Qt.AlignCenter
)
h_line3.addStretch(1)
h_line3.addWidget(winner3, stretch=2)
h_line3.addStretch(1)

def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    winner3.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    winner3.setText('Следуйщий вопрос')                

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    winner1.setText(q.question)
    rbtn_6.setText(q.right_answer)
    show_question()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика')
        print('Всего вопросов -', main_win.total)
        print('Правильных ответов -', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')
    else:
        show_correct('Неверно!')
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')

def show_correct(res):
    rbtn_5.setText(res)
    show_result()

question_list = []
question_list.append(
    Question('Валентность кислорода', 'три', 'четыре', 'один', 'два')
)
question_list.append(
    Question('Какого хим. элемента не существоет', 'Натрий', 'Германий','Мышьяк', 'Кварц')
)
question_list.append(
    Question('Формула дискременанта(D)', 'a2 - 2b + c2', 'Формулы нет', '(-b +- квадратный корень из D)/(2a)', 'b2 - 4ac')
)
question_list.append(
    Question('Сокращение a2 - b2', 'a2-2ab+b2', '(a+b)(a2-ab+b2)', '(a-b)(a2+ab+b2)', '(a-b)(a+b)')
)
question_list.append(
    Question('Сколько длилась столетняя война', '100', '99', '103', '107')
)
question_list.append(
    Question('В каком месяце разливается Нил', 'март', 'январь', 'октябрь', 'июль')
)

def next_qyection():
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    print('Статистика')
    print('Всего вопросов -', main_win.total)
    print('Правильных ответов -', main_win.score)
    ask(q)

def click_OK():
    if winner3.text() == 'Следуйщий вопрос':
        next_qyection()
    else:
        check_answer()
winner3.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0

next_qyection()

main_win.setLayout(v_line)
app.exec_()

 