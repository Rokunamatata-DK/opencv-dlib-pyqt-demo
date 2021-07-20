from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, reset
from PyQt5.QtGui import QImage, QPixmap,QPainter,QPen
from PyQt5 import  QtGui
# image UI class
# class ImageLabel(QLabel):
#     def __init__(self):
#         super().__init__()

#         self.setAlignment(Qt.AlignCenter)
#         self.setText('\n\n Drop Image Here \n\n')
#         self.setStyleSheet('''
#             QLabel{
#                 border: 4px dashed #aaa
#             }
#         ''')

#     def setPixmap(self, image):
#         super().setPixmap(image)
    
#     # def paintEvent(self, e):
#     #     super().paintEvent(e)
#     #     qp = QtGui.QPainter(self)
#     #     qp.drawPixmap(0,0,QtGui.QPixmap("assets\hg.png").scaledToHeight(100)) 

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
        self.image = ""

    def setPixmap(self, image):
        self.image = image
         # convert image file into pixmap
        # load origin size photo
        self.pixmap_image = QPixmap(image)
        # create painter instance with pixmap
        # self.painterInstance = QPainter(self.pixmap_image)
        # self.painterInstance.drawPixmap(100,100,QPixmap("assets\hg.png").scaledToHeight(500))
        # self.painterInstance.end()
        # # set pixmap onto the label widget
        # super().setPixmap(self.pixmap_image.scaledToHeight(400))
        super().setPixmap(self.pixmap_image.scaledToHeight(600))

    def showdot(self,faces):
        if self.image != "":
            # convert image file into pixmap
            # load origin size photo
            self.pixmap_image = QPixmap(self.image)

            # create painter instance with pixmap
            self.painterInstance = QPainter(self.pixmap_image)

            # set rectangle color and thickness
            self.penRectangle = QPen(Qt.red)
            self.penRectangle.setWidth(3)

            # draw rectangle on painter
            self.painterInstance.setPen(self.penRectangle)

            for face in faces:
                location =  face.gethat()
                scale = face.getscale()
                size = 20*scale/100
                self.painterInstance.drawRect(location[0],location[1],size,size)
                face_landmarks = face.getlandmarks()
                for n in range(0, 68):
                    x = face_landmarks.part(n).x
                    y = face_landmarks.part(n).y
                    self.painterInstance.drawRect(x,y,size,size)

            self.painterInstance.end()
            # set pixmap onto the label widget
            super().setPixmap(self.pixmap_image.scaledToHeight(600))

    def add(self,faces):
        # add sticker to face
        if self.image != "":
            # convert image file into pixmap
            # load origin size photo
            self.pixmap_image = QPixmap(self.image)
            # create painter instance with pixmap
            self.painterInstance = QPainter(self.pixmap_image)
            # add to each face
            for face in faces:
                location =  face.gethat()
                scale = face.getscale()
                self.painterInstance.drawPixmap(location[0]-1393*scale/100,location[1]-798*scale/100,QPixmap("assets\hg.png").scaledToHeight(3000*scale/100))

            self.painterInstance.end()
            # set pixmap onto the label widget
            super().setPixmap(self.pixmap_image.scaledToHeight(600))
