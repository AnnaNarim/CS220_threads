import shutil
import os

source = os.listdir("./copyFrom")
destination = "./copyTo"

for file in source:
	shutil.copy("./copyFrom/" + file, destination)

print 'Copied ', source, ' from ./copyFrom to ', destination