
CREATE DATABASE universidade;

USE universidade;

CREATE TABLE alunos (
    id INT PRIMARY key AUTO_INCREMENT,
    nome VARCHAR(250) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    cpf CHAR(11) NOT NULL UNIQUE,
    telefone CHAR(12) UNIQUE,
    endereco VARCHAR(250),
    matricula BOOLEAN DEFAULT TRUE
);