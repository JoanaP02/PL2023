import csv
import math
import matplotlib.pyplot as plt

import csv

def counting_by_sex():
    m=0   
    f=0
    for row in matrix:
        if ((row[1] == "M") & (row[5]=="1")) : m+=1
        elif ((row[1] == "F") & (row[5]=="1")) : f+=1
    pm = round (m / (f+m) *100 , 2)
    pf = round (f / (f+m) *100 , 2 ) 
    #print (*['\n porcentagem masculino: ', pm, '\n porcentagem feminino: ', pf]) 


    totable= [["Masculino", "Feminino"],[f"{pm}%",f"{pf}%"]]
    plt.axis('off')
    plt.title("Distribuição da doença por sexo")
    table = plt.table(cellText=totable, loc='center')
    table.set_fontsize(14)
    table.scale(1, 2)
    plt.show()
    

    sexo = [ "Masculino", "Feminino"]
    score = [pm,pf]
    plt.bar(sexo, score)
    plt.title("Distribuição da doença por sexo")
    plt.xlabel("sexo")
    plt.ylabel("porcentagem")
    plt.show()
    
def counting_by_age():
    # [30-34], [35-39], [40-44]
    arry = [0,0,0,0,0,0,0,0]
    
    for row in matrix:
            if ((int(row[5])) == 1): 
                while ((len(arry)-1)<(((int(row[0]))-30)//5)): arry.append(0)
                arry[(((int(row[0]))-30)//5)]+=1 

    soma = sum(arry) 
    #for i in range(0,len(arry)):
    #    print (f"\n Percentagem faixa etária [{30+5*i}-{34+5*i}] : {round((int(arry[i]) / soma *100) , 2)}") 
    #print(arry)


    faixa_etaria = []
    porcentagem = []
    totable= []
    for i in range(0,len(arry)):
        faixa_etaria.append(f"[{30+5*i}-{34+5*i}]")
        porcentagem.append(round((int(arry[i]) / soma *100) , 2))
        totable.append([f"[{30+5*i}-{34+5*i}]", f"{round((int(arry[i]) / soma *100) , 2)}%"])

    plt.title("Distribuição da doença por faixa etária")
    plt.axis('off')
    table = plt.table(cellText=totable, loc='center')
    table.set_fontsize(14)
    table.scale(1, 2)
    plt.show()

    plt.bar(faixa_etaria, porcentagem)
    plt.title("Distribuição da doença por faixa etária")
    plt.xlabel("faixa_etaria")
    plt.ylabel("porcentagem")
    plt.show()
   
    
    
def counting_min_colestrol():
    # [30-34], [35-39], [40-44]
    arry = [0,0,0,0,0,0,0]

    for row in matrix:
            if ((int(row[5])) == 1): 
                while ((len(arry)-1)<((int(row[3]))//10)): arry.append(0)
                arry[((int(row[3]))//10)]+=1 

    soma = sum(arry) 
    #for i in range(0,len(arry)):
    #    if (arry[i]!=0): print (f"\n Percentagem faixa etária [{10*i}-{9+10*i}] : {round((int(arry[i]) / soma *100) , 2)}") 
    #print(arry)
    colestrol = []
    porcentagem = []
    totable = []
    for i in range(0,len(arry)):
        if (arry[i] != 0):
            colestrol.append(f"[{10*i}-{9+10*i}]")
            porcentagem.append(round((int(arry[i]) / soma *100) , 2))
            totable.append([f"[{10*i}-{9+10*i}]",f"{round((int(arry[i]) / soma *100) , 2)}%"])

    plt.axis('off')
    table = plt.table(cellText=totable, loc='center')
    table.set_fontsize(14)
    table.scale(1, 2)
    plt.show()

    plt.bar(colestrol, porcentagem)
    plt.title("Distribuição da doença por colestrol")
    plt.xlabel("faixa_etaria")
    plt.ylabel("porcentagem")
    table.set_fontsize(2)
    table.scale(1, 1)
    plt.show()
   



with open("myheart.csv", 'r') as file:
  matrix = []
  r=0
  csvreader = csv.reader(file)
  for row in csvreader:
    r=r+1
    matrix.append(row)
  matrix = matrix[1:]  
  print(matrix)  
  print (*['\n nr linhas do ficheiro: ', r])  

counting_by_sex()
counting_by_age()
counting_min_colestrol()