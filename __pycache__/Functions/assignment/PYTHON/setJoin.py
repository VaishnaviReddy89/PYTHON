print("JOIN SETs")
companies={"amazon","flipkart"}
companies2={"accenture","infosys"}
companies1={"snapchat","capgemini"}
companies.update(companies2)
print(companies)
companies0=companies.union(companies2)
companies0=companies|companies2|companies1
#companies0=companies|companies2
print(companies0)

#join set and tuple
x={1,2,3}
y={"a","b"}
d=x|y
print(d)
