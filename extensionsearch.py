#! /usr/bin/env python3

import os

place = input("What directory are you searching?\n")

laExtension = input("What file extension are you searching for?\n")

laExtension = laExtension.lower()

for file in os.listdir(place):
	if file.endswith(laExtension):
		print(os.path.join(place, file))
