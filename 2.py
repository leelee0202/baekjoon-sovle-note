T = int(input())

for B in range(T):
    num_cnt, string = input().split()
    text = ''
    for s in string:
        text += int(num_cnt) * s
    print(text)
 
 

   
    