########################################################## 	THE BLACKOUT ISSUE    #############################################################################################
# In a town in Delhi, electricity system had suddenly broke down. There are lot of different coloured poles (like blue,green,red, yellow etc.) in a town.
#  After complete inspection electricity department found that while moving from Red Pole to Blue Pole, houses between Red Pole and Blue Pole  are facing this serious electricity issue
# that needed to solved as soon as possible. 
# Now electricity department has to find no. of houses between Red Pole and Blue Pole (while moving from Red Pole to Blue Pole)
# to make necessary arrangements to solve this serious issue.
# 1 - Resembles 1 House in below code in list.

def blackout_issue(mylist):
	i = -1
	summylist = 0
	while(i < len(mylist)-1):

		i = i+1

		if mylist[i] == 'Red Pole':
			
			i = i+1
			if type(mylist[i])== int:
				                  
				while(mylist[i] != 'Blue Pole'):
					summylist = summylist+mylist[i]
					
					i=i+1
				
				if mylist[i]=='Blue Pole':
					pass 
					
			else:                  
				while (mylist[i]!='Blue Pole'):
					i=i+1
					      
				
					
		else:
			              
			pass 
				 
	return summylist

print("Total no. of houses between Red Poles and Blue Poles:")		
print(blackout_issue([1,'Red Pole',1,1,1,1,1,'Blue Pole',1,1,'Red Pole','Black Pole','Yellow Pole',1,1,'Blue Pole','Red Pole',1,1,'Blue Pole',1]))

				                                 

		        
		        
		     
		        
		    	
		        
		       


		    
		    

		    
		
		
