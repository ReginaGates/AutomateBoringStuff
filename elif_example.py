#Elif Example from "Automate the Boring Stuff" with Al Sweigart
name = "Bob"
age = 56
if name == "Alice":
    print("Hi, Alice!")
elif age < 12:
        print("You are not Alice, kiddo!")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print("You are not Alice, Granny!")
    
#This code, above, is broken, at the moment. If I input 99, it doesn't work. I,
# Regina Gates, added the following to fix it.
elif age == 12:
    print("Alice, why are you using an alias?")
else:
    print("Who the heck are you?!")
    
