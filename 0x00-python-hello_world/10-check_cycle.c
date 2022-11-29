#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * has a cycle in it.
 * @list: head of the list
 * Return: 1 if there is a loop otherwise return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *previous = list;

	while (current && current->next)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}

	return (0);
}
