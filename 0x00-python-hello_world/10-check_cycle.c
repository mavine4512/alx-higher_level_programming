#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The list to check
 *
 * Return: 0 on success, 1 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

