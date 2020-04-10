def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 4) 
    print(result)
    
yell("You can do it")
yell("Ask for help")

#praise = "You're doing great!"
#praise = praise.upper()
#number_of_characters = len(praise)
#result = praise + "!" * number_of_characters 
#print(result)

def db(word):
    blanks = "-" * len(word)
    print(blanks)
    
print("Puzz 1:")
db("treehouse")
print("Puzz2:")
db("python")