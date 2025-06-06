import numpy as np

def briot_ruffini_division(coefs, x_val):
    """
    Calcula o valor do polinômio P(x) e sua primeira derivada P'(x) no ponto x_val.
    """
    n = len(coefs)
    
    # Prepara para a primeira divisão (para encontrar P(x_val))
    b_coefs = [0.0] * n
    b_coefs[0] = float(coefs[0])

    for i in range(1, n):
        b_coefs[i] = float(coefs[i]) + b_coefs[i-1] * x_val
    
    poly_val = b_coefs[n - 1] # Valor do polinômio em x_val

    # Caso especial para polinômios muito simples (apenas um número)
    if n == 1:
        return (coefs[0], 0.0) 
    
    # Prepara para a segunda divisão (para encontrar P'(x_val))
    c_coefs = [0.0] * (n - 1)
    c_coefs[0] = b_coefs[0]

    for i in range(1, n - 1):
        c_coefs[i] = b_coefs[i] + c_coefs[i-1] * x_val

    deriv_val = c_coefs[n - 2] # Valor da derivada em x_val

    return (poly_val, deriv_val)

def newton_raphson(coefs, x0, tol=1e-12, max_iter=1000, display_precision=14):
    """
    Encontra uma raiz do polinômio usando o método de Newton-Raphson.
    Usa Briot-Ruffini para os cálculos internos.
    """
    x_n = float(x0) # Ponto inicial para começar a busca pela raiz.
    for _ in range(max_iter):
        fx_n, f_prime_x_n = briot_ruffini_division(coefs, x_n) # Calcula P(x) e P'(x)
        
        # Evita divisão por zero se a derivada for muito pequena.
        if abs(f_prime_x_n) < tol:
            return None 
            
        x_n1 = x_n - fx_n / f_prime_x_n # Calcula a próxima estimativa da raiz
        
        # Verifica se a raiz foi encontrada com precisão suficiente.
        if abs(x_n1 - x_n) < tol:
            root_val = round(x_n1, display_precision)
            # Decide se o erro é relativo ou absoluto.
            if abs(root_val) < 1e-9: 
                final_error = abs(x_n1 - x_n)
                error_type = "absoluto"
            else:
                final_error = abs(x_n1 - x_n) / abs(x_n1)
                error_type = "relativo"
            
            return (root_val, final_error, error_type) 
            
        x_n = x_n1 # Atualiza o ponto para a próxima rodada.
        
    # Retorna vazio se a raiz não for encontrada após muitas tentativas.
    return None 

def encontrar_raizes_reais_newton(coefs, display_precision=14):
    """
    Tenta encontrar várias raízes reais do polinômio, testando diferentes pontos de partida.
    """
    raizes_e_erros_encontrados = []
    # Teste muitos pontos para tentar achar todas as raízes.
    for x0_inicial in np.linspace(-500, 500, 1000): 
        result = newton_raphson(coefs, x0_inicial, display_precision=display_precision) 
        if result is not None:
            raiz, erro, tipo_erro = result 
            # Evita colocar raízes repetidas na lista.
            is_duplicada = False
            for r_existente, _, _ in raizes_e_erros_encontrados: 
                if abs(raiz - r_existente) < 1e-5:
                    is_duplicada = True
                    break
            if not is_duplicada:
                raizes_e_erros_encontrados.append((raiz, erro, tipo_erro)) 
    
    raizes_e_erros_encontrados.sort(key=lambda x: x[0]) # Organiza as raízes em ordem.
    return raizes_e_erros_encontrados

if __name__ == "__main__":
    PRECISAO_EXIBICAO = 14 # Quantidade de casas decimais para mostrar as raízes.

    entrada = input("Digite os coeficientes do polinômio (do maior grau ao termo independente), separados por espaço:\nExemplo: para x^2 - 4, digite: 1 0 -4\n")
    try:
        # Corrige vírgulas para pontos e converte os números.
        entrada_tratada = entrada.replace(',', '.')
        coefs = [float(c) for c in entrada_tratada.strip().split()]
    except ValueError:
        print("Erro: Digite apenas números separados por espaço.")
        exit()

    if not coefs:
        print("Erro: Nenhum número foi digitado.")
        exit()

    print(f"\nBuscando raízes reais para o polinômio com coeficientes: {coefs}")
    raizes_e_erros_reais = encontrar_raizes_reais_newton(coefs, display_precision=PRECISAO_EXIBICAO)

    if raizes_e_erros_reais:
        print("\nRaízes reais encontradas (via Newton-Briot-Ruffini):")
        for r, erro, tipo_erro in raizes_e_erros_reais:
            # Mostra a raiz como número inteiro ou com as casas decimais definidas.
            if abs(r - round(r)) < 1e-5:
                print(f"  Raiz: {int(round(r))}")
            else:
                print(f"  Raiz: {r:.{PRECISAO_EXIBICAO}f}")
            print(f"  Erro {tipo_erro}: {erro:.2e}") # Mostra o erro.
    else:
        print("\nNenhuma raiz real foi encontrada com os pontos iniciais testados.")
        print("Dica: Tente mudar o **intervalo** e a **quantidade de pontos iniciais** em `np.linspace` (linha 72).")
        print("Você também pode tentar **reduzir a tolerância** (`tol`, linha 33) e **aumentar o máximo de iterações** (`max_iter`, linha 33).")
        print("Aviso: Aumentar esses parâmetros pode fazer o cálculo demorar mais.")
