"""
Given n as input, print the following pattern
n=2
1*1-1=0 
2*2-2=2
"""

n = 4
num = 0
for i in range(1,n+1):
  num = i*i-i
  print(f'{i}*{i}-{i}={num}')
