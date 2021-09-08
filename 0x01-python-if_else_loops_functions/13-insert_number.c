#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = NULL, *headtmp = *head;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;

	if (!headtmp || headtmp->n >= number)
	{
		newnode->next = headtmp;
		*head = newnode;
		return (newnode);
	}

	while (headtmp && headtmp->next && headtmp->next->n < number)
		headtmp = headtmp->next;

	newnode->next = headtmp->next;
	headtmp->next = newnode;

	return (newnode);
}
