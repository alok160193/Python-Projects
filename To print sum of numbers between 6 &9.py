# To print sum of numbers between 6 & 9 in a given list. 


def summer_69(mylist):
	i=-1
	summylist=0
	while(i<len(mylist)-1): #i=-1,0,1,2,3,4 
		
		i=i+1
		
	
		if mylist[i]==6:
		    i=i+1
		    
		    
		    while(mylist[i]!=9):
		        
		        
		        summylist+=mylist[i]
		        i=i+1
		    if mylist[i]==9:
		        
		        pass
		else:
		    pass 
				 
	return summylist
		
print(summer_69([1,6,1,1,1,9,1,6,1,7,1,9,2,6,6,9]))