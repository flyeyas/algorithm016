学习笔记

### 树

### 树
#### 树和图的区别：
树没有环，图有环
链表是特殊化的树，有两个或多个next指针
树是特殊化的图，没有环的图就是树

#### 树，示例代码
python
```
class TreeNode:
    def _init_(self, val):
        self.val = val
        self.left, self.right = None, None
```

java
```
public class TreeNode{
    public int val;
    public TreeNode left, right;
    public TreeNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
```

#### 二叉树遍历
1、前序（Pre-order）：根-左-右

```
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
```

2、中序（In-order）：左-根-右
```
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)
    
#维护一个栈的方式
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
```


3、后序（Post-order）：左-右-根
```
def postorder(self, root):
    if root:
        self.inorder(root.left)
        self.inorder(root.right)
        self.traverse_path.append(root.val)
```



#### 二叉搜索树
又称，二叉排序树，有序二叉树，排序二叉树，是指一颗空树或者具有下列性质的二叉树：
1、左子树所有节点值均小于它的根节点值
2、右子树所有节点值均大于它的根节点值
3、以此类推，左子树和右子树也为别为二叉查找树

中序遍历：升序排列




### 堆

#### 二叉堆（大顶堆）

##### 特点
实现起来比较容易，时间复杂度刚刚及格
通过完全二叉树实现：
1、是一颗完全树，除了根，每一级节点都是满的
2、树中任意节点的值总是>=其子节点的值


##### 实现细节

使用一维数组实现：
第一个元素索引为0：
根节点（顶堆元素）是a[0]

索引为i的左孩子的索引是（2*i+1）
索引为i的右孩子的索引是（2*i+2）
索引为i的父节点的索引(floor((i-1)/2))