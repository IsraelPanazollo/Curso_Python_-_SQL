# Adicionar tabela e chaves_estrangeiras

CREATE TABLE escola_curso.alunos_cursos(
  id_aluno_curso INT NOT NULL AUTO_INCREMENT,
  id_aluno INT NOT NULL,
  id_curso INT NOT NULL,
  id_nota INT NOT NULL,
  PRIMARY KEY (id_aluno_curso)
);
ALTER TABLE escola_curso.alunos_cursos
ADD INDEX fk_id_aluno_idx (id_aluno ASC) VISIBLE,
ADD INDEX fk_id_curso_idx (id_curso ASC) VISIBLE;

ALTER TABLE escola_curso.alunos_cursos
ADD CONSTRAINT fk_id_aluno
	FOREIGN KEY(id_aluno)
    REFERENCES escola_curso.alunos (id_aluno)
	ON DELETE NO ACTION
    ON UPDATE NO ACTION,
ADD CONSTRAINT fk_id_curso
	FOREIGN KEY(id_curso)
    REFERENCES escola_curso.cursos (id_curso)
	ON DELETE NO ACTION
    ON UPDATE NO ACTION
;

ALTER TABLE escola_curso.notas 
ADD COLUMN id_aluno_curso INT NOT NULL AFTER valor_nota,
ADD INDEX fk_id_aluno_curso_idx (id_aluno_curso ASC) VISIBLE;
;
ALTER TABLE escola_curso.notas 
ADD CONSTRAINT fk_id_aluno_curso
  FOREIGN KEY (id_aluno_curso)
  REFERENCES escola_curso.alunos_cursos(id_aluno_curso)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
