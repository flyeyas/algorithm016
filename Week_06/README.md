### 动态规划



#### 关键点

和递归或者分治没有根本上的区别，关键看有无最优子结构

共性：找到重复子问题

差异性： 最优子结构，中途可以淘汰次优解

1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2])
2. 储存中间状态： opt[i]
3. 递推公式，状态转移方程或者DP方程
   Fib:opt[i] = opt[n-1] + opt[n-2]
   二维路径：opt[i,j] = opt[i+1][j] + opt[i][j+1]



#### 总结
1. 打破自己的思维惯性，行程机器思维（目前为止还不能很好的做到，需要多做题)
2. 理解复杂逻辑的关键
3. 也是职业进阶的要点要领