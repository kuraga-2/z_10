input_data = open('input.txt', 'r')
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
k = None
l = None
m = None
for i in range(-100,101):
    if a*(i**3) + b*(i**2) + c*i + d == 0:
      k=i
      break
for i in range(k+1,101):
   if a*(i**3) + b*(i**2) + c*i + d == 0:
      l=i
      break
for i in range(l+1,101):
   if a*(i**3) + b*(i**2) + c*i + d == 0:
      m=i  
if l is None and m is None:
  o=str(k)
elif m is None:
  o=str(k) + ' ' + str(l)
else:
  o=str(k) + ' ' + str(l) + ' ' + str(m) 
   
output_data = open('output.txt', 'w')
output_data.write(o)
input_data.close()
output_data.close()