import sqlite3      #imports the sqlite3 library so that you can use it
import string
import datetime
db = sqlite3.connect('example.db')     #Connect to the database stored in the file example.sql
                                        #The file will be created if it doesn't already exist
cursor = db.cursor()                    #The cursor will store the results of any query

cursor.execute("DROP TABLE IF EXISTS Companies")          #We can use this to delete a table completely
cursor.execute("DROP TABLE IF EXISTS Notes") 
cursor.execute("DROP TABLE IF EXISTS Activities") 
cursor.execute("CREATE TABLE IF NOT EXISTS Companies(ID INTEGER, CompanyName TEXT, ContactName TEXT, \
               Phone TEXT, Extension TEXT, Address1 TEXT, \
                Address2 TEXT, City TEXT, County TEXT, Postcode Text, Email TEXT, Website TEXT, Other TEXT  )")    #Create a table if it doesn't already exist. The table will contain two fields 'id' and 'name'. The datatypes are INTEGER and TEXT
cursor.execute("CREATE TABLE IF NOT EXISTS Notes(ID INTEGER, CompanyID INTEGER, note TEXT, date DATE, time TIME)")
cursor.execute("CREATE TABLE IF NOT EXISTS Activities(ID INTEGER, CompanyID INTEGER, name TEXT, date DATE, time TIME)")
cursor.execute("CREATE TABLE IF NOT EXISTS Alt_contacts(ID INTEGER, CompanyID INTEGER, name TEXT, age INTEGER)")
def AddCompany(CompanyName, ContactName, Phone, Extension, Email, Website, Address1, Address2, City, County, Postcode):
    cursor.execute("select * from Companies")
    results = cursor.fetchall() # this is used to create the ID number for the contact (this is a slow method - will definitely need revisiting)
    cursor.execute("INSERT INTO Companies(ID, CompanyName, ContactName, Phone, Extension, Email, Website, Address1, Address2, \
                   City, County, Postcode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" , (len(results)+1, CompanyName, ContactName, Phone, Extension, Email, Website, Address1, Address2, City, County, Postcode))

def AddNote(CompanyID, Note):
    date_object = datetime.date.today()
    
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    if len(minute) == 1 :
        minute = "0%s"%(minute)
    time = "%s:%s"%(hour, minute)
    cursor.execute("SELECT * from Notes WHERE CompanyID = %s" %(CompanyID))
    results = cursor.fetchall() # this is used to create the unique ID number for the program (this is a slow method - will definitely need revisiting)
    cursor.execute("INSERT INTO Notes(ID, CompanyID, note, date, time) VALUES (?, ?, ?, ?, ?)" , (len(results)+1, CompanyID, Note, date_object, time))

def AddActivity(CompanyID, date , time, Name):


    cursor.execute("SELECT * from Notes WHERE CompanyID = %s" %(CompanyID))
    results = cursor.fetchall()
    cursor.execute("INSERT INTO Activities(ID, CompanyID, name, date, time) VALUES (?, ?, ?, ?, ?)",(len(results)+1,CompanyID,Name, date, time))
    
    
AddCompany("Sky", "Warren Buffet", "07969421899","" , "hahaemail@email.com", "www.freememes.com", "idk", "baker street", "manny", "Lancashire", "CN1 8PZ")
AddCompany("Virgin", "Richard Branson", "07955123456","" , "richardsemail@email.com", "www.paidmemes.com", "11 nice street", "i mean really nice", "leeds", "Yorkshire", "M20 1BF")
AddCompany("BT", "Bichard Ranson", "07955123456","" , "richardsemail@email.com", "www.paidmemes.com", "11 nice street", "i mean really nice", "leeds", "Yorkshire", "M20 1BF")
db.commit()                                                                         #Commit the changes to the database (this means store them permanently)
AddNote(1,"haha ur mom gay")
AddNote(2,"haha ur dad gay")
AddActivity(1, "2020-10-13","12","meeting regarding toe hair shampoo")
db.commit()     
 
cursor.execute('''SELECT * FROM Companies''')                                        #Search for all students in the database - the * means all fields
for record in cursor:                                                               #For each record print it on the screen. Each record will be stored as a tuple.
    print(record)
cursor.execute('''SELECT * FROM Notes''')                                        #Search for all students in the database - the * means all fields
for record in cursor:                                                               #For each record print it on the screen. Each record will be stored as a tuple.
    print(record)

db.close() 

#Reference: http://www.easypythondocs.com/SQL.html
