import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import numpy as np
import cv2

#classes
from app import AppDemo



if __name__ == '__main__':
    # main()
    app = QApplication(sys.argv)
    demo = AppDemo()

    demo.show()
    sys.exit(app.exec_())