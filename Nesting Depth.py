t=int(input())
for k in range(t):
    numbers=list(input())
    rem=0
    output=''
    for n in numbers:
        no=int(n)
        if(no==rem):
            a=n
        elif(no>rem):
            a='('*(no-rem) + n    
        else:
            a=')'*(rem-no)+n
        rem=no
        output=output+a
    output=output+")"*rem
    print(output)
