### 深度优先搜索
首先访问根节点，在访问左子树，返回访问右子树


#### 模板代码

##### 递归写法
```
#python

visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
        # already visited 
        return 

    visited.add(node) 

    # process current node here. 
    ...
    for next_node in node.children(): 
        if next_node not in visited: 
            dfs(next_node, visited)
```


```
//java
public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> allResults = new ArrayList<>();
    if(root==null){
        return allResults;
    }
    travel(root,0,allResults);
    return allResults;
}


private void travel(TreeNode root,int level,List<List<Integer>> results){
    if(results.size()==level){
        results.add(new ArrayList<>());
    }
    results.get(level).add(root.val);
    if(root.left!=null){
        travel(root.left,level+1,results);
    }
    if(root.right!=null){
        travel(root.right,level+1,results);
    }
}
```

##### 非递归写法
```
#python
def DFS(self, tree): 

    if tree.root is None: 
        return [] 

    visited, stack = [], [tree.root]

    while stack: 
        node = stack.pop() 
        visited.add(node)

        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 

    # other processing work 
    ...
```

### 广度优先搜索
从根节点开始，方问完成所有父节点，在访问子节点

#### 模板代码
```
# python
def BFS(graph, start, end):
    visited = set()
    queue = [] 
    queue.append([start]) 
    while queue: 
        node = queue.pop() 
        visited.add(node)
        process(node) 
        nodes = generate_related_nodes(node) 
        queue.push(nodes)
    # other processing work 
    ...
```

```
//java
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

public List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> allResults = new ArrayList<>();
    if (root == null) {
        return allResults;
    }
    Queue<TreeNode> nodes = new LinkedList<>();
    nodes.add(root);
    while (!nodes.isEmpty()) {
        int size = nodes.size();
        List<Integer> results = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = nodes.poll();
            results.add(node.val);
            if (node.left != null) {
                nodes.add(node.left);
            }
            if (node.right != null) {
                nodes.add(node.right);
            }
        }
        allResults.add(results);
    }
    return allResults;
}
```


### 贪心算法
在每一步选择中选择当前状态下最好或者最优的选择，从而希望导致结果在全局状态下是最好或者最优的算法

和动态规划不同的地方在于它对每一个子问题的解决方案都做出选择，不能回退。动态规划会保存以前的运算结果，并且根据以前的结果对当前进行选择，有回退功能

#### 对比
贪心算法： 当前局部最优选择
回溯：回退功能
动态规划：最优选择+回退功能



### 二分查找
二分查找的前提：
1. 目标函数单调性，单调递增或者单调递减
2. 存在上下界（bounded）
3. 能够通过索引访问（index accessible）

#### 代码模板
python
```
left, right = 0, len(array) - 1 
while left <= right: 
      mid = (left + right) / 2 
      if array[mid] == target: 
            # find the target!! 
            break or return result 
      elif array[mid] < target: 
            left = mid + 1 
      else: 
            right = mid - 1
            
```

java
```
public int binarySearch(int[] array, int target) {
    int left = 0, right = array.length - 1, mid;
    while (left <= right) {
        mid = (right - left) / 2 + left;

        if (array[mid] == target) {
            return mid;
        } else if (array[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return -1;

```