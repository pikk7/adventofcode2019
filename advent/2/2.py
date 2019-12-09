#IntCode computer 

fo = open("input.txt","r")

line=fo.readline()
int_list = [int(i) for i in line.split(",")]

int_list[1]=12
int_list[2]=2

def adding(x,y,place):
    int_list[place]=x+y

def multiplying(x,y,place):
    int_list[place]=x*y

i=0
a=0
while(len(int_list)>=i):
    a=int_list[i]
    if(a==99):
        break
    if(a==1):
        adding(int_list[int_list[i+1]],int_list[int_list[i+2]],int_list[i+3])
        i=i+4
        #instruction pointer itt 4gyel kell mozogjon
    elif(a==2):
        multiplying(int_list[int_list[i+1]],int_list[int_list[i+2]],int_list[i+3])
        i=i+4
        #instruction pointer itt 4gyel kell mozogjon

    else:
        print(a)#maybe error
        i=i+4

    
print(int_list)