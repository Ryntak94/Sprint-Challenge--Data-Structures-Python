class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
        if not self.left:
            self.left = BinarySearchTree(value)
        elif self.left.value == value:
            return value
        else:
            self.left.insert(value)
    elif value > self.value:
        if not self.right:
            self.right = BinarySearchTree(value)
        elif self.right.value == value:
            return value
        else:
            self.right.insert(value)

    # def delete(self, value):
    #     if self.value == value:



  def contains(self, target):
    if self.value == None:
        return True
    if self.value == target:
        return True
    else:
        if self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.value < target:
                if self.right:
                    return self.right.contains(target)
                else:
                    return False

  def get_max(self):
    if self.right:
        return self.right.get_max()
    else:
        return self.value

  def for_each(self, cb):
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)
    return cb(self.value)
