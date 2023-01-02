#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number in to a node
 *
 * @head: a double pointer to the start node
 * @number: the data to be inserted in the node
 *
 * Return: address of the node the number was added
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *curr, *prev;

	new_node = prev = curr = NULL;
	if (!*head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	curr = *head;
	while (curr)
	{
		prev = curr;
		curr = curr->next;
		if (prev->n <= number && curr->n >= number)
		{
			new_node->next = curr;
			prev->next = new_node;
			return (new_node);
		}
		if (prev->n <= number && curr == NULL)
		{
			prev->next = new_node;
			return (new_node);
		}
		if (number < 0)
		{
			new_node = (*head)->next;
			*head = new_node;
			return (new_node);
		}
	}
	return (NULL);
}
