import re

def troco(euros,centi):
    r = {   "2e" : 0,
            "1e" : 0,
            "50c" : 0,
            "20c" : 0,
            "10c" : 0,
            "5c" : 0,
             }
    
    for moeda in euros:
        r[moeda+"e"] +=1

    for moeda in centi:
        r[moeda+"c"] +=1    
    return r

def main():
    pousar = False
    saldo_e = 0
    saldo_c = 0
    saldo=0
    euros = []
    centi = []
    while not pousar:
        word= input()
        if word == "LEVANTAR":
            moedas = input("maq: Introduza moedas\n")
            euros = re.findall(r'(\d)+e',moedas)
            centi = re.findall(r'(\d+)+c',moedas)
            inteuros = []
            for val in euros:
                inteuros.append(int(val))

            intcenti = []
            for val in centi:
                intcenti.append(int(val))      
        
            for moeda in inteuros:
                if moeda==1 or moeda ==2 : 
                    saldo_e += moeda
                else :
                    print( str(moeda) + "e - moeda inválida")  
                
            for moeda in intcenti:
                if moeda==5 or moeda==10 or moeda==20 or moeda==50: 
                    saldo_c += moeda
                else :
                    print( str(moeda) + "c - moeda inválida") 
            
            print("Saldo = " + str(saldo_e) + "e" + str(saldo_c) + "c")
            saldo = (saldo_e*100)+saldo_c
       
        
        elif word == "POUSAR":
            dic = troco(euros, centi)
            string = "Troco = "
            for campo, contador in dic.items():
                if contador != 0:
                    string += str(contador) +"x"+campo+ " "
            
            string += " Volte Sempre!"
            print(string)
            #print("troco = " + str(euro)+ "e" + str(centimos)+"c" " Volte sempre!"  )
            saldo = 0

        elif word == "ABORTAR":
            saldo = 0
            break 

        elif word  == "NUMERO" :
            tel = input("Tel = ")
            if (len(tel) == 9):
                
                if re.match(r'\b(601|640)',tel) :  print ("Esse número não é permitido neste telefone.")
                if re.match(r'\b2',tel): 
                    if saldo < 25 :  print("Saldo insuficiente")
                    else: saldo = saldo-25
                #if re.match(r'\b800',tel): 
                if re.match(r'\b808',tel): 
                    if saldo < 10 :  print("Saldo insuficiente")
                    else: saldo = saldo-10 
                if re.match(r'\b00',tel): 
                    if saldo < 150 :  print("Saldo insuficiente")
                    else: saldo = saldo-150  
            elif  re.match(r'\b00',tel) :
                if saldo < 150 :  print("Saldo insuficiente")
                else: saldo = saldo-150 
            else :
                print("Numero inválido")
                
  
            euro=saldo//100
            centimos= saldo- (euro*100)       
            print("Saldo = "+ str(euro)+ "e" + str(centimos)+"c")

main()    