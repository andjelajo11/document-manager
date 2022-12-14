from abc import ABC, abstractmethod
 

class InterfejsDokument(ABC):
    
    @abstractmethod
    def get_document(self): 
        pass
        
    @abstractmethod
    def updateWorkpsace(self): 
        pass
        
    @abstractmethod
    def group_documents(self): 
        pass
    
    @abstractmethod
    def open_document(self): 
        pass

