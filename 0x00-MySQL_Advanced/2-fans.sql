-- script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
-- Import table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans

-- select columns
SELECT origin AS origin,
	SUM(fans) as nb_fans
       	FROM metal_bands
	GROUP BY origin HAVING COUNT(fans) > 1
	ORDER BY nb_fans DESC;
