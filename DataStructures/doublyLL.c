#include <stdio.h>
#include <stdlib.h>

struct node
{
  int val;
  struct node *next;
};

typedef struct node NODE;

void *createNNode();
NODE *appendList(NODE *,NODE *);
NODE *addBegList(NODE *, NODE *);
int dispMenu();
void dispList(NODE *);
void addNodeKey(NODE *, NODE *);
NODE *popList(NODE *);
void delKey(NODE *);


int main()
{
   
    NODE *newNode=NULL,*temp=NULL,*head=NULL;
    int ch=0, flag=0;
   
   
    while(1)
    {
        ch = dispMenu();
        switch (ch)
        {
        case 1:
            // create node and append to the list
            newNode = (NODE *)createNNode();
            // newNode->next = NULL;
            head = appendList(newNode, head);
            dispList(head);
            break;
        case 2:
            // Add node to the beinging of the list
            newNode = (NODE *)createNNode();
            head = addBegList(newNode, head);
            dispList(head);
            break;
        case 3:
            // add node after the key value
            newNode = (NODE *)createNNode();
            addNodeKey(newNode, head);
            dispList(head);
            break;
        case 4:

            break;
        case 5:
            head = popList(head);
            dispList(head);
            break;
        case 6:
            dispList(head);
            break;
        case 7:
            break;
        case 0:
            printf("\nEnd of the Program\n");
            flag = 1;
            break;
        default:
            printf("\nEnter the correct Choice\n");
            break;
        }

        if (flag == 1)
            break;
       
    }// end of while loop
   
       
    return 0;
}

void *createNNode()
{
    return (malloc(sizeof(NODE)));
}

void dispList(NODE *h)
{
    printf("\nList is\n");
    while(h)
    {
        printf("%d->", h->val);
        h = h->next;
    }
    printf("NULL\n\n");

}

int dispMenu()
{
    int ch = 0;
    printf("\nPress....");
    printf("\n1. Creating New Node");
    printf("\n2. Add Node to the Begining of the List");
    printf("\n3. Add Node after Key value");
    printf("\n4. Delete a node key value");
    printf("\n5. Pop the element from list");
    printf("\n6. Display List");
    printf("\n0. Exit");
    printf("\nChoice: ");
    scanf("%d",&ch);
    return ch;
}

NODE *appendList(NODE *nn, NODE *head)
{
    NODE *temp = head;
    printf("\nEnter the value of New Node: ");
    scanf("%d",&nn->val);
    nn->next = NULL;

    if(temp == NULL)
    {
        head = nn;
        temp = nn;
    }
    else
    {
        while(temp->next)
        {
            temp = temp->next;
        }
        temp->next = nn;
    }

    return head;

}

NODE *addBegList(NODE *nn, NODE *head)
{
    printf("\nAdding New Node to the Begining of the list");
    printf("\nEnter the value of New Node: ");
    scanf("%d",&nn->val);
    nn->next = NULL;

    nn->next = head;
    head = nn;
   
    return head;
}


void addNodeKey(NODE *nn, NODE *head)
{
    NODE *temp = head;
    NODE *nextNode = NULL;
    int key, flag = 0;

    printf("\nEnter the Key Value: ");
    scanf("%d",&key);
    while(temp)
    {
        if (temp->val == key){
            flag = 1;
            break;
        }
        temp = temp->next;
    }

    if (flag == 0)
    {
        printf("\nKey Not found in the list");
        return;
    }
    else
    {
        printf("\nEnter the value of New Node: ");
        scanf("%d",&nn->val);
        nn->next = NULL;

        nextNode = temp->next;
        temp->next = nn;

        nn->next = nextNode;
    }

}


NODE *popList(NODE *head)
{
    while(head->next->next != NULL || head->next != NULL)
    {
        head = head->next;
    }
    if (head->next == NULL){
        printf("\nPoped element : %d\n",head->val);
        head = NULL;
       
    }
    else{
        printf("\nPoped element : %d\n",head->next->val);
        head->next = NULL;
    }

    return head;
}

void delKey(NODE *head){
    
}