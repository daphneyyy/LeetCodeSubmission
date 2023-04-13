// You are given a perfect binary tree where all leaves are on the same level, 
// and every parent has two children. The binary tree has the following definition:

/*
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
*/

// Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
// Initially, all next pointers are set to NULL.

class Solution {
public:
    Node* connect(Node* root) {
        if (root == nullptr) return root;
        Node* leftmost = root;
        while (leftmost->left != nullptr) {
            Node *head = leftmost;
            while (head != nullptr) {
                head->left->next = head->right;
                if (head->next != nullptr) {
                    head->right->next = head->next->left;
                }
                head = head->next;
            }
            leftmost = leftmost->left;
        }
        return root;
    }
};
