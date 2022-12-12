def ztalloc(shape):
    index = 1

    while True:
        try:
            if shape[-1:] == 'd':
                index =index*2
                if index%2 !=0:
                    return(None)

            elif shape[-1] =='u':
                if (((index-1)//3)!= ((index-1)/3)):
                    return(None)
                index = (index-1)//3

                if (index%2 ==0):
                    return(None)
            shape = shape[:-1]

        except:
            return (index)
