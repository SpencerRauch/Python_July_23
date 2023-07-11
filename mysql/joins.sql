-- JOINS

-- SELECT * FROM table_one JOIN table_to_join ON fk = pk; 

SELECT CONCAT_WS(" ", users.first_name, users.last_name) AS tweeter, tweets.* 
FROM users 
JOIN tweets ON tweets.user_id = users.id ;
-- WHERE users.id = 1;

SELECT first_name, COUNT(tweets.id) as tweet_count FROM users 
JOIN tweets ON tweets.user_id = users.id GROUP BY users.id;

SELECT * FROM users 
JOIN faves ON users.id = faves.user_id
JOIN tweets ON faves.tweet_id = tweets.id; 

-- LEFT JOIN will get us all records from the table on the LEFT side of the join
-- whether or not there is matching data on the right side

-- an INNER join, will not (our regular joins are inner joins)
SELECT * FROM users LEFT JOIN tweets ON users.id = user_id;
SELECT * FROM users;
