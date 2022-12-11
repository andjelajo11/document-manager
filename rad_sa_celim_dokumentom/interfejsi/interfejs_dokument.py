from abc import ABC, abstractmethod
 

class InterfejsDokument(ABC):
    # pass
    
    @abstractmethod
    def get_document(self): 
        pass
    
    @abstractmethod
    def create_document(self): 
        pass

    @abstractmethod
    def removeDocument(self): 
        pass
    
    @abstractmethod
    def updateWorkpsace(self): 
        pass
        
    