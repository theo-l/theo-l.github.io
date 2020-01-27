def spiral(count=6, r=1200):
    import math
    rotate_x = 0
    rotate_y = 0
    rotate_z = 0
    for i in range(1,count+1):
        rotate_x += (r/100. * math.pi)
        rotate_y += (r/100. * math.pi)
        rotate_z += (r/100. * math.pi)
        print(f'''
              :data-x: {math.cos(i)*r}    
              :data-y: {math.sin(i)*r}    
              :data-z: {math.log(i)*r}    
                
              :data-rotate-x: {rotate_x}
              :data-rotate-y: {rotate_y}
              :data-rotate-z: {rotate_z}
              \n
              ''')

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) <2:
        spiral()

    if len(args) == 2:
        spiral(args[1])

    if len(args) ==3:
        spiral(*args[1:3])
        
