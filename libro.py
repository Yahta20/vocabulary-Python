import Registrator
def PisaryCisel():
    
    """
    Тема такая
    - создает папку в ней
    12 файлов в каждом из них
    -восьми значный код с латинских букв, и пары символов с верху
    -цифры отдельным файлом, 
    """
    
    cifry = ['0','1','2','3','4','5','6','7','8','9']
    newLine = '\n'
    reg0=reg1=reg2=reg3=reg4=reg5=reg6=reg7=reg8=reg9=cifry[0]
    pisulyka = open('Numbers2.txt',"w")
    
    i=581379
    ostatoc="00000000"
    pisulyka.write("00000000")
    pisulyka.write(newLine)
    while True:
            chislo = str(i)
            subol = len(chislo)
            if subol<8:
                zostatoc = ostatoc[:len(ostatoc)-subol]
                rezostatoc = zostatoc + chislo
            if subol>=8:
                rezostatoc = chislo
            pisulyka.write(rezostatoc)
            pisulyka.write(newLine)
            
            i+=1
             
            if i == 100000000:
                break
    pisulyka.close()
    pass

def PisarySlov():
    
    """
    Тема такая
    - создает папку в ней
    12 файлов в каждом из них
    -восьми значный код с латинских букв, и пары символов с верху
    -цифры отдельным файлом, 
    """
    
    
    newLine = '\n'
    
    pisulyka = open('wordsinumbers.txt',"w")
    
    i=True
    inx=0
    while i:
             
            if Registrator.Zapisately(inx) == "vse":
                break
            pisulyka.write(Registrator.Zapisately(inx))
            pisulyka.write(newLine)
            inx+=1
            

            
    pisulyka.close()

    pass

PisarySlov()
print("vse")
