# 0x0B. SSH
In this directory, we will find a compilation of files that will help us to understand the concept of using ssh keys  and help us to answer the next questions:
-   What is a server
-   Where servers usually live
-   What is SSH
-   How to create an SSH RSA key pair
-   How to connect to a remote host using an SSH RSA key pair
-   The advantage of using  `#!/usr/bin/env bash`  instead of  `/bin/bash`

## Files

 - 0-use_a_private_key is a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/holberton` with the user `ubuntu`.
 - 1-create_ssh_key_pair is a Bash script that creates an RSA key pair.
 - 2-ssh_config is client configuration must be configured to refuse to authenticate using a password
