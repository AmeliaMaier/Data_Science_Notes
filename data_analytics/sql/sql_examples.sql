/*
Using the WHERE clause, write a new SELECT statement that returns all rows
where Campaign_ID is equal to FB
We don't need the campaign id in the result since they are all the same,
 so only include the other two columns.
*/

SELECT userid, dt FROM users
  WHERE campaign_id = 'FB'
  LIMIT 5;

/*
Write a query to get the count of just the users who came from Facebook.
*/

SELECT COUNT(userid) FROM users
  WHERE campaign_id = 'FB';

/*
Now, count the number of users coming from each service. Here you'll have to group by the column you're selecting with a GROUP BY clause.

Try running the query without a group by. Postgres will tell you what to put in your group by clause!
*/

SELECT campaign_id, COUNT(userid) FROM users
  GROUP BY campaign_id;

/*
Use COUNT (DISTINCT columnname) to get the number of unique dates that appear in the users table.
*/

SELECT COUNT(DISTINCT dt) FROM users;

/*
There's also MAX and MIN functions, which do what you might expect. Write a query to get the first and last registration date from the users table.
*/

SELECT MIN(DISTINCT dt) AS first_reg,
        MAX(DISTINCT dt) AS last_reg
  FROM users;

/*
Calculate the mean price for a meal (from the meals table). You can use the AVG function. Your result should look like this:
*/

SELECT AVG(price) FROM meals;

/*
Now get the average price, the min price and the max price for each meal type. Don't forget the group by statement!
*/

SELECT type, AVG(price),MIN(price), MAX(price)
  FROM meals
  GROUP BY type;

/*It's often helpful for us to give our own names to columns. We can always rename columns that we select by doing AVG(price) AS avg_price. This is called aliasing. Alias all the above columns so that your table looks like this:
*/

SELECT type,
      AVG(price) AS avg_price,
      MIN(price) AS min_price,
      MAX(price) AS max_price
  FROM meals
  GROUP BY type;

  /*
  Maybe you only want to consider the meals which occur in the first quarter (January through March). Use date_part to get the month like this: date_part('month', dt). Add a WHERE clause to the above query to consider only meals in the first quarter of 2013 (month<=3 and year=2013).
  */

SELECT type,
        AVG(price) AS avg_price,
        MIN(price) AS min_price,
        MAX(price) AS max_price
  FROM meals
  WHERE
    date_part('month', dt) <= 3
    AND date_part('year', dt) = 2013
  GROUP BY type;

/*
There are also scenarios where you'd want to group by two columns. Modify the above query so that we get the aggregate values for each month and type. You'll need to add the month to both the select statement and the group by statement.

It'll be helpful to alias the month column and give it a name like month so you don't have to call the date_time function again in the GROUP BY clause.

Your result should look like this:
*/

SELECT type,
        date_part('month', dt) AS month,
        AVG(price) AS avg_price,
        MIN(price) AS min_price,
        MAX(price) AS max_price
  FROM meals
  GROUP BY type, month;

/*
From the events table, write a query that gets the total number of buys, likes and shares for each meal id. Extra: To avoid having to do this as three separate queries you can do the count of the number of buys like this: SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END).
*/

SELECT meal_id,
      SUM(CASE WHEN event='bought' THEN 1 ELSE 0 END) as bought,
      SUM(CASE WHEN event='like' THEN 1 ELSE 0 END) as likes,
      SUM(CASE WHEN event='shares' THEN 1 ELSE 0 END) as shares
      FROM events
  GROUP BY meal_id
  ORDER BY meal_id;

  /*
  Let's start with a query which gets the average price for each type. It will be helpful to alias the average price column as 'avg_price'.
  To make it easier to read, sort the results by the type column. You can do this with an ORDER BY clause.
Now return the same table again, except this time order by the price in descending order (add the DESC keyword).
  */

SELECT type,
        date_part('month', dt) AS month,
        AVG(price) AS avg_price,
        MIN(price) AS min_price,
        MAX(price) AS max_price
  FROM meals
  GROUP BY type, month
  ORDER BY type DESC;

  /*
  Sometimes we want to sort by two columns. Write a query to get all the meals, but sort by the type and then by the price. You should have an order by clause that looks something like this: ORDER BY col1, col2.
  */
  SELECT type,
          date_part('month', dt) AS month,
          AVG(price) AS avg_price,
          MIN(price) AS min_price,
          MAX(price) AS max_price
    FROM meals
    GROUP BY type, month
    ORDER BY type DESC, avg_price;

/*
Write a query to get one table that joins the events table with the users table
(on userid) to create the following table.
*/

SELECT users.userid,
        users.campaign_id,
        events.meal_id,
        meals.type,
        meals.price
  FROM ((users
  JOIN events
  ON users.userid = events.userid)
  JOIN meals
  ON events.meal_id = meals.meal_id)
  WHERE events.event = 'bought';

  /*
  Write a query to get how many of each type of meal were bought.

You should again be able to do this without a where clause!
*/
