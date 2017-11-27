old_password = input("Please enter your old password: ")
Password = input("Please set your password now: ")

tries = 0




while tries < 3:
  
    tries += 1
    while Password != old_password:
      new_password = input("Please confirm your new password: ")
      while new_password == Password:
        print ("Your password has been saved!")
      print("Sorry the passwords do not match, try again!")
      new_password = input("Please confirm your new password: ")
      tries +=1
    print("You can't use your old password!")
    Password = input("Please set your password now: ")
    tries += 1
print("You have reached the max attempts.")
