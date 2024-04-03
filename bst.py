class node:
    def __init__(self,x=0):
        self.val=x
        self.left=None
        self.right=None


def insert(r,x):
    if(r==None):
        return node(x)
    elif(x<r.val):
        r.left=insert(r.left,x)
    else:
        r.right=insert(r.right,x)
    return r


def search(r,x):
    if(r==None):
        return 'not found'
    if(r.val==x):
        return 'found'
    elif(x<r.val):
        return search(r.left,x)
    else:
        return search(r.right,x)


def add_all(r):
    if r==None:
        return 0
    return r.val + add_all(r.left) + add_all(r.right)


def inorder(r):
    if(r==None):
        return
    inorder(r.left)
    print(r.val,end=' ')
    inorder(r.right)


def preorder(r):
    if(r==None):
        return
    print(r.val,end=' ')
    preorder(r.left)
    preorder(r.right)


def postorder(r):
    if(r==None):
        return
    postorder(r.left)
    postorder(r.right)
    print(r.val,end=' ')

def height(r):
    if(r==None):
        return -1
    else:
        lh=height(r.left)
        rh=height(r.right)
    return max(lh,rh)+1



r=node(5)

insert(r,2)
insert(r,4)
insert(r,6)
insert(r,16)

print('addall')
print(add_all(r))
print('inorder')
print(inorder(r))
print('preorder')
print(preorder(r))
print('postorder')
print(postorder(r))
print('height')
print(height(r))





