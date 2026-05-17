'''
a python script that converts Celsius to Fahrenheit for three specific ceratures:
- 0 deg C
- 25 deg C
- 100 deg C
'''


celsius = [0, 25, 100]

for c in celsius:
    Fahrenheit1 = (c * 9/5) + 32
    print(f"{c}°C is equal to {Fahrenheit1}°F")