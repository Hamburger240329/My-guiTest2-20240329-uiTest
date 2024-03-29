import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # Qt Designer에서 제작한 Ui를 불러오는 클래스

form_class = uic.loadUiType("ui/test.ui")[0]  # Qt Designer에서 만든 ui를 불러옴. 뒤에 인덱스 [0] 반드시 넣어야 함

class MyWindow(QMainWindow, form_class):  # 부모 두명 에게 상속 받음 - 이중상속?
    def __init__(self):
        super().__init__()  # 부모 클래스 생성자 호출
        self.setupUi(self)  # 위에서 불러온 test.ui 를 연결
        self.setWindowTitle("연습 프로그램")
        self.setWindowIcon(QIcon("img/google.png"))

        self.button1.clicked.connect(self.button1_click)
        # 버튼1이 클릭되면 button1_click 메서드 호출
        self.button2.clicked.connect(self.button2_click)
        # 버튼2가 클릭되면 button2_click 메서드 호출
        # self.button3.clicked.connect(self.button3_click)

        self.statusBar().showMessage("mady by gyojincompany 2024-03-29")
        # 아래 상태표시줄에 메시지를 표시하다 - 스테이터스 바 / 쇼 메시지

    def button1_click(self):
        self.label1.setText("HelloWorld!!")
    def button2_click(self):
        self.label1.setText("안녕하세요!!")

    # def button3_click(self):
        # self.label1.setText("버튼 3번입니다!!"))


if __name__ == "__main__":
    app = QApplication(sys.argv)  # app 작명
    myWin= MyWindow()  # myWin 작명
    myWin.show()
    sys.exit(app.exec_())




