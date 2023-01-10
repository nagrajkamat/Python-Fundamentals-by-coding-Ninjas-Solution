#Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

Fahrenheit to Celsius conversion table. One line for every Fahrenheit and corresponding Celsius value in integer form. 
The Fahrenheit value and its corresponding Celsius value should be separate by single space.

#Input 1-
0 
100 
20

#Output 1-
0   -17
20  -6
40  4
60  15
80  26
100 37


#Code1 -

fahrenheit = int(input())
E = int(input())
W = int(input())
while fahrenheit <= E :
    fahrenheit_to_celsius = (((fahrenheit - 32) * 5) / 9)
    print(fahrenheit, int(fahrenheit_to_celsius))
    fahrenheit = fahrenheit + W

#Code2 -

start=int(input())
end=int(input())
step=int(input())

currentFahrenhietValue = start
while currentFahrenhietValue <= end :
  celsiusValue (5/9) (currentFahrenhietValue - 32)

print(str(currentFahrenhietValue) + " " + str(int(celsiusValue)))
currentFahrenhietValue += step
