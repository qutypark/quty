-- grouping_sets((c1, c2, c3)

-- cube(c1, c2, c3)
(c1, c2, c3)
(c1, c2)
(c2, c3)
(c1,c3)
(c1)
(c2)
(c3)
()

-- ROLLUP(c1,c2,c3) assuming the hierarchy c1 > c2 > c3 as follows:
(c1, c2, c3)
(c1, c2)
(c1)
()

