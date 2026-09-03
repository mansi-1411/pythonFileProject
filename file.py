print("student management system")
print("add the data")
print("display the data")
print("search student")
print("count student")
print("exit student")
option=int(input("enter number"))
if option==1:
    with open('info.txt','w')as f:
        roll=input("enter rollnumber:")
        name=input("enter name:")
        course=input("enter course:")
        fees=input("enter fees:")
        f.write('roll + "," + name + ","+ course + "," + fees\n')
        
elif option==2:
    with open('info.txt','r')as f:
        for i in f:
            print(i.strip())
elif option==3:
    name='vinitha'
    with open('info.txt','r')as f:
        n=False
        for i in f:
            if name in i:
                print('student found')
                print('i')
                n=True
        if n==False:
            print('student not found')
elif option==4:
    c=0
    with open('info.txt','r')as f:
        for i in f:
            c=c+1
        print(c)
elif option==5:
    print("thank you for visitinig ")
else :
    print("invalid choice")



