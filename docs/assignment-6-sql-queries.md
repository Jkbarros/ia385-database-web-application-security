# Assignment 6

**Source:** [`Assignment 6.docx`](../archive/canvas-submissions/Assignment%206.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

To find Mary's phone number, Kevin's address, and search for the first name or last name, you can use the following SQL queries:

```sql
SELECT PhoneNumber FROM Haphazard WHERE FirstName = 'Mary';
```

```sql
SELECT Address FROM Haphazard WHERE FirstName = 'Kevin';
```

```sql
SELECT * FROM Haphazard WHERE FirstName = 'John' OR LastName = 'John';
```

In this case, we are using the SELECT statement to retrieve data from the 'Haphazard' table. We are filtering the data using the WHERE clause, specifying that we only want to retrieve the rows where the FirstName is 'Mary' or 'Kevin', or where the FirstName or LastName is 'John'.

As for searching for 'or 1=1 --' and 'or '1'=1--', SQL does not allow you to search for strings like this using a regular SELECT statement, as the database will interpret it as an attempt to perform a SQL injection attack.

Instead, you can use parameterized queries to achieve this. However, the actual implementation of parameterized queries can vary depending on the database system you are using.

In SQL Server, you can use parameterized queries with the SqlCommand class in ADO.NET.

string connectionString = "Server=(local);Database=HaphazardInc;Integrated Security=True";

string searchQuery = "SELECT * FROM clients WHERE first_name LIKE @first_name OR last_name LIKE @last_name";

using (SqlConnection connection = new SqlConnection(connectionString))

{

connection.Open();

using (SqlCommand command = new SqlCommand(searchQuery, connection))

{

command.Parameters.AddWithValue("@first_name", "%or 1=1 --%");

command.Parameters.AddWithValue("@last_name", "%or '1'=1--%");

using (SqlDataReader reader = command.ExecuteReader())

{

while (reader.Read())

{

Console.WriteLine(string.Format("ClientID: {0}, First Name: {1}, Last Name: {2}", reader["client_id"], reader["first_name"], reader["last_name"]));

}

}

}

}`

This code sets up a parameterized query using the provided search terms, then executes the query and processes the results. This approach ensures that the SQL query and the data used to build the query are kept separate, reducing the risk of SQL injection attacks.

Find Mary's phone number:

```sql
SELECT phone_number
```

FROM clients

WHERE first_name = 'Mary';

Find Kevin's address:

```sql
SELECT address
```

FROM clients

WHERE first_name = 'Kevin';

// ...

command.Parameters.AddWithValue("@first_name", "Kevin");

command.Parameters.AddWithValue("@last_name", "Brown");

Search for your own first name or last name:

```sql
SELECT *
```

FROM clients

WHERE first_name = 'YourFirstName'

OR last_name = 'YourLastName';

Search for 'or 1= 1 --':

```sql
SELECT *
```

FROM clients

WHERE first_name = 'or 1=1 --'

OR last_name = 'or 1=1 --'

OR email = 'or 1=1 --'

OR phone_number = 'or 1=1 --'

OR address = 'or 1=1 --';

Search for 'or '1'= 1--':

```sql
SELECT *
```

FROM clients

WHERE first_name = 'or '1'=1--'

OR last_name = 'or '1'=1--'

OR email = 'or '1'=1--'

OR phone_number = 'or '1'=1--'

OR address = 'or '1'=1--';

Please make sure to replace 'your_first_name' and 'your_last_name' with your actual first and last names. For example, Your_first_name = John and your_last_name = Doe. To find information about John.

Troubleshooting

To troubleshoot these issues, you can check the SQL query for syntax errors, verify that the correct parameters are being provided, and ensure that the table and column names are correct and that the values provided match the expected data types. Additionally, you can check the application's error logs and database server logs for any additional information that may help identify the issue.

Invalid SQL syntax: This can occur if there is an error in the SQL query.

Missing or incorrect parameters: This can happen if the SQL query expects parameters but none are provided, or if the parameters provided do not match the SQL query.

Invalid table or column names: This can occur if the table or column names in the SQL query do not match the actual table or column names in the data base.

Data type mismatch: This can occur if the values provided as parameters do not match the data types of the corresponding columns in the data base.

Null or empty values: This can occur if the SQL query expects non-null or non-empty values for certain parameters or columns, but null or empty values are provided.

Insufficient permissions: This can occur if the user executing the SQL query does not have the necessary permissions to access the specified table or column.

Timeout errors: This can occur if the SQL query takes too long to execute, which may be due to issues such as a large amount of data needing to be processed, network latency, or database server issues.

Database connection issues: This can occur if there is a problem with the connection between the application and the database server, such as network connectivity problems, a misconfigured connection string, or issues with the database server itself.
