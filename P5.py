sentence ="this was the of our biggest our some of the our this"
list_of_words =sentence.split(' ')
print("The initial list is:")
print(f"{list_of_words}")
distinctList=list(set(list_of_words))
for i in distinctList: 
    counter=0
    for j in list_of_words:
        if i == j: counter+=1
    print(f"{i} has occcured {counter} times")

