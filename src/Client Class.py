#file that will contain the class definition for the client
#and any other class definitions that are used within the client
import numpy as np
import string 
import datetime

class Note:
    def __init__(self, The_Note):
        date_object = datetime.datetime.now()
        self.year = date_object.year
        self.month = date_object.month
        self.day = date_object.day
        self.hour = date_object.hour
        self.minute = date_object.minute
        self.contents = The_Note
        self.edited = False
        self.edited_time = date_object
        
    def Edit_Note(self,The_Note): # function used when a note is edited (usually not used)
        self.contents = The_Note
        self.edited = True
        new_date_object = datetime.datetime.now()
        self.edited_time = new_date_object
        
        
class Client:
  
    def __init__(self):
        self.Name = "New Client"
        self.Notes = []
        self.Activities = []

    def set_Name(self, Name):self.Name = Name
    def Give_Name(self):print(self.Name)
    def set_Company_Name(self,Company_Name):self.Company_Name = Company_Name
    def set_Phone_Number(self,Phone_Number):self.Phone_Number = Phone_Number
    def set_Extension(self,Extension):self.Extension = Extension
    def set_Email(self,Email):self.Email = Email
    def set_Website(self,Website):self.Website = Website
    def set_Address1(self,Address1):self.Address1 = Address1
    def set_Address2(self,Address2):self.Address2 = Address2
    def set_City(self,City):self.City = City
    def set_County(self,County):self.County = County
    def set_Postcode(self,Postcode):self.Postcode = Postcode    
    def Add_Note(self, The_Note):
        New_Note = Note(The_Note)
        self.Notes.append(New_Note)
    def Remove_Note(self, Number): #revisit, this will remove the entry for the Note (More often this will just be due to 3 years limit)
        del self.Notes[Number]

   
    

    
    
def main():
    The_Client = Client()
    The_Client.Add_Note()

if __name__ == "__main__":
    main()    
    
    
    
        
        
    
        
        