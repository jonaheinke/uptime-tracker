# -------------------------------------------------------------------------------------------------------------------- #
#                                                        IMPORT                                                        #
# -------------------------------------------------------------------------------------------------------------------- #

import os, time
from datetime import datetime

filename = os.path.abspath("uptime.txt")



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       ON ENTER                                                       #
# -------------------------------------------------------------------------------------------------------------------- #

start_dt = datetime.now()
with open(filename, "a") as file:
	if file.tell():			#if file is not empty
		file.write("\n")	#add new line character
	file.write(start_dt.strftime("%d.%m.: %H:%M - %H:%M"))



# -------------------------------------------------------------------------------------------------------------------- #
#                                                      UPDATE TIME                                                     #
# -------------------------------------------------------------------------------------------------------------------- #

def update_time():
	with open(filename, "r+") as file: #"r+" mode is required to override the last line, with "a" or "a+" is always just appends to the end
		#seeks to end of file
		file.seek(0, 2)
		#seek five characters before the end of the file
		file.seek(file.tell() - 5, 0)
		#override the last five characters with the current time
		file.write(datetime.now().strftime("%H:%M"))



# -------------------------------------------------------------------------------------------------------------------- #
#                                                       MAIN LOOP                                                      #
# -------------------------------------------------------------------------------------------------------------------- #

try:
	#wait until the next minute
	time.sleep(60 - datetime.now().time().second)
	while True:
		update_time()
		time.sleep(60)
except:
	pass