def Zapisately(i):
    SloBukv = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
        'q','w','e','r','t','y','u','i','o','p','a','s','d',
                      'f','g','h','j','k','l','z','x','c','v','b','n','m',
                  '0','1','2','3','4','5','6','7','8','9','0']
    reg= len(SloBukv)
    regi = [0,0,0,0,0,0,0,0]
    if i <0 :
        return "NO"
    if i < reg:
        regi[0]=i
    if i == reg:
        regi[1]=1
    if i > reg:
        buf=[]
        lolo=reg*2
        nextint=i
        while True:
            lolo = int(nextint/reg)
            buf.append(nextint%reg)
            nextint = lolo
            if nextint<reg:
                buf.append(nextint)
                break
            if len(buf)>8:
                return "vse"
                break
        index=0
        while True:
            if len(buf)>index:
                regi[index] = buf[index]
            else:
                break
            index+=1
    
    strochka = SloBukv[regi[7]]+SloBukv[regi[6]]+SloBukv[regi[5]]+SloBukv[regi[4]]+SloBukv[regi[3]]+SloBukv[regi[2]]+SloBukv[regi[1]]+SloBukv[regi[0]]
    return strochka


