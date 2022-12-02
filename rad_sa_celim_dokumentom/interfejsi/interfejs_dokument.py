from abc import ABC, abstractmethod
 

class InterfejsDokument(ABC):
    # pass
    
    @abstractmethod
    def get_document(self): #gde realizovati implementaciju ove metode u kojoj klasi
        pass
    
    @abstractmethod
    def create_document(self): #gde realizovati implementaciju ove metode u kojoj klasi
        pass

    @abstractmethod
    def removeDocument(self): #gde realizovati implementaciju ove metode u kojoj klasi
        pass
    
    @abstractmethod
    def updateWorkpsace(self): #gde realizovati implementaciju ove metode u kojoj klasi
        pass
        
    