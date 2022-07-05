#include "lists.h"

/**
 * list_len - function
 * @h: input list
 *
 * Return: number of elements in a list
 */
unsigned int list_len(const listint_t *h)
{
	unsigned int n;

	for (n = 0; h; n++)
	{
		h = h->next;
	}
	return (n);

} 

/**
 * check_cycle - this function checks if a singly linked list has a cycle in it
 * @list: a linked list to be checked
 *
 * Return: if there is no cycle returns 0, else 1.
 */

int check_cycle(listint_t *list)
{
	unsigned int n;

	/* this approach uses two pointers to iterate through the list */

	listint_t *iterator1 = malloc(sizeof(listint_t));
	listint_t *iterator2 = malloc(sizeof(listint_t));

	/* check if the list is not empty */
	if (list == NULL)
		return (0);

	n = list_len(list);

	if (n <= 2)
		return (0);

	iterator1 = list;
	iterator2 = list;

	/* let iterator1 move 1 step while iterator2 move 2 steps per iteration */
	while (1)
	{
		iterator1 = iterator1->next;
		iterator2 = (iterator2->next)->next;

		if (iterator1 == iterator2)
		{
			return (1);
		}
		if ((iterator1 == NULL) || (iterator2 == NULL))
		{
			return (0);
		}
		else
			continue;
	}
	free(iterator1);
	free(iterator2);

}
