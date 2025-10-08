def pin():
    print("Welcome to ATM")
    cor_pin=2526
    while True:
      pin=int(input("Enter the pin:"))
      if pin==cor_pin:
        print("valid pin")
        print("choose to deposit or withdraw")
        break
      else:
        print("wrong pin")
        
    
def game():
    pin()
    import random
    a=random.randint(1,5)
    print("*****GUESS VALUE*****")
    atp=[]
    for atp in range(1,4):
     b=int(input("Enter the value:"))
     if b==a:
      print ("value matched")
      break
     elif a>b:
      print("value greater")
     elif a<b:
      print("value lesser")
     else:
      print("*****YOU LOST*****")

game()
