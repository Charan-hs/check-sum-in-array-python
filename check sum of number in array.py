


ar = [1,6,1,2]
s = 8

def checkSum(arr,s):
    d = {}
   
    for i in range(len(arr)):
      
        #asking
        if(d.get(arr[i])):
            return "found"
        #adding
        d[s - arr[i]] = "ohh"
        #print(d)
    return "Not Found"
        

        
        
        
print("1st :",checkSum(ar,s))
print("2st :",checkSum([1,2,34,5,6,7,88],




