
# 0x19. Postmortem

-   ## Issue Summary:
    

-   Start time: 09/07/21 9:00 am (GMT-5), End time: 24/09/21 11:00 AM (GMT-5).
    
-   MySQL ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
    
-   Root cause: the system cant connect to the credential file of Mysql
    

  

-   ## Timeline:
    

-   The issue was detected by the user recognized by the id 2753 and continuously work trying to fix it.
    
-   The identification problem could be related to the Ubuntu version, in the first case the task was developed to work in ubuntu 14.04 and the user was using ubuntu 20.04.
    
-   This version of Ubuntu comes with a database management system known as MariaDB, a database open source-based in MySQL, for that reason MySQL is already installed but isn’t configure.
    
-   The first way to solve this problem is to initialize the MySQL with the next command: “sudo service mysql start”
    
-   Try to access MySQL by the command “mysql -uroot -p” with this command we are trying to access to MySQL using the root user, but if MariaDB is already installed is probably can´t access the root user even using root as a password.
    
-   The next step is resetting the password of the root user to access MySQL
    
-   “sudo /etc/init.d/mysql stop” to stop the MySQL server if it is running.
    
-   “sudo mkdir /var/run/mysqld” to verify the existence of this directory and if not created
    
-   “sudo chown mysql /var/run/mysqld” to change the permissions of the directory.
    
-   “sudo mysqld_safe --skip-grant-tables&” with this command you will see something similar to this.
    

[1] 1283

user@server:~$ 2019-02-12T11:15:59.872516Z mysqld_safe Logging to syslog.

2019-02-12T11:15:59.879527Z mysqld_safe Logging to '/var/log/mysql/error.log'.

2019-02-12T11:15:59.922502Z mysqld_safe Starting mysqld daemon with databases from /var/lib/mysql

-   Now we can change the password, with the next command we enter to MySQL as a root user. “sudo mysql --user=root mysql”
    
-   Inside MySQL prompt, we send the next commands “UPDATE mysql.user SET authentication_string=null WHERE User='root';”
    
-   “flush privileges;”
    
-   “ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password_here';”
    
-   “flush privileges;”
    
-   “Exit”
    
-   Now when you enter MySQL before the turn off your computer or close your servers you must send the next command “sudo service mysql stop” this is because when you close your system with MySQL open will damage the user’s file and then you will see this problem again but this time as far I can tell there is no way to fix it.
    

  

-   ## Root cause and resolution:
    

-   Using native installed MySQL versions bounded to MariaDB.
    
-   Damage or nonexisting directory of users in MySQL.
    

  

-   ## Corrective and preventative measures:
    

-   Change the user password and be sure the MySQL is online, if you present this issue constantly I recommend you to use docker.