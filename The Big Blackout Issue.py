########################################################## 	THE BLACKOUT ISSUE    #############################################################################################
# In a town in Delhi, electricity system had suddenly broke down. There are lot of different coloured poles (like blue,green,red, yellow etc.) in a town.
#  After complete inspection electricity department found that only the houses between Red Pole and Blue Pole  are facing this serious electricity issue
# that needed to solved as soon as possible. 
# Now electricity department has to find no. of houses between Red Pole and Blue Pole 
# to make necessary arrangements to solve this serious issue.
# 1 - Resembles 1 House in below code in list.
def blackout_issue(mylist):
	i=-1
	summylist=0
	while(i<len(mylist)-1): 
		
		i=i+1
		
	
		if mylist[i]=='Red Pole':
		    i=i+1
		    
		    
		    while(mylist[i]!='Blue Pole'):
		        
		      #  print("2")
		        summylist=summylist+mylist[i]
		      #  print(summylist)
		        i=i+1
		    if mylist[i]=='Blue Pole':
		        
		        pass
		else:
		    pass 
				 
	return summylist

print("Total no. of houses between Red Poles and Blue Poles:")		
print(blackout_issue([1,'Red Pole',1,1,1,1,'Blue Pole',1,1,'Red Pole',1,1,1,'Blue Pole','Red Pole','Blue Pole',1]))
