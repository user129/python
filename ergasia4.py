join=True
'''words = {} convert an integer number into words'''
num=int(input("give a number to convert to english(999.999.999<):"))
units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
thousands = ['','thousand','million']
                 
words = []

if num==0: words.append('zero')
else:
   numStr = '%d'%num
   numStrLen = len(numStr)
   groups = int((numStrLen+2)/3)
   
   numStr = numStr.zfill(groups*3)
   for i in range(0,groups*3,3):
        h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
        g = int(groups-(i/3+1))
        if h>=1:
            words.append(units[h])
            words.append('hundred')
        if t>1:
            words.append(tens[t])
            if u>=1: words.append(units[u])
        elif t==1:
            if u>=1: words.append(teens[u])
            else: words.append(tens[t])
        else:
            if u>=1: words.append(units[u])        
        if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
   if join: print( ' '.join(words)) 
   print (words)
   