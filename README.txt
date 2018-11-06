##### READ ME FILE#####

########################
     READ ME FIRST
########################

In order for script to run you need to have python 3.x installed and mozila 
firefox (script is written in python 3.6.6).

The script is using python selenium module and python pandas module.
To install this modules use this commands in cmd:

WINDOWS:
	pip install selenium
	pip install pandas
###############################################
                  ALL SET
###############################################
              FILE EXPLAIN
###############################################

##geckodriver.exe - has to be in the same folder as the script.
##file - backup.txt is folder where the script collects data, and save the data
in case of errors.
##file - links.txt has direct links for all categories(you can add or delete links 
to collect data you want from wattpad.com)

##########################
######  WAT.PY  ##########

wat.py is script writen in python to collect the data. When script finish
collecting data it will extract the data in the excel file called Data.xlsx.

To run the script open cmd in folder where the script is and run this command:

	python wat.py

Script will open firefox browser scroll the page and collect data 
#### DATA WILL BE PUT IN backup.txt FILE AND WHEN THE SCRIPT FINISH IT WILL CREATE Data.xlsx FILE WITH DATA!!!

#for windows OS!

#for any troubles be free to contact me i'm here to help :D
