documentation = True
if documentation:
#     There will be 3 cases to consider in the given situation
    # 1. First will be in which node to be deleted Node is leaf node.
    # 2. Node to be deleted has only one child node(left or right)
    # 3. Node to be delted has both child nodes

    # - **Case 1 : N_T_D is Leaf Node**
    #     - Example
            
    #         N_T_D below is 35
            
    
    #         '''
    #                  	   50 
    #                    /	  \	        		
    #                  	30    60
    #         	       /  \	
    #                 15   25	   
    #                  '''		
    
            
        
    #     1. Find the parent node of node to be deleted
    #     2. set its left as None if N_T_D on left else set its right its None if node exist on right
    #     3. Delete the N_T_D
        
    # - **Case 2 : N_T_D is having only one child**
    #     - Example
            
    #         N_T_D below is 35
            
    
    #         '''
    #                  	   50 
    #                    /	  \	        		
    #                  	30    60
    #         	       /  \	
    #                 15 	35	
    #                  		 \
    #                  		 37
    #                  		  \
    #                  		  38
    #                  '''		
    
            
        
    #     1. Find the parent of node to be deleted
    #     2. set its left(if N_T_D is on left) or right (if N_T_D is on right) to map the only child of node to be deleted
    #     3. Delete the N_T_D
        
    # - **Case 3 : N_T_D is having both right as well as left child:**
    #     - Example
            
    #         N_T_D below is 35
            
    #         
    #         
    #                  	   50 
    #                    /	  \	        		
    #                  	30    60
    #         	       /  \	
    #                 15 	35	
    #                  	   /   \
    #                  	 33    39
    #                  	/ \	   / \
    #          		  32  34 36  40
    #              		 /        \
    #              		31         38
    #                  '''		
    #         
            
        
    #     1. Find the P_o_N_T_D
        
    #     2. find parent of min_R_S_N_T_D
        
    #     2 cases -----> a) min_R_S_N_T_D is on right of N_T_D , b) min_R_S_N_T_D is on some nth'node's left
        
    #     Consider case B only
    #     2 cases again
        
    #     2.1 min_R_S_N_T_D is leaf node  (set its parent's left as None) --> delete min_R_S_N_T_D and return the min_R_S_N_T_D's value
        
    #     2.2 min_R_S_N_T_D has single child  (set its parent's left as min_R_S_N_T_D.right) ----> delete min_R_S_N_T_D and return value
        
    #     3. set N_T_D.value as min_R_S_N_T_D.value
    pass

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.left.left = Node(20)
root.left.right = Node(40)
root.left.left.left = Node(15)
root.left.left.right = Node(25)
root.left.right.left = Node(35)
root.left.right.left.right = Node(36)
root.left.right.left.right.right = Node(37)
root.left.right.right = Node(45)


root.right = Node(70)
root.right.left = Node(60)
root.right.right = Node(80)
root.right.left.left = Node(55)
root.right.left.right = Node(65)
root.right.right.left = Node(75)
root.right.right.left.left = Node(72)

"""

                          50
                       /      \
                      /        \
                    30          70
                   /  \        /  \
                 20    40    60    80
                / \   / \   / \    / 
               15 25 35 45 55 65  75
                                 /
                                72 
                          
                                 
"""

"""

                          50
                       /      \
                      /        \
                    30          70
                   /  \        /  \
                 20    40    60    80
                / \   / \   / \    / 
               15 25 35 45 55 65  75
                       \         /
                        36     72 
                          \
                           37
"""

def find_parent(root,key):
    if root is None:
        return None, None
    
    if root.left and root.left.value == key:
        print("----->", root.value, root.left.value)
        return root, root.left
    elif root.right and root.right.value == key:
        return root, root.right
    
    l_s = find_parent(root.left, key)
    r_s = find_parent(root.right, key)
    return l_s if l_s[1] else r_s

def print_tree(root):
    q = [root]
    while len(q)>0:
        curr = q.pop(0)
        print(curr.value, end="   ")
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    print()

# Node to be Deleted is 35, 80 and 30
key1 = 35
key2 = 80
key3 = 30
# P_o_N_T_D, N_T_D = find_parent(root, key1)

# P_o_N_T_D, N_T_D = find_parent(root, key2)

P_o_N_T_D, N_T_D = find_parent(root, key3)


#case in in which N_T_D is leaf node
if N_T_D.left is None and N_T_D.right is None:
    if P_o_N_T_D.left == N_T_D:
        P_o_N_T_D.left = None
    else:
        P_o_N_T_D.right = None

# case in which N_T_D has only one child node:
if N_T_D.left is None or N_T_D.right is None:
    if N_T_D.left:
        if P_o_N_T_D.left == N_T_D:
            P_o_N_T_D.left = N_T_D.left
        else:
            P_o_N_T_D.right = N_T_D.left
    else:
        if P_o_N_T_D.left == N_T_D:
            P_o_N_T_D.left = N_T_D.right
        else:
            # P_o_N_T_D.right = N_T_D.right
# case in which N_T_D has both child nodes
if N_T_D.left and N_T_D.right:
    min_R_S_N_T_D = N_T_D.right
    min_R_S_N_T_D_parent = N_T_D
    while min_R_S_N_T_D.left:
        min_R_S_N_T_D_parent = min_R_S_N_T_D
        min_R_S_N_T_D = min_R_S_N_T_D.left
    if min_R_S_N_T_D.right is None:
        min_R_S_N_T_D_parent.left = None
    else:
        min_R_S_N_T_D_parent.left = min_R_S_N_T_D.right
    N_T_D.value = min_R_S_N_T_D.value
print_tree(root)
