select (case when A=B and B=C and A=C Then 'Equilateral'
        when A!=B and B!=C and C!=A and greatest(A,B,C) < (A+B+C)-greatest(A,B,C) then 'Scalene'
        when greatest(A,B,C) > (A+B+C)-greatest(A,B,C) then 'Not A Triangle'
        when A=B and A!=C and (A+B)> C then 'Isosceles'
        when A=C and A!=B and (A+C)> B then 'Isosceles'
        when B=C and B!=A and (B+C)> A then 'Isosceles'
        else 'Not A Triangle'
end)
from triangles;
