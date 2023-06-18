from BD.conn import DAO
import secondary_func
#This is the main file responsible for luchin the app itself, thid contains the view part of the mvc model
# In this file I didnt leave much comments cuz literally is just basic run of the mil coding
def mainInterface():
      continuation= True
      #boolean values in this fucking language are case sensative be careful
      #  while this is true the mainInterface will show up
      while (continuation):
            #here we just state that while continue = true we will go on to the other while loop aka the rest of the code
            continueIsTrue = False
            # this needs to change to true in order to continue with an option smaller than 5
            while (not continueIsTrue):
                  #I did not get this at first but turns out this how you would write the equivalent of 
                  # while (continueIsTrue != true)
                  print("===========Welcome stranger, my name is Hermes choose an action===========")
                  print("")
                  print("////1) List the clients")
                  print("////2) Register or add a client")
                  print("////3) Update Client Info")
                  print("////4) Delete Client")
                  print("////5) Get the hell out of here")
                  print("")
                  print("========Options have been layed before you, choose one=========")
                  print("")

                  option = int(input(">>>>>>>>>>>>Place your option here, that we might proceed: "))

                  if option < 1 or option > 5:
                        print(" ")
                        print("!!!!!!!!!pick a number between 1-5 next time!!!!!!!!!")
                        print(" ")
                  
                  elif option == 5:
                        continuation = False
                        #This false means the mainInterface shots off
                        print(" ")
                        print("<<<<<<You have exited>>>>>>")
                        print(" ")
                        break
                  else:
                        continueIsTrue = True
                        executeOption(option)

#I decided to explain this at once so listen up since it might be hard to explain for some
# This display has 2 main "switches" which are controlled by boolean values, the thing is that one controls weather or not the display shows and the other controls
#  weather or not you can continues operating
#   Display control is the "continuation" variable and the opcion control is the 

def executeOption(option):
      dao = DAO()

      #////////////////data presentation
      if option == 1:
            try:
                  client= dao.listContent()#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< dao.method
                  #we declare this variable so that we can acces an imported method coming from the connection file
                  # remember, the cursor() method is a postgreSQL method that allows yu to execute postgres commands on a database session
                  print(client)
                  if len(client)>0:
                        #REMEMBER!!!!! client is a variable declared in the previous try of the executeOption fucntion, its job is to import the listContent() method from the conn.py file's DAO
                        print("")
                        print("")
                        print("We have found data")#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        print("")
                        print("We will now proceed to proces and present it")
                        print("")
                        print("")
                        #  here we are gonna import a fuction from another file, doing this will make riding this main file easier as it wont be crouded 
                        #   with an excess of functions giving us a more global view of the code and a more targeted aprouch, those fucntions are stored in
                        #    a file called secondary
                        secondary_func.dataListing(client)#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< this dataListing() method is from the secondary_fucn.py
                  else:
                        print("Have not found anything")
            except:
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!    the excuteOption in the main.py file aint working     !!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  
                  
      #/////////////////data input
      elif option ==2:
            ourClient= secondary_func.dataInput()
            try:
                  dao.swearInClient(ourClient)
            except:
                  print("!!!!!!!!!!!!!!!!!!!!!!error at start of data entry!!!!!!!!!!!!!!!!!!!!!!!")
      
      
      #/////////////////update
      elif option ==3:
            try:
                  thingsToChange= dao.listContent() #>>>>>>>>>>>>>>>>>>>>>>>>>>
                  if len(thingsToChange)>0:
                        thingsToChange= None #>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        if thingsToChange: #if its true
                              dao.changeData(thingsToChange)#>>>>>>>>>>>>>>
                        else:
                              print("the object of change was not found")
                  else:
                        print("No data was found")
            except:
                  print("An error has ocurred")
                  
                  
                  
      
      
      
      #//////////////////delete
      elif option ==4:
            try:
                  print("We are working towards eliminating data")
                  potentialDeletion= dao.listContent()
                  #Remember dao.listContent already gives us info on tables rows
                  if len(potentialDeletion) > 0:
                        print(potentialDeletion)
                        #varifies that there is content
                        elimination= secondary_func.dataForDeletion(potentialDeletion)
                        if not(elimination == ""):
                              #here we are saying that if after do the dataDeletion() method the callback is not empty
                              # then we can proceed with eliminating the data
                              dao.deleteClient(elimination)
                        else:
                              print("Client not found")
                  else:
                        print("Data not found")
            except:
                  print("error")
            
            
            
      else:
            print("If thou seeth this you done fucked up somewhere")
      
mainInterface()