'https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/
https://www.w3schools.com/sql/


Database Level'

CREATE DATABASE database_name;
	creates an empty database.

DROP DATABASE database_name;
	deletes a database and all data/tables in it (perminant).

CREATE TABLE table_name (
	column1 datatype,
	column2 datatype,
	... );
	creates a table in the database with the given column names and data type requirements.

CREATE TABLE new_table_name AS
	SELECT column1, column2....
	FROM existing_table_name
	WHERE ...;
	creates a new table from data in an existing table based on some logical rule(s).

CREATE TABLE new_table (
	column1 datatype constraint,
	column2 datatype constraint,
	...);
	constraint options: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT, INDEX
	constraints can be at the table or column level.

DROP TABLE table_name;
	perminantly deletes table and any data in it.

TRUNCATE TABLE table_name;
	deletes all data in the table but not the table itself.

ALTER TABLE table_name ADD column_name datatype;
	adds a column to the table.

ALTER TABLE table_name DROP COLUMN column_name;
	deletes the column from the table.

ALTER TABLE table_name ALTER COLUMN column_name datatype;
	sql server/ms access: changes columns datatype.

ALTER TABLE table_name MODIFY COLUMN column_name datatype;
	my sql/oracle(prior 10g): changes columns datatype.

ALTER TABLE table_name MODIFY column_name datatype;
	oracle(10g and after): changes columns datatype.


'Table or Report Level'

SELECT * FROM TableName;
	returns all data from all columns in the table

SELECT column1, column2... FROM TableName;
	returns all data from the columns listed in the table

SELECT DISTINCT column1, column2... FROM TableName;
	returns only the unique records (one for each that is repeated). Unique based on all values (all columns) being returned for a given row.

SELECT COUNT(DISTINCT column1) FROM TableName;
	returns the number of distinct values in the column.

SELECT column1, column2... FROM TableName
	WHERE condition;
	where limits the comand to only data points that meet the conditional statement.
	Conditionals: =, <>, <, >, <=, >=, BETWEEN, LIKE, IN

...WHERE condition AND condition;
	requires both conditionals to be met.

...WHERE condition OR condition;
	requires one conditional to be met.

...WHERE NOT condition;
	requires the conditional is not met.

SELECT * FROM TableName
	ORDER BY  column1, column2...ASC;
	sorts the data returned in an ascending order.

SELECT * FROM TableName
	ORDER BY  column1, column2...DESC;
	sorts the data returned in a descending order.

INSERT INTO TableName (column1, column2...)
	VALUES (value1, value2...);
	insert a row into the table, mapping values to columns based on order each entered into query.

INSERT INTO TableName
	VALUES (value1, value2...);
	insert a row into the table, mapping values to columns based on order values entered into query and columns exist in database.

...IS NULL;
	any empty datapoint in the table.

...IS NOT NULL;
	any non-empty datapoint in the table.

UPDATE TableName
	SET column1 = value1, column2 = value2...
	WHERE condition;
	modifies existing records that meet the condition with the values in the 'set' statement.

DELETE FROM TableName
	WHERE condition;
	deletes all records in the table that meets the condition.

DELETE * FROM TableName;
	deletes all records from the table.

SELECT TOP number FROM TableName;
	SQL Server/MS Access: returns the top rows from the table.

SELECT column_name(s) FROM TableName
	WHERE condition(s)
	 LIMIT number;
	mySQL: returns the top rows from the table.

SELECT * FROM TableName
	WHERE ROWNUM <= number;
	Oracle: returns the top rows from the table.

SELECT MIN(column_name) FROM TableName
	WHERE condition;
	returns the smallest value from the column where the record(s) pass the conditional.

SELECT MAX(column_name) FROM TableName
	WHERE condition;
	returns the largest value of the selected column where the record meets the conditional.

SELECT COUNT(column_name) FROM TableName;
	returns the number of records in the column.

SELECT AVG(column_name) FROM TableName;
	returns the average of the numeric values in the column.

SELECT SUM(column_name) FROM TableName;
	returns the sum of the numeric values in the column.

SELECT * FROM TableName
	WHERE column_name LIKE pattern;
	Patterns: % - represents n characters
			   _ - represents a single character
	Example: 'a%', '%a', '_or%'

SELECT column_name(s) FROM TableName
	WHERE column_name IN (value1, value2...);
	returns records where one of the values exists in the column.

SELECT * FROM TableName
	WHERE column_name IN(SELECT column2_name FROM table2_name);
	returns records where the first column has a value that exists in the second column. Allows comparison between two tables.

...WHERE...BETWEEN...AND...;
	returns where value is between, inclusively, the two values given

SELECT column_name AS alias_name FROM TableName;
	renames the column name for the duration of the query.

SELECT column_name FROM TableName AS alias_name;
	renames the table name for the duration of the query.

SELECT t1.c1, t1.c2, t2.c1, t2.c2... FROM t1
	JOIN t2 ON t1.c1 = t2.c3;
	joins together two tables. Types of joins:
	(INNER) JOIN: returns records that match on both sides only
	LEFT (OUTER) JOIN: returns all values from the left table and the matched records from the right table.
	RIGHT (OUTER) JOIN: returns all values from the right table and the matched records from the left table.
	FULL (OUTER) JOIN: returns all records from both tables.
	code example:
		SELECT Order.orderID, Customers.customerName, Shippers.shipperName FROM ((Orders
			INNER JOIN Customers ON Orders.customerID = Customers.ID)
			INNER JOIN Shippers ON Orders.shipperID = Shippers.ID);

SELECT ... FROM  t1 UNION SELECT ... FROM t2;
	combines the result-set for 2 or more tables. Only returns district values.

SELECT ... FROM t1 UNION ALL SELECT ... FROM t2;
	combines the result-set for 2 or more tables. Allows duplicate values to be returned.

SELECT * FROM TableName
	WHERE condition
	GROUP BY column_name(s)
	ORDER BY column_name(s);
	usually used with aggrogate functions (like COUNT, MAX...). Group By groups the results by data in the given column(s).
