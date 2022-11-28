from abc import ABC
import json
from rad_sa_celim_dokumentom.interfejsi.interfejs_dokument import InterfejsDokument


class ExtensionDokument(InterfejsDokument, ABC):

    def __init__(self,  iworkspace):
        self.iworkspace = iworkspace

    
    #metoda za citanje i deserijalizaciju json-a(iz stringa u obj)
    def get_document(naziv_dokumenta):
        with open('workspace.json') as data_file:  
            data = json.load(data_file)
        for i in data:
            for j in data[i]:
                # print(j)
                for z in data[i][j]:
                    # print(z)
                    if z == naziv_dokumenta:
                        return z
    
    
def create_document(workspace, kolekcija, naziv_dokumenta):
        with open('workspace.json') as data_file:  
            data = json.load(data_file)
        for i in data:
            if i == workspace:
                for j in data[i]:
                    if j == kolekcija:
                        for z in data[i][j]:
                            if naziv_dokumenta not in data[i][j]:
                                z == naziv_dokumenta
                                data[i][j].append(z)
                                return data
                            else : print("Naziv dokumenta nije validan")                           
            #         elif j != kolekcija: print("Ne postoji trazena kolekcija za uneti workspaca ")
            # elif i !=  workspace: print("Ne postoji trazeni workspace")

        
        
        

