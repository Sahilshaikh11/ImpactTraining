#include <stdio.h>

typedef struct node
{
    int data;
    struct node *next;
    struct node *perv;
}NODE;

void dispFList(NODE *);
void dispBList(NODE *);

int main()
{
    NODE n1,n2,n3,n4;
    NODE *head=NULL,*temp=NULL;

    n1.data = 10;
    n1.next = NULL;
    n1.perv = NULL;

    n2.data = 20;
    n2.next = NULL;
    n2.perv = NULL;

    n3.data = 30;
    n3.next = NULL;
    n3.perv = NULL;

    n1.next = &n2;
    n2.perv = &n1;
    n2.next = &n3;
    n3.perv = &n2;

    head = &n1;
    temp = head;

    dispFList(temp);

    dispBList(temp);
    return 0;
}

void dispFList(NODE *t)
{
    printf("\nList is\n");
    while(t)
    {
        printf("%d->", t->data);
        t = t->next;
    }
    printf("NULL\n\n");
}

void dispBList(NODE *t)
{
    printf("\bBackward List\n");
    while(t->next != NULL)
    {
        t = t->next;
    }
    // printf("\nBL: %d",t->data);

    while(t)
    {
        printf("%d->", t->data);
        t = t->perv;
    }
    printf("NULL\n\n");
}