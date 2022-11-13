car_name= input('enter car name')
brand_name= input('enter brand name')
engine_type= input('enter engine type')
fuel_type= input('enter fuel type')
suspension= input('enter suspension info')
dimension_and_capacity= input('enter dimension')
comfort_and_convenience= input('enter comfort zone')
interior= input('enter interior information')
exterior= input('enter exterior information')
safety= input('enter safety information')
additional_feature= input('enter aditional feature')

print("Best Maruti Suzuki cars in India")
print()
intro= f"""
There are 17 cars available in India, among which popular car models include Thar, Brezza, Nexon, XUV700, Punch & many 
more. The top Indian car brands are Mahindra, Maruti Suzuki, Tata,. Explore the list of best cars price in India and 
Compare cars to find the right car for you. Also, check out Top Electric cars in India which are available for sale.
Here we will discuss about {car_name} from {brand_name} and its key features.
"""
print(intro)
print('Standout Features of', car_name)
main_text= f"""
1.  Car Name                : {car_name}
2.  Brand Name              : {brand_name}
3.  Engine Type             : {engine_type}
4.  Fuel Type               : {fuel_type}
5.  Suspension              : {suspension}
6.  Dimension and Capacity  : {dimension_and_capacity}
7.  Comfort and Convenience : {comfort_and_convenience}
8.  Interior                : {interior}
9.  Exterior                : {exterior}
10. Safety                  : {safety}
11. Additional Feature      : {additional_feature}
"""
print(main_text)
print()
conclusion= f"""
This is the quick look of {car_name} manufactured by {brand_name}. To know more like this exciting cars and its features
follow our website.  
"""
print(conclusion)