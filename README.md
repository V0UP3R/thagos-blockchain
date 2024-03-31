# Thagos Blockchain

Este é um projeto simples de uma blockchain em Python, chamada Thagos Blockchain, usando Flask para criar uma interface de comunicação.

## Funcionamento

A Thagos Blockchain é uma implementação básica de uma blockchain com as seguintes funcionalidades:

1. **Mineração de Blocos**: Os novos blocos são adicionados à blockchain por meio de um processo de mineração, onde os mineradores resolvem um desafio computacional difícil para encontrar um novo bloco válido.

2. **Transações**: Os usuários podem criar transações, que são agrupadas em blocos e adicionadas à blockchain. Cada transação inclui o remetente, destinatário e a quantidade de moeda transferida.

3. **Validação da Blockchain**: A integridade da blockchain é mantida através da validação de cada bloco. Cada novo bloco inclui o hash do bloco anterior, garantindo uma ligação criptográfica entre os blocos.

## Como Usar

1. **Instalação**: Clone este repositório em sua máquina local.

    ```bash
    git clone https://github.com/V0UP3R/thagos-blockchain.git
    cd thagos-blockchain
    ```

2. **Configuração do Ambiente Virtual**:
   
   - Crie um ambiente virtual Python (venv):
   
     ```bash
     python -m venv venv
     ```

   - Ative o ambiente virtual:
   
     - No Windows:
       ```bash
       venv\Scripts\activate
       ```

     - No macOS e Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Instalação das Dependências**:
   
   Com o ambiente virtual ativado, instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

4. **Execução do Projeto**:
   
   Execute o arquivo `app.py` para iniciar o servidor Flask:

    ```bash
    python app.py
    ```

5. **Interagindo com a Blockchain**:

    - **Mineração de um Novo Bloco**:
    
        Faça uma solicitação GET para `/mine`. Isso resolverá o problema de prova de trabalho e adicionará um novo bloco à blockchain.

    - **Criar uma Nova Transação**:
    
        Faça uma solicitação POST para `/transactions/new`, fornecendo os detalhes da transação no corpo da solicitação em formato JSON (remetente, destinatário e quantidade).

    - **Ver a Cadeia Completa**:
    
        Faça uma solicitação GET para `/chain`.

6. **Desativação do Ambiente Virtual**:
   
   Quando terminar de trabalhar no projeto, desative o ambiente virtual:

    ```bash
    deactivate
    ```

## Considerações Finais

Este é um projeto básico para entender os conceitos fundamentais de uma blockchain. Ele não inclui recursos avançados como segurança robusta, persistência de dados, consenso de rede, entre outros. Sinta-se à vontade para explorar, experimentar e expandir este projeto de acordo com suas necessidades e interesses.
