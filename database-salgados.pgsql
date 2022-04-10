SELECT * FROM salgados;


SELECT
  salgados.id AS salgados_id,
  salgados.nome AS salgados_nome,
  salgados.preco AS salgados_preco
FROM salgados;


-- Seleção com filtro por Primary Key
SELECT
  salgados.id AS salgados_id,
  salgados.nome AS salgados_nome,
  salgados.preco AS salgados_preco
FROM salgados
WHERE salgados.id = 1;



-- Seleções com SQLAlchemy .first()
SELECT
  salgados.id AS salgados_id,
  salgados.nome AS salgados_nome,
  salgados.preco AS salgados_preco
FROM salgados
  LIMIT 1

-- .filter() / .filter_by()
SELECT
  salgados.id AS salgados_id,
  salgados.nome AS salgados_nome,
  salgados.preco AS salgados_preco
FROM salgados
WHERE salgados.nome = 'Coxinha'
  LIMIT 1


-- .filter_by()
SELECT *
  FROM salgados
WHERE nome = 'Coxinha';

