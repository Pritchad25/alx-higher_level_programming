#include "lists.h"

/**
 * check_cycle - this function checks if a linked list
 * contains a cycle
 * @list: the linked list to check
 * Return: 1(Success) if the linked list has a cycle,
 * 0 (failure) if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
	{
		return (0);
	}
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
