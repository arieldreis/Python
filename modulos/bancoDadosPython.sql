create database testePython;
use testePython;

create table usuarios(
	id int auto_increment primary key,
    nome varchar(50),
    sobrenome varchar(50),
    nascimento date,
    email varchar(60)
);

select * from usuarios;
