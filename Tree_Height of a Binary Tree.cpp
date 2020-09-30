#include <bits/stdc++.h>

using namespace std;

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

class Solution {
    public:
  		Node* insert(Node* root, int data) {
            if(root == NULL) {
                return new Node(data);
            } else {
                Node* cur;
                if(data <= root->data) {
                    cur = insert(root->left, data);
                    root->left = cur;
                } else {
                    cur = insert(root->right, data);
                    root->right = cur;
               }

               return root;
           }
        }
/*The tree node has data, left child and right child
class Node {
    int data;
    Node* left;
    Node* right;
};

*/
    int height(Node* root){
        //Because the result was one less than the height of the tree
        //Used the idea of polymorphism
        return (height(root,1)-1);
    }
    int height(Node* root,int a) {
        // Write your code here.
        if(root==NULL)
            return 0;
        else{
            int ldepth=height(root->left,1);
            int rdepth=height(root->right,1);

            if(ldepth>rdepth)
                return (ldepth+1);
            else
                return (rdepth+1);
        }

    }

}; //End of Solution
