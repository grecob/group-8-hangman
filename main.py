import Dictionary

#print messeges to help with pre GUI testing    
print("please choose a category")
print("1. Dictionary") #more categories can be added
choice = input()
from Dictionary import Dictionary
dictionary = Dictionary() 
#has to be forced into int or it wont get the correct 
dictionary.choose_category(int(choice)) 
dictionary.read_csv()

    

