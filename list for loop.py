football = ['barcelona', 'real madrid', 'liverpool']
for soccer in football :
    print(soccer)
    
football_2 = ['barcelona 2', 'real madrid 2', 'liverpool 2']
for soccer in range(len(football_2)):
    print(football_2[soccer])

#WHILE LOOP 
football_3 = ['barcelona 3', 'real madrid 3', 'liverpool 3']
soccer_3 = 0
while soccer_3 < len(football_3):
    print(football_3[soccer_3])
    soccer_3 = soccer_3 + 1
    
football_4 = ['barcelona 4', 'real madrid 4', 'liverpool 4']
[print(soccer_4) for soccer_4 in football_4 ]

#SORT
integers = [1, 0.234, 789]
integers.sort()
print(integers)

#Reverse Sort 
integers = [1, 0.234, 789]
integers.sort(reverse = False)
print(integers)

integers = [1, 0.234, 789]
integers.sort(reverse = True)
print(integers)

