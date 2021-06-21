## 0x05. Processes and signals
In this frepositorty , we will find a compilation of files that will help us to understand concepts and aplicactions related to the uses of PID creation and deletion of process and help us to answer the next questions:

-   What is a PID
-   What is a process
-   How to find a process’ PID
-   How to kill a process
-   What is a signal
-   What are the 2 signals that cannot be ignored

## Files
 - 0-what-is-my-pid is a Bash script that displays its own PID.
 - 1-list_your_processes is a Bash script that displays a list of currently running processes.
 - 2-show_your_bash_pid is a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
 - 3-show_your_bash_pid_made_easy is a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
 - 4-to_infinity_and_beyond is 4-to_infinity_and_beyond
 - 5-dont_stop_me_now is a Bash script that stops `4-to_infinity_and_beyond` process.
 - 6-stop_me_if_you_can is a Bash script that stops `4-to_infinity_and_beyond` process.
 - 7-highlander is a Bash script that displays:
    `To infinity and beyond`  indefinitely
     With a  `sleep 2`  in between each iteration
     `I am invincible!!!`  when receiving a  `SIGTERM`  signal
- 8-beheaded_process is a Bash script that kills the process `7-highlander`.