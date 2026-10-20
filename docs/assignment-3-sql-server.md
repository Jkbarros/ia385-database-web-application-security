# Assignment 3

**Source:** [`Assignment 3.docx`](../archive/canvas-submissions/Assignment%203.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

Download the SQL Server Community Edition installer from the Microsoft website. The installation process typically includes these steps: On the download page, you'll see various editions of SQL Server available. Choose the edition that best suits your needs. The Community Edition is typically a good choice for personal or small-scale use. Click on the "Download" button for the edition you've selected. This will initiate the download process. You'll be prompted to select the installation package. SQL Server is available in different formats, including an executable installer and ISO image. The executable installer is easier to work with for most users. Choose your preferred installation language from the available options. After selecting the installation package and language, click the "Download" button once more. Once the download is complete and verified, you can run the installer to start the installation process. When you run the installer, it opens the SQL Server Installation Center. Here you'll find options for installation and additional tools. Choose "New SQL Server stand-alone installation or add feature to an existing installation." Review and accept the license terms. Choose the features you want to install. Ensure you select "Database Engine Services," which is the core SQL Server database component. You can choose to install a Default Instance (SQL Server will use the computer name) or a Named Instance (you specify a name). Most users choose the Default Instance. Configure service accounts. Use the default service accounts for simplicity unless you have specific requirements. Choose authentication mode. It's recommended to use "Mixed Mode" (SQL Server and Windows Authentication). Set a strong password for the "sa" account. You will use this "sa" account initially as an administrator.

Creating a Non-Admin User:

To create a non-admin user in SQL Server, follow these steps:

a. Open SQL Server Management Studio (SSMS), which should be installed along with SQL Server.

b. Log in using the "sa" account or another account with administrative privileges.

c. In SSMS, expand the "Security" folder in the Object Explorer.

d. Right-click on "Logins" and choose "New Login."

e. Enter the user's login name and choose the authentication type (usually SQL Server Authentication).

f. Provide a password for the new user.

g. Under "Server Roles," do not assign the "sysadmin" role. This role grants administrative privileges. Instead, you can assign the user to specific roles or grant the necessary permissions at the database level.

h. Under "User Mapping," select the database(s) where this user should have access. Assign appropriate roles within the database.

i. Click "OK" to create the new user.

The errors I faced were only I was creating the non admin user. The first error was "User cannot be added to role 'xyz' because the role does not exist, or you do not have permission." to fix it i had to create a new role to add the user.

The second error was “A network-related or instance-specific error occurred while establishing a connection to SQL Server." to solve it I had to Ensure SQL Server is running, and that the server instance name is correctly specified in SQL Server.

References

SQL Server downloads. Microsoft. (n.d.). https://www.microsoft.com/en-us/sql-server/sql-server-downloads

YouTube. (2023, February 14). How to install Microsoft SQL server 2022 on Windows 10. YouTube. https://www.youtube.com/watch?v=P6y0R3XzWlc

YouTube. (2020, August 30). Install SQL server 2019 step by step | developer edition | free software | install ssms. YouTube. https://www.youtube.com/watch?v=7GVFYt6_ZFM
