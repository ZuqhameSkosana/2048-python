def push_up (grid):
    """merge grid values upwards"""
    grid = grid
    row=0
            
    for col in range(0,4):
                
        if grid[row][col]!=0 or grid[row+1][col]!=0 or grid[row+2][col]!=0 or grid[row+3][col]!=0:
                    
            if grid[row][col]==0:
                        
                while grid[row][col]==0:
                            
                    grid[row][col]=grid[row+1][col]
                            
                    grid[row+1][col]=grid[row+2][col]
                            
                    grid[row+2][col] = grid[row+3][col]
                            
                    grid[row+3][col]=0
                    
            if grid[row+1][col]==0 and (grid[row+2][col]!=0 or grid[row+3][col]!=0):
                        
                while grid[row+1][col]==0:
    
                    grid[row+1][col]=grid[row+2][col]
                            
                    grid[row+2][col]=grid[row+3][col]
                            
                    grid[row+3][col]=0
                    
            if grid[row+2][col]==0 and (grid[row+3][col]!=0):
                        
                while grid[row+2][col]==0:
                            
                    grid[row+2][col]=grid[row+3][col]
                            
                    grid[row+3][col]=0
            
    row=0
            
    for col in range(0,4):
                
        if grid[row][col]==grid[row+1][col]:
                    
            grid[row][col]=grid[row][col]+grid[row+1][col]
                    
            grid[row+1][col]=grid[row+2][col]
                    
            grid[row+2][col]=grid[row+3][col]
                    
            grid[row+3][col]=0
                
        if grid[row+1][col]==grid[row+2][col]:
                    
            grid[row+1][col]=grid[row+1][col]+grid[row+2][col]
                    
            grid[row+2][col]=grid[row+3][col]
                    
            grid[row+3][col]=0
                
        if grid[row+2][col]==grid[row+3][col]:
                    
            grid[row+2][col]=grid[row+2][col]+grid[row+3][col]
                    
            grid[row+3][col]=0       
 
           
def push_down (grid):
    """merge grid values downwards"""
    grid = grid
    row=0
            
    for col in range(0,4):
                
        if grid[row][col]!=0 or grid[row+1][col]!=0 or grid[row+2][col]!=0 or grid[row+3][col]!=0:
                    
            if grid[row+3][col]==0:
                        
                while grid[row+3][col]==0:
                            
                    grid[row+3][col]=grid[row+2][col]
                            
                    grid[row+2][col]=grid[row+1][col]
                            
                    grid[row+1][col]=grid[row][col]
                            
                    grid[row][col]=0
                    
        if grid[row+2][col]==0 and (grid[row+1][col]!=0 or grid[row][col]!=0):
                        
            while grid[row+2][col]==0:
                            
                grid[row+2][col]=grid[row+1][col]
                            
                grid[row+1][col]=grid[row][col]
                            
                grid[row][col]=0
     
                    
        if grid[row+1][col]==0 and grid[row][col]!=0:
                        
            while grid[row+1][col]==0:
                            
                grid[row+1][col]=grid[row][col]
                            
                grid[row][col]=0
            
    row=0
            
    for col in range(0,4):
                
        if grid[row+3][col]==grid[row+2][col]:
                    
            grid[row+3][col]=grid[row+3][col] + grid[row+2][col]
                    
            grid[row+2][col]=grid[row+1][col]
                    
            grid[row+1][col]=grid[row][col]
                    
            grid[row][col]=0
                
        if grid[row+2][col]==grid[row+1][col]:
                    
            grid[row+2][col]=grid[row+2][col]+grid[row+1][col]
                    
            grid[row+1][col]=grid[row][col]
                    
            grid[row][col]=0
                
        if grid[row+1][col]==grid[row][col]:
                    
            grid[row+1][col]=grid[row+1][col]+grid[row][col]
                    
            grid[row][col]=0                                 

                        
def push_left (grid):
    """merge grid values left"""
    grid = grid                               
    col=0
            
    for row in range(0,4):
             
        if grid[row][col]!=0 or grid[row][col+1]!=0 or grid[row][col+2]!=0 or grid[row][col+3]!=0:
                    
            if grid[row][col]==0:
                        
                while grid[row][col]==0:
                            
                    grid[row][col]=grid[row][col+1]
                            
                    grid[row][col+1]=grid[row][col+2]
                            
                    grid[row][col+2] = grid[row][col+3]
                            
                    grid[row][col+3]=0
                    
            if grid[row][col+1]==0 and (grid[row][col+2]!=0 or grid[row][col+3]!=0):
                        
                while grid[row][col+1]==0:
                            
                    grid[row][col+1]=grid[row][col+2]
                            
                    grid[row][col+2]=grid[row][col+3]
                            
                    grid[row][col+3]=0
                    
            if grid[row][col+2]==0 and (grid[row][col+3]!=0):
                        
                while grid[row][col+2]==0:
                            
                    grid[row][col+2]=grid[row][col+3]
                            
                    grid[row][col+3]=0
            
    col=0
            
    for row in range(0,4):
                
        if grid[row][col]==grid[row][col+1]:
                    
            grid[row][col]=grid[row][col]+grid[row][col+1]
                    
            grid[row][col+1]=grid[row][col+2]
                    
            grid[row][col+2]=grid[row][col+3]
                    
            grid[row][col+3]=0
                
        if grid[row][col+1]==grid[row][col+2]:
                    
            grid[row][col+1]=grid[row][col+1]+grid[row][col+2]
                    
            grid[row][col+2]=grid[row][col+3]
                    
            grid[row][col+3]=0
                
        if grid[row][col+2]==grid[row][col+3]:
                    
            grid[row][col+2]=grid[row][col+2]+grid[row][col+3]
                    
            grid[row][col+3]=0    
                    
def push_right (grid):
    """merge grid values right"""
    grid = grid
    col=0
            
    for row in range(0,4):
                
        if grid[row][col]!=0 or grid[row][col+1]!=0 or grid[row][col+2]!=0 or grid[row][col+3]!=0:
                    
            if grid[row][col+3]==0:
                        
                while grid[row][col+3]==0:
                            
                    grid[row][col+3]=grid[row][col+2]
                            
                    grid[row][col+2]=grid[row][col+1]
                            
                    grid[row][col+1]=grid[row][col]
                            
                    grid[row][col]=0
                    
            if grid[row][col+2]==0 and (grid[row][col+1]!=0 or grid[row][col]!=0):
                        
                while grid[row][col+2]==0:
                            
                    grid[row][col+2]=grid[row][col+1]
                            
                    grid[row][col+1]=grid[row][col]
                            
                    grid[row][col]=0
     
                    
            if grid[row][col+1]==0 and grid[row][col]!=0:
                        
                while grid[row][col+1]==0:
                            
                    grid[row][col+1]=grid[row][col]
                            
                    grid[row][col]=0
            
    col=0
            
    for row in range(0,4):
                
        if grid[row][col+3]==grid[row][col+2]:
                    
            grid[row][col+3]=grid[row][col+3] + grid[row][col+2]
                    
            grid[row][col+2]=grid[row][col+1]
                    
            grid[row][col+1]=grid[row][col]
                    
            grid[row][col]=0
                
        if grid[row][col+2]==grid[row][col+1]:
                    
            grid[row][col+2]=grid[row][col+2]+grid[row][col+1]
                    
            grid[row][col+1]=grid[row][col]
                    
            grid[row][col]=0
                
        if grid[row][col+1]==grid[row][col]:
                    
            grid[row][col+1]=grid[row][col+1]+grid[row][col]
                    
            grid[row][col]=0    