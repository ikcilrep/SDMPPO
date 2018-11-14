m    	- message  
e    	- random number generated separatly for each message  
p, k	- two parts of private key  
r	- radius * radius  
C	- encrypted message    
a = (e - k) / (m - p)  
b = e - ma  
r = m^2 + e^2  
x = (b^2 - r) / ((a^2 + 1)m)  
y = ax - b  
C = (x, y)  
