## 2. Joining Three Tables ##

SELECT
    il.track_id,
    t.name track_name,
    mt.name track_type,
    il.unit_price,
    il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
WHERE il.invoice_id = 4;

## 3. Joining More Than Three Tables ##

select il.track_id, t.name track_name, ar.name artist_name, mt.name track_type, il.unit_price, il.quantity from invoice_line il
inner join track t on t.track_id = il.track_id
inner join media_type mt on mt.media_type_id = t.media_type_id
inner join album al on al.album_id = t.album_id
inner join artist ar on ar.artist_id= al.artist_id
where il.invoice_id = 4; 

## 4. Combining Multiple Joins with Subqueries ##

select ta.album_title album,
       ta.artist_name artist,
       count(*) tracks_purchased
from invoice_line il
inner join (
            select
                t.track_id,
                al.title album_title,
                ar.name artist_name
            from track t
            inner join album al on al.album_id = t.album_id
            inner join artist ar on ar.artist_id = al.artist_id
            ) ta
            on ta.track_id = il.track_id
group by 1, 2
order by 3 desc limit 5;

          

## 5. Recursive Joins ##

select e1.first_name ||" " ||  e1.last_name as employee_name,
e1.title employee_title, e2.first_name || " " || e2.last_name as supervisor_name, e2.title supervisor_title from employee e1 left join employee e2 on e1.reports_to = e2.employee_id
order by 1;

## 6. Pattern Matching Using Like ##

select first_name, last_name, phone from customer where first_name like '%Belle%';

## 7. Revisiting CASE ##

select c.first_name || ' ' || c.last_name customer_name,
count(i.invoice_id) number_of_purchases,
sum(i.total) total_spent,
case
    when sum(i.total) < 40 then 'small spender'
    when sum(i.total) > 100 then 'big spender'
    else 'regular'
    end
    as customer_category
from invoice i
inner join customer c on i.customer_id = c.customer_id
group by 1 order by 1;