#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *nodeMin = *head;
	listint_t *nodeMax = (*head)->next;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	if (!nodeMin || number <= (*head)->n)
	{
		newNode->next = nodeMin;
		*head = newNode;
		return (newNode);
	}
	if (!nodeMax && nodeMin)
	{
		nodeMin->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	while (nodeMin && nodeMax->next)
	{
		if (nodeMin->n <= number && nodeMax->n >= number)
		{
			newNode->next = nodeMax;
			nodeMin->next = newNode;
			return (newNode);
		}
		nodeMin = nodeMin->next;
		nodeMax = nodeMax->next;
	}
	if (!nodeMax->next)
	{
		nodeMax->next = newNode;
		newNode->next = NULL;
		return (newNode);
	}
	return (newNode);
}