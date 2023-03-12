import csv
import json
import re
import numpy as np

csv_file = 'alunos3.csv'
json_file = 'alunos.json'

data = []


with open(csv_file, 'r') as file:
        i=0
        for line in file :


            dic={}
            ##print(line)
            if i==0:
                caso1 = re.search(r'(\w+),(\w+),(\w+)',line)
                caso2 = re.search(r'(\w+){((\d+)|(\d+,\d+))}(::(\w+))?,,,,,',line)
                numero = caso1.group(1)
                nome = caso1.group(2)
                curso = caso1.group(3)
                i=1   
            else: 
                valores = re.split(',',line.strip())
                dic[numero] = valores[0]
                dic[nome] = valores[1]
                dic[curso] = valores[2]
                array = []
                if (caso2 and (i !=0)):
                    for valor in valores[3:]:     
                        if valor.isdigit() : 
                            array.append(int(valor))
                    if(caso2.group(6)) : 
                        if( caso2.group(6) == "sum"): 
                            dic[caso2.group(1)] = sum(array)  
                        else :
                            arr = np.array(array)
                            dic[caso2.group(6)] = np.mean(arr)        
                    else : dic[caso2.group(1)] = array    

                data.append(dic)        

        print(data)

with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



##(\w+),(\w+ ?\w+),(\w+ ?\w+),