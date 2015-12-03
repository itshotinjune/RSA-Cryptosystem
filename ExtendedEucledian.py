'''This module implements the Extended Eucledian Algorithm as described in the class'''

from modulo import modulo

def gcd(a, b, disp):
    x,y, u,v = 0,1, 1,0
    count = 1
    template = "{0:2}|{1:7}|{2:7}|{3:7}|{4:7}|{5:6}|{6:6}" # column widths: 8, 10, 15, 7, 10
    if disp:
	    print ("------------------------------------------------")
	    print template.format("i","qi","r","ri+1","ri+2","si","ti")
	    print ("------------------------------------------------")
    while a != 0:
        q, r = b/a, modulo(b,a)
        if disp:
        	print template.format(str(count),str(q),str(b),str(a),str(r),str(y),str(x))
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n 
        count = count+1 

    gcd = b

    if disp:
	    print template.format(str(count),"",str(b),"","",str(y),str(x))
	    print ("------------------------------------------------\n") 
	    
    return gcd, x, y