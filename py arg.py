def myFun(*argv):
    for argv in argv:        
        if type(argv)==int: 
            print ('int argument :', argv)
        elif type(argv)==str:
            print ('str argument :', argv)
        elif type(argv)==float:
            print ('float argument :', argv)
        else:
            print ('Dont know :', argv)            
