print "heloo gremo se FIZZBUZZ"
izbranoSt=int(raw_input("Vnesi stevilo:  "))

for i in range(izbranoSt):
    if  ((i+1) % 15) == 0:
        print "fizzbuzz"
    elif (i+1) % 5 == 0:
            print "buzz"
    elif  (i+1) % 3 == 0:
        print "fizz"
    else:
        print (i+1)


