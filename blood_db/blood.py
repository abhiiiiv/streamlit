import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="Root",host="localhost",database='blood_db'
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("succesfully connected")
    def get(self):
        #reading all records from db table
        query="select*from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:

            print("No Records found")
    def post(self,name,blood_group,phone,city,last_donation):

        query="insert into donor(name,blood_group,phone,city,last_donation)values(%s,%s,%s,%s,%s)"
        data=(name,blood_group,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted succesfully")
        records = self.cursor.fetchone()
        if records:

            print(records)
        else:

            print("No Records found")


    def getid(self,id):
        query="select* from donor where id=%s"
        data=(id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchone()
        if records:

            return records
        else:

            print("No Records found")
    def put(self,id,name,blood_group,phone,city,last_donation):
        query="update book set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data = (name,blood_group,phone,city,last_donation,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("data inserted succesfully")
    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("data is deleted")
        else:
            print("no records found")