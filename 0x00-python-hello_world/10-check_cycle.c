#include "lists.h"

/**
 * check_cycle - checks if a singly linked list
 * has a cycle in it.
 * @list: head of the list
 * Return: 1 if there is a loop otherwise return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = slow = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
