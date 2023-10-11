# python 3y

import os

save = "Foi salvo no histórico"

# Verifica se o arquivo do histórico existe.
if os.path.exists("histórico.txt"):
   print("ok")

else:
    os.system("touch histórico.txt")

# Mostra a primeira lista de opções.
print("1 | cálcular")
print("2 | histórico")

# Resposta do usúario
option1 = int(input("Oq quer fazer? "))

# Verifica qual opção escolheu.
if option1 == 1:
   os.system("clear")
   print("1 | adição")
   print("2 | subtração")
   print("3 | multiplicação")
   print("4 | divisão")

# Resposta do usúario.
   option2 = int(input("Que tipo de calcúlo quer fazer? "))

# Verifica qual opção escolheu.
   match option2:

         case 1:
               adição1 = int(input("Qual o primeiro número que quer por para somar?\n"))
               adição2 = int(input("Qual o segundo?"))
               adi_calcúlo = adição1 + adição2
               print(f"{adição1} + {adição2} =")
               print(adi_calcúlo)

               cal_histórico = input("Quer salvar no histórico? y ou n ")

               match cal_histórico:

                     case "y":
                           with open("histórico.txt", "a") as adi_histórico:
                                adi_histórico.write(f"\n{adição1} + {adição2} = {adi_calcúlo}")
                                print(save)

                     case "n":
                           print("Ok")

                     case _:
                           print("y ou n")

         case 2:
               subtração1 = int(input("Qual o primeiro número? "))
               subtração2 = int(input("Qual o segundo? "))
               sub_calcúlo = subtração1 - subtração2
               print(f"{subtração1} - {subtração2} =")
               print(sub_calcúlo)

               cal_histórico = input("Quer salvar no histórico? y ou n ")

               match cal_histórico:

                     case "y":
                             with open("histórico.txt", "a") as sub_histórico:
                                  sub_histórico.write(f"\n{subtração1} - {subtração2} = {sub_calcúlo}")
                                  print(save)
                     case "n":
                             print("Ok")

                     case _:
                           print("y ou n")

         case 3:
               multiplicação1 = int(input("Qual o primero? "))
               multiplicação2 = int(input("Qual o segundo? "))
               mul_calcúlo = multiplicação1 * multiplicação2
               print(f"{multiplicação1} + {multiplicação2} =")
               print(mul_calcúlo)

               cal_histórico = input("Quer salvar no histórico? ")

               match cal_histórico:

                     case "y":
                             with open("histórico.txt", "a") as mul_histórico:
                                  mul_histórico.write(f"\n{multiplicação1} * {multiplicação2} = {mul_calcúlo}")
                                  print(save)
                     case "n":
                             print("Ok")

                     case _:
                           print("y ou n")

         case 4:
            divisão1 = int(input("Qual o primeiro?"))
            divisão2 = int(input("Qual o segundo?"))
            div_resultado = divisão1 / divisão2
            print(f"{divisão1} / {divisão2} =")
            print(div_resultado)

            cal_histórico = input("Quer salvar no histórico?")

            match cal_histórico:

              case "y":
                with open("histórico.txt", "a") as div_histórico:
                  div_histórico.write(f"\n{divisão1} / {divisão2} = {div_resultado}")
                  print(save)

              case "n":
                print("Ok")

              case _:
                print("y ou n")

         case _:
               print("Coloque o número que corresponde ao tipo de calcúlo")

elif option1 == 2:
     with open("histórico.txt", "r") as histórico:
          ver = histórico.read()

          print(ver)

else:
    print("ok3")
