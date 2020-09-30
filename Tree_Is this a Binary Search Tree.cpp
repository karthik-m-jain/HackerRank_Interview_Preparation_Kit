//Remaining code is hidden at HackerRank

/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.

The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/
	bool checkBST(Node* root) {
        return checkBST(root,0,10000);
    }
    bool checkBST(Node *temp,int min,int max){
        if(temp==NULL)
            return 1;
        if(temp->data<min || temp->data>max)
            return 0;
        return checkBST(temp->left,min,temp->data-1) && checkBST(temp->right,temp->data+1,max);
    }
