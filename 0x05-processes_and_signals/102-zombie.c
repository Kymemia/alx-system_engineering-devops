#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - function that runs infinitely
 * Return: Always 0
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
 * main - creates 5 zombie processes
 * Return: if successful, returns 0
 */
int main(void)
{
	int z = 0;
	pid_t pid;

	while (z < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: ZOMBIE PID: %d\n", pid);
		z++;
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
