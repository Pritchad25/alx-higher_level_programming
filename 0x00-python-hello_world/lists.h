#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - the singly linked list
 * @n: the integer
 * @next: the points to the next node
 *
 * Description: the singly linked list node structure for
 * the Holberton Project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);

#endif /* LISTS_H */
