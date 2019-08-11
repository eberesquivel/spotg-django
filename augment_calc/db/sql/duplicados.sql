/* Esta consulta se encarga de encontrar los valores repetidos */
SELECT id, attribute_id, count(attribute_id) as ct FROM augment_skill GROUP BY attribute_id HAVING ct > 1;