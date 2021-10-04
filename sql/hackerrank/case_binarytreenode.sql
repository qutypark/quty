/*
Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node. *when p is not null*
Inner: If node is neither root nor leaf node.
*/

select distinct(N) as node, (case when P is NULL then "Root"
        when N not in (select distinct(P) from BST where p is not NULL) then "Leaf"
        else "Inner"
        end)
from BST
order by node asc;

