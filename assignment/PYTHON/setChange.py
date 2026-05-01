#Once a set is created, you cannot change its items, but you can add new items.
IPLteams={"SRH","RCB","RR","PBKS","CSK","MI","DC"}
#add() is defined to accept only 1 argument.
IPLteams.add("GT")
print(IPLteams)
IPLteams.update(["KKR","LSG","GT"])
print(IPLteams)