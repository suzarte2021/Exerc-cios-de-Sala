for numero in [
    326,
    300,
    100,
    320,
    310,
    305,
    301,
    101,
    311,
    111,
    25,
    20,
    10,
    21,
    11,
    1,
    7,
    16,
]:
    # O laço for foi utilizado para o teste automático dos valores
   
    # numero = int(input("Digite o inteiro menor que 1000: "))
    print(f"\nNumero: {numero}")
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ""
    separador2 = ""
    # Se ambos unidade, dezena e centena
    if centena > 0 and dezena > 0 and unidade > 0:
        separador1 = " , "  
        separador2 = " e "  
    # Senão, se tiver uma centena e uma dezena
    elif centena > 0 and dezena > 0:
        separador1 = " e "  
        separador2 = ""
    # Se tiver só a centena e a unidade, ou só a dezena e a unidade
    elif (centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""  # Não haverá separador entre centena e dezena
        separador2 = " e "  # Mas entre centena/dezena e unidade

    # Se a centena não estiver zerada
    if centena > 0:
        if centena == 1:
            # Se ela for igual a 1
            centena = "1 centena"
        else:
            # Senão
            centena = f"{centena} centenas"
    else:
      
        # vazia para nada ser impresso
        centena = ""
    # Dezena
    if dezena > 0:
        if dezena == 1:
            dezena = "1 dezena"
        else:
            dezena = f"{dezena} dezenas"
    else:
        dezena = ""
    # Unidade
    if unidade > 0:
        if unidade == 1:
            unidade = "1 unidade"
        else:
            unidade = f"{unidade} unidades"
    else:
        unidade = ""


    # Resultado
    print(f"{centena}{separador1}{dezena}{separador2}{unidade}")