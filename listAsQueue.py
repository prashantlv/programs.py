from collections import deque

annu = deque(['check','hussian','anam','bill','board'])

print(annu)

annu.append('append')
print(annu)

annu.popleft()			# allow us to pop from index 0

print(annu)