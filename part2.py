dict1={"#":5,
           "O":3,
           "X": 1,
            "!": -1,
             "!!": -3,
       "!!!":-5}




def check_scores(list1):
    total=0
    for i in list1:
        for j in i:
            total+=dict1[j]
    if total<0:
                print(0)
    else:
        print(total)
    
           
    
check_scores([["#", "!"],["!!", "X"]])
check_scores([["!!!","O","!"],["X","#","!!!"],["!!","X","O"]])
