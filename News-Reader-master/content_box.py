from PIL import Image
from PyQt5.QtCore import Qt
import requests
import shutil
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

class content_box(QWidget):

    counter = 0

    def __init__(self, title,url, description, urltoimage):
        super().__init__()

        self.setFixedHeight(121)
        self.setFixedWidth(681)
        self.set_pic(self.get_img(urltoimage))
        self.set_title(title,url)
        self.set_des(description)
    
    def get_img(self,urltoimg):
        '''Convert url into image and store it in temp folder'''

        if urltoimg:
            response = requests.get(url = urltoimg, stream = True)
            with open(f"temp/{content_box.counter}.png", 'wb') as out_file:
                shutil.copyfileobj(response.raw,out_file)
            del response
            content_box.counter += 1
            return f"temp/{content_box.counter}"
        else :
            return False

    # def resize_img(self,pathtoimg):
        
    #     img = Image.open(pathtoimg)
    #     new_img = img.resize(())

    def set_pic(self,imgpath):

        lbl = QLabel(self)
        
        lbl.setGeometry(0,0,121,121)
        
        if imgpath:
            lbl.setPixmap(QPixmap(imgpath))
        else:
            lbl.setText('Error')
            lbl.setFont(QFont('Arial',12))
    def set_title(self, title, url):

        lbl = QLabel(f"<a href = {url}> {title} </a>", self)
        lbl.setFont(QFont('Arial',12,QFont.Bold))
        lbl.setGeometry(140,20,621,21)
        lbl.setTextInteractionFlags(Qt.TextBrowserInteraction)
        lbl.setOpenExternalLinks(True)


    def set_des(self,des):

        lbl = QLabel(des,self)
        lbl.setWordWrap(True)
        
        lbl.setGeometry(140,50,621,51)


