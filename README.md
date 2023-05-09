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

<p align="center">
<img src=./images/formula.png/>
</p>


The term $g(x)$ is calculated as the **path distance** from any given node to the start node. The **path distance** from the start node to the node outlined in red is 10 because it takes a minimum of 10 "moves" to get there.

The term $h(x)$ is calculated as the **manhattan distance** from any given node to the end/goal node. The **manhattan distance** from the start node to the node outlined in red is 4. Manhattan distance is calculated as: $d_m = |x_1-x_2| + |y_1-y_2|$.

<p align="center">
<img src=./images/distance.png/>
</p>

<p align="center">

|Algorithm|Formula|Notes|
|------|------|------|
|UCS|$f(x) = g(x)$|Takes a long time, but always finds shortest path.|
|BFS|$f(x) = h(x)$|Very quick, but will often find a path that is **NOT** the shortest.|
|A*|$f(x) = g(x) + h(x)$|Always finds shortest path and is quicker than UCS (but slower than BFS).|

</p>

<br/>

The numbers inside the yellow cells are the hueristic value for that node or the $f(x)$. Once the path has been found and gets revealed by the $\color{lightblue}{\textsf{light blue}}$ cells, the number changes from hueristic value to path distance value. This change only occurs in $\color{lightblue}{\textsf{light blue}}$ cells.


<br/>

## A* Variable (Alternatives)
The original formula can be modified to give the user more control over the algorithm:

$$\huge f(x) = ag(x) + bh(x)$$

The $a$ and $b$ coefficients allow the user to change the hueristic of the function.


<p align="center">

|a = 1, b = 1|a = 1, b = 0.5|a = 0.5, b = 1
|------|------|------|
|![](/images/astar11.png)|![](/images/astar105.png)|![](/images/astar051.png)|

</p>

$a = 1,\ b = 0$ would be the same as UCS.

$a = 0,\ b = 1$ would be the same as BFS.

$a = 1,\ b = 1$ would be the same as A*.

# Hyperparameters

<p align="center">

|Hyperparameter|Description|
|--|--|
|Ticktime|How long to wait until expanding next node (in ms).|
|Window Height|How many pixels tall the window is.|
|Window Width|How many pixels wide the window is.|
|Block Size|Number of rows is equal to Window Height divided by Block Size. Number of columns is equal to the Window Width divided by Block Size. |

</p>

### Examples
<p align="center">

|800x800 Block Size of 10|1000x1000 Block Size of 40|
|--|--|
|![](/images/800x800cs10.png)|![](/images/1000x1000cs40.png)|

|Ticktime of 0|Ticktime of 20|Ticktime of 100|
|--|--|--|
|![](/images/tickrate0.gif)|![](/images/default.gif)|![](/images/tickrate100.gif)|

</p>

*All images above used UCS search algorithm and are 800x800 with block size of 20.*

# Other Examples

||UCS|BFS|A*|
|--|--|--|--|
|Screen|![](/images/ucs1.gif)|![](/images/bfs1.gif)|![](/images/astar1.gif)|
|Path Length|$\color{green}{66}$|$\color{red}{76}$|$\color{green}{66}$|
|Nodes Expanded|$\color{red}{1199}$|$\color{green}{117}$|$\color{yellow}{708}$|

</br>

||UCS|BFS|A*|
|--|--|--|--|
|Screen|![](/images/ucs2.gif)|![](/images/bfs2.gif)|![](/images/astar2.gif)|
|Path Length|$\color{green}{45}$|$\color{red}{75}$|$\color{green}{45}$|
|Nodes Expanded|$\color{red}{1242}$|$\color{green}{148}$|$\color{yellow}{513}$|

