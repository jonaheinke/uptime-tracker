# -------------------------------------------------------------------------------------------------------------------- #
#                                                        IMPORT                                                        #
# -------------------------------------------------------------------------------------------------------------------- #

import os, time
from datetime import datetime



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       SETTINGS                                                       #
# -------------------------------------------------------------------------------------------------------------------- #

filename = os.path.abspath("uptime.txt")
new_date_format_string = "%d.%m.%Y: %H:%M - %H:%M"
replacement_format_string = "%H:%M"



# -------------------------------------------------------------------------------------------------------------------- #
#                                                WRITE NEW DATE TO FILE                                                #
# -------------------------------------------------------------------------------------------------------------------- #

def new_date_entry():
	with open(filename, "a") as file:
		if file.tell():			#if file is not empty
			file.write("\n")	#add a new line character
		file.write(datetime.now().strftime(new_date_format_string))



# -------------------------------------------------------------------------------------------------------------------- #
#                                                      UPDATE TIME                                                     #
# -------------------------------------------------------------------------------------------------------------------- #

def update_time():
	#generate the new time
	time_str = datetime.now().strftime(replacement_format_string)
	with open(filename, "r+") as file: #"r+" mode is required to override the last line, with "a" or "a+" it always just appends to the end
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
	new_date_entry()
	while True:
		#wait until the next minute
		time.sleep(60 - datetime.now().second)
		now = datetime.now()
		if now.hour or now.minute:
			#write the current time to file every minute
			update_time()
		else:
			#write a new date every day at midnight
			new_date_entry()
except:
	pass