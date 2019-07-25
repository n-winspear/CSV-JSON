#CSV to JSON file converter

import csv
import json
import os

for file in os.listdir("./CSVS"):
	working_file = open("./CSVS/{}".format(file), "rU")
	file_reader = csv.DictReader(working_file, fieldnames = ("stepNumber", "instructions/0/position", "instructions/0/action", "instructions/1/position", "instructions/1/action", "instructions/2/position", "instructions/2/action", "directiveIdeas"))
	output = json.dumps([row for row in file_reader])
	output_file = open("./JSONS/{}.json".format(file[:-4]), "w")
	output_file.write(output)
	output_file.close()

print("All Parsed & Saved")
