import pyodbc

connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\MJ\Download(D)\School\2021 2nd sem\Final\OOP\Database1.accdb;')

ID = 11
Inventors = 'Legaspi, Mart Joven C.'
Invention = 'Lab9'
Date = '5/22/2022'
Description = "First check if your pycharm or python program have the pydobc installed in the Python Interpreter. Once it is installed, you can now use pycharm to connect and edit a MS Access database. Adding data with the use of <object>.execute('INSERT INTO <TableName> (<ColName1>,<ColName2>,...) VALUES (?,?...)', (Parameters)). The use of [] for ColNames in order for spaces to be recognized. And don't forget to add the <object>.commit() in order for the execute to work"

record = connection.cursor()
record.execute('INSERT INTO tblInventor (ID, Inventors, Invention, [Date of Invention], Description) VALUES (?,?,?,?,?)', (ID, Inventors, Invention, Date, Description))
record.commit()
print("Data is added")

