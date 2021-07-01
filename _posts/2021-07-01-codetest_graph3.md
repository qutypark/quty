



```python
def solution(arrows):
    point=set([(0,0)])
    line=set()
    move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]]
    pre_point=(0,0)
    for A in arrows:
        next_point=(pre_point[0]+move[A][0],  pre_point[1]+move[A][1] )
        mid_point=(pre_point[0]+move[A][0]//2,  pre_point[1]+move[A][1]//2 )
        point.add(next_point)
        point.add(mid_point)
        line.add((pre_point,mid_point))
        line.add((mid_point,pre_point))
        line.add((mid_point,next_point))
        line.add((next_point,mid_point))
        pre_point=next_point
    answer = len(line)//2-len(point)+1
    return answer if answer>=0 else 0
```
