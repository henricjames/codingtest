

def print_series(count):
    flag=0;
    num=1
    while(flag!=count):
        if (num%2!=0):
            print(num)
            flag+=1
        num+=1

print_series(5)