


def new_password():
  

  tries = 0
  
  while tries < 3:
    
    Password = input("Please set your password now: ")
  
    tries += 1
    while Password != old_password:
      new_password = input("Please confirm your new password: ")
      if new_password == Password:
        print ("Your password has been saved!")
        return new_password
      else:
        print("Sorry the passwords do not match, try again!")
        tries +=1
    if Password == old_password:
      print("You can't use your old password!")
      
      tries +=1
  else:
    print("You have reached the max attempts.")
  


yn = input("Do you need to reset your password? ")
if yn == "Y" or yn == "y":
  old_password = input("Please enter your old password: ")
  new_password()
  
elif yn == "N" or yn == "n":
  print("Bye!")
else:
  print("You can only input Y/N")
  


      
