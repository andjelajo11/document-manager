from PySide2 import QtWidgets

class MonotipTab(QtWidgets.QTabWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.delete_tab)

    

    def textEditor(self, textEditor):
        self.addTab(textEditor, "Text Editor")
        self.setCurrentWidget(textEditor)
    
    def vectorImage(self, image):
        self.addTab(image, "Vector")
        self.setCurrentWidget(image)
    
    def rasterImage(self, image):
        self.addTab(image, "Raster")
        self.setCurrentWidget(image)
    
    def videoPlayer(self, video):
        self.addTab(video, "Video Player")
        self.setCurrentWidget(video)
        
    def audioPlayer(self, audio):
        self.addTab(audio, "Audio Player")
        self.setCurrentWidget(audio)
    
    def delete_tab(self,index):
        self.removeTab(index)
        
    
