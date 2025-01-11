from typing import List, Optional
import turtle

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(string):
    #print(f'\t>>> string = {string}')
    if string == '{}' or string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    #print(f'\t>>> nodes = {nodes}')
    kids = nodes[::-1]
    #print(f'\t>>> kids = {kids}')
    root = kids.pop()
    #print(f'\t>>> root = {root}')
    for node in nodes:
        #print(f'\t\t>>> node = {node}')
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    #import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        self.root = TreeNode()
        def dfs(node1, node2, node):
            if node1 and node2:
                #print(f'node1.val, node2.val, node.val = {node1.val}, {node2.val}, {node1.val+node2.val}')
                node.val = node1.val + node2.val
                if node1.left or node2.left:
                    node.left = TreeNode()
                    dfs(node1.left, node2.left, node.left)
                if node1.right or node2.right:
                    node.right = TreeNode()
                    dfs(node1.right, node2.right, node.right)
            elif node1:
                #print(f'node1.val, node.val = {node1.val}, {node1.val}')
                node.val = node1.val
                if node1.left:
                    node.left = TreeNode()
                    dfs(node1.left, None, node.left)
                if node1.right:
                    node.right = TreeNode()
                    dfs(node1.right, None, node.right)
            elif node2:
                #print(f'node2.val, node.val = {node2.val}, {node2.val}')
                node.val = node2.val
                if node2.left:
                    node.left = TreeNode()
                    dfs(None, node2.left, node.left)
                if node2.right:
                    node.right = TreeNode()
                    dfs(None, node2.right, node.right)

        if root1 is None and root2 is None:
            return None
        dfs(root1, root2, self.root)
        #print('=======')
        return self.root

# Main section
for btree1, btree2 in [
                         ('[1,3,2,5,null]', '[2,1,3,null,4,null,7]'),
                         ('[5,2,null,3,null,4,null]', '[6,null,2,null,3,null,4]'),
                         ('[]', '[]'),
                      ]:
    print(f'btree1, btree2 = {btree1}, {btree2}')
    root1 = deserialize(btree1)
    root2 = deserialize(btree2)
    sol = Solution()
    r = sol.mergeTrees(root1, root2)
    print(f'r = {r}')
    drawtree(r)
    turtle.TurtleScreen._RUNNING = True
    print('===========================')


