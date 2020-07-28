'''
a simple sunrise/sunset calculator
source for formulae: National Oceanic and Atmospheric Administration (NOAA)
https://www.esrl.noaa.gov/gmd/grad/solcalc/solareqns.PDF
'''

import sys
import math

def utc_times(lon, hour_angle, eq_time):
	#returns utc sunrise and sunset times based on parameters
	sunrise = 720-4*(lon+hour_angle)-eq_time
	sunset = 720-4*(lon-hour_angle)-eq_time
	return (sunrise, sunset)

def is_leap(year):
	#checks if the date occurs in a leap year
	year=int(year)
	if (year%4==0 and year%100!=0) or (year%400==0):
		return True
	else:
		return False

def date_to_doy(date):
	#converts date of format yyyymmdd to the number day of the year
	days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	month = int(date[4:6])
	the_day = int(date[6:])
	doy = 0
	for num in days_in_months[:month-1]:
		doy+=num
	doy+=the_day
	if is_leap(date[0:4]) and month>2:
		doy+=1
	return doy

def mins_to_time(mins):
	#converts raw number of minutes to hours and minutes
	hour=int(mins//60)
	minutes=int(mins%60)
	return (hour, minutes)

def print_out(lat_d, lon_d, times):
	#converts output to a more readable form and prints it
	times_out = (mins_to_time(times[0]), mins_to_time(times[1]))
	print "For coordinates %f, %f in your selected time zone:" % (lat_d, lon_d)
	print "Sunrise: %dhr, %dmin" %(times_out[0][0], times_out[0][1])
	print "Sunset: %dhr, %dmin" %(times_out[1][0], times_out[1][1])

def go(lat_d, lon_d, date, time_zone=0):
	lat = math.radians(lat_d)
	lon = math.radians(lon_d)
	if is_leap(date[0:4]):
		leap = 1
	else:
		leap = 0
	day = date_to_doy(date)
	frac_year = ((math.pi*2)/(365+leap))*(day-1) #radians
	eq_time = 229.18*(0.000075+(0.001868*math.cos(frac_year))\
				-(0.032077*math.sin(frac_year))-(0.014615*math.cos(2*frac_year))\
				-(0.040849*math.sin(2*frac_year))) #minutes
	decl = 0.006918-(0.399912*math.cos(frac_year))+(0.070257*math.sin(frac_year))\
				-(0.006758*math.cos(2*frac_year))+(0.000907*math.sin(2*frac_year))\
				-(0.002697*math.cos(3*frac_year))+(0.00148*math.sin(3*frac_year)) #radians
	hour_angle = math.degrees(math.acos(\
				math.cos(math.radians(90.833))/(math.cos(lat)*math.cos(decl))\
				-(math.tan(lat)*math.tan(decl)))) #degrees

	times = utc_times(lon_d, hour_angle, eq_time)
	converted = ((times[0]+time_zone*60), (times[1]+time_zone*60))
	print_out(lat_d, lon_d, converted)

def main():
	if len(sys.argv)>4:
		go(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]), float(sys.argv[4]))
	else:
		go(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]))

if __name__ == '__main__':
  main()
