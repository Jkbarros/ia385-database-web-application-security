# Assignment 5

**Source:** [`Assignment 5.docx`](../archive/canvas-submissions/Assignment%205.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

### Creating Users and Roles

### Connect to MySQL and create the users:

### CREATE USER 'NLitzinger'@'localhost' IDENTIFIED BY 'Dubrucr90';

### CREATE USER 'HMimnaugh'@'localhost' IDENTIFIED BY 'EvCsvds01';

### CREATE USER 'TylerM'@'localhost' IDENTIFIED BY 'Fwdtwet12';

### Grant SELECT and UPDATE permissions to NLitzinger on the 'clients' table

### GRANT SELECT, UPDATE ON Server1 TO 'NLitzinger'@'localhost';

### Grant SELECT and DELETE permissions to HMimnaugh on the 'clients' table

### GRANT SELECT, DELETE Server1 TO 'HMimnaugh'@'localhost';

### Grant SELECT and INSERT permissions to TylerM on the 'clients' table

### GRANT SELECT, INSERT ON Server1 TO 'TylerM'@'localhost';

### Create role Most_Privileged

### CREATE ROLE Most_Privileged;

### Grant UPDATE and DELETE permissions on the 'clients' table to Most_Privileged

### GRANT UPDATE, DELETE ON Server1 TO Most_Privileged;

Add all users to the Most_Privileged role;

GRANT Most_Privileged TO 'NLitzinger'@'localhost', 'HMimnaugh'@'localhost', 'TylerM'@'localhost';

### Password Policy

-- Set password complexity as a necessity

```sql
SET GLOBAL validate_password.policy = 'MEDIUM';
```

-- Set the minimum password length to seven characters

```sql
SET GLOBAL validate_password.length = 7;
```

-- Allow users to reuse passwords after a minimum of 10 changes

```sql
SET GLOBAL validate_password.reuse = 10;
```

-- Lock accounts after more than three failed login attempts

```sql
SET GLOBAL max_connect_errors = 3;
```

-- Expire passwords every 60 days

```sql
ALTER USER 'NLitzinger'@'localhost' PASSWORD EXPIRE INTERVAL 60 DAY;
```

```sql
ALTER USER 'HMimnaugh'@'localhost' PASSWORD EXPIRE INTERVAL 60 DAY;
```

```sql
ALTER USER 'TylerM'@'localhost' PASSWORD EXPIRE INTERVAL 60 DAY;
```

### References

Saxon, C. (n.d.). How to create users, grant them privileges, and remove them in Oracle Database. Oracle Blogs. https://blogs.oracle.com/sql/post/how-to-create-users-grant-them-privileges-and-remove-them-in-oracle-database

Chapter 6 installing the MySQL Password Validation Component. MySQL. (n.d.). https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/secure-deployment-password-validation.html

G., D. (2023, July 18). How to create mysql user and grant privileges in 2023. Hostinger Tutorials. https://www.hostinger.com/tutorials/mysql/how-create-mysql-user-and-grant-permissions-command-line
