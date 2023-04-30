# r=range(beginning,end,step)
# r=range(inclusive,exclusive,common gap)
# other ways to create range
# 1)range(end) beg=0,step=1
# 2)range(beg,end) step=1

# r=range(10,1,-2)
# for i in r:
#     print(i)

a=range(int(input("Enter a number: ")))
for i in a:
    print(i+1,end=" ")