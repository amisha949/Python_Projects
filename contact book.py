names=[]
numbers=[]
emails=[]
address=[]
n=int(input("how many contacts you want to save??"))
for i in range(n):
    name=input("name=")
    names.append(name)
    num=int(input("contact number="))
    numbers.append(num)
    em=input("email=")
    emails.append(em)
    ad=input("address=")
    address.append(ad)
print("Names\t\t\tContacts\t\t\t  Emails\t\t\t\tAddress")
for j in range(n):
    print(names[j],"\t\t\t",numbers[j],"\t\t\t",emails[j],"\t\t\t",address[j])
while True:
    a=input("Do you want to add any contact yes or no=")
    if(a=="yes"):
        na=input("name=")
        names.append(na)
        nu=int(input("contact number="))
        numbers.append(nu)
        e=input("email=")
        emails.append(e)
        add=input("address=")
        address.append(add)
    else:
        print("No contact added")
        break
b=input("Enter the contact name to be deleted=")
if b in names:
    inde=names.index(b)
    names.remove(names[inde])
    numbers.remove(numbers[inde])
    emails.remove(emails[inde])
    address.remove(address[inde])
    print("Element deleted")
else:
    print("Element not found")
s=input("Enter the name to be searched for=")
if s in names:
    ind=names.index(s)
    print(f"Name:{names[ind]}\t\tContact:{numbers[ind]}\t\tEmail:{emails[ind]}\t\tAddress:{address[ind]}")
else:
    print("Element not found")
print("Contact Book after updation:-")
print("Names\t\tContacts\t\t\tEmails\t\t\tAddress")
for k in range(len(names)):
    print(names[k],"\t\t",numbers[k],"\t\t",emails[k],"\t\t",address[k])
    

        
    