import os
from datetime import datetime
from time import sleep

from halo import Halo


def wait_for_run(sleep_time, scheduled_time, command):
	spinner = Halo(text='Waiting for the command to run at: {}.'.format(scheduled_time), spinner = {
		"interval": 80,
		"frames": [
			"⠁",
			"⠁",
			"⠉",
			"⠙",
			"⠚",
			"⠒",
			"⠂",
			"⠂",
			"⠒",
			"⠲",
			"⠴",
			"⠤",
			"⠄",
			"⠄",
			"⠤",
			"⠠",
			"⠠",
			"⠤",
			"⠦",
			"⠖",
			"⠒",
			"⠐",
			"⠐",
			"⠒",
			"⠓",
			"⠋",
			"⠉",
			"⠈",
			"⠈"
		]
	})

	try:
		spinner.start()
		sleep(sleep_time)
		success_message = "Loading success. Running: {}.".format(command)
		spinner.succeed(success_message)
	except(KeyboardInterrupt, SystemExit):
		spinner.stop()

def get_current_time():
	now = datetime.now()
	return now

def get_date_from_string(dt_string):
	try: 
		return datetime.strptime(dt_string, '%d-%m-%Y %H:%M:%S')
	except ValueError as err:
		print("Enter the correct date format: DAY-MONTH-YEAR HOUR:MINUTE:SECOND, for example: 21-05-2022 14:55:23.")
		exit()

def get_seconds_to_run(scheduled_time, current_time):
	return(scheduled_time - current_time).total_seconds()

def run_command(command):
	os.system(command)

def schedule_command(scheduled_time, command):
	now = get_current_time()
	scheduled_date = get_date_from_string(scheduled_time)
	time_between = get_seconds_to_run(scheduled_date, now)

	# validate if scheduled date is in the past
	if time_between <= 0:
		print("No past date can be given.")
		exit()

	wait_for_run(time_between, scheduled_date, command)
	run_command(command)
