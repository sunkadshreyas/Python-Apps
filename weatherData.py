import xlsxwriter
import requests,json
import time

# Opening a Excel workbook with two sheets
workbook = xlsxwriter.Workbook('example.xlsx')
worksheet1 = workbook.add_worksheet('Sheet 1')
worksheet2 = workbook.add_worksheet('Sheet 2')

# In sheet 1 writing the column headings
# First column is City and next three are temperatures 
worksheet1.write(0,0,'City')
worksheet1.write(0,1,'Temp in celsius')
worksheet1.write(0,2,'Temp in fahrenheit')

# Initializing the start time
starttime = time.time()

# Initializing an empty list
cities = []

# Input the number of entries for every city
print ('Enter the number of entries for each city : ')
entries = int(input())

# Input the cities
print ('Enter the cities and 0 to stop: ')
while True:
	city = input('Enter city name : ')
	if city=='0':
		break
	else:
		cities.append(city)

# Write the list of cities in second sheet
worksheet2.write(0,0,'Cities')
for i in range(0,len(cities)):
	worksheet2.write(i+1,0, cities[i])		
			

# function to write data into sheet 1
def writeSheet(row, city,celsius,fahrenheit):
	worksheet1.write(row,0,city)
	worksheet1.write(row,1,celsius)
	worksheet1.write(row,2,fahrenheit)
	
	
# function to make API call to site and get temperature in 
# various scales
def getWeatherData(city):

	base_url = 'http://api.openweathermap.org/data/2.5/weather?'

	api = '' # use the api key from website

	url = base_url + 'appid=' + api + '&q=' + city

	data = requests.get(url)

	data_json = data.json()

	temperature_in_kelvin = round(data_json['main']['temp'],3)
	temperature_in_celsius = round(temperature_in_kelvin - 273.15,3)
	temperature_in_fahrenheit = round(temperature_in_celsius * (9/5) + 32,3)

	#print (city)
	#print ('{0} {1} {2}\n'.format(temperature_in_celsius, temperature_in_fahrenheit,temperature_in_kelvin))

        
	return (temperature_in_celsius, temperature_in_fahrenheit)



# iterate over entries for every 20 seconds
# number can be changed to update at desired interval
for row in range(entries):
	for i in range(len(cities)):
		c,f = getWeatherData(cities[i])
		writeSheet(row+1+(i*entries), cities[i], c, f)
	time.sleep(20.0 - ((time.time() - starttime) % 20.0))

		
print ('End of function!!\nClosing the Excel file!!')		
# closing the workbook		
workbook.close()		
			


