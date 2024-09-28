while True:
    print("Seleccione una opción")
    print("1. Calcular IVA")
    print("2. Calcular descuento")
    print("3. Calcular IMC")
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        precio = float(input("Ingrese el precio del producto: "))
        iva = 0.19
        def multiplica(precio, iva):
            total = precio * iva
            return total
        print("El iva de su producto es: ", multiplica(precio, iva))
    
    elif opcion == 2:
        producto = int(input("Ingrese el precio del producto: "))
        descuento = int(input("Ingrese el descuento del producto: "))
        descuento_valido = True
        
        if descuento > producto:
            print("El descuento no puede ser mayor al precio del producto")
            descuento_valido = False
        elif descuento == producto:
            print("El descuento no puede ser igual al precio del producto")
            descuento_valido = False
        else:
            def resta(producto, descuento):
                total = producto - descuento
                return total
        
        if descuento_valido:
            print("El precio final del producto es: ", resta(producto, descuento))
    
    elif opcion == 3:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        def imc(peso, altura):
            return peso / (altura ** 2)
        
        valor_imc = imc(peso, altura)
        print("Su índice de masa corporal es: ", valor_imc)
        
        
        if valor_imc < 18.5:
            print("Bajo peso")
        elif valor_imc >= 18.5 and valor_imc < 25:
            print("Normal")
        elif valor_imc >= 25 and valor_imc < 30:
            print("Sobrepeso")
        elif valor_imc >= 30 and valor_imc < 35:
            print("Obesidad grado 1")
        elif valor_imc >= 35 and valor_imc < 40:
            print("Obesidad grado 2")
        elif valor_imc >= 40:
            print("Obesidad grado 3")
    
    else:
        print("Opción no válida")
