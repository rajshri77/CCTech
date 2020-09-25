"""	
	Aim: To Calculate the surface of the building exposed to sunlight
	25 Sepetember 2020, Rajshri Shinde	
"""

"""Basically we are considering there are n buildings and we have to calculate the length of suarface area covered by sunlight. 
Here I have first calculated the height and top surface of first building. 
Then calculate the height of second building but height of second buiding is not totally covered by sunlight because shadow of first building falls on second building. 
So we have to remove that shadow region from our calculation so we subtract the height of first building from height of secong building.
Now we get the height of second building actually covered by sunlight and calculate the length of top surface for second bulding(total top surface covered by sunlight for each building) by subtracting Ymax from Ymin. 
Follow this whole procedure upto nth.
Finally add length of heights and top surfaces for all the n buildings so that we can get the total length covered by sunlight """


import numpy as np
  
def minmax_for_x(a,k):

	xmax = []
	xmin = []
	j=0
	
	for i in range(n):
		p = a[i][j][k]
		if(p<0):
			a[i][j][k] = -p

		maxi = a[i][j][k]
		mini = a[i][j][k]

		for j in range(coords):
			p = a[i][j][k]
			if(p<0):
				a[i][j][k] = -p

			if(a[i][j][k]<mini):
				mini=a[i][j][k]
			if(a[i][j][k]>maxi):
				maxi=a[i][j][k]

		xmax.append(maxi)
		xmin.append(mini)

	return xmin, xmax	
 
a=np.array( [[[4,0],[4,-5],[7,-5],[7,0]]]  ) 
pt = [1,1]
dim = a.ndim
n=(np.size(a))/((dim+1)*2)
coords=dim+1

#calculating min and max for x and y coordinates
x = minmax_for_x(a,0)
Xmin = x[0]
Xmax = x[1]

y = minmax_for_x(a,1)
Ymin = y[0]
Ymax = y[1]

#calculate the length of building
total_length = 0
height = []
total_height = 0 
total_upper_surface = 0
upper_surface = 0

#subtract the Ymax from Ymin so that we can get the height of first building
height.append(Ymax[0]-Ymin[0])
total_height = total_height + height[0]

#Subtract the Xmax from Xmin So that we can get the width i.e. top surface of first builging
upper_surface = upper_surface + (Xmax[0]-Xmin[0])
total_upper_surface = total_upper_surface + upper_surface

for i in range(1,n):

	#subtract the Ymax from Ymin so we get the height of current building and then sunbratct the shadow of peiveous building i.e.height of peiveous building from current height so that we can get the height of area covered by sunlight for the building
	height.append((Ymax[i]-Ymin[i])-(height[i-1]))
	total_height = total_height + height[i]

	#Subtract the Xmax from Xmin So that we can get the width i.e. top surface of builgings
	total_upper_surface = total_upper_surface + (Xmax[i]-Xmin[i])
	
#Add all the heights and surface area covered by sunlight
total_length = total_length + total_height + total_upper_surface
print total_length

