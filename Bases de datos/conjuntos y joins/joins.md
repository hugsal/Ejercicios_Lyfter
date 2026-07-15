## Joins

| Tipo | Descripcion | Sentencia |
| --- | --- | --- |
| SELECT | Selecciona las filas que cumplen con una condición. | SELECT * FROM tabla1 WHERE columna = valor; |
| ORDER BY | Ordena los resultados de un query. | SELECT * FROM tabla1 ORDER BY columna ASC; |
| LIMIT | Limita el número de filas devueltas. | SELECT * FROM tabla1 LIMIT 10; |
| GROUP BY | Agrupa las filas que tienen los mismos valores en una o más columnas. | SELECT * FROM tabla1 GROUP BY columna; |
| INNER JOIN | Devuelve las filas que tienen valores coincidentes en ambas tablas. | SELECT * FROM tabla1 INNER JOIN tabla2 ON tabla1.columna = tabla2.columna; |
| LEFT JOIN | Devuelve todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha. | SELECT * FROM tabla1 LEFT JOIN tabla2 ON tabla1.columna = tabla2.columna; |
| RIGHT JOIN | Devuelve todas las filas de la tabla derecha y las filas coincidentes de la tabla izquierda. | SELECT * FROM tabla1 RIGHT JOIN tabla2 ON tabla1.columna = tabla2.columna; |
| FULL OUTER JOIN | Devuelve todas las filas de ambas tablas. | SELECT * FROM tabla1 FULL OUTER JOIN tabla2 ON tabla1.columna = tabla2.columna; |