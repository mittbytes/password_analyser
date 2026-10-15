print("===============================")
print("        PASSWORD ANALYSER")
print("===============================")


common_password = ["password" , "admin" , "123456" , "letmein" , "qwerty"  ]
while True:
  score = 0
  password = input("enter password(or type quit to exit) :")

  if password.lower() == "quit":
    print("goodbye!!")
    break

  if password == "":
    print("password cannot be empty.")
    continue
  print("=======================")
  print("     PASSWORD ANALYSIS")
  print("=======================")

  print("length : " , len(password), "character")
  print("checks ;")
  if len(password) >= 8:
    print("password has good length")
    score += 1
  else:
    print("password length too short")

  if any(char.isdigit() for char in password):
    print("has a number")
    score += 1
  else:
    print("no number")

  if any(char.isupper()for char in password):
    print("has an uppercase character")
    score += 1
  else:
    print("no uppercase character")

  if any(not char.isalnum() for char in password):
    print("has a special character")
    score += 1
  else:
    print("no special character")

  if any(char.islower() for char in password):
    print("has a lowercase character")
    score += 1
  else:
    print("no lowercase character")
    
  print("score : " , score)

  if score <= 2:
    print("strength : weak")

  elif score <= 4 :
    print("strength : medium")

  else:
    print("stregth : strong")

  print("\nsuggestions")
  suggestions = 0
  if password.lower() in common_password:
    print("warning : this is a commonly used password")
    suggestions += 1
  if len(password) < 8:
    print("- make your password atleast 8 characters long")
    suggestions += 1
  if not any(char.isdigit() for char in password):
    print("- add a number")
    suggestions += 1
  if not any(char.isupper() for char in password):
    print("- add an uppercase character")
    suggestions += 1
  if not any(char.islower() for char in password):
    print("- add a lowerase character")
    suggestions += 1
  if not any(not char.isalnum() for char in password ):
    print("- add a special character")
    suggestions += 1
  if len(set(password)) < 4:
    print("warning : too many repetative characters")
    suggestions += 1
  if " " in password:
    print("warning : password contains space.")
    suggestions += 1

  if suggestions == 0:
    print("NO suggestions!! all basic check passed!")

  print("=========================================")
  print("       PASSWORD ANALYSIS COMPLETE")
  print("=========================================")
