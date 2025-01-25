<h1>Jornada Python 🐍- Hashtag Treinamentos</h1> 
Evento intensivão de Python realizado do dia 13/01 à 16/01 com o total de 8 horas  de duração.

Cada aula é dedicada a um tema específico de Python, abordando problemas reais do dia a dia e incluindo projetos práticos, como:

  
  - [Aula 01 - Automação com Python 🤖](#aula01)
  - [Aula 02 - Análise de Dados com Python grafico 📊🔍](#aula02)
  - [Aula 03 - Inteligência Artificial e Previsões 🧠📈](#aula03)
  - [Aula 04 - Criação de Sites e Sistemas com Python👨🏻‍💻🐍](#aula04)

<h2 id="aula01">Aula 01 - Automação com Python - 13/01</h2>
<h3> Desafio proposto:</h3> 
**Cadastrar uma lista de produtos de uma base de Dados de forma automática no site de uma empresa.**

O programa usa a Library pyautogui para automação em Python e o pandas junto com o pacote openpyxl para ler a base de Dados.
O programa simula uma rotina de trabalho cadastrando uma base de Dados em um site, controlando mouse e teclado do computador. 
- Abre o navegador e entra no site de login da empresa 
- Efetua o Login
- Importa a Base de Dados dos produtos
- Cadastra os produtos um a um até consumir toda Base de Dados
  
<h2 id="aula02">Aula 02 - Análise de Dados com Python - 14/01</h2>
<h3>Desafio proposto:</h3>
**Case - Cancelamento de Clientes**

**Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.**

**Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.**

Foi utilizado a Library pandas para trabalhar com  a base de Dados e plotly para trabalhar com gráficos.
- Importação e visualização da Base de Dados 
- Tratamento de Dados
- Análise Inicial -> quantos clientes cancelaram e qual a % dos clientes
- Análise de causa do cancelamento dos clientes
- Percorre todas as colunas da tabela com um for e gera um histograma com o índice de cancelamento de cada

**Conclusão:**

Através da análise dos Dados o índice de cancelamento de 56% caiu para 19% e foi possível indentificar os seguintes motivos de cancelamento:

1º- **Usuários do contrato mensal sempre cancelam.**

**possível solução:** evitar o contrato mensal e incentivar (aplicar descontos) nos contratos anuais e trimestrais.

2º- **Todos os usuários que ligaram mais de 4 vezes para o call center, cancelaram o serviço.**

**possível solução:** criar um processo no qual quando, o usuário atingir 3 ligações para o call center, gere um alerta para que seja tomada alguma atitude para solucionar o problema do cliente. 

3º - **Usuários que atrazaram o pagamento mais de 20 dias, cancelaram o serviço.**

**possível solução:** criar um aviso para quando o atraso do pagamento atingir 15 dias, entrar em contato com o cliente.

<h2 id="aula03">Aula 03 - Inteligência Artificial e Previsões - 15/01</h2>
<h3>Desafio proposto:</h3>
**Case: Score de Crédito dos Clientes**

**Você foi contratado por um banco para conseguir definir o score de crédito dos clientes. Você precisa analisar todos os clientes do banco e, com base nessa análise, criar um modelo que consiga ler as informações do cliente e dizer automaticamente o score de crédito dele: Ruim, Ok, Bom.**

Foi utilizado a Library pandas para trabalhar com a Base de Dados e o scikit-learn para criar IAs

- Importação e vizualização da Base de Dados
- Preparo da Base de Dados para IA (Machine Learning)
- Treinamento da IA
- Modelos de IAs usados -> RandomForest e Neirest Neighbors
- Escolha do melhor modelo de IA
- Uso do melhor modelo para fazer a previsão dos novos clientes
  
<h2 id="aula04">Aula 04 - Criação de Sites e Sistemas com Python - 16/01</h2>
<h3> Desafio proposto:</h3>
**Criar um site bate-papo chamado Hashzap**

Foi utilizado o Framework Flet para desenvolvimento de toda UI da aplicação.
