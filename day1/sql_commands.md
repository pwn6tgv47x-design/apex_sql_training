# SQL Commands Guide - Day 1

## DDL (Data Definition Language) Commands

DDL commands are used to define and manage database structures.

### CREATE
Creates new database objects (tables, indexes, views, etc.)

```sql
-- Create a table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    emp_email VARCHAR(100) UNIQUE,
    emp_salary DECIMAL(10, 2),
    dept_id INT,
    hire_date DATE DEFAULT CURRENT_DATE
);

-- Create a view
CREATE VIEW active_employees AS
SELECT emp_id, emp_name, emp_email, emp_salary
FROM employees
WHERE emp_status = 'Active';

-- Create an index
CREATE INDEX idx_emp_name ON employees(emp_name);
```

### ALTER
Modifies existing database structures

```sql
-- Add a column
ALTER TABLE employees
ADD COLUMN emp_phone VARCHAR(15);

-- Modify a column
ALTER TABLE employees
MODIFY COLUMN emp_salary DECIMAL(12, 2);

-- Drop a column
ALTER TABLE employees
DROP COLUMN emp_phone;

-- Rename a column
ALTER TABLE employees
RENAME COLUMN emp_email TO employee_email;

-- Rename a table
ALTER TABLE employees
RENAME TO staff;
```

### DROP
Deletes database objects

```sql
-- Drop a table
DROP TABLE employees;

-- Drop a view
DROP VIEW active_employees;

-- Drop an index
DROP INDEX idx_emp_name;
```

### TRUNCATE
Removes all rows from a table without deleting the structure

```sql
-- Truncate a table (faster than DELETE, cannot rollback in some systems)
TRUNCATE TABLE employees;
```

---

## DML (Data Manipulation Language) Commands

DML commands are used to manipulate data within tables.

### INSERT
Adds new records to a table

```sql
-- Insert single record
INSERT INTO employees (emp_id, emp_name, emp_email, emp_salary, dept_id)
VALUES (1, 'John Doe', 'john@example.com', 50000, 10);

-- Insert multiple records
INSERT INTO employees (emp_id, emp_name, emp_email, emp_salary, dept_id)
VALUES 
    (2, 'Jane Smith', 'jane@example.com', 55000, 20),
    (3, 'Mike Johnson', 'mike@example.com', 60000, 10),
    (4, 'Sarah Williams', 'sarah@example.com', 52000, 30);

-- Insert from another table
INSERT INTO employees_backup
SELECT * FROM employees
WHERE dept_id = 10;
```

### UPDATE
Modifies existing records

```sql
-- Update single record
UPDATE employees
SET emp_salary = 52000
WHERE emp_id = 1;

-- Update multiple columns
UPDATE employees
SET emp_salary = emp_salary * 1.10, dept_id = 15
WHERE emp_status = 'Active';

-- Update with JOIN
UPDATE employees
SET emp_salary = emp_salary + 5000
WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name = 'IT');
```

### DELETE
Removes records from a table

```sql
-- Delete specific records
DELETE FROM employees
WHERE emp_id = 1;

-- Delete multiple records with condition
DELETE FROM employees
WHERE emp_salary < 40000;

-- Delete all records (use with caution!)
DELETE FROM employees;

-- Delete with JOIN
DELETE FROM employees
WHERE dept_id NOT IN (SELECT dept_id FROM departments);
```

### SELECT
Retrieves data from tables

```sql
-- Basic SELECT
SELECT emp_id, emp_name, emp_salary
FROM employees;

-- SELECT with WHERE clause
SELECT * FROM employees
WHERE emp_salary > 50000 AND dept_id = 10;

-- SELECT with ORDER BY
SELECT emp_name, emp_salary
FROM employees
ORDER BY emp_salary DESC;

-- SELECT with GROUP BY and HAVING
SELECT dept_id, COUNT(*) as emp_count, AVG(emp_salary) as avg_salary
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2;

-- SELECT with JOIN
SELECT e.emp_name, d.dept_name, e.emp_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- SELECT with DISTINCT
SELECT DISTINCT dept_id
FROM employees;
```

---

## TCL (Transaction Control Language) Commands

TCL commands manage transactions and ensure data consistency.

