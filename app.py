from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, reset
from PyQt5.QtGui import QImage, QPixmap,QPainter,QPen
# import cv2
# import dlib

from face import Face,findfaces
from ImageLabel import ImageLabel
from mouse import MouseTracker

# app
class AppDemo(QWidget):
    ##########################################################################
    def __init__(self):
        super().__init__()
        # data filed
        self.path=""
        self.faces = []

        self.resize(400, 400)
        self.setAcceptDrops(True)
        mainLayout = QVBoxLayout()
        
        # self.setMouseTracking(True)
        # self.label = QLabel()
        # self.label.resize(150, 30)
        # mainLayout.addWidget(self.label)
        # self.tracker = MouseTracker()  
        # mainLayout.addWidget(self.tracker)


        # add photo UI
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        
        # add btn
        self.btn = QPushButton("process")
        self.btn_dot = QPushButton("show dots")
        # add click event
        self.btn.clicked.connect(self.clickEvent)
        self.btn_dot.clicked.connect(self.showdot)
        mainLayout.addWidget(self.btn)
        mainLayout.addWidget(self.btn_dot)
       

        self.setLayout(mainLayout)


    ##########################################################################
    # def mouseMoveEvent(self, event):
    #     self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))
    # process
    def showdot(self):
        if self.path != "":
            self.btn.setText("processing")
        self.faces = findfaces(self.path)
        # test log 
        for face in self.faces:
            print(face.gethat())
            print(face.getscale())
        self.photoViewer.showdot(self.faces)

    def clickEvent(self):
        if self.path != "":
            self.btn.setText("processing")
            self.faces = findfaces(self.path)
            self.photoViewer.add(self.faces)
      
        
    # getter
    def getphotopath(self):
        return self.path

    def getbtn(self):
        return self.btn
    ##########################################################################
    # drag and drop /  load img
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            print(file_path)
            self.path = file_path
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def set_image(self, file_path):
        # pixmap =  QPixmap(file_path)
        # pixmap = pixmap.scaledToHeight(600)
        self.photoViewer.setPixmap(file_path)
    ##########################################################################
        