def funcion_mayor_precio (precio_comparar : float) :
    try:
        maximo_precio = 0
        proveedor_comparar = ""
        if precio_comparar > maximo_precio: 
            maximo_precio = precio_comparar
            proveedor_comparar = linea_catalogo[3].strip()
        return maximo_precio, proveedor_comparar
    except Exception as e:
        return e

try:
    #variables adicionales


    componentes_solicitados = open("parcial2/productos_requeridos.txt", "r")
    catalogo = open("parcial2/catalogo.txt", "r")

    componentes_solicitados.readline()
    catalogo.readline()

    lista_componentes_requeridos = componentes_solicitados.readlines()
    lista_catalogo = catalogo.readlines()

    componentes_solicitados.close()
    catalogo.close()

    maximo_precio = 0
    minimo_precio = 700
    proveedor_caro = ""
    proveedor_barato = ""
    contador = 0

    for linea in lista_componentes_requeridos:
        contador += 1
        componente_y_marca = linea.split(";")
        
        componente_requerido = componente_y_marca[0].strip()
        marca_requerida = componente_y_marca[1].strip()

        for i in lista_catalogo:
            linea_catalogo = i.split(";")

            componente_catalogo = linea_catalogo[1].strip()
            marca_catalogo = linea_catalogo[2].strip()



            if componente_requerido == componente_catalogo and marca_catalogo == marca_requerida:

                precio_actual = linea_catalogo[4].strip()
                precio_actual = precio_actual.replace("USD", "").replace(",", ".")
                precio_actual = float(precio_actual)

                maximo_precio, proveedor_caro = funcion_mayor_precio(precio_comparar = precio_actual)
                
                if precio_actual < minimo_precio :
                    minimo_precio = precio_actual
                    proveedor_barato = linea_catalogo[3].strip()

        print(f"----------------\nreporte precios {contador}: \n----------------")
        print(f"producto: {componente_requerido}")
        print(f"marca: {marca_requerida}")
        print(f"precio mayor: {maximo_precio} :: Encontrado en: {proveedor_caro}")
        print(f"precio menor: {minimo_precio} :: Encontrado en: {proveedor_barato}\n")
            
except Exception as e:
    print(e)