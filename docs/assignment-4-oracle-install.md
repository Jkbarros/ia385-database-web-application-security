# Assignment 4 Install Oracle 1

**Source:** [`Assignment 4 Install Oracle 1.docx`](../archive/canvas-submissions/Assignment%204%20Install%20Oracle%201.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

### Installing the Oracle

Download the Oracle Database Software:

Visit the Oracle Technology Network (OTN) or Oracle Software Delivery Cloud and download the Oracle Database software for your specific version and operating system. In my case I had the Oracle Software Delivery Cloud already installed in my machine.

Prepare the Server:

Ensure your server meets the system requirements, including memory, disk space, and a compatible operating system.

Create a dedicated user and group for the Oracle installation.

Unzip/Extract the Oracle Software:

Unzip or extract the downloaded software to a location on your server.

Run the Oracle Universal Installer (OUI):

Navigate to the directory where you extracted the Oracle software and locate the "runInstaller" or "setup.exe" executable. Run it.

Perform a Software Only or Database Installation:

During the installation, you can choose to perform a software-only installation or a database installation. The software-only installation sets up the Oracle software without creating a database, while the database installation creates a new database instance.

Follow the Installation Wizard:

The Oracle Universal Installer will guide you through the installation process. You will need to make various configuration choices, including the Oracle home directory, database edition, and other settings.

Configure Oracle Database:

If you chose a database installation, you will need to configure the database by specifying the database name, character set, memory allocation, and other parameters.

Create and Configure Listener:

After the installation, you'll need to create and configure a listener. This is essential for clients to connect to the Oracle database.

Perform Post-Installation Tasks:

You may need to configure environment variables, set up user permissions, and perform other post-installation tasks as specified in the Oracle documentation.

Verify the Installation:

Once the installation and configuration are complete, you should verify that the Oracle Database is running correctly. You can use SQL*Plus or other database management tools to connect and run SQL queries.

Optional: Apply Patches and Updates:

It's good practice to keep your Oracle Database up to date by applying the latest patches and updates.

Back Up Your Database:

It's crucial to establish a backup and recovery strategy to protect your data.

Creating a Non-Admin User

To ensure that the Oracle Database starts up and create a non-admin user, I had to use those commands.

sqlplus / as sysdba

SQL> STARTUP;

This command starts the database in the default instance (SID) as a sysdba user. To create a new user with privileges I used this command.

sqlplus / as sysdba

SQL> CREATE USER Jkbarros IDENTIFIED BY P@ssword;

SQL> GRANT CONNECT, RESOURCE TO Jkbarros;

SQL> ALTER USER Jkbarros QUOTA UNLIMITED ON USERS;

After creating a new user I needed to give Grant Provileges for this user to avoid any problem in the future.

SQL> GRANT CREATE TABLE, INSERT, UPDATE, DELETE TO Jkbarros;

After that I can log in to the new user.

sqlplus Jkbarros/P@ssword.

Possible Problems

This case I haven’t any issues during this assignment since I had worked with Oracle before, the only problem I to figure out how to solve was Network Problems which are Issues with network configuration, including firewall rules, can affect database connectivity. To solve this problem check your network settings and ensure that port and listener configurations are correct. Make sure that any firewalls or security rules allow Oracle Database traffic.

The other problem I had to fix was the insufficient permissions Problem: The user running the installation does not have the necessary permissions.

Solution: Ensure that the installation is run with proper permissions, and the installation directories have the correct permissions. It's often recommended to use a dedicated user for Oracle installations.

### References

YouTube. (2019, July 17). How to install oracle database 19C on windows 10 by Manish Sharma. YouTube. https://www.youtube.com/watch?v=Hnpmy2kB5Mo

Saxon, C. (n.d.). How to create users, grant them privileges, and remove them in Oracle Database. Oracle Blogs. https://blogs.oracle.com/sql/post/how-to-create-users-grant-them-privileges-and-remove-them-in-oracle-database
