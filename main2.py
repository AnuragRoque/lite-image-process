import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

import subprocess
import os
import cmd
import time


class WelcomeHome(QDialog):
    def __init__(self):
        super(WelcomeHome, self).__init__()
        loadUi("ui\welcome.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.start.clicked.connect(self.WelcomeScreen)
        
    
    def WelcomeScreen(self):
        welcomess=WelcomeScreen()
        widget.addWidget(welcomess)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("ui\mainhome.ui",self)
        self.pushButton_3.clicked.connect(self.gotoimgsketch)
        self.handwritingbtn.clicked.connect(self.gototexthandwriting)
        self.pushButton_2.clicked.connect(self.gotoimgtext)
        self.pushButton_4.clicked.connect(self.gotohandgesture)
        self.pushButton_6.clicked.connect(self.gotoerror)
        self.pushButton_7.clicked.connect(self.gotoqrreader)
        # self.exit.clicked.connect(lambda: os.system(cmd))
        self.exit.clicked.connect(self.close)
        
        self.__subclasshook__
        self.__init__() 

        
        
        self.home.clicked.connect(self.__init__)
  
        #self.exitbtn.clicked.connect(self.close)
  
    
    def gotoimgsketch(self):
        imgsketch=imgsketchscreen()
        widget.addWidget(imgsketch)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.show()


    def gototexthandwriting(self):
        texthandwriting=handwritingscreen()
        widget.addWidget(texthandwriting)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoimgtext(self):
        imgtxt=imgtxtscreen()
        widget.addWidget(imgtxt)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotohandgesture(self):
        # command="python handgesture.py"
        # subprocess.Popen(command)
        print(None)
    
    def gotoqrreader(self):
        # command="python QR-Code-master/custom_qr.py"
        # subprocess.Popen(command)
        print(None)


    def gotoerror(self):
        # msg = QMessageBox()
        # msg.setWindowTitle("ERROR")
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("Unable to fetch Libraries")
        # x = msg.exec_()
        print(None)




class imgtxtscreen(QDialog):
    def __init__(self):
        super(imgtxtscreen, self).__init__()
        loadUi("ui\img-txt.ui",self)
        self.home.clicked.connect(self.gotohome)
        self.pushButton_10.clicked.connect(self.getImage)
        self.exit.clicked.connect(self.close())

    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','', "Image files (*.jpg *.jpeg *.png)")
        global imagepath
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        self.label_4.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())



class imgsketchscreen(QDialog):
    def __init__(self):
        super(imgsketchscreen, self).__init__()
        loadUi("ui\img-sketch.ui",self)
        self.home.clicked.connect(self.gotohome)
        self.pushButton_11.clicked.connect(self.haha)
        self.pushButton_10.clicked.connect(self.getImage)
        self.exit.clicked.connect(lambda: os.system(cmd))

        # file = open('geek.txt','w')
        # file.write(" ", sketchpath)
        # print('sketchpath')
        #self.exit.clicked.connect(self.close)
    

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','', "Image files (*.jpg *.jpeg *.png)")
        global imagepath
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        self.label_4.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())
    
    def haha(self):
        #os.system("sketch.py 1")
                        
       # os.system("sketch.py 1")
       
        # image = cv2.imread(imagepath)
        # height, width, channels = image.shape
        # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # invert=cv2.bitwise_not(gray_image)
        # blur=cv2.GaussianBlur(invert, (21, 21), 0)
        # invertedblur = cv2.bitwise_not(blur)

        # pencil_sketch = cv2.divide(gray_image, invertedblur,scale=225.0)
        # #output_size = (height,widget)
        # resized_image = cv2.resize(pencil_sketch,(1080,720))
        # resized_image2 = cv2.resize(image,(1080,720))
        # cv2.imwrite("output.png",resized_image)
        # cv2.imshow("original image", resized_image2)
        # #cv2.waitKey()
        # cv2.imshow("pencil sketch", resized_image)
        # cv2.waitKey()
        print(None)
        

    def save_text(self):
        text, ok = self.le.text()   
        filename=self.textEdit.toPlainText(self, 'Save File', '.')
       # filename = QtWidget.QFileDialog.getSaveFileName(self, 'Save File', '.')
        fname = open(filename, 'w')
        fname.write(self.le.setText(str(text)))
        fname.close()
    
    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class handwritingscreen(QDialog):
    def __init__(self):
        super(handwritingscreen, self).__init__()
        loadUi("ui\\text-handwriting.ui",self)
        self.home.clicked.connect(self.gotohome)
        # self.convert.clicked.connect(self.goconvert)
        self.exit.clicked.connect(self.close())

        
    def goconvert(self):
        mytext = self.textEdit_2.toPlainText()
        with open('textinput.txt', 'w') as filef:
            filef.write(str(mytext))
        

        #os.system("\text-to-handwritten\txttohandwriting.py 1")
        # command="txttohandwriting.py"
        # subprocess.Popen(command)
        # os.system('python txttohandwriting.py')
        # os.system('image_handwritten.pdf')
    
    def gotohome(self):
        welcomescreen=WelcomeScreen()
        widget.addWidget(welcomescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        




def pushButton_3_clicked():
    print("Opening Image to Sketch")
    # command="python sketch.py"
    # subprocess.Popen(command)

#self.pushButton_3.clicked.connect(pushButton_3_clicked)


#main
app = QApplication(sys.argv)
welcome = WelcomeHome()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1080)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")





