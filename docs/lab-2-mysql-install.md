# Lab 2 Final

**Source:** [`Lab 2 Final.docx`](../archive/canvas-submissions/Lab%202%20Final.docx)  
**Course:** IA 385 - Database and Web Application Security (EMU)  
**Author:** Julio Barros

## Assignment 2: Install MySQL

Julio Barros

Eastern Michigan University

IA 385: Database & Web App Security

Professor (or Dr.) Rachel Kinsella

10/08/2023

### Installing the MySQL

### First, I began by opening my Ubuntu machine. After opening the terminal on the Ubuntu system, I added the command "sudo apt update" to check and make sure my system was updated and free of any bugs. After running the update package, I needed to open the terminal again to start the process of downloading MySQL. Using the command "sudo apt install mysql-server," I was able to create and install MySQL. During the installation, I had to set the root password for MySQL, and I chose to use the classic "P@ssword" for my SQL. The only issue I encountered during the installation was an error with the update because my initial update package crashed and was not completed until I restarted the machine and ran the update again.

### Setting up SQL was easier than I thought. I followed the instructions in the video I was watching and followed the steps, such as opening the terminal to ensure that MySQL was properly installed. I also made sure to enable automatic boot using the command "sudo systemctl enable mysql" to avoid future problems when I forgot to open MySQL. From this point, my SQL was pretty much set up to run while I used my virtual machine. The only issue I faced in this step was that the MySQL service failed to start after I restarted my machine. To solve this, I checked Stack Overflow to see if other users had encountered this problem before and how they fixed it. The easiest way to fix it was to run a log scan and check for any anomalies using this command (/var/log/mysql/error.log). In my case, it was a configuration conflict. Now, I had to focus on securing my server to improve my experience and my server's security.

### Adding Secure the MySQL Installation:

### I had to run a specific script to enhance the server's security. Using the prompt "sudo mysql_secure_installation," I added the package to my machine. During the installation, there were several questions that I had to answer. Here were my answers to solve them:

### Enter the root password you set during installation.

### Remove anonymous users: Answer "Y" (Yes).

### Disallow root login remotely: Answer "Y" (Yes).

### Remove the test database and access to it: Answer "Y" (Yes).

### Reload privilege tables now: Answer "Y" (Yes).

### After that, my SQL was ready to receive a non-admin user. Using the prompt "sudo mysql -u root -p," a password request was prompted in my terminal, and I used the password I had chosen earlier. After gaining admin access, I executed the command "CREATE USER 'Julio Barros'@'localhost' IDENTIFIED BY '123456';" to create a user. Now, I needed to give access to this user using the command "GRANT SELECT ON documents TO 'Julio Barros'@'localhost';" so that this user could access the "documents" folder. I could give more access to this user, but I wasn't sure if it was necessary, so for now, I just created one to ensure that the command was working properly. To complete all the changes, I had to run the scripts "FLUSH PRIVILEGES;" and "EXIT;" so that all the changes were applied and ran properly. In this step, I did not encounter any issues. However, according to Stack Overflow, the most common error for this step is syntax errors or permission issues when creating a non-admin user and granting privileges. Therefore, it's important to double-check your SQL statements for syntax errors and ensure that you have the necessary privileges to create users and grant permissions, which typically requires root access. Additionally, verify that the database you're granting access to exists.

### References

Stack Overflow. (2017, February 22). Job for mysqld.service failed. See 'systemctl status mysqld.service'. https://stackoverflow.com/questions/42317139/job-for-mysqld-service-failed-see-systemctl-status-mysqld-service

Stack Overflow. (n.d.). The Definitive Guide to Form-Based Website Authentication. Stack Overflow. https://stackoverflow.com/questions/549/the-definitive-guide-to-form-based-website-authentication/477578#477578

YouTube. (2022, December 23). Setup MS SQL server 2022 on ubuntu 20.04 LTS. YouTube. https://www.youtube.com/watch?v=QuP8k66pYdM

YouTube. (2023, April 4). Installing SQL Server on linux. YouTube. https://www.youtube.com/watch?v=GBboALYvvuE
