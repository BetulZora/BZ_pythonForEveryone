# convert elevator floors from European floors to US floor
# In US the ground floor is floor 1
# In Europe the ground floor is floor 0

inp = input('Floor number in Europe?')
usf = int(inp) +1
print('US Floor', usf)