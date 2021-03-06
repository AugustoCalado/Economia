import numpy as np
import matplotlib.pyplot as plt

class Elasticidade:
    
    def __init__(self):
        self.renda_familia = np.array([])
        self.file = None


    def read_csv(self):

        lines = open("../Arquivos_de_Entrada/elasticidade.csv").readlines()
        lines = [li.strip() for li in lines]
        lines = [[float(x) for x in li.split(",")] for li in lines]
        return np.array(lines)


    def setup_wizard(self):
        print("----------------------------\n")
        print("Cálculo da Elasticidade \n ")
        print("----------------------------\n")
        print("Calculamos a elasticidade de renda, a elasticidade de preço da demanda de um produto e a elasticidade cruzada entre dois produtos. \n")
        print("Entrada: o arquivo elasticidade.csv \n")
        print("Saida: O coeficiente de elasticidade de preço da demanda, de preço e cruzada e uma explicação sobre o resultado\n")
        print("----------------------------\n")


    def input_data(self):
        print("----------------------------\n")
        #self.file = input("Digite o nome do arquivo csv de entrada (o arquivo deve estar no mesmo diretorio do executavel ou deve ser passado o caminho global como parametro) : ")
        print("----------------------------\n")


    def open_csv(self):
        Df = self.read_csv()
        self.renda_familia = Df[0, :]
        self.quantidade_demandada_1 = Df[1, :]
        self.preco_1 = Df[2, :]
        self.quantidade_demandada_2 = Df[3, :]
        self.preco_2 = Df[4, :]

    def calculos(self):

        self.elasticidade_demanda_1 = ((self.quantidade_demandada_1[1]-self.quantidade_demandada_1[0])*100/(self.quantidade_demandada_1[0]))/((self.preco_1[1]-self.preco_1[0])*100/(self.preco_1[0]))
        self.elasticidade_demanda_2 = ((self.quantidade_demandada_2[1]-self.quantidade_demandada_2[0])*100/(self.quantidade_demandada_2[0]))/((self.preco_2[1]-self.preco_2[0])*100/(self.preco_2[0]))
        self.elasticidade_renda_1 = ((self.quantidade_demandada_1[1]-self.quantidade_demandada_1[0])*100/(self.quantidade_demandada_1[0]))/((self.renda_familia[1]-self.renda_familia[0])*100/self.renda_familia[0])
        self.elasticidade_renda_2 = ((self.quantidade_demandada_2[1]-self.quantidade_demandada_2[0])*100/(self.quantidade_demandada_2[0]))/((self.renda_familia[1]-self.renda_familia[0])*100/self.renda_familia[0])
        self.elasticidade_cruzada = (((self.quantidade_demandada_1[1]-self.quantidade_demandada_1[0])*100)/(self.quantidade_demandada_1[0]))/(((self.preco_2[1]-self.preco_2[0])*100)/self.preco_2[0])

    def resultados(self):

        #Resultados
        print("As elasticidades dos produtos sao as seguintes:\n")
        print("A elasticidade preço da demanda do produto 1 é "+ str(self.elasticidade_demanda_1))

        if self.elasticidade_demanda_1<0: 
            print("\n Assim, o produto 1 é considerado um bem comum \n \n")
        else: 
            print("\n Assim, o produto 1 é considerado um bem de Giffen \n \n")

        print("\nA elasticidade preço da demanda do produto 2 é "+ str(self.elasticidade_demanda_2))


        if self.elasticidade_demanda_2<0: 
            print("\n Assim, o produto 2 é considerado um bem comum \n \n")
        else: 
            print("\n Assim, o produto 2 é considerado um bem de Giffen \n \n")
 
        print("\nA elasticidade renda produto 1 é "+ str(self.elasticidade_renda_1))

        if(self.elasticidade_renda_1 >0 and self.elasticidade_renda_1 <1):
            print("\n Assim o produto 1 é considerado um bem essencial \n\n")
        elif(self.elasticidade_renda_1 >=1):
            print("\n Assim o produto 1 é considerado um bem de luxo \n\n")
        elif(self.elasticidade_renda_1 < 0):
            print("\n Assim o produto 1 é considerado um bem inferior \n\n")
        else: 
            print("\n Assim o produto 1 é considerado um bem inferior \n\n")


        print("\nA elasticidade renda produto 2 é  "+ str(self.elasticidade_renda_2))


        if(self.elasticidade_renda_2 >0 and self.elasticidade_renda_2 <1):
            print("\n Assim o produto 2 é considerado um bem essencial \n\n")
        elif(self.elasticidade_renda_2 >=1):
            print("\n Assim o produto 2 é considerado um bem de luxo \n\n")
        elif(self.elasticidade_renda_2 < 0):
            print("\n Assim o produto 2 é considerado um bem inferior \n\n")
        else: 
            print("\n Assim o produto 2 é considerado um bem inferior \n\n")

        print("\nA elasticidade cruzada entre o produto 1 e 2 é "+ str(self.elasticidade_cruzada)+ "\n")
        
        if (self.elasticidade_cruzada >0 ): 
            print("\n Assim o produto 1 é um bem substituto do produto 2 \n \n")
        elif(self.elasticidade_cruzada<0):
            print("\n Assim o produto 1 é um bem complementar do produto 2 \n \n")
        else:
            print("\n Assim o produto 1 e o produto 2 são bens independentes \n \n")            
        

        print("----------------------------\n")

        
        
if __name__=="__main__":

    el = Elasticidade()
    el.setup_wizard()
    el.input_data()
    el.open_csv()
    el.calculos()
    el.resultados()