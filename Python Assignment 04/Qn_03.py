def long_word(list):
        l2=[]
        for i in list:
           l2.append(len(i))
        return l2

user=int(input("Enter how many words you want to put in list: "))
l1=[]

for i in range(user):
    i=input(f"enter word {i+1} : ")
    l1.append(i)

value=long_word(l1)
print(value)