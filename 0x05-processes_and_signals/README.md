# Processes and Signals

### 0-what-is-my-pid

	Displays it's own PID

### 1-list_your_processes

	Displays a list of currently running processes

### 2-show_your_bash_pid

	Displays a list of currently running processes containing the word "bash"

### 3-show_your_bash_pid_made_easy

	Displays the PID, along with the process name, of processes whose name contain the word bash

### 4-to_infinity_and_beyond

	Displays "To infinity and beyond" indefinitely

### 5-dont_stop_me_now

	Stops 4-to_infinity_and_beyond process

### 6-stop_me_if_you_can

	Stops 4-to_infinity_and_beyond process


### 7-highlander

	Displays:

		* To infinity and beyond indefinitely
		* With a sleep 2 in between each iteration
		* I am invincible!!! when receiving a SIGTERM signal

### 8-beheaded_process

	Kills 7-highlander

### 100-process_and_pid_file

	* Creates the file /var/run/myscript.pid containing its PID
	* Displays To infinity and beyond indefinitely
	* Displays I hate the kill command when receiving a SIGTERM signal
	* Displays Y U no love me?! when receiving a SIGINT signal
	* Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

### manage_my_process

	Indefinitely writes "I am alive!" to /tmp/my_process

### 101-manage_my_process

	Manages manage_my_process.

	Requirements:

	* When passing the argument start:
		* Starts manage_my_process
		* Creates a file containing its PID in /var/run/my_process.pid
		* Displays manage_my_process started
	* When passing the argument stop:
		* Stops manage_my_process
		* Deletes the file /var/run/my_process.pid
		* Displays manage_my_process stopped
	* When passing the argument restart
		* Stops manage_my_process
		* Deletes the file /var/run/my_process.pid
		* Starts manage_my_process
		* Creates a file containing its PID in /var/run/my_process.pid
		* Displays manage_my_process restarted
	* Displays Usage: manage_my_process {start|stop|restart} if any other argument or no argument is passed

### 102-zombie.c

	Creates 5 zombie processes
