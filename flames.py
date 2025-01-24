def names(Person_1, Person_2):
    
    first = list(Person_1)
    
    second = list(Person_2)

    for i in Person_1:
        
        if i in second:
                
            first.remove(i)
                
            second.remove(i)      
        

    String = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    remain = len(first) + len(second)

    while len(String) > 1:
        
        index = (remain % len(String)) - 1
        
        String.remove(String[index])
        
        String = String[index + 1:] + String[:index]

    print(String[0])
    

