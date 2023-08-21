nome_completo= input("Informe seu nome: \n")    
def ano_nascimento():
   while True:
            print ("Informe o ano em que nasceu entre 1922 e 2021: \n")
            try:
                ano =int(input())
                if 1922<= ano <=2021:
                    idade=2022 - ano
                    print("Bem vindo", nome_completo, "em 2022 você completou ou completará", idade , "anos." )
                    break
                else:
                      print("O ano está fora do período, por favor informe um ano entre 1922 e 2021. \n")
            except ValueError:
                 print("Insira um número válido")
            
ano_nascimento()

 