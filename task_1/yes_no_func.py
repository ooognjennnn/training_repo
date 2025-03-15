def yes_or_no(collection: list) -> None:
    seen = set()
    for item in collection:
        if item in seen:
            print("Yes")
        else:
            print("No")
            seen.add(item)


yes_or_no([1, 2, 3, 1, 2, 4, 2])
    

