from plugins.video_plugin.videoPlayer import VideoPlayer
from plugin_framework.extension import Extension
import json





class Plugin(Extension):
    def __init__(self, specification, iface):
        """
        :param iface: main_window aplikacije
        """
        super().__init__(specification, iface)
        


    # FIXME: implementacija apstraktnih metoda
    def activate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)

        plugins["video_plugin"] = True
        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)   
        self.activated = True
        print("Activated")

    def deactivate(self):
        with open("plugin_framework/plugins.json", "r") as json_file:
            plugins = json.load(json_file)
        
        plugins["video_plugin"] = False

        with open("plugin_framework/plugins.json", "w") as json_file:
            json.dump(plugins, json_file)
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        print(type(self.monotipTab))
        tab_name = "Video Player"
        tabs_with_same_name = []
        for i in range(self.monotipTab.count()):
            if self.monotipTab.tabText(i) == tab_name:
                tabs_with_same_name.append(i)
        for i in reversed(tabs_with_same_name):
            self.monotipTab.removeTab(i)
    
    def slotSelected(self, path):
        print("video slot selected")
        # with open("plugin_framework/plugins.json", "r") as json_file:
        #     plugins = json.load(json_file)
        
        # activated = plugins["video_plugin"]
        # if activated == True:
        self.videoPlayer = VideoPlayer(path)
        self.monotipTab = self.iface.layout.itemAt(0).widget().layout().itemAt(1).widget() 
        self.monotipTab.videoPlayer(self.videoPlayer)
