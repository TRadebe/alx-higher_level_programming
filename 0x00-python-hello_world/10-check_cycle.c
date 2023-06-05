#include "list.h"

/**
 * struct Node - Structure for a linked list node
 * @data: The data stored in the node
 * @next: Pointer to the next node in the linked list
 */
typedef struct Node {
int data;
struct Node* next;
} listint_t;

/**
 * check_cycle - Checks if a linked list contains a loop or not
 *
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if no loop is present, 1 if loop is present
 */

int check_cycle(listint_t *list)
{
listint_t *current = list;
while (current != NULL)
{
if (current->data == -1)
return (1); /* Detected a loop */

current->data = -1; /* Mark the node as visited */
current = current->next;
}

return (0); /* No loop found */
}

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
listint_t *head = malloc(sizeof(listint_t));
head->data = 1;

head->next = malloc(sizeof(listint_t));
head->next->data = 2;

head->next->next = malloc(sizeof(listint_t));
head->next->next->data = 3;

head->next->next->next = head; /* Creating a cycle by pointing the last node to the head */

int hasCycle = check_cycle(head);
if (hasCycle)
printf("The linked list contains a cycle.\n");
else
printf("The linked list does not contain a cycle.\n");

free(head->next->next);
free(head->next);
free(head);

return (0);
}
