def driving_cost(miles_per_gallon:float, dollars_per_gallon:float, miles_driven:float):
   return dollars_per_gallon / miles_per_gallon * miles_driven

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   