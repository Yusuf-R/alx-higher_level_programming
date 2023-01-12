#include "lists.h"

/**
  * odd_node_case -  Perform odd node action
  *
  * @mid: pointer to the mid point after split
  * @adjuster: to set the end node to null
  * @slow: the pointer from the initail traversing
  *
  * Return: a pointer to the start of the half node
 */

listint_t *odd_node_case(listint_t *mid, listint_t *adjuster, listint_t *slow)
{
	mid = slow->next;
	while (adjuster)
	{
		if (adjuster->next == slow)
		{
			adjuster->next = NULL;
			slow->next = NULL;
			break;
		}
	adjuster = adjuster->next;
	}
	adjuster = NULL;
	return (mid);
}

/**
  * even_node_case -  Perform even node action
  *
  * @mid: pointer to the mid point after split
  * @adjuster: to set the end node to null
  * @slow: the pointer from the initail traversing
  *
  * Return: a pointer to the start of the half node
 */

listint_t *even_node_case(listint_t *mid, listint_t *adjuster, listint_t *slow)
{
	mid = slow->next;
	while (adjuster)
	{
		if (adjuster->next == slow)
		{
			adjuster->next = NULL;
			break;
		}
		adjuster = adjuster->next;
	}
	adjuster = NULL;
	return (mid);
}




/**
  * is_palindrome - a function to check if a list is a palindrome
  *
  * @head: the double pointer to the start of the node
  *
  * Return: return 1 or 0 depending if the True or False
  *
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *mid, *prev, *next, *adjuster;

	if (!head)
		return (0);
	if (!(*head))
		return (1);
	fast = slow = *head;
	mid = prev = next = adjuster = NULL;
	if (fast == NULL || fast->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
	{
		fast = NULL, adjuster = *head;
		mid = odd_node_case(mid, adjuster, slow);
	}
	else if (!fast)
	{
		adjuster = *head, mid = slow;
		mid = even_node_case(mid, adjuster, slow);
	}
	adjuster = NULL;
	while (mid != NULL)
	{
		next = mid->next, mid->next = prev, prev = mid, mid = next;
	}
	while (prev != NULL && *head != NULL)
	{
		if ((*head)->n != prev->n)
			return (0);
		prev = prev->next, *head = (*head)->next;
	}
	return (1);
}
