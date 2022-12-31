#include "lists.h"

/**
 * check_cycle - check if the list has a loop
 *
 * @list: is a pointer to the start node
 *
 * Return: a 1 is loop exits or 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = slow = list;
	while (slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
