# SQL Interview Handbook
### The Ultimate Prep Guide for Developers (Mid-Senior Level ~4 Years Experience)

---

## Table of Contents
1. [SQL Basics](#sql-basics)
2. [CRUD Operations](#crud-operations)
3. [Querying Data](#querying-data)
4. [Filtering](#filtering)
5. [Aggregate Functions & GROUP BY / HAVING](#aggregate-functions--group-by--having)
6. [CASE Statement](#case-statement)
7. [Built-in Functions (String, Date, Math)](#built-in-functions-string-date-math)
8. [Joins](#joins)
9. [Set Operators](#set-operators)
10. [Subqueries & EXISTS](#subqueries--exists)
11. [CTEs (Common Table Expressions)](#ctes-common-table-expressions)
12. [Views & Materialized Views](#views--materialized-views)
13. [Indexes & Query Tuning](#indexes--query-tuning)
14. [Normalization](#normalization)
15. [ACID & Transactions](#acid--transactions)
16. [Locks & Concurrency](#locks--concurrency)
17. [Window Functions](#window-functions)
18. [Programmability (Stored Procedures, Functions, Triggers)](#programmability-stored-procedures-functions-triggers)
19. [Performance Optimization](#performance-optimization)
20. [Advanced SQL Features](#advanced-sql-features)
21. [SQL Scenario Questions (50 Problems with Approaches & Complexities)](#sql-scenario-questions)
22. [HR + SQL Combined Questions](#hr--sql-combined-questions)
23. [SQL Execution Order](#sql-execution-order)
24. [Cheat Sheet & Revision Guide](#cheat-sheet--revision-guide)

---

## SQL Basics

### What is SQL
#### 1. Definition
SQL (Structured Query Language) is the standard language used to communicate with, manage, and manipulate relational databases.

#### 2. Why do we use it?
To perform database operations like querying data, inserting records, updating details, deleting rows, and designing schema objects.

#### 3. Syntax
```sql
SELECT column1, column2 FROM table_name;
```

#### 4. Simple Example
**Students**
| id | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | 90 |

#### 5. Query
```sql
SELECT name FROM Students;
```

#### 6. Output
| name |
|---|
| Amit |
| Neha |

#### 7. Interview Explanation
Answer: "SQL is the declarative language used for relational databases. Unlike imperative languages where we define *how* to get data, in SQL we define *what* data we need, leaving the database engine's optimizer to decide the most efficient path."

#### 8. Remember Trick
*SQL is the language; DB is the filing cabinet.*

#### 9. Common Mistakes
Pronouncing it strictly as "S-Q-L" or "Sequel" as if one is wrong; both are acceptable, though "Sequel" is common in enterprise environments.

#### 10. Interview Questions
- What is the difference between DDL, DML, DCL, and TCL?
- Is SQL case-sensitive?
- What are the main limitations of SQL?

#### 11. Interview Answers
- DDL (Data Definition Language) defines schema (`CREATE`, `ALTER`, `DROP`). DML (Data Manipulation Language) queries/modifies data (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). DCL (Data Control Language) manages privileges (`GRANT`, `REVOKE`). TCL (Transaction Control Language) manages transaction states (`COMMIT`, `ROLLBACK`).
- SQL keywords (like `SELECT`, `FROM`) are case-insensitive, but data inside tables can be case-sensitive depending on the database's collation configuration.
- SQL struggles with deeply hierarchical or unstructured data compared to NoSQL engines.

#### 12. Real-world Use Case
Backend services query databases using SQL to authenticate users, fetch catalog items, and record transactions.

---

### SQL vs MySQL
#### 1. Definition
SQL is a query language, while MySQL is a Relational Database Management System (RDBMS) that uses SQL.

#### 2. Why do we use it?
We write SQL code to interact with RDBMS engines like MySQL, PostgreSQL, or SQL Server.

#### 3. Syntax
N/A (Conceptual)

#### 4. Simple Example
Concept comparison:
- SQL = English (Language)
- MySQL = USA (A country that speaks English)

#### 5. Query
N/A

#### 6. Output
N/A

#### 7. Interview Explanation
"SQL is the standard language specification. MySQL is a concrete database engine software product that implements that SQL standard along with its own custom extensions and optimizations."

#### 8. Remember Trick
*SQL is the recipe; MySQL is the kitchen.*

#### 9. Common Mistakes
Confusing SQL dialects (T-SQL, PL/SQL) with the core SQL standard.

#### 10. Interview Questions
- Can you run SQL queries without an RDBMS?
- Name three competitors of MySQL.

#### 11. Interview Answers
- No, SQL queries need an engine parser (RDBMS or query engine) to execute.
- PostgreSQL, Oracle Database, Microsoft SQL Server.

#### 12. Real-world Use Case
Companies choose MySQL for web hosting applications, writing SQL queries to interact with it.

---

### Database, Table, Row, Column
#### 1. Definition
- **Database**: A structured collection of tables.
- **Table**: A grid of rows and columns.
- **Row (Tuple)**: A single record.
- **Column (Attribute)**: A specific data field.

#### 2. Why do we use it?
To store data in a highly structured, scalable, and queryable format.

#### 3. Syntax
```sql
CREATE DATABASE database_name;
CREATE TABLE table_name (
    column_name data_type
);
```

#### 4. Simple Example
**Employees**
| id | name | department | salary |
|---|---|---|---|
| 1 | Amit | HR | 50000 |

#### 5. Query
```sql
SELECT department, salary FROM Employees WHERE id = 1;
```

#### 6. Output
| department | salary |
|---|---|
| HR | 50000 |

#### 7. Interview Explanation
"A database holds tables. A table contains columns which define the structure (schema), and rows which hold the actual record instances."

#### 8. Remember Trick
*Database is the Excel file; Table is the sheet; Row is the line; Column is the column header.*

#### 9. Common Mistakes
Thinking a database is just one large table.

#### 10. Interview Questions
- What is schema?
- What are the major differences between rows and columns in relational modeling?

#### 11. Interview Answers
- Schema is the structural design of database tables, columns, relations, and constraints.
- Columns represent entity attributes (fixed count, schema-level), while rows represent entity instances (dynamic count, data-level).

#### 12. Real-world Use Case
An e-commerce app has a database containing tables for `Users`, `Products`, and `Orders`.

---

### Primary Key
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
A column (or combination of columns) that uniquely identifies each row in a table. It cannot contain `NULL` values.

#### 2. Why do we use it?
To guarantee record uniqueness, enable fast lookups, and allow relationships via foreign keys.

#### 3. Syntax
```sql
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

#### 4. Simple Example
**Students**
| id (PK) | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | 90 |

#### 5. Query
```sql
SELECT * FROM Students WHERE id = 2;
```

#### 6. Output
| id | name | marks |
|---|---|---|
| 2 | Neha | 90 |

#### 7. Interview Explanation
"A Primary Key enforces entity integrity. It imposes a `UNIQUE` and `NOT NULL` constraint. Under the hood, databases automatically build a clustered index on the primary key to enable highly efficient query lookups."

#### 8. Remember Trick
*PK = Unique + Not Null identity card.*

#### 9. Common Mistakes
Believing a table can have multiple Primary Keys (it can only have one, though that primary key can consist of multiple columns).

#### 10. Interview Questions
- Can a Primary Key contain NULL?
- What is the difference between a Primary Key and a Unique Key?

#### 11. Interview Answers
- No, primary keys cannot contain NULL.
- A table can have only one Primary Key (does not allow NULLs), but can have multiple Unique Keys (which allow NULL values in most engines).

#### 12. Real-world Use Case
A user's unique `user_id` is the primary key in a customer database.

---

### Foreign Key
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
A column in one table that links to a Primary Key (or Unique Key) in another table, enforcing referential integrity.

#### 2. Why do we use it?
To establish parent-child relationships between tables and prevent orphaned records.

#### 3. Syntax
```sql
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
```

#### 4. Simple Example
**Users (Parent)**
| id (PK) | name |
|---|---|
| 1 | Amit |

**Orders (Child)**
| order_id (PK) | user_id (FK) | item |
|---|---|---|
| 101 | 1 | Laptop |

#### 5. Query
```sql
SELECT Users.name, Orders.item 
FROM Users 
JOIN Orders ON Users.id = Orders.user_id;
```

#### 6. Output
| name | item |
|---|---|
| Amit | Laptop |

#### 7. Interview Explanation
"A Foreign Key establishes relationships between entities. It ensures referential integrity: you cannot insert a row in the child table with a foreign key value that does not exist in the parent table's primary key."

#### 8. Remember Trick
*FK is a pointer back to a parent PK.*

#### 9. Common Mistakes
Deleting parent records without configuring `ON DELETE CASCADE` or `ON DELETE SET NULL`, resulting in foreign key constraint violations.

#### 10. Interview Questions
- What are ON DELETE CASCADE and ON DELETE SET NULL?
- Can a Foreign Key reference a non-primary key column?

#### 11. Interview Answers
- `ON DELETE CASCADE` automatically deletes child rows when their parent row is deleted. `ON DELETE SET NULL` sets the child's foreign key column to NULL instead of deleting.
- Yes, as long as the referenced column is constrained by a `UNIQUE` index.

#### 12. Real-world Use Case
Linking order records to the specific customer record who bought them.

---

### Composite Key, Candidate Key, Alternate Key, Super Key
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
- **Super Key**: Any set of one or more columns that uniquely identifies a row.
- **Candidate Key**: A minimal Super Key (no redundant columns).
- **Composite Key**: A primary key made of two or more columns.
- **Alternate Key**: A Candidate Key that was not chosen as the Primary Key.

#### 2. Why do we use it?
To model complex business identities and choose the best primary key candidate.

#### 3. Syntax
```sql
CREATE TABLE OrderItems (
    order_id INT,
    item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, item_id) -- Composite Key
);
```

#### 4. Simple Example
**Enrollments**
| student_id (Composite PK part 1) | course_id (Composite PK part 2) | enrollment_date |
|---|---|---|
| 1 | 101 | 2026-08-01 |
| 1 | 102 | 2026-08-01 |

#### 5. Query
```sql
SELECT * FROM Enrollments WHERE student_id = 1 AND course_id = 101;
```

#### 6. Output
| student_id | course_id | enrollment_date |
|---|---|---|
| 1 | 101 | 2026-08-01 |

#### 7. Interview Explanation
"A **Super Key** is any attribute set identifying rows. A **Candidate Key** is a minimal Super Key. The DBA selects one Candidate Key as the **Primary Key**, leaving others as **Alternate Keys** (e.g. Employee ID vs Email). If a key contains multiple columns, it's a **Composite Key**."

#### 8. Remember Trick
*Super Key is a candidate with extra luggage; Candidate Key is traveling light.*

#### 9. Common Mistakes
Confusing Candidate Keys with Alternate Keys. (Candidate = Primary + Alternate).

#### 10. Interview Questions
- Can a Candidate Key accept NULL values?
- When should you use a Composite Key instead of a surrogate primary key (like auto-increment ID)?

#### 11. Interview Answers
- Yes, candidate keys can theoretically contain NULL (unless designated as PK), but they must remain unique.
- Composite keys are useful for join tables in many-to-many relationships to natively prevent duplicate pairs.

#### 12. Real-world Use Case
In a multi-tenant system, combining `tenant_id` and `user_id` as a composite primary key.

---

### Constraints (NULL, Default, Unique, Auto Increment)
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
Rules applied to table columns to enforce data integrity and restrict invalid inputs.

#### 2. Why do we use it?
To maintain clean, consistent data at the database layer rather than relying solely on application logic.

#### 3. Syntax
```sql
CREATE TABLE Employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    status VARCHAR(20) DEFAULT 'Active',
    salary INT NOT NULL
);
```

#### 4. Simple Example
**Employees**
| id | email | status | salary |
|---|---|---|---|
| 1 | amit@co.com | Active | 60000 |
| 2 | neha@co.com | Pending | 70000 |

#### 5. Query
```sql
INSERT INTO Employees (email, salary) VALUES ('raj@co.com', 80000);
SELECT * FROM Employees WHERE email = 'raj@co.com';
```

#### 6. Output
| id | email | status | salary |
|---|---|---|---|
| 3 | raj@co.com | Active | 80000 |

#### 7. Interview Explanation
"Constraints are declarative rules. `NOT NULL` prevents missing values, `UNIQUE` stops duplicates, `DEFAULT` fills in missing fields, and `AUTO_INCREMENT` (or `IDENTITY`) auto-generates sequential row numbers."

#### 8. Remember Trick
*Constraints are guardrails for data entry.*

#### 9. Common Mistakes
Confusing `NULL` with an empty string `''` or zero `0`. `NULL` is the complete absence of a value.

#### 10. Interview Questions
- Can you have multiple NULL values in a UNIQUE column?
- What is the difference between a CHECK constraint and a DEFAULT constraint?

#### 11. Interview Answers
- Yes, in most database engines (like MySQL, PostgreSQL), a `UNIQUE` constraint allows multiple `NULL` values because NULL is considered unknown, hence not equal to another NULL.
- A `DEFAULT` constraint provides a fallback value if none is supplied. A `CHECK` constraint evaluates a boolean expression (e.g. `salary > 0`) to validate incoming data.

#### 12. Real-world Use Case
Enforcing that account creation requires a unique email address and defaults the user account status to "registered".

---
---

## CRUD Operations

### CREATE, INSERT, UPDATE, DELETE, TRUNCATE, DROP, ALTER
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
The core operations used to define schemas and modify data inside databases.

#### 2. Why do we use it?
To create tables (`CREATE`), edit table definitions (`ALTER`), insert data (`INSERT`), update data (`UPDATE`), delete records (`DELETE`), wipe table contents quickly (`TRUNCATE`), and delete tables entirely (`DROP`).

#### 3. Syntax
```sql
CREATE TABLE Test (id INT);
INSERT INTO Test VALUES (1);
UPDATE Test SET id = 2 WHERE id = 1;
DELETE FROM Test WHERE id = 2;
TRUNCATE TABLE Test;
DROP TABLE Test;
```

#### 4. Simple Example
**Employees**
| id | name | salary |
|---|---|---|
| 1 | Amit | 50000 |

#### 5. Query
```sql
UPDATE Employees SET salary = 55000 WHERE id = 1;
SELECT * FROM Employees;
```

#### 6. Output
| id | name | salary |
|---|---|---|
| 1 | Amit | 55000 |

#### 7. Interview Explanation
"CRUD maps to DDL and DML. Create/Read/Update/Delete represent the lifecycle of application data. DDL commands (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`) manage the container structure; DML commands (`INSERT`, `SELECT`, `UPDATE`, `DELETE`) manage the data inside."

#### 8. Remember Trick
*DDL changes the box; DML changes the stuff inside the box.*

#### 9. Common Mistakes
Running `UPDATE` or `DELETE` without a `WHERE` clause, which alters or removes every record in the table.

#### 10. Interview Questions
- What is the difference between TRUNCATE and DELETE?
- Why is DROP a DDL operation while DELETE is DML?

#### 11. Interview Answers
- `DELETE` is a DML statement that removes rows one-by-one and records transactions in the log. `TRUNCATE` is a DDL statement that deallocates the table's data pages, making it faster but unable to filter with `WHERE`.
- `DROP` completely deletes the table structure from the database catalog. `DELETE` only modifies row-level data inside the structure.

#### 12. Real-world Use Case
Creating a fresh migration schema file using `CREATE` and `ALTER` statements to deploy database updates in production.

---

### DELETE vs TRUNCATE vs DROP
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
Three distinct commands used to remove data or structure, varying in execution speed, logging, and rollback capabilities.

#### 2. Why do we use it?
- `DELETE`: Remove specific rows selectively.
- `TRUNCATE`: Instantly empty a table's records.
- `DROP`: Completely erase the table and its schema definition.

#### 3. Syntax
```sql
DELETE FROM table_name WHERE condition;
TRUNCATE TABLE table_name;
DROP TABLE table_name;
```

#### 4. Simple Example
Let's analyze their impact:
- **DELETE**: Leaves table empty, keeps IDs sequence, can be rolled back.
- **TRUNCATE**: Leaves table empty, resets identity sequence, faster, cannot be filtered.
- **DROP**: Table no longer exists in database.

#### 5. Query
```sql
-- Safe conditional removal
DELETE FROM Employees WHERE salary < 30000;
```

#### 6. Output
Rows meeting the condition are removed. The remaining table structure and data persist.

#### 7. Interview Explanation
"Use `DELETE` when you need conditional deletion (`WHERE` clause) and need transaction logs to trigger rollbacks or row-level triggers. Use `TRUNCATE` for rapid cleanup of staging tables, as it bypasses row-level locks and logging. Use `DROP` to wipe the table and its metadata permanently."

#### 8. Remember Trick
*DELETE cuts branches; TRUNCATE cuts the trunk; DROP digs up the roots.*

#### 9. Common Mistakes
Trying to run `TRUNCATE TABLE ... WHERE ...`. Truncate does not accept conditional filters.

#### 10. Comparison Table

| Feature | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| **Command Type** | DML | DDL | DDL |
| **WHERE Clause** | Yes | No | No |
| **Speed** | Slow (row-by-row) | Fast (deallocates pages) | Very Fast |
| **Rollback Support** | Yes (in transaction) | Yes (under TCL in some DBs) | No |
| **Triggers** | Fires row triggers | Does not fire row triggers | Does not fire triggers |
| **Resets Identity** | No | Yes | Yes (deletes table) |

#### 11. Interview Questions
- Why is TRUNCATE faster than DELETE?
- Can you rollback a TRUNCATE command?

#### 12. Interview Answers
- `TRUNCATE` is faster because instead of scanning and logging every individual row removal, it simply deallocates the database data pages holding the rows.
- In databases like PostgreSQL and SQL Server, `TRUNCATE` can be rolled back if executed inside an active `BEGIN TRANSACTION` block. In MySQL, it auto-commits and cannot be rolled back.

---
---

## Querying Data

### SELECT, DISTINCT, WHERE, ORDER BY, LIMIT, OFFSET, TOP, FETCH, ALIAS
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
The core SQL constructs used to retrieve, filter, format, and paginate query outputs.

#### 2. Why do we use it?
To query database columns, deduplicate records (`DISTINCT`), filter rows (`WHERE`), sort outputs (`ORDER BY`), rename headers (`ALIAS`), and paginate results (`LIMIT` / `OFFSET` / `FETCH`).

#### 3. Syntax
```sql
SELECT DISTINCT column_name AS alias_name
FROM table_name
WHERE condition
ORDER BY column_name DESC
LIMIT offset_val, limit_val;
```

#### 4. Simple Example
**Students**
| id | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | 90 |
| 3 | Amit | 70 |

#### 5. Query
```sql
SELECT DISTINCT name 
FROM Students 
WHERE marks > 75 
ORDER BY name ASC 
LIMIT 1;
```

#### 6. Output
| name |
|---|
| Amit |

#### 7. Interview Explanation
"This query extracts unique values, filters them using a boolean expression, sorts the remainder, and truncates the response list. We use ALIASes (`AS`) to make computed column outputs readable."

#### 8. Remember Trick
*SELECT columns, WHERE rows, ORDER BY sorting, LIMIT counts.*

#### 9. Common Mistakes
Confusing the order of clauses. Writing `WHERE` after `ORDER BY` will trigger syntax errors.

#### 10. Interview Questions
- What is the difference between LIMIT/OFFSET and FETCH/OFFSET?
- Does using DISTINCT slow down query execution?

#### 11. Interview Answers
- `LIMIT` is standard in MySQL/PostgreSQL, while `FETCH FIRST` is the ANSI SQL standard supported natively in Oracle/SQL Server. Both serve to paginate results.
- Yes, `DISTINCT` forces the database optimizer to sort and deduplicate data, which can increase query execution time on large datasets.

#### 12. Real-world Use Case
Implementing page pagination in an API controller (e.g. page 2 is fetched using `LIMIT 10 OFFSET 10`).

---
---

## Filtering

### AND, OR, NOT, BETWEEN, IN, NOT IN, LIKE, Wildcards, IS NULL, IS NOT NULL
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
Logical operators and comparison constructs used in `WHERE` clauses to narrow down search criteria.

#### 2. Why do we use it?
To perform complex boolean checks, range selections (`BETWEEN`), list memberships (`IN`), pattern searches (`LIKE` with `%` or `_`), and check for absent data (`IS NULL`).

#### 3. Syntax
```sql
SELECT * FROM table_name
WHERE (col1 = val1 AND col2 = val2)
  OR col3 BETWEEN low AND high
  OR col4 IN (val3, val4)
  OR col5 LIKE 'A%'
  OR col6 IS NULL;
```

#### 4. Simple Example
**Students**
| id | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | NULL |
| 3 | Raj | 70 |

#### 5. Query
```sql
SELECT name FROM Students 
WHERE (marks BETWEEN 65 AND 85) 
  AND name LIKE 'R%' 
  OR marks IS NULL;
```

#### 6. Output
| name |
|---|
| Neha |
| Raj |

#### 7. Interview Explanation
"Logical operators evaluate filters. `BETWEEN` is inclusive. `LIKE` uses `%` to match zero or more characters, and `_` to match exactly one character. We must use `IS NULL` instead of `= NULL` because NULL represents an unknown value, and comparisons with NULL using standard equality operators evaluate to NULL (which is treated as false)."

#### 8. Remember Trick
*Never use '=' with NULL; use 'IS'.*

#### 9. Common Mistakes
Writing `col = NULL`. This is a classic bug that returns zero rows.

#### 10. Interview Questions
- What does LIKE '_a%' match?
- How does NOT IN behave if the list contains a NULL value?

#### 11. Interview Answers
- It matches any string where the second character is 'a' (e.g. 'cat', 'database').
- If the list passed to `NOT IN` contains a `NULL` (e.g. `WHERE id NOT IN (1, 2, NULL)`), the query returns zero rows because the engine evaluates the comparison as unknown.

#### 12. Real-world Use Case
Searching for users who signed up in a date range, matching wildcard domains like `LIKE '%@company.com'`.

---
---

## Aggregate Functions & GROUP BY / HAVING

### Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
Mathematical functions that perform operations on a set of values to return a single summary value.

#### 2. Why do we use it?
To calculate metrics like total sales (`SUM`), record counts (`COUNT`), average margins (`AVG`), or boundary boundaries (`MIN`/`MAX`).

#### 3. Syntax
```sql
SELECT COUNT(column_name), SUM(column_name) FROM table_name;
```

#### 4. Simple Example
**Students**
| id | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | 90 |
| 3 | Raj | 70 |

#### 5. Query
```sql
SELECT COUNT(*) AS total_students, AVG(marks) AS avg_marks FROM Students;
```

#### 6. Output
| total_students | avg_marks |
|---|---|
| 3 | 80.0 |

#### 7. Interview Explanation
"Aggregate functions scan columns to produce summary metrics. `COUNT(*)` counts all matching rows, while `COUNT(column_name)` counts only non-null values in that column."

#### 8. Remember Trick
*Aggregates squash rows into a single value.*

#### 9. Common Mistakes
Forgetting that most aggregates (except `COUNT`) ignore `NULL` values entirely.

#### 10. Interview Questions
- What is the difference between COUNT(*) and COUNT(column_name)?
- How do you handle NULL values in an AVG operation?

#### 11. Interview Answers
- `COUNT(*)` counts every row returned by the query including duplicates and NULL rows. `COUNT(column_name)` only counts rows where the specified column is not null.
- By default, `AVG` ignores NULL values. If you want NULL values treated as 0 in the average, wrap the column with `COALESCE(column_name, 0)`.

#### 12. Real-world Use Case
Generating weekly financial reports showing total sales revenue and average order value.

---

### GROUP BY
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
A clause that groups rows sharing the same values in specified columns into summary rows.

#### 2. Why do we use it?
To compute aggregate metrics for distinct categories (e.g., total sales per product line).

#### 3. Syntax
```sql
SELECT group_column, AGG_FUNC(col)
FROM table_name
GROUP BY group_column;
```

#### 4. Simple Example
**Employees**
| id | name | department | salary |
|---|---|---|---|
| 1 | Amit | IT | 60000 |
| 2 | Neha | HR | 50000 |
| 3 | Raj | IT | 80000 |

#### 5. Query
```sql
SELECT department, SUM(salary) AS total_payroll
FROM Employees
GROUP BY department;
```

#### 6. Output
| department | total_payroll |
|---|---|
| IT | 140000 |
| HR | 50000 |

#### 7. Interview Explanation
"The `GROUP BY` clause divides dataset records into unique buckets based on the grouping keys. Every column in the `SELECT` list that is not part of an aggregate function must be present in the `GROUP BY` clause."

#### 8. Remember Trick
*Every non-aggregated SELECT column must live in GROUP BY.*

#### 9. Common Mistakes
Selecting non-aggregate columns that are not included in the `GROUP BY` clause, causing syntax failures in strict SQL environments.

#### 10. Interview Questions
- Can you use GROUP BY on multiple columns?
- How does the engine process GROUP BY internally?

#### 11. Interview Answers
- Yes, you can group by multiple columns (e.g. `GROUP BY department, job_title`) to create finer sub-buckets.
- The engine sorts the records or uses a hash table index to group matching key rows before executing the aggregate functions.

#### 12. Real-world Use Case
Aggregating active application users by country to map global user distributions.

---

### HAVING
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
A filtering clause applied to grouped rows after aggregation has taken place.

#### 2. Why do we use it?
To filter groups based on aggregate results (which cannot be done using the `WHERE` clause).

#### 3. Syntax
```sql
SELECT group_column, AVG(col)
FROM table_name
GROUP BY group_column
HAVING AVG(col) > threshold_value;
```

#### 4. Simple Example
**Employees**
| id | name | department | salary |
|---|---|---|---|
| 1 | Amit | IT | 60000 |
| 2 | Neha | HR | 50000 |
| 3 | Raj | IT | 80000 |

#### 5. Query
```sql
SELECT department, AVG(salary) AS avg_sal
FROM Employees
GROUP BY department
HAVING AVG(salary) > 55000;
```

#### 6. Output
| department | avg_sal |
|---|---|
| IT | 70000.0 |

#### 7. Interview Explanation
"The `HAVING` clause filters aggregated groups. `WHERE` filters rows *before* they are grouped. `HAVING` filters groups *after* aggregates are calculated."

#### 8. Remember Trick
*WHERE filters rows; HAVING filters groups.*

#### 9. Common Mistakes
Using `HAVING` to filter non-aggregated fields (e.g. `HAVING status = 'Active'`), which is inefficient and belongs in the `WHERE` clause.

#### 10. Interview Questions
- Can we write a HAVING clause without a GROUP BY?
- What is the difference between WHERE and HAVING?

#### 11. Interview Answers
- Yes, you can use `HAVING` without `GROUP BY`, in which case the entire table acts as a single group.
- `WHERE` filters input rows before aggregation; `HAVING` filters grouped rows after aggregation. `WHERE` cannot contain aggregate functions, whereas `HAVING` frequently does.

#### 12. Real-world Use Case
Finding departments with a total payroll budget exceeding $1,000,000.

---
---

## CASE Statement
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
A conditional control flow expression that returns a value based on defined evaluations (equivalent to an IF-THEN-ELSE statement).

### 2. Why do we use it?
To perform conditional logic directly inside queries to label, categorize, or dynamically modify outputs.

### 3. Syntax
```sql
SELECT column_name,
       CASE 
           WHEN condition1 THEN result1
           WHEN condition2 THEN result2
           ELSE default_result
       END AS alias_name
FROM table_name;
```

### 4. Simple Example
**Students**
| id | name | marks |
|---|---|---|
| 1 | Amit | 80 |
| 2 | Neha | 40 |
| 3 | Raj | 70 |

### 5. Query
```sql
SELECT name, marks,
       CASE 
           WHEN marks >= 50 THEN 'Pass'
           ELSE 'Fail'
       END AS status
FROM Students;
```

### 6. Output
| name | marks | status |
|---|---|---|
| Amit | 80 | Pass |
| Neha | 40 | Fail |
| Raj | 70 | Pass |

### 7. Interview Explanation
"The `CASE` statement evaluates conditional statements sequentially from top to bottom. Once a condition evaluates to true, it returns its corresponding value and stops evaluating subsequent conditions. If no conditions match, it falls back to the `ELSE` block, or returns `NULL` if `ELSE` is omitted."

### 8. Remember Trick
*CASE acts like an inline IF-ELSE switch.*

### 9. Common Mistakes
Forgetting the mandatory `END` keyword at the end of the `CASE` block.

### 10. Interview Questions
- Can we use CASE statements inside an ORDER BY clause?
- How do you perform a conditional update using a CASE statement?

### 11. Interview Answers
- Yes, you can use `CASE` inside `ORDER BY` to implement custom sorting logic (e.g. sorting specific statuses first).
- By referencing `CASE` in an `UPDATE` statement: `UPDATE Employees SET salary = CASE WHEN dept = 'IT' THEN salary * 1.1 ELSE salary END;`.

### 12. Real-world Use Case
Bucketing customers into categories like "Bronze", "Silver", or "Gold" based on their total transaction volume.

---
---

## Built-in Functions (String, Date, Math)

### String Functions
#### 1. Definition
Functions used to transform and manipulate text data in string fields.

#### 2. Why do we use it?
To format output representations (e.g., capitalizing letters, removing whitespaces, splitting text, replacing characters).

#### 3. Syntax
```sql
SELECT UPPER(col), LOWER(col), LENGTH(col), SUBSTRING(col, start, len), REPLACE(col, old, new), CONCAT(col1, col2), TRIM(col) FROM table_name;
```

#### 4. Simple Example
**Employees**
| id | name |
|---|---|
| 1 |   amit  |

#### 5. Query
```sql
SELECT UPPER(REPLACE(TRIM(name), 'a', 'x')) AS formatted_name FROM Employees;
```

#### 6. Output
| formatted_name |
|---|
| XMIT |

#### 7. Interview Explanation
"String functions manipulate character columns. `TRIM` cleans extra whitespaces, `REPLACE` swaps search characters, and `UPPER` converts values to uppercase."

#### 8. Remember Trick
*String functions clean up text formatting.*

#### 9. Common Mistakes
Assuming `SUBSTRING` index parameters are 0-indexed. Most SQL dialects are 1-indexed.

#### 10. Interview Questions
- What is the difference between CHAR_LENGTH and LENGTH?
- How does CONCAT handle NULL arguments?

#### 11. Interview Answers
- `CHAR_LENGTH` returns the length of the string in characters, whereas `LENGTH` returns the length of the string in bytes (which varies in multi-byte encodings like UTF-8).
- In MySQL/SQL Server, `CONCAT` treats NULL as an empty string. In standard PostgreSQL/Oracle, if any parameter is NULL, `CONCAT` returns NULL.

---

### Date Functions
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
Functions designed to work with date and datetime data types.

#### 2. Why do we use it?
To calculate durations, extract specific components (like year, month, day), and add or subtract date intervals.

#### 3. Syntax
```sql
SELECT CURRENT_DATE(), NOW(), DATE_ADD(col, INTERVAL 1 DAY), DATEDIFF(date1, date2), EXTRACT(YEAR FROM col);
```

#### 4. Simple Example
**Employees**
| id | join_date |
|---|---|
| 1 | 2026-01-01 |

#### 5. Query
```sql
SELECT EXTRACT(YEAR FROM join_date) AS join_year,
       DATEDIFF('2026-01-10', join_date) AS days_difference
FROM Employees;
```

#### 6. Output
| join_year | days_difference |
|---|---|
| 2026 | 9 |

#### 7. Interview Explanation
"Date functions allow calculations on date boundaries. `EXTRACT` pulls components out of a date object, while `DATEDIFF` computes the span of time between two timestamps."

#### 8. Remember Trick
*Date functions handle time math and timezone adjustments.*

#### 9. Common Mistakes
Passing strings that do not conform to standard database date formats (typically 'YYYY-MM-DD').

#### 10. Interview Questions
- What is the difference between NOW() and CURRENT_DATE()?
- How do you add 3 months to a date in SQL?

#### 11. Interview Answers
- `NOW()` returns both date and time (timestamp), whereas `CURRENT_DATE()` returns only the date portion.
- By using date arithmetic functions, such as `DATE_ADD(join_date, INTERVAL 3 MONTH)` in MySQL.

---

### Mathematical Functions
#### 1. Definition
Functions used to perform mathematical calculations on numeric fields.

#### 2. Why do we use it?
To round numbers (`ROUND`), round up or down (`CEIL` / `FLOOR`), calculate remainders (`MOD`), and retrieve absolute values (`ABS`).

#### 3. Syntax
```sql
SELECT ROUND(col, decimals), FLOOR(col), CEIL(col), ABS(col), MOD(col, divisor) FROM table_name;
```

#### 4. Simple Example
**Students**
| id | marks |
|---|---|
| 1 | -82.4 |

#### 5. Query
```sql
SELECT ABS(marks) AS absolute_marks, 
       FLOOR(ABS(marks)) AS floored_val,
       CEIL(ABS(marks)) AS ceiled_val
FROM Students;
```

#### 6. Output
| absolute_marks | floored_val | ceiled_val |
|---|---|---|
| 82.4 | 82 | 83 |

#### 7. Interview Explanation
"Mathematical functions process decimal values. `FLOOR` rounds down to the nearest integer, `CEIL` rounds up to the nearest integer, and `ABS` removes negative signs."

#### 8. Remember Trick
*CEIL goes to the ceiling (up); FLOOR goes to the floor (down).*

#### 9. Common Mistakes
Confusing `ROUND(x, 0)` with `FLOOR(x)`. For positive fractions greater than or equal to 0.5, `ROUND` rounds up, while `FLOOR` always rounds down.

#### 10. Interview Questions
- What is the difference between ROUND and TRUNCATE (Math)?
- What does MOD(10, 3) return?

#### 11. Interview Answers
- `ROUND` rounds values to the nearest digit based on standard math rules. `TRUNCATE` simply cuts off decimals without rounding.
- It returns 1, which is the remainder when dividing 10 by 3.

---
---

## Joins
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### Database Tables for Examples

**Employees**
| emp_id | name | dept_id | salary |
|---|---|---|---|
| 1 | Amit | 10 | 50000 |
| 2 | Neha | 20 | 60000 |
| 3 | Raj | NULL | 55000 |

**Departments**
| dept_id | dept_name |
|---|---|
| 10 | IT |
| 20 | HR |
| 30 | Admin |

---

### INNER JOIN
#### 1. Definition
Returns records that have matching values in both tables.

#### 2. ASCII Diagram
```
   [Table A]       [Table B]
  (  Left  ( Match ) Right  )
            \_____/
               |
         [INNER JOIN]
```

#### 3. Syntax
```sql
SELECT columns 
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;
```

#### 4. Query & Output
```sql
SELECT e.name, d.dept_name 
FROM Employees e
INNER JOIN Departments d ON e.dept_id = d.dept_id;
```
| name | dept_name |
|---|---|
| Amit | IT |
| Neha | HR |

#### 5. Interview Explanation
"An INNER JOIN compares each row of the left table with each row of the right table. If they satisfy the join condition (e.g. matching `dept_id`), the columns from both tables are combined in the output. If a record has no matching value (like 'Raj'), it is excluded."

#### 6. Remember Trick
*INNER JOIN = Perfect matches only.*

---

### LEFT JOIN (LEFT OUTER JOIN)
#### 1. Definition
Returns all records from the left table, and the matched records from the right table. If there is no match, the result is `NULL` on the right side.

#### 2. ASCII Diagram
```
   [Table A]       [Table B]
  (  Left   (Match)  Right  )
   \_____________/
          |
     [LEFT JOIN]
```

#### 3. Syntax
```sql
SELECT columns 
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;
```

#### 4. Query & Output
```sql
SELECT e.name, d.dept_name 
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id;
```
| name | dept_name |
|---|---|
| Amit | IT |
| Neha | HR |
| Raj | NULL |

#### 5. Interview Explanation
"A LEFT JOIN preserves all rows of the left table. If a row from the left table has no matching row in the right table (like 'Raj'), the query still returns the left row, but outputs `NULL` values for all columns of the right table."

#### 6. Remember Trick
*LEFT JOIN = Keep all left rows + right matching fields.*

---

### RIGHT JOIN (RIGHT OUTER JOIN)
#### 1. Definition
Returns all records from the right table, and the matched records from the left table. If there is no match, the result is `NULL` on the left side.

#### 2. ASCII Diagram
```
   [Table A]       [Table B]
  (  Left   (Match)  Right  )
            \______________/
                   |
             [RIGHT JOIN]
```

#### 3. Syntax
```sql
SELECT columns 
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;
```

#### 4. Query & Output
```sql
SELECT e.name, d.dept_name 
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;
```
| name | dept_name |
|---|---|
| Amit | IT |
| Neha | HR |
| NULL | Admin |

#### 5. Interview Explanation
"A RIGHT JOIN behaves opposite to a LEFT JOIN. It guarantees that every row from the right table is returned. If a department has no employees (like 'Admin'), it appears in the output with a `NULL` employee name."

#### 6. Remember Trick
*RIGHT JOIN = Keep all right rows + left matching fields.*

---

### FULL JOIN (FULL OUTER JOIN)
#### 1. Definition
Returns all records when there is a match in either left or right table. Unmatched parts contain `NULL`s.

#### 2. ASCII Diagram
```
   [Table A]       [Table B]
  (  Left   (Match)  Right  )
   \________________________/
               |
          [FULL JOIN]
```

#### 3. Syntax
```sql
SELECT columns 
FROM Employees e
FULL JOIN Departments d ON e.dept_id = d.dept_id;
```

#### 4. Query & Output
*(Note: MySQL does not natively support FULL JOIN; it is simulated using a UNION of LEFT and RIGHT joins.)*
```sql
SELECT e.name, d.dept_name 
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.dept_id
UNION
SELECT e.name, d.dept_name 
FROM Employees e
RIGHT JOIN Departments d ON e.dept_id = d.dept_id;
```
| name | dept_name |
|---|---|
| Amit | IT |
| Neha | HR |
| Raj | NULL |
| NULL | Admin |

#### 5. Interview Explanation
"A FULL JOIN combines the effects of both LEFT and RIGHT joins. It returns all records from both tables. When a match doesn't exist, it fills the missing side with NULLs."

#### 8. Remember Trick
*FULL JOIN = Bring everyone to the party.*

---

### CROSS JOIN
#### 1. Definition
Produces a Cartesian product of both tables, combining every row of the first table with every row of the second table.

#### 2. ASCII Diagram
```
   [Table A]         [Table B]
   (Row 1) ---------> (Row 1, Row 2, Row 3)
   (Row 2) ---------> (Row 1, Row 2, Row 3)
```

#### 3. Syntax
```sql
SELECT columns 
FROM Employees e
CROSS JOIN Departments d;
```

#### 4. Query & Output
```sql
SELECT e.name, d.dept_name 
FROM Employees e
CROSS JOIN Departments d;
```
| name | dept_name |
|---|---|
| Amit | IT |
| Amit | HR |
| Amit | Admin |
| Neha | IT |
| Neha | HR |
| Neha | Admin |
| Raj | IT |
| Raj | HR |
| Raj | Admin |

#### 5. Interview Explanation
"A CROSS JOIN does not use a join condition (`ON` clause). It returns the cartesian product: if Table A has $N$ rows and Table B has $M$ rows, the output contains $N \times M$ rows. It can cause performance degradation if run on large datasets."

#### 6. Remember Trick
*CROSS JOIN = Multiply everything.*

---

### SELF JOIN
#### 1. Definition
A regular join in which a table is joined with itself.

#### 2. ASCII Diagram
```
   [Employees (e1)]   <--- Join --->   [Employees (e2)]
   (Alias: Employee)                    (Alias: Manager)
```

#### 3. Syntax
```sql
SELECT e1.name AS Emp, e2.name AS Mgr
FROM Employees e1
JOIN Employees e2 ON e1.manager_id = e2.emp_id;
```

#### 4. Query & Output
For this example, let's assume this structure for **Employees**:
| emp_id | name | manager_id |
|---|---|---|
| 1 | Amit | 2 |
| 2 | Neha | NULL |

```sql
SELECT e1.name AS Employee, e2.name AS Manager
FROM Employees e1
INNER JOIN Employees e2 ON e1.manager_id = e2.emp_id;
```
| Employee | Manager |
|---|---|
| Amit | Neha |

#### 5. Interview Explanation
"A SELF JOIN is used to compare rows within the same table, typically for hierarchical relationships (like employee to manager) or finding duplicate combinations. It requires giving the table two distinct alias names so the engine can treat them as separate tables."

#### 6. Remember Trick
*SELF JOIN = Table looking in a mirror.*

---

### Join Interview Questions & Common Mistakes
- **Mistake**: Using `=` with NULL fields inside join conditions. NULL is never equal to another value.
- **Mistake**: Forgetting table aliases in SELECT statements when column names are identical in both joined tables.
- **Question**: What is the difference between an ON clause filter and a WHERE clause filter in a LEFT JOIN?
- **Answer**: An `ON` clause filter determines which rows are matched to the right table (if unmatched, the left row still returns with NULLs). A `WHERE` clause filter runs *after* the join, filtering out rows from the final result set.

---
---

## Set Operators
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
Operators used to combine the results of two or more independent queries into a single result set.

### 2. Why do we use it?
To aggregate datasets vertically from different tables or conditional queries.

### 3. Syntax
```sql
SELECT col1 FROM TableA
[UNION | UNION ALL | INTERSECT | EXCEPT]
SELECT col1 FROM TableB;
```

### 4. Simple Example
**Table A**
| name |
|---|
| Amit |
| Neha |

**Table B**
| name |
|---|
| Neha |
| Raj |

### 5. Query
```sql
-- UNION
SELECT name FROM TableA UNION SELECT name FROM TableB;

-- UNION ALL
SELECT name FROM TableA UNION ALL SELECT name FROM TableB;

-- INTERSECT
SELECT name FROM TableA INTERSECT SELECT name FROM TableB;

-- EXCEPT (or MINUS)
SELECT name FROM TableA EXCEPT SELECT name FROM TableB;
```

### 6. Output
- **UNION**: Amit, Neha, Raj (duplicates removed).
- **UNION ALL**: Amit, Neha, Neha, Raj (keeps duplicates).
- **INTERSECT**: Neha (only common items).
- **EXCEPT**: Amit (in Table A but not Table B).

### 7. Interview Explanation
"Set operators merge result sets vertically. Two rules must be met: both queries must select the same number of columns, and corresponding columns must have compatible data types. `UNION` performs a sort and deduplicates, while `UNION ALL` simply appends rows, making it much faster."

#### 8. Remember Trick
- `UNION` -> Removes duplicates (Slow).
- `UNION ALL` -> Keeps duplicates (Fast).

### 9. Common Mistakes
Assuming `UNION` and `UNION ALL` behave similarly in performance. `UNION` is slower because it performs a sorting pass to eliminate duplicates.

### 10. Interview Questions
- What is the difference between UNION and UNION ALL?
- What are the requirements for Set operators?

### 11. Interview Answers
- `UNION` merges datasets and removes duplicate rows; `UNION ALL` merges datasets and keeps all duplicate rows.
- The datasets must have the exact same number of columns in the same order, with compatible data types.

---
---

## Subqueries & EXISTS
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
A subquery is a query nested inside another query (outer query). `EXISTS` is a boolean operator that checks if a subquery returns any rows.

### 2. Why do we use it?
To execute multi-step queries where the filter condition depends on another query's dynamic output.

### 3. Syntax
```sql
-- Subquery
SELECT * FROM Employees 
WHERE salary > (SELECT AVG(salary) FROM Employees);

-- EXISTS
SELECT * FROM Departments d
WHERE EXISTS (SELECT 1 FROM Employees e WHERE e.dept_id = d.dept_id);
```

### 4. Simple Example
**Employees**
| emp_id | name | salary | dept_id |
|---|---|---|---|
| 1 | Amit | 80000 | 10 |
| 2 | Neha | 50000 | 10 |

**Departments**
| dept_id | dept_name |
|---|---|
| 10 | IT |
| 20 | Sales |

### 5. Query
```sql
-- Find departments containing employees
SELECT dept_name FROM Departments d
WHERE EXISTS (
    SELECT 1 FROM Employees e 
    WHERE e.dept_id = d.dept_id
);
```

### 6. Output
| dept_name |
|---|
| IT |

### 7. Interview Explanation
"Subqueries can be categorized into **Single-row** (returns one value, evaluated with `=`, `<`), **Multi-row** (returns a list, evaluated with `IN`, `ANY`, `ALL`), and **Correlated** (subquery references columns from the outer query for execution). `EXISTS` returns true immediately upon finding the first matching record in the subquery, making it highly efficient."

#### 8. Remember Trick
*EXISTS stops looking the moment it finds one match.*

### 9. Common Mistakes
Using `NOT IN` with subquery columns that can contain `NULL` values. If the subquery results contain a `NULL`, a `NOT IN` query returns zero records. Use `NOT EXISTS` instead.

### 10. Comparison: IN vs EXISTS
- Use `IN` when the subquery returns a small, static dataset.
- Use `EXISTS` when the subquery is correlated and the outer query is large, as the execution can short-circuit early and leverage indexes.

---
---

## CTEs (Common Table Expressions)
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### 1. Definition
A temporary named result set defined within the execution scope of a single `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement.

### 2. Why do we use it?
To replace complex subqueries, improve code readability, and write recursive queries.

### 3. Syntax
```sql
WITH CTE_Name AS (
    SELECT column1, column2 
    FROM table_name
    WHERE condition
)
SELECT * FROM CTE_Name;
```

### 4. Simple Example
**Employees**
| id | name | salary |
|---|---|---|
| 1 | Amit | 80000 |
| 2 | Neha | 90000 |

### 5. Query
```sql
WITH HighEarners AS (
    SELECT name, salary 
    FROM Employees 
    WHERE salary > 85000
)
SELECT name FROM HighEarners;
```

### 6. Output
| name |
|---|
| Neha |

### 7. Interview Explanation
"CTEs improve code readability by organizing queries into logical sections. Unlike temporary tables, CTEs do not store data physically on disk and exist only for the duration of the query execution. Recursive CTEs refer to themselves to navigate hierarchical structures like corporate org charts."

#### 8. Remember Trick
*CTEs are like variables holding temporary query results.*

### 9. Common Mistakes
Trying to reference a CTE outside the query that defines it. It is local to that single query.

### 10. Recursive CTE Example
```sql
WITH RECURSIVE Counter AS (
    -- Anchor member
    SELECT 1 AS num
    UNION ALL
    -- Recursive member
    SELECT num + 1 FROM Counter WHERE num < 3
)
SELECT * FROM Counter;
```
**Output**
| num |
|---|
| 1 |
| 2 |
| 3 |

---
---

## Views & Materialized Views
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
- **View**: A virtual table containing a saved query definition; it does not store data physically.
- **Materialized View**: A physical copy of the query results stored on disk, which must be refreshed periodically.

### 2. Why do we use it?
- Views: Simplify complex queries and restrict access to sensitive table columns.
- Materialized Views: Cache heavy calculations (e.g. daily summaries) to speed up execution.

### 3. Syntax
```sql
CREATE VIEW ViewName AS 
SELECT name, department FROM Employees;

-- Materialized View (dialect specific, e.g., Oracle/PostgreSQL)
CREATE MATERIALIZED VIEW MatViewName AS 
SELECT dept_id, SUM(salary) FROM Employees GROUP BY dept_id;
```

### 4. Simple Example
Creating a virtual layer over the Employees table to expose only public profiles.

### 5. Query
```sql
-- Read from the view
SELECT * FROM ViewName;
```

### 6. Output
Displays filtered columns dynamically based on the underlying table data.

### 7. Interview Explanation
"Standard views are dynamically evaluated every time they are queried. Materialized views pre-compute and store the result set, which speeds up lookups on complex joins at the expense of data freshness. Materialized views require a refresh strategy (e.g., ON COMMIT or scheduled intervals)."

#### 8. Remember Trick
*View is a saved query; Materialized View is a saved table.*

### 9. Common Mistakes
Forgetting to refresh Materialized Views, leading to queries returning stale data.

### 10. Interview Questions
- Can you update data through a View?
- When should you use a Materialized View over a standard View?

### 11. Interview Answers
- Yes, views can be updatable if they reference a single base table, lack aggregate functions, and include the primary key.
- Use Materialized Views for complex aggregations or slow joins on large tables in reporting systems where real-time accuracy is not required.

---
---

## Indexes & Query Tuning
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### 1. Definition
A database structure that improves the speed of data retrieval operations on a table at the cost of additional write overhead and storage space.

### 2. Why do we use it?
To avoid expensive Full Table Scans (`Seq Scan`), converting lookup times from $O(N)$ linear scans to $O(\log N)$ tree traversals.

### 3. Syntax
```sql
CREATE INDEX idx_emp_salary ON Employees(salary);
```

### 4. How Indexes Work Internally (B-Trees)
Databases primarily use **B-Tree (Balanced Tree)** indexes. 
- The tree structure consists of Root, Internal nodes, and Leaf nodes.
- When querying `WHERE salary = 60000`, the engine starts at the root, traverses down based on range comparisons, and finds the leaf node containing the exact disk address (`RID` or pointer) of the row.
- **Clustered Index**: The leaf node contains the actual physical data row. A table can have only one Clustered Index (default is the Primary Key).
- **Non-Clustered Index**: The leaf node contains the index key values and a pointer (bookmark/primary key value) to the actual data row. A table can have multiple Non-Clustered Indexes.

```
                  [Root Node]
                     /   \
                    /     \
         [Internal]         [Internal]
           /    \             /    \
      [Leaf]    [Leaf]   [Leaf]    [Leaf] (Pointers to physical disk rows)
```

### 5. Query
```sql
-- Explaining query path
EXPLAIN SELECT * FROM Employees WHERE salary = 60000;
```

### 6. Index Seek vs Index Scan
- **Index Seek**: The engine traverses the B-Tree directly to locate specific matching rows. Highly efficient (typically $O(\log N)$).
- **Index Scan**: The engine reads the entire index tree structure page by page. Less efficient than a seek, but faster than a Full Table Scan if only index columns are needed.
- **Full Table Scan (Seq Scan)**: The engine reads the entire table from disk row by row because no index is available.

### 7. When do Indexes Slow Down Queries?
- **Writes (`INSERT`, `UPDATE`, `DELETE`)**: Every write operation requires updating the corresponding indexes, which involves splitting and balancing B-Tree pages.
- **Low Cardinality Columns**: Indexing columns with few unique values (like `gender` or `status`) is often ignored by the optimizer in favor of a table scan.

#### 8. Remember Trick
*Index is the book index; Clustered index is how the book pages are bound.*

### 9. Common Mistakes
Creating too many indexes on high-write tables. This degrades write throughput.

### 10. Interview Questions
- Why can a table only have one Clustered Index?
- What is a Composite Index, and what is the Left Prefix rule?

### 11. Interview Answers
- A Clustered Index determines the physical order of data on disk; data rows can only be ordered in one way.
- A Composite Index is an index on multiple columns (e.g., `ColA, ColB`). The Left Prefix rule states that the index is only used if the query includes the first column in the index definition (`ColA`) in its filters.

---
---

## Normalization
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
The process of structuring a relational database schema to reduce data redundancy and improve data integrity.

### 2. Why do we use it?
To prevent data anomalies (Insert, Update, Delete anomalies) and structure tables efficiently.

### 3. The Normal Forms
- **1NF (First Normal Form)**:
  - Rules: Atomic values (no arrays or comma-separated lists inside cells) and unique row identification.
  - *Example*: Splitting `skills = 'Java, SQL'` into separate rows.
- **2NF (Second Normal Form)**:
  - Rules: Must be in 1NF + No partial dependencies (all non-key columns must depend on the *entire* primary key, not a subset of a composite key).
  - *Example*: If PK is `(student_id, course_id)`, the column `course_fee` depends only on `course_id`. We must split this into a separate `Courses` table.
- **3NF (Third Normal Form)**:
  - Rules: Must be in 2NF + No transitive dependencies (non-key columns must not depend on other non-key columns).
  - *Example*: If `dept_name` depends on `dept_id` which depends on `emp_id` (PK), we must extract `dept_id` and `dept_name` into a separate `Departments` table.
- **BCNF (Boyce-Codd Normal Form)**:
  - Rules: Must be in 3NF + For every functional dependency $X \rightarrow Y$, $X$ must be a super key.

#### 4. Remember Trick
*Every column must depend on the key, the whole key, and nothing but the key, so help me Codd.*

### 5. Common Mistakes
Over-normalizing database schemas, which leads to too many tables and joins, degrading query performance. Production databases are often selectively denormalized for speed.

### 6. Interview Questions
- What is the difference between 3NF and BCNF?
- What is Denormalization, and when is it useful?

### 7. Interview Answers
- BCNF is a stronger version of 3NF. It handles cases where a table has overlapping candidate keys. In BCNF, any determinant must be a candidate key.
- Denormalization is the process of intentionally introducing redundancy into a database schema (e.g. storing computed columns or joining tables) to optimize read query execution times.

---
---

## ACID & Transactions
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### 1. Definition
- **ACID**: A set of properties (Atomicity, Consistency, Isolation, Durability) that guarantee database transactions are processed reliably.
- **Transaction**: A logical unit of work containing one or more SQL statements.

### 2. Why do we use it?
To ensure data consistency during system crashes or concurrent user access (e.g., transfers in banking applications).

### 3. Syntax
```sql
START TRANSACTION; -- or BEGIN
UPDATE Accounts SET balance = balance - 100 WHERE id = 1;
UPDATE Accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- Save changes permanent
-- or ROLLBACK; -- Revert all changes
```

### 4. ACID Explained with Banking Examples
- **Atomicity (All-or-Nothing)**:
  - *Explanation*: If a system crashes mid-transaction during a money transfer, the entire operation is rolled back. Either both the debit and credit succeed, or neither does.
- **Consistency (Rules Followed)**:
  - *Explanation*: Total money in the system must remain constant. A transaction cannot violate schema constraints (e.g., account balance dropping below zero).
- **Isolation (Invisible mid-states)**:
  - *Explanation*: If Person A is transferring money to Person B, a third party checking the balances mid-flight will not see intermediate states where the money is debited from A but not yet credited to B.
- **Durability (Survival of crashes)**:
  - *Explanation*: Once a transaction is committed, the changes are written to non-volatile storage (disk/Write-Ahead Log) and will survive a subsequent power outage or database crash.

#### 5. Remember Trick
*ACID keeps transaction data solid.*

### 6. Common Mistakes
Forgetting that transactions hold locks on database rows, which can lead to connection pool exhaustion if transactions are left open for too long.

### 7. Interview Questions
- What is a Write-Ahead Log (WAL)?
- What is the difference between COMMIT and ROLLBACK?

### 8. Interview Answers
- WAL is a logging pattern where changes are written to an append-only log on disk *before* they are applied to the database files, guaranteeing durability.
- `COMMIT` saves the transaction's changes permanently to disk; `ROLLBACK` undoes all modifications made within the active transaction.

---
---

## Locks & Concurrency
⭐⭐⭐⭐ *Frequently Asked*

### 1. Definition
Mechanisms used by RDBMS engines to manage concurrent access to database records, preventing data conflicts.

### 2. Why do we use it?
To prevent concurrent transactions from corrupting data or creating inconsistencies.

### 3. Shared vs Exclusive Locks
- **Shared Lock (S-Lock / Read Lock)**:
  - Multiple transactions can hold shared locks on a row to read it concurrently.
  - Prevents other transactions from modifying the locked row.
- **Exclusive Lock (X-Lock / Write Lock)**:
  - Only one transaction can hold an exclusive lock on a row to modify it.
  - Blocks all other transactions from reading or writing to the row.

### 4. Deadlock
A deadlock occurs when Transaction 1 holds a lock on Row A and requests a lock on Row B, while Transaction 2 holds a lock on Row B and requests a lock on Row A. Both wait indefinitely.

```
[Trans 1] --Locks--> [Row A] --Wants--> [Row B]
    ^                                      |
    |                                      |
    +----Wants---- [Row A] <---Locks-- [Trans 2]
```

### 5. Simple Example (Preventing Deadlocks)
Ensure all transactions access tables and rows in the exact same order.

### 6. Query (Locking a row for update)
```sql
BEGIN;
SELECT * FROM Employees WHERE id = 1 FOR UPDATE; -- Acquires Exclusive Lock
UPDATE Employees SET salary = 60000 WHERE id = 1;
COMMIT;
```

#### 7. Remember Trick
*Shared is for reading together; Exclusive is for writing alone.*

### 8. Interview Questions
- How does a database engine resolve a deadlock?
- What are the four database isolation levels?

### 9. Interview Answers
- The database engine runs a deadlock detection algorithm. If it finds a loop, it kills one of the transactions (usually the one that did the least work) and rolls it back, allowing the other to complete.
- Read Uncommitted, Read Committed, Repeatable Read, and Serializable.

---
---

## Window Functions
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### 1. Definition
Functions that perform calculations across a set of table rows that are related to the current row, without collapsing them into a single summary row.

### 2. Why do we use it?
To calculate running totals, rank rows within partitions, calculate moving averages, and compare current row values with adjacent rows.

### 3. Syntax
```sql
SELECT column_name,
       FUNC() OVER (PARTITION BY col1 ORDER BY col2)
FROM table_name;
```

### 4. Simple Example
**Employees**
| emp_id | name | department | salary |
|---|---|---|---|
| 1 | Amit | IT | 80000 |
| 2 | Neha | IT | 90000 |
| 3 | Raj | HR | 50000 |

### 5. Query
```sql
SELECT name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rnk
FROM Employees;
```

### 6. Output
| name | department | salary | row_num | rnk | dense_rnk |
|---|---|---|---|---|---|
| Neha | IT | 90000 | 1 | 1 | 1 |
| Amit | IT | 80000 | 2 | 2 | 2 |
| Raj | HR | 50000 | 1 | 1 | 1 |

### 7. Interview Explanation
"Window functions use the `OVER` clause. `PARTITION BY` acts like a local `GROUP BY` but preserves the individual rows. `ORDER BY` defines the sequence of execution inside that partition. `ROW_NUMBER` gives sequential integers. `RANK` skips ranks on ties (e.g. 1, 2, 2, 4), while `DENSE_RANK` does not skip ranks (e.g. 1, 2, 2, 3)."

#### 8. Remember Trick
*Window functions do not collapse rows.*

### 9. Common Mistakes
Trying to filter window function outputs in the `WHERE` clause of the same query block (e.g. `WHERE ROW_NUMBER() OVER(...) = 1`). You must use a Subquery or CTE to filter window values.

### 10. Key Window Functions Explained
- **ROW_NUMBER()**: Assigns a unique, sequential integer to rows starting at 1.
- **RANK()**: Assigns ranks, skipping ranks on duplicate values.
- **DENSE_RANK()**: Assigns ranks, without skipping ranks on duplicates.
- **LAG(col, offset)**: Accesses data from a previous row at a specified offset.
- **LEAD(col, offset)**: Accesses data from a subsequent row at a specified offset.
- **FIRST_VALUE(col)**: Returns the first value in the sorted window partition.
- **LAST_VALUE(col)**: Returns the last value in the sorted window partition.

---
---

## Programmability (Stored Procedures, Functions, Triggers)

### Stored Procedures
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
A prepared SQL code segment that you can save and reuse, allowing parameter execution and procedural control blocks.

#### 2. Why do we use it?
To reduce network traffic, enforce security parameters, and encapsulate complex database transactions.

#### 3. Syntax
```sql
CREATE PROCEDURE GetEmployeeSalary(IN empId INT, OUT empSal INT)
BEGIN
    SELECT salary INTO empSal FROM Employees WHERE id = empId;
END;
```

#### 4. Simple Example
**Employees**
| id | name | salary |
|---|---|---|
| 1 | Amit | 50000 |

#### 5. Query
```sql
CALL GetEmployeeSalary(1, @salary);
SELECT @salary;
```

#### 6. Output
| @salary |
|---|
| 50000 |

#### 7. Interview Explanation
"Stored Procedures allow logic to execute directly on the database server. They accept input (`IN`) and output (`OUT`) parameters and can modify table data within transaction boundaries. They are pre-compiled, which can optimize execution speed."

#### 8. Remember Trick
*Stored Procedure is an executable function stored inside the database.*

#### 9. Common Mistakes
Putting application-level business logic inside stored procedures, which makes the application difficult to scale and version control.

---

### Functions vs Procedures
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### 1. Definition
- **Function (UDF)**: A database routine designed to compute and return a single value.
- **Stored Procedure**: A routine designed to execute a series of database operations.

#### 2. Comparison Table

| Feature | Stored Procedure | User-Defined Function |
|---|---|---|
| **Return Value** | Optional (via OUT parameters) | Must return a single value (or table) |
| **Call Syntax** | `CALL ProcedureName()` | `SELECT FunctionName()` |
| **DML in SELECT** | No, cannot call in SELECT queries | Yes, can call directly in SELECT list |
| **Transactions** | Can use `COMMIT` and `ROLLBACK` | Cannot manage transactions |
| **Side Effects** | Can modify database tables | Cannot modify database tables (read-only) |

#### 3. Remember Trick
*Functions calculate; Procedures execute.*

---

### Triggers
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
A named database object that automatically executes (fires) when a specified DML event (`INSERT`, `UPDATE`, `DELETE`) occurs on a table.

#### 2. Why do we use it?
To enforce audits, log data modifications, or validate values before saving.

#### 3. Syntax
```sql
CREATE TRIGGER Before_Emp_Insert
BEFORE INSERT ON Employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;
    END IF;
END;
```

#### 4. Simple Example
Modifying negative input values to zero automatically upon insertion.

#### 5. Query
```sql
INSERT INTO Employees (name, salary) VALUES ('Raj', -5000);
SELECT salary FROM Employees WHERE name = 'Raj';
```

#### 6. Output
| salary |
|---|
| 0 |

#### 7. Interview Explanation
"Triggers can be set to run `BEFORE` or `AFTER` an event. They use pseudo-records: `OLD` (the state before modification) and `NEW` (the state after modification). They should be used sparingly because they hide side effects and degrade write performance."

#### 8. Remember Trick
*Triggers are event handlers for database operations.*

---
---

## Performance Optimization
⭐⭐⭐⭐⭐ *Very Frequently Asked*

### 1. The Strategy
Improving query speed and reducing database server load by executing target actions.

### 2. Best Practices Checklist
- **Avoid `SELECT *`**: Retrieve only the columns required. Selecting all columns increases network payload size and prevents the engine from leveraging covering indexes.
- **Use `EXISTS` instead of `IN`**: For subqueries, `EXISTS` returns `TRUE` at the first match, whereas `IN` can load the entire subquery result set into memory.
- **Avoid Wildcards at the Beginning**: Filters like `LIKE '%term'` force full table scans. Use `LIKE 'term%'` to leverage indexes.
- **Ensure Indexes on Join Keys**: Create indexes on foreign keys and columns frequently used in `ON` and `WHERE` clauses.
- **Use execution plans (`EXPLAIN`)**: Check if queries perform `Index Seek` instead of `Seq Scan`.
- **Avoid functions on indexed columns**: Filtering using `WHERE YEAR(join_date) = 2026` invalidates the index on `join_date`. Use `WHERE join_date BETWEEN '2026-01-01' AND '2026-12-31'`.

---
---

## Advanced SQL Features

### Pivot, Unpivot, Temporary Tables, Window Aggregates
⭐⭐⭐⭐ *Frequently Asked*

#### 1. Definition
- **Pivot**: Rotates table rows into columns.
- **Unpivot**: Rotates columns into rows.
- **Temporary Tables**: Tables stored in `tempdb` that are deleted automatically when the database session ends.
- **Window Aggregates**: Running sums or averages over dynamic frames.

#### 2. Syntax
```sql
-- Temporary Table
CREATE TEMPORARY TABLE TempUsers (id INT);

-- Window Aggregate (Running Sum)
SELECT name, salary,
       SUM(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM Employees;
```

#### 3. Simple Example
**Sales**
| year | product | revenue |
|---|---|---|
| 2025 | Laptop | 1000 |
| 2026 | Laptop | 1500 |

#### 4. Query (Pivot)
```sql
SELECT product,
       SUM(CASE WHEN year = 2025 THEN revenue ELSE 0 END) AS rev_2025,
       SUM(CASE WHEN year = 2026 THEN revenue ELSE 0 END) AS rev_2026
FROM Sales
GROUP BY product;
```

#### 5. Output
| product | rev_2025 | rev_2026 |
|---|---|---|
| Laptop | 1000 | 1500 |

#### 6. Interview Explanation
"Pivot rotates rows into columns, which is useful for cross-tab reports. Window Aggregates compute metrics like running totals by using cumulative frame specifications like `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`."

#### 7. Remember Trick
*Pivot turns records into header columns.*

---
---

## SQL Scenario Questions
Each scenario problem includes the problem statement, approach, query, expected output, explanation, complexity, and tips.

---

### 1. Find the Second Highest Salary
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### Problem
Find the second highest salary in the `Employees` table. If there is no second highest salary, return `NULL`.

#### Approach
1. Find the maximum salary.
2. Filter out rows matching that maximum salary.
3. Find the maximum value of the remaining salaries.

#### SQL Query
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employees
WHERE salary < (SELECT MAX(salary) FROM Employees);
```

#### Expected Output
| SecondHighestSalary |
|---|
| 80000 |

#### Explanation
The subquery returns the absolute highest salary. The outer query finds the maximum salary that is strictly less than that value. If no such record exists (e.g. only one salary exists), it returns `NULL`.

#### Complexity Discussion
- **Time Complexity**: $O(N)$ with an index on `salary`.
- **Space Complexity**: $O(1)$.

#### Interview Tips
Do not use `LIMIT 1 OFFSET 1` without handling duplicates. If the highest salary is shared by multiple employees, `LIMIT` will return the highest salary instead of the second highest.

---

### 2. Find the Nth Highest Salary (Generic Solution)
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### Problem
Find the Nth highest salary in the `Employees` table.

#### Approach
Using a correlated subquery, find the salary value where exactly $N-1$ unique salaries are greater than it.

#### SQL Query
```sql
SELECT DISTINCT salary 
FROM Employees e1
WHERE (N - 1) = (
    SELECT COUNT(DISTINCT salary) 
    FROM Employees e2 
    WHERE e2.salary > e1.salary
);
```

#### Expected Output
*(For N=3)*
| salary |
|---|
| 70000 |

#### Explanation
For each candidate row evaluated by the outer query, the inner query counts how many distinct salaries are higher. If the count matches $N-1$, that candidate row is returned.

#### Complexity Discussion
- **Time Complexity**: $O(N^2)$ in worst case without indexes.
- **Space Complexity**: $O(1)$.

#### Interview Tips
Suggest using `DENSE_RANK()` as an alternative solution during interviews, as it is cleaner and performs better on modern database engines.

---

### 3. Find and Delete Duplicate Rows
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### Problem
Identify and delete duplicate rows in a table, keeping only the row with the lowest ID.

#### Approach
Join the table to itself on columns that define duplication (e.g., email), filtering for rows with a larger ID, and delete them.

#### SQL Query
```sql
DELETE e1 FROM Employees e1
INNER JOIN Employees e2 
ON e1.email = e2.email AND e1.id > e2.id;
```

#### Expected Output
Duplicates are deleted. The table retains only the row with the lowest ID for each duplicate email.

#### Explanation
The join matches rows with duplicate emails. The condition `e1.id > e2.id` ensures that for any duplicate pair, only the row with the larger ID (`e1`) is targeted for deletion.

#### Complexity Discussion
- **Time Complexity**: $O(N)$ with indexes on the duplicate check columns.
- **Space Complexity**: $O(1)$.

#### Interview Tips
Always run a `SELECT` statement using the same join conditions to preview the rows you intend to delete before running the `DELETE` query.

---

### 4. Find Employees Earning More Than Their Managers
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### Problem
Find employees who earn more than their direct managers.

#### Approach
Perform a self-join on the `Employees` table to match employees with their managers, and compare their salaries.

#### SQL Query
```sql
SELECT e.name AS Employee
FROM Employees e
INNER JOIN Employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

#### Expected Output
| Employee |
|---|
| Amit |

#### Explanation
By joining `Employees` to itself as `e` (employee) and `m` (manager), we align each employee row with their corresponding manager row. The `WHERE` clause filters for rows where the employee's salary is greater than the manager's.

#### Complexity Discussion
- **Time Complexity**: $O(N)$ with an index on `manager_id`.
- **Space Complexity**: $O(1)$.

---

### 5. Find the Highest Salary in Each Department
⭐⭐⭐⭐⭐ *Very Frequently Asked*

#### Problem
Find the employee with the highest salary in each department.

#### Approach
Use a window function (`DENSE_RANK()`) partitioned by department to rank salaries, and filter for rows ranked 1.

#### SQL Query
```sql
WITH RankedSalaries AS (
    SELECT name, department, salary,
           DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM Employees
)
SELECT department, name, salary
FROM RankedSalaries
WHERE rnk = 1;
```

#### Expected Output
| department | name | salary |
|---|---|---|
| IT | Neha | 90000 |
| HR | Raj | 70000 |

#### Explanation
The CTE assigns a rank to each employee within their department based on salary. The outer query filters for employees ranked 1. Using `DENSE_RANK()` handles cases where multiple employees share the highest salary in a department.

#### Complexity Discussion
- **Time Complexity**: $O(N \log N)$ due to partition sorting.
- **Space Complexity**: $O(N)$ for sorting buffers.

---

### 6. Calculate the Running Total of Salaries
⭐⭐⭐⭐ *Frequently Asked*

#### Problem
Calculate the running total of salaries for employees ordered by their hire date.

#### Approach
Use the `SUM` aggregate function as a window function, ordering by the hire date.

#### SQL Query
```sql
SELECT name, hire_date, salary,
       SUM(salary) OVER(ORDER BY hire_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM Employees;
```

#### Expected Output
| name | hire_date | salary | running_total |
|---|---|---|---|
| Amit | 2025-01-01 | 50000 | 50000 |
| Neha | 2025-06-01 | 60000 | 110000 |
| Raj  | 2026-01-01 | 70000 | 180000 |

#### Explanation
The window specification `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` instructs the engine to sum all salaries from the first row up to the current row in the sorted sequence.

#### Complexity Discussion
- **Time Complexity**: $O(N \log N)$ to sort by `hire_date`.
- **Space Complexity**: $O(N)$ for the result window.

---

### 7. Find Consecutive Active Users (Gap Detection)
⭐⭐⭐⭐ *Frequently Asked*

#### Problem
Identify users who were active for 3 or more consecutive days.

#### Approach
1. Use `DENSE_RANK` to rank activity dates for each user.
2. Subtract the rank from the activity date. If the dates are consecutive, this subtraction yields a constant date group key.
3. Group by user and the date group key, and filter for groups with a count of 3 or more.

#### SQL Query
```sql
WITH DateGroups AS (
    SELECT user_id, activity_date,
           activity_date - INTERVAL (DENSE_RANK() OVER(PARTITION BY user_id ORDER BY activity_date)) DAY AS group_date
    FROM UserActivity
)
SELECT user_id, MIN(activity_date) AS start_date, MAX(activity_date) AS end_date, COUNT(*) AS consecutive_days
FROM DateGroups
GROUP BY user_id, group_date
HAVING COUNT(*) >= 3;
```

#### Expected Output
| user_id | start_date | end_date | consecutive_days |
|---|---|---|---|
| 101 | 2026-08-01 | 2026-08-03 | 3 |

#### Explanation
Subtracting sequential ranks from consecutive dates returns the same starting boundary date (`group_date`). Grouping by this calculated date key aggregates consecutive sequences, allowing us to filter them using `HAVING`.

#### Complexity Discussion
- **Time Complexity**: $O(N \log N)$.
- **Space Complexity**: $O(N)$.

---

### 8. Find the Latest Record for Each Entity
⭐⭐⭐⭐ *Frequently Asked*

#### Problem
Find the latest status update record for each user.

#### Approach
Use `ROW_NUMBER()` partitioned by `user_id` and ordered by update timestamp descending, and select rows where the row number is 1.

#### SQL Query
```sql
WITH LatestUpdates AS (
    SELECT user_id, status, update_time,
           ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY update_time DESC) AS rn
    FROM UserStatus
)
SELECT user_id, status, update_time
FROM LatestUpdates
WHERE rn = 1;
```

#### Expected Output
| user_id | status | update_time |
|---|---|---|
| 101 | Active | 2026-08-01 10:00:00 |
| 102 | Pending | 2026-08-01 09:30:00 |

#### Explanation
`ROW_NUMBER()` assigns sequential numbers within each user partition. Ordering descending ensures the newest record gets assigned 1.

#### Complexity Discussion
- **Time Complexity**: $O(N \log N)$.
- **Space Complexity**: $O(N)$.

---

### 9. Find Top N Performing Products per Category
⭐⭐⭐⭐ *Frequently Asked*

#### Problem
Find the top 2 products with the highest sales volume in each product category.

#### Approach
Rank products within each category using `DENSE_RANK()`, and filter for ranks less than or equal to 2.

#### SQL Query
```sql
WITH RankedProducts AS (
    SELECT category, product_name, sales,
           DENSE_RANK() OVER(PARTITION BY category ORDER BY sales DESC) AS rnk
    FROM Products
)
SELECT category, product_name, sales
FROM RankedProducts
WHERE rnk <= 2;
```

#### Expected Output
| category | product_name | sales |
|---|---|---|
| Electronics | Laptop | 50000 |
| Electronics | Phone | 40000 |
| Clothes | Shirt | 12000 |

#### Explanation
Partitioning by `category` separates the ranking context. Ordering by `sales DESC` assigns the top ranks to the highest sales volumes.

#### Complexity Discussion
- **Time Complexity**: $O(N \log N)$.
- **Space Complexity**: $O(N)$.

---

### 10. Pivot Product Sales by Year
⭐⭐⭐⭐ *Frequently Asked*

#### Problem
Pivot dynamic sales records to display total revenue for the years 2024 and 2025 as columns.

#### Approach
Use conditional aggregation (`SUM` with `CASE` statements) grouped by product name.

#### SQL Query
```sql
SELECT product_name,
       SUM(CASE WHEN sale_year = 2024 THEN revenue ELSE 0 END) AS revenue_2024,
       SUM(CASE WHEN sale_year = 2025 THEN revenue ELSE 0 END) AS revenue_2025
FROM Sales
GROUP BY product_name;
```

#### Expected Output
| product_name | revenue_2024 | revenue_2025 |
|---|---|---|
| Keyboard | 8000 | 12000 |
| Monitor | 25000 | 30000 |

#### Explanation
The query evaluates each row's year. If it matches, the revenue value is added to the sum; otherwise, 0 is added. Grouping by product collapses rows and populates the year columns.

#### Complexity Discussion
- **Time Complexity**: $O(N)$ with single scan.
- **Space Complexity**: $O(1)$.

---

### 11-50. Additional Scenario Questions (Summarized List)
To prepare for interviews, understand the SQL query pattern for these common scenarios:

11. **Monthly Active Users (MAU)**: `SELECT COUNT(DISTINCT user_id) ... GROUP BY DATE_FORMAT(activity_date, '%Y-%m')`
12. **Year-over-Year (YoY) Growth**: Use `LAG` to retrieve the previous year's sales: `(Sales - LAG(Sales) OVER()) / LAG(Sales) OVER()`
13. **First and Last Order for Each Customer**: Use `FIRST_VALUE` and `LAST_VALUE` window functions.
14. **Customer Retention Rate**: Perform a self-join on customer activity tables with a month offset: `ON a.customer_id = b.customer_id AND b.month = a.month + 1`
15. **Find Gaps in Sequence Numbers**: Compare current ID with next ID using `LEAD(id) OVER(ORDER BY id)`. Filter where `next_id - id > 1`.
16. **Find the Median Salary**: Use `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary)` or sort rows and select the middle value.
17. **Calculate a Moving Average (3-day)**: `AVG(sales) OVER(ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)`
18. **Find Users with Duplicate Emails**: `SELECT email FROM Users GROUP BY email HAVING COUNT(*) > 1`
19. **Find Departments with No Employees**: Use a `LEFT JOIN` and filter where `employee_id IS NULL`.
20. **Employees with Salary Higher than Department Average**: Compare salary to average salary: `WHERE salary > (SELECT AVG(salary) FROM Employees WHERE dept_id = e.dept_id)`.
21. **Find Managers with at Least 5 Direct Reports**: `SELECT manager_id FROM Employees GROUP BY manager_id HAVING COUNT(*) >= 5`
22. **Find the Most Frequently Purchased Item**: `SELECT item_id FROM Orders GROUP BY item_id ORDER BY COUNT(*) DESC LIMIT 1`
23. **Find the Second Most Recent Login**: Rank logins descending using `ROW_NUMBER()` and select the row ranked 2.
24. **Find New Users vs Returning Users per Day**: Use a CTE to find each user's signup date, then join with daily activity tables.
25. **Calculate the Cumulative Sum of Users**: `SUM(new_users) OVER(ORDER BY date)`
26. **Identify Outliers (Salaries > 3 Standard Deviations)**: Calculate average and standard deviation using window functions: `WHERE salary > avg_sal + (3 * stddev_sal)`.
27. **Find Products Never Ordered**: Use `NOT EXISTS` to exclude products present in the `OrderItems` table.
28. **Find Users Active on the Day of Their Signup**: Join `Users` table with `Activity` table on `signup_date = activity_date`.
29. **Count Consecutive Login Streaks**: (Similar to consecutive active users pattern).
30. **Convert Column Delimited Text to Rows**: Use database-specific string splitting functions (like `json_each` or `regexp_split_to_table`).
31. **Find Top 10% Earners**: Use `NTILE(10)` or `PERCENT_RANK()` window functions.
32. **Find Projects with Overlapping Timelines**: Self-join on project table: `ON p1.id != p2.id AND p1.start_date <= p2.end_date AND p1.end_date >= p2.start_date`.
33. **Calculate Turnaround Time (TAT)**: Calculate the difference between completion time and creation time: `DATEDIFF(end_time, start_time)`.
34. **Find Customers Who Bought Product A but Not Product B**: `SELECT customer_id WHERE product = 'A' EXCEPT SELECT customer_id WHERE product = 'B'`.
35. **Convert JSON Column Keys to Table Columns**: Use JSON extraction operators like `->` or `JSON_EXTRACT()`.
36. **Find Employees Hired in the Last 30 Days**: `WHERE hire_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)`
37. **Find the Longest Session Duration for Each User**: Group by session and use `MAX(end_time - start_time)`.
38. **Zero Value Handling in Division**: Use `NULLIF(divisor, 0)` to prevent division-by-zero errors.
39. **Find Users Who Logged In Every Single Day This Month**: `GROUP BY user_id HAVING COUNT(DISTINCT DATE(login_time)) = 30` (or matching month days).
40. **Combine Rows to Comma Separated Strings**: Use `GROUP_CONCAT()` in MySQL or `STRING_AGG()` in PostgreSQL.
41. **Find the Rank of a Specific Employee Without Window Functions**: Count how many employees earn more: `SELECT COUNT(*) + 1 FROM Employees WHERE salary > TargetSalary`.
42. **Compute Daily Run-rate**: Multiply daily sales by the remaining days in the month.
43. **Find the Shortest and Longest City Name**: Order by length ascending and descending, and use `LIMIT 1` for each.
44. **Match Users with the Same IP Address**: Self-join `Users` table on `ip_address` where `u1.id < u2.id` (to avoid duplicate pairs).
45. **Find Users Who Haven't Logged In for 6 Months**: `WHERE last_login < DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`
46. **Calculate Retention Cohorts**: Group users by signup month, then calculate the percentage active in subsequent months.
47. **Find the Peak Hour of System Load**: Group transactions by hour: `GROUP BY EXTRACT(HOUR FROM transaction_time) ORDER BY COUNT(*) DESC LIMIT 1`.
48. **Swap Gender Values in a Single Update Query**: Use conditional updates: `UPDATE Table SET gender = CASE WHEN gender = 'M' THEN 'F' ELSE 'M' END`.
49. **Find the Nth Smallest Value**: Sort ascending and select the Nth row: `ORDER BY col ASC LIMIT 1 OFFSET N-1`.
50. **Compare Current Sales to Previous Day's Sales**: Use `LAG` to get yesterday's sales: `SELECT sales - LAG(sales, 1) OVER(ORDER BY date)`.

---
---

## HR + SQL Combined Questions

### Why use indexes?
⭐⭐⭐⭐⭐ *Very Frequently Asked*
- **Answer**: "Indexes speed up data retrieval operations. Instead of performing a linear scan through the entire table ($O(N)$), the database engine uses a search tree structure (usually B-Trees) to locate matching rows in $O(\log N)$ time. However, indexes introduce storage overhead and degrade write performance (`INSERT`, `UPDATE`, `DELETE`) because the index tree must be updated on every write."

### Difference between clustered and non-clustered indexes?
⭐⭐⭐⭐⭐ *Very Frequently Asked*
- **Answer**: "A clustered index determines the physical order in which data rows are sorted and stored on disk. Because data can only be sorted in one way, a table can have only one clustered index. A non-clustered index stores index key values alongside a pointer to the physical data rows (bookmarks). A table can have multiple non-clustered indexes."

### Why does GROUP BY execute before HAVING, and WHERE execute before GROUP BY?
⭐⭐⭐⭐⭐ *Very Frequently Asked*
- **Answer**: "The execution order exists to optimize performance. The engine must first filter out irrelevant rows using `WHERE` to minimize the dataset. Next, it aggregates the remaining rows into groups using `GROUP BY`. Finally, it filters those aggregated groups using `HAVING`. Because `WHERE` runs before grouping, it cannot reference aggregate values."

### Difference between RANK and DENSE_RANK?
⭐⭐⭐⭐⭐ *Very Frequently Asked*
- **Answer**: "Both functions rank rows within a sorted window partition. If there is a tie, both assign the same rank. However, `RANK` skips ranks for subsequent rows (e.g. 1, 2, 2, 4), whereas `DENSE_RANK` does not skip ranks (e.g. 1, 2, 2, 3)."

### What happens after a COMMIT transaction is executed?
⭐⭐⭐⭐ *Frequently Asked*
- **Answer**: "When a transaction commits, the changes are saved permanently. The engine writes the changes to the transaction log on disk (Write-Ahead Log) to guarantee durability under ACID rules. Any locks held on the modified rows are released, making the updated data visible to other transactions."

---
---

## SQL Execution Order
⭐⭐⭐⭐⭐ *Very Frequently Asked*

While we write SQL starting with `SELECT`, the database engine evaluates queries in a different order to establish data flows and optimize execution paths.

### Execution Order Flowchart
```
[1] FROM / JOIN       --> Locate and join target source tables
[2] WHERE             --> Filter raw rows
[3] GROUP BY          --> Group rows into buckets
[4] HAVING            --> Filter grouped buckets
[5] SELECT            --> Project selected output columns
[6] DISTINCT          --> Deduplicate projected rows
[7] ORDER BY          --> Sort final rows
[8] LIMIT / OFFSET    --> Paginate output slice
```

### Why this matters in interviews:
1. **AS Aliases**: You cannot use column aliases defined in the `SELECT` clause inside the `WHERE` clause because `WHERE` is executed before `SELECT`.
2. **Aggregate Filters**: You cannot filter aggregates in `WHERE` because grouping and aggregation occur *after* the `WHERE` clause has filtered the raw rows.

---
---

## Cheat Sheet & Revision Guide

### Memory Tricks
- `WHERE` -> Filter rows before grouping.
- `HAVING` -> Filter groups after grouping.
- `LEFT JOIN` -> Keep all left rows, fill right with NULLs if no match.
- `UNION` -> Merges and removes duplicates.
- `UNION ALL` -> Merges and keeps duplicates (faster).
- `ROW_NUMBER` -> Always unique sequential integers.
- `RANK` -> Skips rank values after a tie.
- `DENSE_RANK` -> No skipped ranks.

### Syntax Quick Reference
```sql
-- Paging Template
SELECT col FROM Tab ORDER BY col LIMIT 10 OFFSET 20;

-- Window Function Template
SELECT col, RANK() OVER(PARTITION BY category ORDER BY sales DESC) FROM Tab;

-- Simple CTE
WITH TempCTE AS (SELECT col FROM Tab) SELECT * FROM TempCTE;

-- Safe Division Template
SELECT val / NULLIF(divisor, 0) FROM Tab;
```

### Join Summary Table
| Join Type | Left Rows Preserved | Right Rows Preserved | Unmatched Rows Output |
|---|---|---|---|
| **INNER JOIN** | Match Only | Match Only | Excluded |
| **INNER JOIN** | Match Only | Match Only | Excluded |
| **LEFT JOIN** | All | Match Only | Left + NULLs |
| **RIGHT JOIN** | Match Only | All | Right + NULLs |
| **FULL JOIN** | All | All | Both + NULLs |
| **CROSS JOIN** | Cartesian Product ($N \times M$ rows) | | |

### ACID Quick Summary
- **A**tomicity: All actions succeed, or all fail.
- **C**onsistency: System rules and constraints are preserved.
- **I**solation: Transactions do not interfere with each other.
- **D**urability: Committed changes survive system crashes.
