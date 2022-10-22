# Corretor de Provas

Este é o manual do script Python para correção automática de simulados.

Primeiramente, agradeço por usar meu script. Espero que ele cumpra seu propósito e lhe seja útil para seus simulados.

## Pastas e Arquivos
`script/`: Pasta dos scripts do corretor. Nela estão dois arquivos:
  
- "check.py": Arquivo principal do script;
- "utils.py": Módulo de funções do script;
  
**Não altere estes arquivos** se você não souber manipulá-los.

`gabaritos/`: Pasta para armazenar os gabaritos das provas.

- Coloque as respostas da prova aqui, em arquivos de texto `(.txt)`

- O arquivo deve ter **uma letra por linha**, representando a alternativa correta da questão.

`user_input.txt` : Arquivo de respostas do usuário. Coloque as suas respostas aqui.

- O arquivo deve ter **uma letra por linha**, representando a alternativa escolhida.

`run.sh`
  Arquivo BASH de encapsulamento do script. Use-o para iniciar o script.

## MODO DE USO
1. Certifique-se de que sua prova está dentro da pasta `gabaritos/`

2. Após anotar suas respostas no arquivo `user_input.txt`, abra o terminal na pasta do script e digite `./run.sh`

3. Digite o nome da prova que você quer corrigir. 
   - Digite `test` para testar o script com um arquivo pré-definido.
   - Caso o nome de um arquivo não existente seja passado, o script retornará uma **lista com as provas disponíveis**

4. Você verá o resultado da sua prova imediatamente. Além disso, esses dados serão **salvos em um arquivo com o nome da prova**, no formato `results_<nome-da-prova>.txt`
