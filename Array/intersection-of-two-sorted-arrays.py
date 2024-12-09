 
 ans = []
 while (i < len(arr1) and j < len(arr2)) 
       
    if (A[i] < B[j]) : 
      i += 1
    elif (B[j] < A[i]) :
      j += 1
    else:
      ans.append(A[i]); 
      i += 1
      j += 1

  
  return ans