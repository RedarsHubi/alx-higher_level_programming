#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
  * insert_node - inserts node in sorted list
  * @head: head of list
  * @number: num to insert
  * Return: address of new node, or NULL
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = *head;

	new = malloc(sizeof(listint_t));
	temp = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		 *head = new;
	}
	else
	{
		while (temp != NULL && (temp->n) < number)
			temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	if (new == NULL)
		return (NULL);
	if (temp == NULL)
		return (NULL);
	return (new);
}
