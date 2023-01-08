# -------------------------------------------------------------------------------------------------------------------- #
#                                                        IMPORT                                                        #
# -------------------------------------------------------------------------------------------------------------------- #

import os, time
from datetime import datetime



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       SETTINGS                                                       #
# -------------------------------------------------------------------------------------------------------------------- #

filename = os.path.abspath("uptime.txt")
original_format_string = "%d.%m.%Y: %H:%M - %H:%M"
replacement_format_string = "%H:%M"



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       ON ENTER                                                       #
# -------------------------------------------------------------------------------------------------------------------- #

with open(filename, "a") as file:
	if file.tell():			#if file is not empty
		file.write("\n")	#add a new line character
	file.write(datetime.now().strftime(original_format_string))



# -------------------------------------------------------------------------------------------------------------------- #
#                                                      UPDATE TIME                                                     #
# -------------------------------------------------------------------------------------------------------------------- #

def update_time():
	with open(filename, "r+") as file: #"r+" mode is required to override the last line, with "a" or "a+" is always just appends to the end
		#generate the new time
		time_str = datetime.now().strftime(replacement_format_string)
		#seek to EOF
		file.seek(0, 2)
		#seek to length of the new time string before EOF, has to be seperate from the previous seek because python is weird and prevents seeking backwards from EOF since 3.2
		file.seek(file.tell() - len(time_str), 0)
		#override the last characters with the current time
		file.write(time_str)



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       MAIN LOOP                                                      #
# -------------------------------------------------------------------------------------------------------------------- #

try:
	#wait until the next minute
	time.sleep(60 - datetime.now().time().second)
	while True:
		#write the current time to file every minute
		update_time()
		time.sleep(60)
except:
	pass