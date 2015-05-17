def preorder(root):
    if(root is None):
        return
    print root[0]
    preorder(root[1])
    preorder(root[2])

n5 = (5, None, None)
n4 = (4, None, None)
n3 = (3,None,None)
n2 = (2,n4,n5)
root = (1,n2,n3)
preorder(root)
