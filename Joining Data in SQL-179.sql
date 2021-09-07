## 1. Introducing Joins ##

select * from facts inner join cities on facts.id = cities.facts_id limit 10;

## 2. Understanding Inner Joins ##

select b.*, a.name as country_name from facts a inner join cities b on a.id = b.facts_id limit 5;

## 3. Practicing Inner Joins ##

select b.name as country, a.name as capital_city from cities a inner join facts b on b.id= a.facts_id where a.capital = 1 

## 4. Left Joins ##

select a.name as country, a.population from facts a left join cities b on a.id = b.facts_id where b.name is null;

## 6. Finding the Most Populous Capital Cities ##

select b.name capital_city, a.name country, b.population
from facts a inner join cities b on a.id = b.facts_id
where b.capital = 1
order by 3 desc
limit 10;

## 7. Combining Joins with Subqueries ##

select c.name capital_city, f.name country, c.population population from facts f inner join (select * from cities where capital = 1 and population > 10000000) c on c.facts_id = f.id order by c.population desc;

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT
    f.name country,
    c.urban_pop,
    f.population total_pop,
    (c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN (
            SELECT
                facts_id,
                SUM(population) urban_pop
            FROM cities
            GROUP BY 1
           ) c ON c.facts_id = f.id
WHERE urban_pct > .5
ORDER BY 4 ASC;