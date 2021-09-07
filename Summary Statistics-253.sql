## 2. A Simple Question ##

select MIN(Unemployment_rate) from recent_grads;

## 3. Aggregate Functions ##

select SUM(Total) from recent_grads;

## 4. Order of Execution ##

select COUNT(Major) from recent_grads where MEN > WOMEN;

## 5. Missing Values ##

select COUNT(*), COUNT(Unemployment_rate) from recent_grads;

## 6. Combining Multiple Aggregation Functions ##

select AVG(Total), MIN(Men), MAX(Women) from recent_grads;

## 7. Customizing the Results ##

select COUNT(*) as 'Number of Majors', MAX(Unemployment_rate) as 'Highest Unemployment Rate' from recent_grads;

## 8. Counting Unique Values ##

SELECT COUNT(DISTINCT Major ) unique_majors,
       COUNT(DISTINCT Major_category) unique_major_categories,
       COUNT(DISTINCT Major_code) unique_major_codes
  FROM recent_grads;

## 10. String Functions and Operations ##

select 'Major: ' || LOWER(Major) as Major, Total, Men, Women, Unemployment_rate, LENGTH(Major) as Length_of_name from recent_grads order by Unemployment_rate DESC;

## 11. Performing Arithmetic in SQL ##

select Major, Major_category, (P75th - P25th) quartile_spread from recent_grads order by quartile_spread limit 20;