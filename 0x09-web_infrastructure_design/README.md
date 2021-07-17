# 0x09. Web infrastructure design
In this directory, we will find a compilation of files that will help us to understand  the concept of  designing a web infrastructure system, be able to draw each step and their functionality help us to answer the next questions:
-   You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
-   You must be able to explain what each component is doing
-   You must be able to explain system redundancy
-   Know all the mentioned acronyms: LAMP, SPOF, QPS

## Files

 - 0-simple_web_stack is a design a one server web infrastructure that hosts the website that is reachable via  `www.foobar.com`. Start your explanation by having a user wanting to access your website.
    -   1 server
    -   1 web server (Nginx)
    -   1 application server
    -   1 application files (your code base)
    -   1 database (MySQL)
    -   1 domain name  `foobar.com`  configured with a  `www`  record that points to your server IP  `8.8.8.8`
  
  - 1-distributed_web_infrastructure is adesign a three server web infrastructure that hosts the website  `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.
    -   3 firewalls
    -   1 SSL certificate to serve  `www.foobar.com`  over HTTPS
    -   3 monitoring clients (data collector for Sumologic or other monitoring services)
 
   - 2-secured_and_monitored_web_infrastructure is a design a three server web infrastructure that hosts the website  `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.
    -   3 firewalls
    -   1 SSL certificate to serve  `www.foobar.com`  over HTTPS
    -   3 monitoring clients (data collector for Sumologic or other monitoring services)