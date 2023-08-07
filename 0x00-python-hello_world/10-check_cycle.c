include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The list to check
 *
 * Return: 0 on success, 1 on failure
 */
int check_cycle(linkint_t list)
{
	listint_t *i = list, *tortoise = list

		if (list == NULL)
		{
			while (i && i->next)
			{
				i = i->next->next;
				tortoise = tortoise->next;
				if (i == tortoise)
				{
					tortoise = list;
					while (tortoise != i)
					{
						tortoise = tortoise->next;
						i = i->next;
					}
					return (1);
				}
			}
		}
	return (0);
}

