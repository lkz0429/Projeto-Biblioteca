# Projeto-Biblioteca
Um organizador para bibliotecas reais

1 - Análises de usuários em um treeview de seus dados e cadastro de prazo fixo em tempo real.

2 - Cadastro ou remoção de usuários por meio de CPF. (e inserção de nome opcional)

3 - Adição ou remoção de penalidades. (ocorre automaticamente ao descumprimento de prazo sugerido)

4 - Associação de livro ao cadastro realizado pelo CPF. (prazo fixo)

5 - Cadastro da devolução de livros ao informe de CPF. (evita de receber penalidades quando dentro do prazo)

extra - Dados armazenados em "Dados.JSON", sem uso de memória volátil a não ser para a atualização dos ticks por segundo durante a execução do programa. (para contabilizar o prazo real)

erros - Mensagens de erro adicionadas para situações inusitadas, impede a execução de ações que contrariam a lógica do programa, como pegar um livro emprestado sem informar o livro,
devoluções sem informe de cpf, ou negativação do sistema de pontos. (apenas alguns exemplos)