def tracesum(mx,n):
    s=0
    for i in range(n):
        s+=mx[i][i]
    return s
 
def ascending(order_square, top_left_number):
    rows_counter = 0
    ll=[]
    for rows in range(1, order_square + 1):
        latin_number = top_left_number + (rows - 1)
        if latin_number > order_square:
            latin_number = 1 + rows_counter
            rows_counter += 1
        row_counter = 0
        l=[]
        
        for row in range(1, order_square + 1):
            l.append(latin_number)
            latin_number += 1
            if latin_number > order_square:
                latin_number = 1 + row_counter
                row_counter += 1
        ll.append(l)

    return ll

 
def main():
    for _ in range(1,int(input())+1):
        order_square, trace=map(int, input().split())
        flag=False
        for i in range(1,order_square+1):
            x=ascending(order_square,i)
            if tracesum(x,order_square)==trace:
                flag=True
                break
                
        if flag:
            print("Case #",end="")
            print(_,end="")
            print(": POSSIBLE")
            for i in x:
                print(*i,sep=" ")
        else:
            print("Case #",end="")
            print(_,end="")
            print(": IMPOSSIBLE")
            
