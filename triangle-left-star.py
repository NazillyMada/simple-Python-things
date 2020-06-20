x=int(input("insert rows : "))
space= 2*x-2;
for i in range(0,x):
    for j in range (0,space):
        print(end=" ")
    space=space-2;
    for j in range(0, i+1):
        print("*", end=" ");
    print("")