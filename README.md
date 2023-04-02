# Ouvidoria
Projeto de Ouvidoria - Fase 2

Alunos:
- Flávia Amorim
- João Vitor
- Jonathan Gois
- Kleiton Ferreira
- Sabrina Marques
- Sandro Ramos

Observações:

1) No MySQL Wokbench, cria o schema chamado "ouvidoria" com as seguintes tabelas:

create table reclamacoes (
codigo int auto_increment,
reclamacao varchar (1000),
primary key (codigo)

);

create table elogios_sugestoes (
codigo int auto_increment,
elogio_sugestao varchar (1000),
primary key (codigo)

);


2) Trocar a senha do MySQL Workbench, no aquivo ouvidoria.py (código pricipal), pela senha do MySQL em uso na hora de rodar o código para estabelecer a conexão entre o Pycharm e o MySQL.

3) Copia o arquivo operacoesbd.py para a pasta do projeto, para poder rodar o código integrado ao MySQL.

4) Utilizamos o código “Try Except” para evitar erros ao digitar floats e strings nas opções de input.

