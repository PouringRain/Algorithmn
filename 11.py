# -*- coding:utf-8 -*-                           
class Solution:                                  
    def FindContinuousSequence(self, tsum):      
        # write code here                        
        # t至少为2                                  
        res = []                                 
        if tsum < 3: return []                   
        upbound = tsum // 2                      
                                                 
        for i in range(1, upbound+1):            
            s = tsum; sub = []                   
                                                 
            for j in range(i, tsum):             
                if s - j == 0:  # 找到了            
                    sub.append(j)                
                    res.append(sub)              
                elif s - j > 0:  # 还能匹配          
                    s -= j                       
                    sub.append(j)                
                else:  # 拉倒吧                     
                    break                        
                                                 
        return res                               
                                                 
