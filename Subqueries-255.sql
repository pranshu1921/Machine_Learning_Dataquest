## 1. Writing More Complex Queries ##

select Major, ShareWomen from recent_grads where ShareWomen > 0.5225502029537575;

## 2. Subqueries ##

select Major, Unemployment_rate from recent_grads where Unemployment_rate < (select avg(Unemployment_rate) from recent_grads);

## 3. Subquery in SELECT ##

SELECT CAST(COUNT(*) as FLOAT)/(SELECT COUNT(*)
                                  FROM recent_grads
                               ) AS proportion_abv_avg
  FROM recent_grads
 WHERE ShareWomen > (SELECT AVG(ShareWomen)
                       FROM recent_grads
                    );

## 4. The IN Operator ##

select Major_category, Major from recent_grads where Major_category in ("Business","Humanities & Liberal Arts", "Education");

## 5. Returning Multiple Results in Subqueries ##

select Major_category, Major from recent_grads where Major_category in(select Major_category from recent_grads group by Major_category order by sum(Total) desc limit 3);

## 6. Building Complex Subqueries ##

select avg(cast(Sample_size as float) / Total) as avg_ratio from recent_grads;

## 7. Practice Integrating A Subquery With The Outer Query ##

select Major, Major_category, cast(Sample_size as float)/Total as ratio from recent_grads where ratio > (select avg(cast(Sample_size as float) / Total) as avg_ratio from recent_grads);