### COMMIT
Saves all changes made in the current transaction permanently

```sql
INSERT INTO employees (emp_id, emp_name, emp_email, emp_salary, dept_id)
VALUES (5, 'Tom Brown', 'tom@example.com', 48000, 20);

UPDATE employees
SET emp_salary = 51000
WHERE emp_id = 3;

-- Save all changes
COMMIT;
```

### ROLLBACK
Undoes all changes made in the current transaction

```sql
-- Start a transaction
BEGIN;

DELETE FROM employees
WHERE emp_salary < 40000;

-- Undo the delete if something goes wrong
ROLLBACK;

-- All deleted records are restored
```

### SAVEPOINT
Creates a checkpoint within a transaction

```sql
-- Create a savepoint
SAVEPOINT sp1;

DELETE FROM employees
WHERE emp_id = 1;

-- If error occurs, rollback to savepoint
ROLLBACK TO SAVEPOINT sp1;

-- Continue with other operations
INSERT INTO employees (emp_id, emp_name, emp_email, emp_salary, dept_id)
VALUES (6, 'Lisa Anderson', 'lisa@example.com', 54000, 10);

COMMIT;
```

### SET TRANSACTION
Defines transaction properties (Isolation Level, Read/Write mode)

```sql
-- Set transaction as read-only
SET TRANSACTION READ ONLY;

SELECT * FROM employees;

-- Set isolation level
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

-- Set transaction as read-write
SET TRANSACTION READ WRITE;
```

---

## DCL (Data Control Language) Commands

DCL commands manage user permissions and access control.

### GRANT
Gives privileges to users

```sql
-- Grant SELECT privilege
GRANT SELECT ON employees TO user1;

-- Grant multiple privileges
GRANT SELECT, INSERT, UPDATE ON employees TO user2;

-- Grant all privileges
GRANT ALL PRIVILEGES ON employees TO user3;

-- Grant with GRANT OPTION (user can grant to others)
GRANT SELECT ON employees TO user4 WITH GRANT OPTION;

-- Grant on specific columns
GRANT SELECT (emp_name, emp_email) ON employees TO user5;

-- Grant to all users
GRANT SELECT ON employees TO PUBLIC;
```

### REVOKE
Removes privileges from users

```sql
-- Revoke SELECT privilege
REVOKE SELECT ON employees FROM user1;

-- Revoke multiple privileges
REVOKE SELECT, INSERT, UPDATE ON employees FROM user2;

-- Revoke all privileges
REVOKE ALL PRIVILEGES ON employees FROM user3;

-- Revoke GRANT OPTION
REVOKE GRANT OPTION FOR SELECT ON employees FROM user4;

-- Revoke from all users
REVOKE SELECT ON employees FROM PUBLIC;
```

### CREATE USER (and related)
Creates new database users

```sql
-- Create a user
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password123';

-- Create user with specific privileges
CREATE USER 'dbuser'@'192.168.1.%' IDENTIFIED BY 'secure_pass';

-- Alter user password
ALTER USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword456';

-- Drop user
DROP USER 'newuser'@'localhost';
```

---

## Quick Reference Summary

| Command Type | Commands | Purpose |
|---|---|---|
| **DDL** | CREATE, ALTER, DROP, TRUNCATE | Define database structure |
| **DML** | SELECT, INSERT, UPDATE, DELETE | Manipulate data |
| **TCL** | COMMIT, ROLLBACK, SAVEPOINT | Control transactions |
| **DCL** | GRANT, REVOKE, CREATE USER | Control access permissions |

---

## Key Points to Remember

✅ **DDL** - Structural changes (auto-commit in most systems)
✅ **DML** - Data operations (can be rolled back)
✅ **TCL** - Transaction management (COMMIT/ROLLBACK)
✅ **DCL** - Security & permissions (user access control)

---

## Practice Exercises

Try executing these commands in your SQL environment:

1. Create a `departments` table with columns: `dept_id`, `dept_name`, `location`
2. Insert 5 departments
3. Create an `employees` table linked to departments
4. Insert 10 employees
5. Update employee salaries by 10%
6. Create a view for high-salary employees
7. Practice COMMIT and ROLLBACK
8. Create a new user and grant SELECT permission

Happy Learning! 🚀
