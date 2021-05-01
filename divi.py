def func():
    for data in range(1,16):
        if data%3==0 and data%5 == 0:
            print("fizz buzz")
        elif data % 5==0:
            print("buzz")
        elif data % 3==0:
            print("fizz")    
        else:
            print(data)           
func()                       
            
