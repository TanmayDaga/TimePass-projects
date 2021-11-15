import os
import sys
import json
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow
from GUI import Ui_MainWindow
from content_box import content_box

from newsapi import NewsApiClient

class config(Ui_MainWindow):

    def __init__(self,MainWindow):
        super().__init__(MainWindow)
        if self.check_api_key():
            with open('data/data.json','r') as f:
                dicti = json.load(f)
                self.API_KEY = dicti['API_KEY']
            self.newsapi = NewsApiClient(api_key = self.API_KEY)
            self.list_contents =[]      
            self.      
            self.add_option()
            self.add_details()
            self.add_action() 
            self.action()
            
    
    
    def check_api_key(self):

        with open('data/data.json','r') as f:
            dicti = json.load(f)

        if  dicti['API_KEY'] == None:
            text,ok = QInputDialog.getText(self,'Api key','Please enter your api key.\nTo get your api key <a href = https://newsapi.org>Click Here</a>')

            if ok:
                os.remove('data/data.json')
                with open('data/data.json','w') as l:
                    
                    dicti['API_KEY'] = text
                    json.dump(dicti,l,indent = 4)
                    return True

            else :
                return False

        return True

    def add_option(self):

        self.Option.addItem("Top Headlines")
        self.Option.addItem("Everything")
        self.Option.activated[str].connect(self.changeStackWid)

        self.Option_2.addItem("Everything")
        self.Option_2.addItem("Top Headlines")     
        self.Option_2.activated[str].connect(self.changeStackWid)


    def add_details(self):

        with open('data/data.json') as f:
            dicti = json.load(f)
            
        #   Page 1

            #Adding Category
            for i in dicti['top_headline_category']:
                self.Cat.addItem(i)

            #Adding Country
            for i in dicti['top_headline_country'].keys():
                self.count.addItem(i)

        #   Page 2

            #Adding Language
            for i in dicti['everything_language'].keys():
                self.Language.addItem(i)

            #Adding sortBy
            for i in dicti['everything_sortBy'].keys():
                self.Sort_by.addItem(i)

    def add_action(self):
        
        self.count.activated[str].connect(self.action)
        self.Cat.activated[str].connect(self.action)
        self.Language.activated[str].connect(self.action)
        self.Sort_by.activated[str].connect(self.action)
        
    def eventFilter(self,obj,event):
        if event.type() == QtCore.QEvent.KeyPress and (obj is self.q_2 or obj is self.q_3):
            if event.key() == QtCore.Qt.Key_Return:
                self.action()  

    def changeStackWid(self,text):
        
        if text == "Everything":
            self.stackedWidget_2.setCurrentIndex(1)
            self.action()
        else: 
            self.stackedWidget_2.setCurrentIndex(0)
            self.action()

    def action(self):

        if self.Option.currentText() == "Top Headlines":

            q = self.q_2.displayText()
            category = self.Cat.currentText()

            with open('data/data.json') as f:
                dicti = json.load(f) 
                Country = dicti['top_headline_country'][self.count.currentText()]
            self.top_headline_add(q,category,Country)

        else : 
            q = self.q_3.displayText()
            with open('data/data.json') as f:
                dicti = json.load(f)
                Language = dicti['everything_language'][self.Language.currentText()]
                sortby = dicti['everything_sortBy'][self.Sort_by.currentText()]
            self.everything_add(q,Language,sortby) 

    def top_headline_add(self,q, category,country):

        response = self.newsapi.get_top_headlines(q=q,category=category,country=country)
        self.del_content_boxes()
        m=0
        
        for i in response['articles']:
            if m==3:
                break
            self.add_content_boxes(i['url'],i['urlToImage'],i['title'],i['description'])       
            m+=1
    
    def everything_add(self,q,lang,sorty):
        response = self.newsapi.get_everything(q=q,language=lang,sort_by=sorty)
        self.del_content_boxes()
        m=0
        for i in response['articles']:
            if m==3:
                break
            self.add_content_boxes(i['url'],i['urlToImage'],i['title'],i['description'])
            m+=1

    def add_content_boxes(self,url,urltoimg,title,description):

        obj = content_box(title,url,description,urltoimg)
        
        self.list_contents.append(obj)
        self.verticalLayout.addWidget(obj)
    
    def del_content_boxes(self):
        
        if len(self.list_contents) > 0:
            for items in self.list_contents:
        #         self.verticalLayout.removeWidget(items) 
        # self.verticalLayout.update()
                    items.hide()
            import trial
            trial.main()
def main():
    app = QApplication(sys.argv)
    UI = QMainWindow()
    UI.show()
    ex = config(UI)
    # ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
