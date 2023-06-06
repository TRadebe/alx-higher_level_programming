#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/* Structure for a linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to insert a new node into a sorted linked list */
listint_t *insertNode(listint_t **head, int number);

#endif /* LISTS_H */
