# 0x0C. Web server
In this directory, we will find a compilation of files that will help us to understand the concept of web sever and how to automtisize several commands using the NginiX and help us to answer the next questions:
-   What is the main role of a web server
-   What is a child process
-   Why web servers usually have a parent process and child processes
-   What are the main HTTP requests

## Files

 - 0-transfer_file is a Bash script that transfers a file from our client to a server:
 - 1-install_nginx_web_server is a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
 - 2-setup_a_domain_name is -   provide the domain name only (example:  `foobar.tech`), no subdomain (example:  `www.foobar.tech`)
-   configure your DNS records with an A entry so that your root domain points to your  `web-01`  IP address
- 3-redirection is configure your Nginx server so that `/redirect_me` is redirecting to another page.
- 4-not_found_page_404 is Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.