w, h ,b = map(int,input().split(' '))
imageFile = round(w * h * b / 8 / 1024 / 1024,2)
print("%.2f MB" %(imageFile))