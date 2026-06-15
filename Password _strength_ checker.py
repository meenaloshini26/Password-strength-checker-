password =input( "Enter password:")
print(password)
score = 0
if len(password) >= 8:
    print("Length is good")
    score =+1
else:
    print("Length is too short")  
    
    
    for ch in password:
        if ch.islower():
            print("Contains lowercase")
            score =+1
            break
    for ch in password:
        if ch.isupper():
           print("Contains uppercase")
           score =+1
           break
    for ch in password:
         if ch.isdigit():
           print("Contains number")
           score =+1
           break
           
           special = "@#$%^&*!"
    for ch in password:
         if ch in special:
           print("Contains special character")
           score =+1
           break
           print("Score =", score)

         if   score <= 2:
          print("Weak Password")
         elif score <= 4:
          print("Medium Password")
         else:
          print("Strong Password")
