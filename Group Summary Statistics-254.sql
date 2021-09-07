## 2. If/Then in SQL ##

select CASE
       WHEN Sample_size < 200 THEN 'Small'
       WHEN Sample_size < 1000 THEN 'Medium'
       ELSE 'Large'
       END AS Sample_category
   FROM recent_grads;       

## 3. Dissecting CASE ##

SELECT Major, Sample_size,
       CASE
       WHEN Sample_size < 200 THEN 'Small'
       WHEN Sample_size < 1000 THEN 'Medium'
       ELSE 'Large'
       END AS Sample_category
  FROM recent_grads;

## 4. Calculating Group-Level Summary Statistics ##

select Major_category, SUM(Total) as Total_graduates from recent_grads group by Major_category;


## 5. GROUP BY Visual Breakdown ##

select Major_category, avg(ShareWomen) as Average_women from recent_grads group by Major_category;

## 6. Multiple Summary Statistics by Group ##

select Major_category, sum(Women) as Total_women, avg(ShareWomen) as Mean_women, sum(Total)*avg(ShareWomen) as Estimate_women from recent_grads group by Major_category;

## 7. Multiple Group Columns ##

select Major_category, Sample_category, avg(ShareWomen) as Mean_women, sum(Total) as Total_graduates from new_grads group by Major_category, Sample_category;

## 8. Querying Virtual Columns With the HAVING Statement ##

select Major_category, avg(low_wage_jobs) / avg(Total) as Share_low_wage from new_grads group by Major_category having Share_low_wage > .1;

## 10. Rounding Results With the ROUND() Function ##

select round(ShareWomen, 4) as Rounded_women, Major_category from new_grads limit 10;

## 11. Nesting functions ##

select Major_category, round(avg(College_jobs) / avg(Total), 3) as Share_degree_jobs from new_grads group by Major_category having Share_degree_jobs < .3;

## 12. Casting ##

select Major_category, cast(sum(Women) as FLoat) / cast(sum(Total) as Float ) as SW from new_grads group by Major_category order by SW;