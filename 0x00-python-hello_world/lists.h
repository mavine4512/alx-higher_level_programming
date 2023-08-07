#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
 * struct listint_s - singly linked list
 * @n: interger number
 * @next: pointer to the next node
 *
 * Description: Singly linked list node structure
 * for HOLberton Project 
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_s;

size_t print_listint(const listint_t *h);
listint_t *add_node(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif
