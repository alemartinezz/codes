# Talk to the Zoo Database

Just below on this page is a text editor window, containing an SQL query about gorillas. This is just here as a demonstration of how we'll be doing SQL exercises in this course, and how query results will show up. Don't worry about the details of this query for now; just run it (with the Test Run button) and see what it does.

At the top of the file are a few lines that start with two dashes. This is the SQL way to write comments. A comment in SQL starts with -- and continues to the end of the line — pretty much the same as Python or Ruby comments that start with #.

When you run a query in this course, you'll see the results of the query below the editor. Give it a try now:

```sql
select name, birthdate from animals where species = 'gorilla';
```
+---------+------------+
   | name | birthdate |
+=========+============+ 
| Max | 2001-04-23 | 
| Dave | 1988-09-29 | 
| Becky | 1979-07-04 | 
| Liz | 1998-06-12 | 
| George | 2011-01-09 | 
| George | 1998-05-18 | 
| Wendell | 1982-09-24 | 
| Bjorn | 2000-03-07 |
| Kristen | 1990-04-25 |
+---------+------------+

```sql
select name, birthdate from animals where species = 'gorilla';
```
+---------+------------+ 
| name | birthdate | 
+=========+============+
| Max | 2001-04-23 |
| Dave | 1988-09-29 | 
| Becky | 1979-07-04 |
| Liz | 1998-06-12 |
| George | 2011-01-09 | 
| George | 1998-05-18 | 
| Wendell | 1982-09-24 |
| Bjorn | 2000-03-07 |
| Kristen | 1990-04-25 |
 +---------+------------+