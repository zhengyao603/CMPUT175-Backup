class BinaryTree:
  def __init__(self, rootElement):
    self.key = rootElement
    self.left = None
    self.right = None
    self.elements = []

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getRootVal(self):
    return self.key

  def setRootVal(self,val):
    self.key = val
  
  def insertLeft(self,newNode):
    if self.left == None:
      self.left = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.left = self.left
      self.left = t
  
  def insertRight(self,newNode):
    if self.right == None:
      self.right = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.right = self.right
      self.right = t
  
  def contains(self, anObject):
    # Todo: returns true iff the receiver contains anObject
    print(self.getRootVal())
    if self.getRootVal() == anObject:
      return True
    
    if self.getLeft() != None:
      return self.getLeft().contains(anObject)
    if self.getRight() != None:
      return self.getRight().contains(anObject)


def preorder(tree):
  if tree != None:
    print(tree.getRootVal(), end=' ')
    preorder(tree.getLeft())
    preorder(tree.getRight())


def inorder(tree):
  if tree != None:
    inorder(tree.getLeft())
    print(tree.getRootVal(), end=' ')
    inorder(tree.getRight())


def postorder(tree):
  if tree != None:
    postorder(tree.getLeft())
    postorder(tree.getRight())
    print(tree.getRootVal(), end=' ')


def findMinValue(tree):
  # Todo: find and return the minimum value of the tree
  # if the node is a leaf node
  if tree.getLeft() == None and tree.getRight() == None:
    return tree.getRootVal()
  
  # if there is no node at the left of the current node
  if tree.getLeft() == None:
    return min(findMinValue(tree.getRight()), tree.getRootVal())
  # if there is no node at the right of the current node
  elif tree.getRight() == None:
    return min(findMinValue(tree.getLeft()), tree.getRootVal())
  
  return min(findMinValue(tree.getLeft()), findMinValue(tree.getRight()), tree.getRootVal())


def findMaxValue(tree):
  # Todo: find and return the maximum value of the tree
  # if the node is a leaf node
  if tree.getLeft() == None and tree.getRight() == None:
    return tree.getRootVal()
  
  # if there is no node at the left of the current node
  if tree.getLeft() == None:
    return max(findMinValue(tree.getRight()), tree.getRootVal())
  # if there is no node at the right of the current node
  elif tree.getRight() == None:
    return max(findMinValue(tree.getLeft()), tree.getRootVal())
  
  return max(findMaxValue(tree.getLeft()), findMaxValue(tree.getRight()), tree.getRootVal())  


def main():
  tree = BinaryTree(1)
  tree.insertLeft(2)
  tree.insertRight(7)
  tree.getLeft().insertLeft(3)
  tree.getLeft().insertRight(6)
  tree.getLeft().getLeft().insertLeft(4)
  tree.getLeft().getLeft().insertRight(5)
  tree.getRight().insertLeft(8)
  tree.getRight().insertRight(9)

  preorder(tree)
  print()
  inorder(tree)
  print()
  postorder(tree)
  print()

  print('Max value in tree:', findMaxValue(tree))
  print('Min value in tree:', findMinValue(tree))

  print(tree.contains(1))
  print(tree.contains(2))
  print(tree.contains(7))

if __name__ == "__main__":
  main()
