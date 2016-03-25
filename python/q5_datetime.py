from datetime import date
from time import strptime
# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def a():
	from datetime import date

	date_start = '01-02-2013'    
	date_stop = '07-28-2015'

	date_start_list = date_start.split('-')
	date_stop_list  = date_stop.split('-')


	start = date(int(date_start_list[2]), int(date_start_list[0]), int(date_start_list[1]))
	stop = date(int(date_stop_list[2]), int(date_stop_list[0]), int(date_stop_list[1]))

	days = stop - start
	print(days)

def b():
	date_start = '12312013'  
	date_stop = '05282015'  

	start = date(int(date_start[4:]), int(date_start[0:2]), int(date_start[2:4]))
	stop = date(int(date_stop[4:]), int(date_stop[0:2]), int(date_stop[2:4]))

	days = stop -start 

	print(days)

def c():
	date_start = '15-Jan-1994'      
	date_stop = '14-Jul-2015'  

	date_start = date_start.split('-')
	date_stop = date_stop.split('-')
	month = date_start[1]
	start_mon = strptime(month,'%b').tm_mon
	month1 = date_stop[1]
	stop_mon = strptime(month1,'%b').tm_mon


	start = date(int(date_start[2]), start_mon, int(date_start[0]))
	stop = date(int(date_stop[2]), stop_mon, int(date_stop[0]))


	days = stop - start
	print(days)


a()
b()
c()