#include "lists.h"
/**
* is_palindrome - checks if the list get is a palindrome
* @head: pointer to list
* Return: 1 if the list is palidrome or 0 is not
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *temp2 = *head;
	int len, i, j, array[1024];

	if (!head)
		return (0);

	if (!*head || (*head)->next == NULL)
		return (1);

	for (len = 0; temp->next != NULL; len++)
		temp = temp->next;

	for (i = 0; i <= len; i++)
	{
		array[i] = temp2->n;
		temp2 = temp2->next;
	}
	for (j = 0, len; j < len; j++, len--)
	{
		if (array[len] != array[j])
			return (0);
	}
	return (1);
}