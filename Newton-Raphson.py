import sympy as sp
import numpy as np

def calcular_derivada(coefs):
    """
    Calcula a derivada do polinômio.
    """
    x = sp.symbols('x')
    # Monta o polinômio com os coeficientes.
    polinomio = sum(coefs[i] * x**(len(coefs)-1-i) for i in range(len(coefs)))
    # Encontra a derivada do polinômio.
    derivada = sp.diff(polinomio, x)
    # Transforma a derivada em uma função que podemos usar.
    return sp.lambdify(x, derivada, 'numpy')

def newton_raphson(coefs, x0, tol=1e-12, max_iter=1000, display_precision=14):
    """
    Encontra uma raiz do polinômio usando o método de Newton-Raphson.
    """
    # Cria a função do polinômio.
    f = lambda x_val: sum(coefs[i] * x_val**(len(coefs)-1-i) for i in range(len(coefs)))
    # Obtém a função da derivada.
    f_prime = calcular_derivada(coefs)
    
    x_n = float(x0) # Começa com um ponto inicial.
    for _ in range(max_iter):
        fx_n = f(x_n)
        f_prime_x_n = f_prime(x_n)
        
        # Evita dividir por zero se a derivada for muito pequena.
        if abs(f_prime_x_n) < tol:
            return None 
            
        x_n1 = x_n - fx_n / f_prime_x_n # Calcula a próxima estimativa da raiz.
        
        # Para quando a raiz é encontrada com precisão suficiente.
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
        
    # Retorna vazio se a raiz não for encontrada em muitas tentativas.
    return None 

def encontrar_raizes_reais_newton(coefs, display_precision=14):
    """
    Tenta encontrar várias raízes reais do polinômio, testando diferentes pontos de partida.
    """
    raizes_e_erros_encontrados = []
    # Teste muitos pontos para tentar achar todas as raízes.
    for x0_inicial in np.linspace(-500, 500, 10001): 
        result = newton_raphson(coefs, x0_inicial, display_precision=display_precision) 
        if result is not None:
            raiz, erro, tipo_erro = result 
            # Evita colocar raízes repetidas.
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
        print("\nRaízes reais encontradas (via Newton-Raphson):")
        for r, erro, tipo_erro in raizes_e_erros_reais:
            # Mostra a raiz como número inteiro ou com as casas decimais definidas.
            if abs(r - round(r)) < 1e-5:
                print(f"  Raiz: {int(round(r))}")
            else:
                print(f"  Raiz: {r:.{PRECISAO_EXIBICAO}f}")
            print(f"  Erro {tipo_erro}: {erro:.2e}") # Mostra o erro.
    else:
        print("\nNenhuma raiz real foi encontrada com os pontos iniciais testados.")
        print("Dica: Tente mudar o **intervalo** e a **quantidade de pontos iniciais** em `np.linspace` (linha 60).")
        print("Você também pode tentar **reduzir a tolerância** (`tol`, linha 16) e **aumentar o máximo de iterações** (`max_iter`, linha 16).")
        print("Aviso: Aumentar esses parâmetros pode fazer o cálculo demorar mais.")
