Password = input("Please set your password now: ")
tries = 0




while tries < 3:
  
    entry = input("Please confirm your new password: ")
  
    tries += 1
  if entry == Password:
    
    print ("Your password has been saved!")

    print("You can navigate away now")

    
    break

  elif  entry != Password and tries < 3:

    print("Sorry the passwords do not match, try again!")
    
    
  
  else:
    print ("You're locked out, call Mateusz")