__author__ = "那位先生Beer"


def flatten( self, root ):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if root == None:
        return None
    head = root
    while root != None:
        if root.left != None:
            p = root.left
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None
        root = root.right