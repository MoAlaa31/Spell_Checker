def bublesort(alist):
    #second requirement
  list_words=[]
  n=len(alist)
  if n>6:
      c=n-6
  else:
      c=0
  for i in range(n-1,c,-1):
     for j in range(i):
         if alist[j][0]>alist[j+1][0]:
             alist[j],alist[j+1]=alist[j+1],alist[j]
  alist.reverse()
  for i in range(6):
        list_words.append(alist[i][1])
  return list_words