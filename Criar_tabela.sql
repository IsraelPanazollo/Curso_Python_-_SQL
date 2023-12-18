# Criar tabela de alunos, curso e notas

CREATE TABLE escola_curso.alunos (
  id_aluno INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_aluno)
);

CREATE TABLE escola_curso.curso (
  id_curso INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_curso)
);

CREATE TABLE escola_curso.notas (
  id_nota INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id_nota)
);
