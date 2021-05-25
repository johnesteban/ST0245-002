import numpy as np
class LZ77:
    
    def __init__(self, longitud):
        window_size=longitud
        self.window_size=int(window_size)
        self.buffer_size=15
        
    def longest_match(self, data, cursor):
        end_buffer=min(cursor+self.buffer_size,len(data)-1) 
        p=-1  
        l=-1  
        c='' 
        for j in range(cursor+1,end_buffer): 
            start_index=max(0,cursor-self.window_size+1) 
            substring=data[cursor+1:j+1] 
            for i in range(start_index,cursor+1): 
                repetition=len(substring)/(cursor-i+1) 
                last=len(substring)%(cursor-i+1) 
                matchedstring=np.append(data[i:cursor+1]*int(repetition),data[i:i+last],0)
                if np.array_equal(matchedstring,substring) and len(substring)>l: 
                    p=cursor-i+1  
                    l=len(substring) 
                    c=data[j+1] 
                    
        if p==-1 and l==-1: 
            return 0,0,data[cursor+1]  
        return p,l,c 
    
    def compress(self,mensaje):
        i=-1 
        out=[]
        while i<len(mensaje)-1: 
            (p,l,c)=self.longest_match(mensaje,i)
            out.append((p, l, c)) 
            i+=(l+1) 
        return out 
    
    def decompress(self, compressed):
        cursor=-1 
        out=[] 
        for (p,l,c) in compressed: 
            inicio=cursor-p+1 
            if p == 0 and l == 0: 
                out.append(c)  
            elif p>=l: 
                out.extend(out[inicio:inicio+l]) 
                out.append(c) 
            elif p<l: 
                repetition=l/p 
                last=l%p  
                out.extend(out[inicio:inicio+l]*int(repetition)) 
                out.extend(out[inicio:last]) 
                out.append(c) 
            cursor+=(l+1) 
        return out 
    
    