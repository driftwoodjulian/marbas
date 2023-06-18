#here we add our server acording to the model-viewer-controller architecture


#we have to import a module first

import mysql.connector #this is like the require-mysql procedure we do on mysqlpython ‐‐version
from mysql.connector import Error #this module import the error form the realm of the mysql.connecto module



class DAO(): #this is us declaring an object which will actualy be our server persay, notice in python we use ":" instead of "{}"

      def __init__(self): 
            #here we made the constructor notice in python when you use def you star a fuction you initalize it with "def" as in define or definition, here "self" is the name of the parameter that will go give atributes their values
            # when you use __init__ it signals persay what is the constructor within, therfore validating the objects atributes
            #  next we are going to use a try and except combo. The method "try" lets you test a block of code for error while "except" lets you handle such error
            try:
                  print("trying server conection")
                  
                  self.conexion = mysql.connector.connect(
                    host = 'ivar3.toservers.com',
                    port = "3306",
                    user = 'jalexzeb_carpediem',
                    password = 'carpediem123123',
                    db= 'jalexzeb_exp',
                  )
                  print("Server conection succesfull")
            except Error as ex:
                        print("1. An error has ocurred while trying to conect to the mysql database in ivar3: {s}".format(ex))
      

      def listContent(self):#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> dao method
      #here we add another fuction which in this case it lets us use as a method for the object
      # notice that we didnt use __init__ since this here is no constructor

            if self.conexion.is_connected():
                  try:
                        cursor = self.conexion.cursor()
                        #the cursor() method is a postgreSQL method that allows yu to execute postgres commands on a database session
                        # in this particular example we made a variable that conects cursor to our database
                        cursor.execute("SELECT * FROM client_inf ORDER BY name ASC")
                        #  we use this to execute the specified postergres commands on our database
                        #   here we use this to execute "SELECT * FROM client ORDER BY name ASC"
                        #    that commands takes all variables from the "client" column and presents them in ascending order
                        results = cursor.fetchall()
                        #     fetchall() method retrives all remaining tuple from a table after the last executed statement from that table 
                        print (results)
                        print ("we have a connection to ivar3")
                        return results
                  except Error as ex:
                        print("2. An error has ocurred while trying to conect to the mysql database in ivar3: {s}".format(ex))
                        #      warning: I seem to have a thing in which when I see "except Error as e" I think of the "e" as an event 
                        #       from javascript so when I found out I could use "ex" as well I started using that one

      def swearInClient(self, ourClient):
            if self.conexion.is_connected:
                  try:
                        print("  ")
                        print("Data Entry in process")
                        print("  ")
                        cursor= self.conexion.cursor()
                        sql = "INSERT INTO client_inf (row, id, name, worth) VALUES ('{0}', '{1}', '{2}', '{3}')"
                        cursor.execute(sql.format(ourClient[0], ourClient[1], ourClient[2], ourClient[3]))
                        self.conexion.commit()
                        print("  ")
                        print("Data Entry Succesful")
                        print("  ")
                  except Error as ex:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("An error has ocurred during data entry, oparation unsucessful: {s}".fomat(ex))
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        
                        
                        
      def deleteClient(self, elimination):
            if self.conexion.is_connected():
                  try:
                        print("Data deletion in progress")
                        cursor= self.conexion.cursor()
                        sql = "DELETE FROM client_inf WHERE id = '{0}'"
                        cursor.execute(sql.format(elimination[0]))
                        print("Data deletion Successful")
                  except Error as ex:
                        print("An error has ocurred during deletion process: \n {s}".format(ex))
                        
      def changeData(self, thingsToChange):
             if self.conexion.is_connected:
                  try:
                        print("  ")
                        print("Data changes in process")
                        print("  ")
                        cursor= self.conexion.cursor()
                        sql = "UPDATE client_if SET row={0}, id = {1}, name = '{2}' , worth = {3} "
                        cursor.execute(sql.format( thingsToChange[1], thingsToChange[2], thingsToChange[3], thingsToChange[0]))
                        self.conexion.commit()
                        print("  ")
                        print("Data update Succesful")
                        print("  ")
                  except Error as ex:
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print("An error has ocurred during data update in data base, oparation unsucessful: {s}".fomat(ex))
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
            
            
            
            
            


















