"""	
	Aim: To Check if the given point lies inside or outside a polygon
	25 Sepetember 2020, Rajshri Shinde	
"""

"""
Here I have solution by two way for this problem. 

1)We have two inputs co-ordinates of polygon and coordinates of point to be checked inside or outside of the polygon.
First of all we draw the line from point to the right side of the point upto outside the polygon.
Then we check the how many times line is intersect with polygon edges.
If count is odd or if point is on edge of polygon then we can say point is inside the polygon otherwise point is outside the polygon.

2)We can divide the polygon into number of small triangles without considering the point to be checked inside or outside.
Then calculate the area of polygon by calculating the area of each triangle and add all the areas i.e. A1
After that we can draw the line from the point to be checked inside or outside to every coordinate of polygon, now we get the different triangles.
Again calculate the areas of all triangles and add it i.e. A2
Now compare A1 and A2. If A1 is equals to A2 then we can say point is inside the polygon, if not then we can say point is outside the polygon.
"""

from sympy import Point, Line
import numpy as np

def isInside(a,n,pt):
	count = 0
	i = 0 
	l1 = Line(pt,lenght_of_line)
	print l1
	

a=np.array([[1,0], [8,3], [8,8], [1,5]]) 
pt = [3,5]
n = np.size(a)/np.size(a[0])
lenght_of_line = 100
result = isInside(a,n,pt)

