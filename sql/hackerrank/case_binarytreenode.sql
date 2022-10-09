/*
Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node. *where p is not null*
Inner: If node is neither root nor leaf node.
*/
-- 2022-10-09
select
    N
    , case when P is null then 'Root'
           when N in (select P from bst where p is not null) then 'Inner'
           else 'Leaf' end as ans
from bst
order by 1

-- past
select distinct(N) as node, (case when P is NULL then "Root"
        when N not in (select distinct(P) from BST where p is not NULL) then "Leaf"
        else "Inner"
        end)
from BST
order by node asc;

