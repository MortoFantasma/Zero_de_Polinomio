# Métodos de Newton para Encontrar Raízes

Este repositório apresenta duas implementações do método de Newton-Raphson para localizar raízes reais de polinômios. Cada script adota uma estratégia distinta para o cálculo da função e sua derivada, explorando as vantagens de bibliotecas de álgebra simbólica e de algoritmos numéricos eficientes.

---

## Projetos

### 1. Newton-Raphson (com SymPy)

Este script oferece uma abordagem para o método de Newton-Raphson que se beneficia da álgebra simbólica para garantir a exatidão no cálculo da derivada do polinômio.

#### Como Funciona

O coração deste método reside na utilização da biblioteca **SymPy**, que é uma biblioteca Python para matemática simbólica. Com ela, podemos definir o polinômio de forma simbólica e, em seguida, usar a função `sp.diff()` para obter a derivada exata. Depois disso, `sp.lambdify()` é usado para converter a expressão simbólica em uma função numérica eficiente com **NumPy**.

A principal vantagem desta abordagem é a precisão inquestionável da derivada, pois ela é calculada analiticamente. No entanto, para polinômios de grau muito elevado, o custo do cálculo simbólico pode ser um fator a considerar.

#### Exemplo de Uso

Para encontrar as raízes do polinômio `x² − 4`:  

Digite os coeficientes do polinômio (do maior grau ao termo independente), separados por espaço:  
Exemplo: para x² - 4, digite: 1 0 -4  

1 0 -4  

Saída esperada:

Buscando raízes reais para o polinômio com coeficientes: [1.0, 0.0, -4.0]  

Raízes reais encontradas (via Newton-Raphson):  
Raiz: -2  
Erro absoluto: 0.00e+00  
Raiz: 2  
Erro absoluto: 0.00e+00  

---

### 2. Newton-Raphson (com Briot-Ruffini)

Esta versão do método é projetada para ser eficiente e puramente numérica, utilizando o algoritmo de **Briot-Ruffini** para avaliar o polinômio e sua derivada.

#### Como Funciona

O algoritmo de **Briot-Ruffini** (ou divisão sintética) permite calcular o valor de um polinômio `P(x)` e de sua derivada `P′(x)` em um ponto `x₀` de forma muito eficiente, operando diretamente sobre os coeficientes do polinômio. A técnica envolve duas divisões sintéticas consecutivas para obter `P(x₀)` e `P′(x₀)`.

A principal vantagem é o desempenho, pois evita dependências simbólicas, tornando-o ideal para ambientes com restrições de performance ou bibliotecas.

#### Exemplo de Uso

Para encontrar as raízes do polinômio `x³ − 6x² + 11x − 6`:  

Digite os coeficientes do polinômio (do maior grau ao termo independente), separados por espaço:  
Exemplo: para x³ − 6x² + 11x − 6, digite: 1 -6 11 -6  

1 -6 11 -6  

Saída esperada:

Buscando raízes reais para o polinômio com coeficientes: [1.0, -6.0, 11.0, -6.0]  

Raízes reais encontradas (via Newton-Briot-Ruffini):  
Raiz: 1  
Erro absoluto: 0.00e+00  
Raiz: 2  
Erro absoluto: 0.00e+00  
Raiz: 3  
Erro absoluto: 0.00e+00  

---

## Como Usar os Scripts

### 1. Instale o Python

Certifique-se de ter o **Python 3.x** instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

---

### 2. Obtenha os Arquivos

#### Se você usa Git:

git clone https://github.com/SeuUsuario/SeuRepositorio.git  
cd SeuRepositorio  
Ou baixe diretamente:  
Baixe o repositório como ZIP via GitHub e extraia os arquivos em uma pasta local.

3. Instale as Dependências
No terminal, dentro da pasta do projeto:  
pip install sympy numpy  

Nota: sympy é necessário apenas para o script com SymPy.

4. Execute os Scripts
Para a versão com SymPy:  
python Newton-Raphson.py

Para a versão com Briot-Ruffini:  
python Newton-Briot-Ruffini.py

Siga as instruções na tela para inserir os coeficientes do polinômio.

Observação: Ambos os métodos procuram raízes reais dos polinômios. Se você deseja buscar também raízes complexas, será necessário adaptar os scripts ou utilizar bibliotecas específicas para esse fim.

Desenvolvido com fins educacionais e científicos.
