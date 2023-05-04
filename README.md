# Pathfinder
This python application showcases pathfinding using the Uniform Cost Search, Best First Search, and A* search algorithms.

Below is an example output of UCS:
![](/images/default.gif)

The <span style="color:green">Green</span> cell is the *starting* node

The <span style="color:red">Red</span> cell is the *ending/goal* node

The <span style="color:black">Black</span> cells are the *wall* nodes

The <span style="color:blue">Blue</span> cell is the *current expanded* node

The <span style="color:yellow">Yellow</span> cells are the *previously expanded* nodes

The <span style="color:lightblue">Light Blue</span> cells are the *calculated path* nodes


# Algorithms
All three algorithms are some form of the formula below. The goal of each algorithm is to minimize the function $f(x)$.

![](/images/formula.png)

The term $g(x)$ is calcluated as the **path distance** from any given node to the start node. The **path distance** from the start node to the node outlined in red is 10 because it takes a minimum of 10 "moves" to get there.

The term $h(x)$ is calcluated as the **manhattan distance** from any given node to the start node. The **manhattan distance** from the start node to the node outlined in red is 4. Manhattan distance is calculated as: $d_m = |x_1-x_2| + |y_1-y_2|$.

![](/images/distance.png)

|Algorithm|Formula|
|------|------|
|UCS|$f(x) = g(x)$|
|BFS|$f(x) = h(x)$|
|A*|$f(x) = g(x) + h(x)$|