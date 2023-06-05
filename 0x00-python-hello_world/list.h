#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

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
 * create_node - Creates a new node with the given data
 *
 * @data: The data to be stored in the node
 *
 * Return: A pointer to the newly created node
 */
listint_t *create_node(int data);

/**
 * add_node - Adds a new node with the given data to the list
 *
 * @list: Pointer to the head of the list
 * @data: The data to be stored in the new node
 */
void add_node(listint_t **list, int data);

/**
 * free_list - Frees the memory allocated for the list
 *
 * @list: Pointer to the head of the list
 */
void free_list(listint_t *list);

/**
 * print_list - Prints the elements in the list
 *
 * @list: Pointer to the head of the list
 */
void print_list(listint_t *list);

/**
 * check_cycle - Checks if a linked list contains a loop or not
 *
 * @list: Pointer to the head of the linked list
 *
 * Return: 0 if no loop is present, 1 if loop is present
 */
int check_cycle(listint_t *list);

#endif /* LIST_H */

