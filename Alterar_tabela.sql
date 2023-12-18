# Alterar tabela de alunos, curso e notas

ALTER TABLE escola_curso.alunos
	ADD COLUMN nome VARCHAR(100) NOT NULL AFTER id_aluno,
    ADD COLUMN data_nascimento DATE NOT NULL AFTER nome,
    ADD COLUMN endereco VARCHAR(255) NOT NULL AFTER data_nascimento,
    ADD COLUMN cidade VARCHAR(100) NOT NULL AFTER endereco,
    ADD COLUMN estado VARCHAR(2) NOT NULL AFTER cidade,
    ADD COLUMN cpf VARCHAR(14) NOT NULL AFTER estado;

ALTER TABLE escola_curso.curso
	ADD COLUMN nome VARCHAR(100) NOT NULL AFTER id_curso;

ALTER TABLE escola_curso.notas
	ADD COLUMN atividade VARCHAR(100) NOT NULL AFTER id_nota,
    ADD COLUMN valor_nota DECIMAL(5,2) NOT NULL AFTER atividade; 