from __future__ import unicode_literals
import os
import sys
import time

from halo import Halo

spinner = Halo(text='Waiting for the test to start. Launching the test at: XXX', spinner={
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

def get_current_time():
	return 0

def get_seconds_to_run(scheduled_time, current_time):
	return 0

def run_command(command):
	return 0

def schedule(scheduled_time, command):
	


try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Much Colors'
    spinner.color = 'magenta'
    time.sleep(2)
    spinner.text = 'Very emojis'
    spinner.spinner = 'hearts'
    time.sleep(2)
    spinner.stop_and_persist(symbol='🦄'.encode('utf-8'), text='Wow!')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
