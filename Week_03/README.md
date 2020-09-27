### 递归

#### 特性，参照
1、向下进入不同的递归层，向上回到原来的层，不能跳跃，必须一层一层的向下或者返回
2、使用参数传递不同层之间的传递变量
3、每一层的环境和周围都是一份新的拷贝，参数穿越不同的层: 发生和携带变化

#### 思维要点
1、不能人肉递归（经常出现的问题，每次第一反应就是人肉递归，需要改变）
2、找到最近最简解决方法，拆分为重复子问题
3、数学归纳法： 最开始最简单的问题成立，推导出后面的重复问题也是成立的。 例子：当n=1成立时，推导出n=2,n=3...也是成立的


#### 代码模板
```
# python
def recursion(level, param1, param2, ...): 
    # 终止递归
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # 递归主逻辑
    process(level, data...) 
    # 向下递归
    self.recursion(level + 1, p1, ...) 

    # 反转当前状态（在需要时）
```

```
// java
public void recur(int level, int param) { 
  // 终止递归
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // 主逻辑
  process(level, param); 
  // 向下递归
  recur( level: level + 1, newParam); 

  // 反转当前状态（如果有需要）
 
}
```


### 分治
递归的一种细致的划分

#### 特性
1. 把一个大问题拆解成若干子问题处理，最后合并所有子问题的结果



#### 代码模板

```
// java
private static int divide_conquer(Problem problem, ) {
  
  // 终止递归
  if (problem == NULL) {
    int res = process_last_result();
    return res;     
  }
  //拆解成为子问题
  subProblems = split_problem(problem)
  
  //向下递归
  res0 = divide_conquer(subProblems[0])
  res1 = divide_conquer(subProblems[1])
  
  //合并子问题结果
  result = process_result(res0, res1);
  
  //清理变量，如果有需要
 
}
```

```
# python
def divide_conquer(problem, param1, param2, ...): 
  # 终止递归 
  if problem is None: 
	print_result 
	return 

  # 拆解成为子问题
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # 向下递归子问题 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # 合并结果
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # 清理变量，如果有需要
```

### 回溯
递归的一种

#### 特性
试错机制，一层一层试探，没有正确答案就返回上一层或者上几层，重新试探

### 记录
针对回溯相关的算法题需要多多练习