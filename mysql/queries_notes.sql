-- INSERT

-- INSERT INTO table_name (column_name1, column_name2) 
-- VALUES('column1_value', 'column2_value');

INSERT INTO users (first_name, last_name, email)
VALUES ('Sam','Rauch','me@me.com'), ('Sally','Bobberts','bob@bob.com');

INSERT INTO licenses (state, expiration, user_id)
VALUES ("OR","2023-10-05", 3);

INSERT INTO licenses (state, expiration, user_id)
VALUES ("OR","2023-10-05", 30); -- cannot do, user doesn't exist

INSERT INTO dmvs (location)
VALUES ('Gresham');

INSERT INTO users_visit_dmvs (dmv_id, user_id)
VALUES ('1','1');
-- SELECT
-- SELECT columns_we_want_to_grab FROM table_to_grab_them_from WHERE condition;

SELECT * FROM users;

SELECT first_name 
FROM users 
WHERE id > 2;

sElEct first_name 
FrOm users 
WhErE id > 2;

SELECT * FROM users WHERE first_name LIKE "S%";

SELECT first_name, last_name, CONCAT_WS(" ", first_name, last_name) AS full_name FROM users;

SELECT email as log_info FROM users;
SELECT * from users;

-- UPDATE

-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition; THE WHERE CONDITION IS VERY IMPORTANT FOR AN UPDATE (use the primary key)
SET SQL_SAFE_UPDATES = 0;

UPDATE users SET first_name = 'CoolGuy', last_name = 'TheBest' WHERE id = 20;

-- DELETE

-- DELETE FROM table_name WHERE condition; <--- use a where clause when deleting!!!
DELETE FROM users;
