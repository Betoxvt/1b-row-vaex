# Desafio da Aula 05 - 1 bilhão de linhas
## Melhorar o projeto que lê o arquivo, e apresenta uma tabela ordenada pelo nome das estações com a mínima máxima e média das temperaturas (1 casa decimal).
[Link para a aula](https://github.com/lvgalvao/data-engineering-roadmap/tree/176b2e83fc5a12e032d70a6dff257d861a23d55a/Bootcamp%20-%20Python%20para%20dados/aula05)
### Neste projeto vou tentar utilizar Vaex para processar os dados.
- Se já converteu o arquivo de dados para .hdf5 não precisa mais e fica mais ágil o processamento.
- Vaex 4.17.0 funciona em Python 3.10.14, por isso fiz outro repositório
- 100M levou 2.79s (mais 28.94s da conversão para hdf5)
- 1B levou 32.46s (mais 316.52s da conversão para hdf5)
### Próximos passos
- Aplicar os conhecimentos das aulas anteriores para melhorar o código.
- Será que é possível deixar mais rápido? Algum outro jeito de converter e abrir o arquivo. Pesquisar multiprocessamento, talvez em paralelo com a GPU...
