# Pathfinder
This python application showcases pathfinding using the Uniform Cost Search, Best First Search, and A* search algorithms.

Below is an example output of UCS:
![](/images/default.gif)

The $\color{green}{\textsf{Green}}$ cell is the *starting* node

The $\color{red}{\textsf{Red}}$ cell is the *ending/goal* node

The $\color{black}{\textsf{Black}}$ cells are the *wall* nodes

The $\color{blue}{\textsf{Blue}}$ cell is the *current expanded* node

The $\color{yellow}{\textsf{Yellow}}$ cells are the *previously expanded* nodes

The $\color{lightblue}{\textsf{Light Blue}}$ cells are the *calculated path* nodes


# Algorithms
All three algorithms are some form of the formula below. The goal of each algorithm is to minimize the function $f(x)$.

![](/images/formula.png)

The term $g(x)$ is calculated as the **path distance** from any given node to the start node. The **path distance** from the start node to the node outlined in red is 10 because it takes a minimum of 10 "moves" to get there.

The term $h(x)$ is calculated as the **manhattan distance** from any given node to the start node. The **manhattan distance** from the start node to the node outlined in red is 4. Manhattan distance is calculated as: $d_m = |x_1-x_2| + |y_1-y_2|$.

![](/images/distance.png)

|Algorithm|Formula|
|------|------|
|UCS|$f(x) = g(x)$|
|BFS|$f(x) = h(x)$|
|A*|$f(x) = g(x) + h(x)$|