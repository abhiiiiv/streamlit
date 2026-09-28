# #define a class to perform database opeeations on book table
# #create a class named booklistcreateretrieveupdatedelete and define method
# #list() for readig all records
# #create() for creating a new record
# retrieve(id) for reading a speifc record
#update (id,data) for updating a specific record
#delete(id) for deleting a specific record
# from idlelib import query

import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="Root",host="localhost",database='library_db'
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("succesfully connected")
    def list(self):
        #reading all records from db table
        query="select*from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:

            print("No Records found")
    def create(self,title,author,price,pages,language):

        query="insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted succesfully")
        records = self.cursor.fetchone()
        if records:

            print(records)
        else:

            print("No Records found")


    def retrieve(self,id):
        query="select* from book where id=%s"
        data=(id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchone()
        if records:

            return records
        else:

            print("No Records found")
    def update(self,title, author, price, pages, language,id):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data = (title, author, price, pages, language,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("data inserted succesfully")
    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("data is deleted")
        else:
            print("no records found")

book_instance=BookListCreateRetrieveUpdateDelete()
# book_instance.create("abc","qwe",234,123,"english")
# book_instance.retrieve(1)
# book_instance.delete(2)
# book_instance.update(3,"abc","qwe",234,123,"english")