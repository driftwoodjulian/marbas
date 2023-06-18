def dataListing(client):#>>>>>>>>>>>>>> this uses a variable "client" created using dao method that is then passed down afte it was used un the main file but we import the parameter(result) and re do the file here for simplicity
      #client variable came from main this being secondary
      print("........................................................................................")
      print("........................................................................................")
      print("........................................................................................")
      print("Clients are as follows: ")
      #counter= 1
      for custumer in client:
            #here we must understand how to interpret info coming from database as is the variable "client"
            # in reality a database basicaly stores variables withing an array that is itself stored in an array if
            #  you which to simplify it like that, I wouldnt be surprised if I was talking out of my ass but for now it works
            data = "{0}   ====  idCode: {1} ==== name: {2} ==== company networth: {3}"
            print(data.format(custumer[0], custumer[1], custumer[2], custumer[3]))
            #what the format method does is asign a value which is fond in the array "client" 
            #counterInc= counter + 1
            print(" ")
      print("........................................................................................")
      print("........................................................................................")
      print("........................................................................................")
# so this will be called upon everytime you use dataListing >>>>>> main.py



def dataInput():
      validCode= False
      while(not validCode):
            row =input("declara a row number: ")
            if len(row)>0 and len(row)<3 and row.isnumeric():
                  validCode = True
            elif row>25 or row<1:
                  print("Minimally give me a row number within 25")
            else:
                  print("thats not a number")
            
      validCode= False
      while(not validCode):
            id= input("declare an id number: ")
            if len(id)>0 and len(id)<4 and id.isnumeric():
                  id= int(id)
                  validCode = True
            else:
                  print("You aint breaking this data base")
      
      name= input("declara a name: ")
      
      validCode= False
      while(not validCode):
            worth= input("declare a years networth: ")
            if len(worth)>0 and len(worth)<16 and worth.isnumeric():
                  worth= int(worth)
                  validCode = True
            else:
                  print("You aint breaking this data base")
      
      theClient= (row, id, name, worth)
      
      return theClient

def dataForDeletion(potentialDeletion): #carefull with that parameter
      #this function's job is to varify if the client number exists
      dataListing(potentialDeletion)
      #this is only to show you th potencial deletions
      print()
      thereIsAnId=False
      eliminationId= int(input("Give us the account ID of the accuat you want to delete: "))
      
      for unlucky in potentialDeletion:
            # we going to check data in the arrays positions
            if unlucky[1] == eliminationId:
                  
                  print("the client has a match")
                  #I could have a break but I coul have the program check if there ar more clients in that account
                  thereIsAnId=True
                  break
      if (not thereIsAnId):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            eliminationId= ""
            

      return eliminationId
      #this will return a value or a blank
     
      
      
def infoForChange(thingsToChange):
      dataListing(thingsToChange)
      
      thereIsAnId=False
      changeId= int(input("Give us the account ID of the accuat you want to delete: "))
      
      for unfortunate in thingsToChange:
            if unfortunate[1] == changeId:
                  thereIsAnId= True
                  break
      
      if thereIsAnId:
            changeName= input("Give us the name of a client")

            hasWorth= False
            while (not hasWorth):
                  worth= input("Give us the worth of this client")
                  
                  if worth.isnumeric():
                        if (int(worth))> 0:
                              hasWorth= True
                              worth= int(worth)
                        else:
                              print("The worth of the client must be bigger than 0")
                  
                  else:
                        print("Thats not a number")
            
            thingsToChange= (changeId, changeId, worth)
            
      else:
            thingsToChange= None
      
      return thingsToChange
            