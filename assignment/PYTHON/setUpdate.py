IPLteams={"SRH","RCB","RR","PBKS","CSK","MI","DC"}
#To add items from another set into the current set, use the update() method.
ipl2={"KKR","LSG","GT"}
IPLteams.update(ipl2)
print(IPLteams)
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)