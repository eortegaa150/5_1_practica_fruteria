# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 16:39:44 2020

@author: Lalo
"""

print('''
      ************************************************
      
                  FRUTERÍA DE LALO :D
      
      ************************************************
      ''')

reporteFrutas = {} #Diccioanrio de la Frutería
#Este diccionario contiene {Fruta: [kg en Tienda, kg Vendidos, costo del Provedor, costo al Cliente, dinero Gastado, ganancia] }
#                                       0               1              2                  3                  4            5
#                                    float            float          
#
#DEFINIR VARIABLEs
pesoTienda = 0
pesoVendidos = 0

#Hacemos reinicio igual a 1 para que pueda entrar al for
while(True):
    respuesta = input('''Elige una opción:
   a) Comprar fruta
   b) Vender fruta a un cliente
   c) Ver reporte total de la frutería
   d) Salir     
   Respuesta: ''')
    
    #CASO 1: COMPRAR FRUTA       
    #Ingresar los datos de la fruta comprada
    if(respuesta.upper() == "A"):
        fruta = input("Ingresa el nombre de la fruta que compraste: ")
        pesoCompra = input("Ingresa la cantidad de kilogramos que se compraron: ")
        costoProv = input("Ingresa el costo de venta del provedor: ")
        costoCliente = input("Ingresa el costo de venta al cliente: ")
    
        x = fruta.upper() in reporteFrutas
        
        #Revisar si la fruta ya se encuentra en el sistema
        if(x == True):
            #Si ya se encuentra, a los kilogramos que hay en la tienda se les suman los kg de la compra
            pesoTienda = reporteFrutas.get(fruta.upper())[0] + float(pesoCompra)
            #Los kilogramos vendidos van a ser los mismos porque no se ha vendido nada
            pesoVendidos = reporteFrutas.get(fruta.upper())[1]
            #El dinero gastado en la fruta es igual al peso de la compra por el costo del provedor mas lo que ya se encuentra en la tienda
            dineroGastado  = reporteFrutas.get(fruta.upper())[4] + float(pesoCompra) * float(costoProv)
            #La ganancia es igual a - dineroGastado + los que ya se encuentra en la tienda
            ganancia = reporteFrutas.get(fruta.upper())[5] - ( float(pesoCompra) * float(costoProv) )
        else:
            #Si NO se encuenta, el peso de la Tienda es igual al peso de la compra
            pesoTienda = float(pesoCompra)
            #Y el peso de vendidos es igual a 0
            pesoVendidos = 0
            #El dinero gastado en la fruta es igual al peso de la compra por el costo del provedor
            dineroGastado  = float(pesoCompra) * float(costoProv)
            #La ganancia es igual a - dineroGastado
            ganancia = - ( float(pesoCompra) * float(costoProv) )
            
        reporteFrutas.update( { fruta.upper() : [float(pesoTienda) , float(pesoVendidos), float(costoProv), float(costoCliente), float(dineroGastado), float(ganancia) ] } )
        
        #print(reporteFrutas.items())
    
    #CASO 2 VENDER FRUTA
    elif(respuesta.upper() == "B"):
        #While para buscar fruta
        while(True):
            fruta = input("Ingresa el nombre de la fruta que se va a vender o 'F' para volver: ")
            #Comprobar si la fruta que se ingresa NO se encuentra en la tienda
            x = fruta.upper() in reporteFrutas 
            if(x == False and fruta.upper() != "F"):
                #Si la fruta no se encuentra aparece un mensaje
                print('''
                      ****************************************************
                      
                      La fruta ingresada NO se encuentra, intenta de nuevo
                                  o presiona INGRESA 'F' para salir
                      
                      ****************************************************''')
            elif(fruta.upper() == "F"):
                #Si el usuario ingresa F se sale del while
                break
            else:
                #Si la fruta si se encuentra se sale de while
                break
            
        #Ingresar los kilogramos que se van a vender
        while(True):
            print('''
                  ****************************************
                  
                      Se tiene %.2f kg de %s
                      
                      El precio por kilogramo es: $ %.2f
                     
                  ****************************************'''%( reporteFrutas.get(fruta.upper())[0], fruta.upper(), reporteFrutas.get(fruta.upper())[3] ) )
            pesoVenta = input("Ingresa la cantidad de kilogramos que se van a vender: ")
            #Verificar si la cantidad de kilogramos vendidos es menor a la cantidad de kilogramos vendidos
            x = reporteFrutas.get(fruta.upper())[0] #Esto no puedo ponerlo dentro del if, por eso lo pongo fuera y lo igualo a una variable
            if(float(pesoVenta) > x):
                print('''
                      *******************************************************************************
                      
                      El peso de venta es menor al numero de kg disponibles en Tienda, intenta de nuevo
                      
                      **********************************************************************************
                      ''')
            else: 
                break  
            
        #Operaciones en el diccionario
        #El peso de tienda es eñl peso que se tiene menos el peso de la venta
        pesoTienda = reporteFrutas.get(fruta.upper())[0] - float(pesoVenta)
        #Los kg vendidos se suman a los que ya se tienen
        pesoVendidos = reporteFrutas.get(fruta.upper())[1] + float(pesoVenta)
        #El precio del provedor se mantiene igual
        costoProv = reporteFrutas.get(fruta.upper())[2]
        #El precio de la venta se mantiene igual
        costoCliente = reporteFrutas.get(fruta.upper())[3]
        #El dinero gastado se mantiene igual
        dineroGastado = reporteFrutas.get(fruta.upper())[4]
        #La ganacia se le suma lo que se gano en la venta
        ganancia = reporteFrutas.get(fruta.upper())[5] + ( float(pesoVenta) * reporteFrutas.get(fruta.upper())[2])
        #Precio total de la venta es igual al peso por el costoCliente
        precioTotal = float(pesoVenta) * reporteFrutas.get(fruta.upper())[2]
        
        print('''
              *****************************************************
                         La venta se realizó con exito
                         Se vendieron: %.2f kg de %s
                         El precio por kg es: %.2f
                         El precio total es: %.2f
              *****************************************************'''%(float(pesoVenta), fruta.upper(), reporteFrutas.get(fruta.upper())[3], precioTotal  ) ) 
        
        reporteFrutas.update( { fruta.upper() : [float(pesoTienda) , float(pesoVendidos), float(costoProv), float(costoCliente), float(dineroGastado), float(ganancia), float(float(pesoVenta) * reporteFrutas.get(fruta.upper())[2])] } )
        
        #print(reporteFrutas.items())
    
    #CASO 3: REPORTE
    elif(respuesta.upper() == "C"):
        print('''
              ***************************************
                          REPORTE FRUTERIA
              ***************************************''')
        
        x=1 #Contador de las frutas
        for k,v in reporteFrutas.items():
            print('''
                  **********************************************
                  PRODUCTO %i
                  Nombre: %s
                  kg en Tienda: %.2f
                  kg Vendidos: %.2f
                  Precio de Compra al Proveedor: %.2f
                  Precio de Venta al Cliente: %.2f
                  Dinero gastado: %.2f
                  Ganancia: %.2f
                  **********************************************'''%(x,k, reporteFrutas.get(k)[0], reporteFrutas.get(k)[1], reporteFrutas.get(k)[2], reporteFrutas.get(k)[3], reporteFrutas.get(k)[4], reporteFrutas.get(k)[5]) )
            x+=1  
    elif(respuesta.upper() == "D"):
        print('''
              **********************************************
                              VUELVE PRONTO
              **********************************************''')
        break
    else:
        print('''
              *************************************************
                              OPCIÓN NO VÁLIDA
              *************************************************''')