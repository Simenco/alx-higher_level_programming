#include "lists.h"

/**
 * check_cycle - this function checks if a singly linked list has a cycle in it
 * @list: a linked list to be checked
 *
 * Return: if there is no cycle returns 0, else 1.
 */

int check_cycle(listint_t *list)
{
	/* this approach uses two pointers to iterate through the list */

	listint_t *iterator1, *iterator2;

	/* check if the list is not empty or just having 1 node */
	if (list == NULL || list->next == NULL)
		return (0);

	/* iterator1 moves 1 step while iterator 2 moves 2 steps each time*/

	iterator1 = list->next;
	iterator2 = list->next->next;

	while (iterator1 && iterator2 && iterator2->next)
	{
		if (iterator1 == iterator2)
		{
			return (1);
		}

		iterator1 = iterator1->next;
		iterator2 = iterator2->next->next;
	}

	return (0);

}
