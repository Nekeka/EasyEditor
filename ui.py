from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, 
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

app = QApplication([])
windows = QWidget()
windows.resize(800, 400)

btn_left = QPushButton("вліво")
btn_right= QPushButton()
btn_ok= QPushButton()
btn_change = QPushButton()
btn_do_bw = QPushButton("чорно-білий")

lbl_picture = QLabel("картинка")

hl_buttons = QHBoxLayout()
vl_picture_and_bnts = QVBoxLayout()
# додаємо кнопки у гор макет
hl_buttons.addWidget(btn_do_bw)
hl_buttons.addWidget(btn_right)
hl_buttons.addWidget(btn_ok)
hl_buttons.addWidget(btn_change)

hl_buttons.addWidget(btn_left)


vl_picture_and_bnts.addWidget(lbl_picture)
vl_picture_and_bnts.addLayout(hl_buttons)

windows.setLayout(vl_picture_and_bnts)
windows.show()
app.exec()