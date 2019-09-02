num = 0
def counter():
    global num
    while True:
        num += 1
        yield num
for i in range(13):
    n = next(counter())
    print(n,end =" ")
