#include "lists.h"

/*
 * insertNode - Inserts a new node into a sorted linked list
 * @head: Pointer to the head of the linked list
 * @number: The data value to be stored in the new node
 *
 * Returns: The address of the new node or NULL on failure
 */

listint_t *insertNode(listint_t **head, int number)
{
listint_t *newNode = malloc(sizeof(listint_t));
if (newNode == NULL)
{
return NULL;
}

newNode->n = number;
newNode->next = NULL;

if (*head == NULL || number <= (*head)->n)
{
newNode->next = *head;
*head = newNode;
return newNode;
}

listint_t *current = *head;
listint_t *prev = NULL;

while (current != NULL && number > current->n)
{
prev = current;
current = current->next;
}

prev->next = newNode;
newNode->next = current;

return newNode;
}
