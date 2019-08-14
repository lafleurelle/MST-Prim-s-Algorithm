# MST-Prim-s-Algorithm

This is a part of programming assignment for the the course "Algorithms" from Coursera.
In this programming problem Prim's minimum spanning tree algorithm is solved.
This file "edges.txt" describes an undirected graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]

[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]

[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

...

For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. The task is to run Prim's minimum spanning tree algorithm on this graph and report the overall cost of a minimum spanning tree.
There is a heap-based implementation. The approach stores the unprocessed vertices in the heap, as described in the lecture.
