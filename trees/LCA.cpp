#include <iostream>

// Node class
class Node {
public:
    int value;
    Node* left;
    Node* right;

    Node(int data) {
        value = data;
        left = nullptr;
        right = nullptr;
    }
};

// Function to find the Lowest Common Ancestor
Node* findLCA(Node* curr_node, int n1, int n2) {
    if (curr_node == nullptr)
        return nullptr;

    if (curr_node->value == n1 || curr_node->value == n2)
        return curr_node;

    Node* left_lca = findLCA(curr_node->left, n1, n2);
    Node* right_lca = findLCA(curr_node->right, n1, n2);

    if (left_lca != nullptr && right_lca != nullptr)
        return curr_node;

    if (left_lca != nullptr)
        return left_lca;
    else
        return right_lca;
}

int main() {
    // Creating the binary tree
    Node* root = new Node(20);
    root->left = new Node(8);
    root->right = new Node(22);
    root->left->left = new Node(4);
    root->left->right = new Node(12);
    root->left->right->left = new Node(10);
    root->left->right->right = new Node(14);

    int n1 = 10, n2 = 14;
    Node* lca = findLCA(root, n1, n2);

    if (lca != nullptr)
        std::cout << "LCA of " << n1 << " and " << n2 << " is " << lca->value << std::endl;
    else
        std::cout << "LCA does not exist" << std::endl;

    return 0;
}