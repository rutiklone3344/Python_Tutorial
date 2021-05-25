# Convert The Celcius to Farenheit
def convert (cel):
    return((cel * 9/5) + 32)

c = int(input("Enter the Temperature in Celcius: "))
f = convert(c)
print("Converted Farenheit Temperature is: "+ str(f))