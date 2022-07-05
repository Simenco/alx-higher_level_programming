#include "lists.h"

/**
 * check_cycle - this function checks if a singly linked list has a cycle in it
 * 
 * @list: a linked list to be checked
 *
 * Return: if there is no cycle returns 0, else 1.
 */

int check_cycle(listint_t *list)
{

	/* this approach uses two pointers to iterate through the list */

	listint_t *iterator1 = malloc(sizeof(listint_t));
	listint_t *iterator2 = malloc(sizeof(listint_t));

	/* check if the list is not empty */
	if (list == NULL)
		return (0);

	iterator1 = list;
	iterator2 = list;

	/* let iterator1 move 1 step while iterator2 move 2 steps per iteration */
	while (1)
	{
		iterator1->next = iterator1;
		(iterator2->next) -> next = iterator2;

		if (iterator1->next == iterator2->next)
		{
			/*free(iterator2->next);*/
			return (1);
		}
		if ((iterator1->next == NULL) || (iterator2->next == NULL))
		{
			/*free(iterator1->next);
			free(iterator2->next);*/
			return (0);
		}
		else
			continue;
	}
	free(iterator1->next);
	free(iterator2->next);

}
