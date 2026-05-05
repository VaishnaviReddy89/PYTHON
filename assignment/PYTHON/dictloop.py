print("Loop")
servey={
    "Father":"A.RajiReddy",
    "Mother":"A.Madhavi",
    "Brother":"A.Rushi Kesh Reddy",
    "Sister":"A.Vaishnavi Reddy"
}
for s in servey:
    print(s)
    print("Print all values in the dictionary, one by one:")
    print(servey[s])
    print("*****VALUES*******")
    for s in servey.values():
        
        print(s)
        print("*******ITEMS*********")
        for s,y in servey.items():
            print(s,y)
