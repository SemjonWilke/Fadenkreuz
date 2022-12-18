import sys
import signal
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from keyboard import add_hotkey

signal.signal(signal.SIGINT, signal.SIG_DFL)

print("F10: show/hide Crosshair")
print("Alt+F10: quit")

app = QApplication(sys.argv)

window = QMainWindow()
window.setAttribute(Qt.WA_TranslucentBackground, True)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

pixmap = QPixmap('Fadenkreuz.png')

label = QLabel(window)
label.setPixmap(pixmap)
label.setGeometry(0, 0, pixmap.width(), pixmap.height())

window.label = label
window.resize(pixmap.width(),pixmap.height())

hidden = False
def hide():
    global hidden
    hidden = not hidden
    label.setVisible(not hidden)
add_hotkey('F10', hide)
add_hotkey('alt+F10', app.quit)

window.show()
sys.exit(app.exec_())