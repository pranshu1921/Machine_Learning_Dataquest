## 3. Your First Query ##

select * from recent_grads;



## 4. Understanding Your First Query ##

select * from recent_grads;


## 6. The LIMIT Clause ##

select * from recent_grads limit 5;

## 7. Selecting Specific Columns ##

select Major, ShareWomen from recent_grads;

## 8. Filtering Rows Using WHERE ##

select Major, ShareWomen from recent_grads where ShareWomen < 0.5;

## 9. Expressing Multiple Filter Criteria Using 'AND' ##

select Major, Major_category, Median, ShareWomen from recent_grads where ShareWomen > 0.5 and Median > 50000;

## 10. Returning One of Several Conditions With OR ##

select Major, Median, Unemployed from recent_grads where Median >= 10000 or Men > Women limit 20;

## 11. Grouping Operators with Parentheses ##

SELECT Major, Major_category, ShareWomen, Unemployment_rate
  FROM recent_grads
 WHERE (Major_category = 'Engineering') 
   AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051);
   

## 12. Ordering Results Using ORDER BY ##

select Major, ShareWomen, Unemployment_rate from recent_grads where ShareWomen > 0.3 and Unemployment_rate < .1 order by ShareWomen desc;

## 13. Practice Writing a Query ##

select Major_category, Major, Unemployment_rate from recent_grads where Major_category in('Engineering', 'Physical Sciences') order by Unemployment_rate;