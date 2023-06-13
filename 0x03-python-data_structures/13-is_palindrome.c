#include <stddef.h>
#include "lists.h"

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - this function reverses a singly
 * linked list listint_t.
 * @head: A pointer to the starting node of
 * the list to reverse.
 *
 * Return: the pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;

	return (*head);
}
/**
 * is_palindrome - this function checks if a singly linked
 * list is a palindorme
 * @head: the pointer to the head of the linked list.
 *
 * Return: 1 (Success) if the linked list is a
 * palindrome otherwise 0(failure) the linked
 * list is not a palindrome.
 */
int is_palindrome(listint_t **head)
{
	size_t size = 0, i;
	listint_t *tmp, *rev, *mid;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
	{
		tmp = tmp->next;
	}

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
	{
		return (0);
	}
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
		{
			return (0);
		}
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
