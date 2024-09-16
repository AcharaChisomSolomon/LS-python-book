my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

[print(n) 
 for x in my_list 
 for n in x 
 if n % 2 == 0
]