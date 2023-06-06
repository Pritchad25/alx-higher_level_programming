#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - this function inserts a number into a
 * sorted singly linked list.
 * @head: the pointer to the head of the linked list
 * @number: the number to insert in the linked list
 *
 * Return: the pointer to the new node(Success), otherwise
 * NULL if the function fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *runner;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (runner->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new->next = runner->next;
			runner->next = new;

			return (new);
		}

		runner = runner->next;
	}
	new->next = NULL;
	runner->next = new;

	return (new);
}
