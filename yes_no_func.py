def yes_or_no(collections: list) -> None:
    seen = []
    for char in collections:
        if char in seen:
            print("Yes")
        else:
            print("No")
            seen.append(char)

yes_or_no([1,2,3,1,2,4,2])



                
    

