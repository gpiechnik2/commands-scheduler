from __future__ import unicode_literals
import os
import sys
import time

from halo import Halo


spinner = Halo(text='Creating instances', spinner={
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
