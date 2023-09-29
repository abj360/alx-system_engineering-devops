#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * infinite_while - infintite while loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0
 */
int main(void)
{
	pid_t zombie;
	int i = 5;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie > 0)
			printf("Zombie process created, PID: %d\n", zombie);
		else
			exit(0);
	}
	infinite_while();

	return (0);
}
