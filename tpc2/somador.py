

def somador():
    texto =  input()
    digito = "0"
    soma = 0
    contador = True
    string= ""
    for dig in texto :
        if ((not(dig.isdigit()))) :  
            soma += int(digito)
            digito = "0"

            if(dig =="="): print (soma)
            else: 
                string = string + dig
                #print(string.lower())
                if ("off" in string.lower()): 
                    contador = False
                    string= "" 
                elif ("on" in string.lower()): 
                    contador = True
                    string= "" 
                #print(contador)
        elif (dig.isdigit() and contador): 
            digito= digito+dig  
            string= ""      
        else : string = ""     

somador() 

