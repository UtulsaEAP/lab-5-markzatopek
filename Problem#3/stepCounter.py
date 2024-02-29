def feet_to_steps(user_feet):
   return int(user_feet / 2.5 + .5)

if __name__ == '__main__':
    #take input feet steps here
    feet_walked = float(input())
    #store it into the function
    
    #print your steps here
    print(feet_to_steps(feet_walked))