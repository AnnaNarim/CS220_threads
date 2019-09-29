from concurrent.futures import ThreadPoolExecutor
import shutil
import os

source = os.listdir("./copyFrom")
destination = "./copyTo"

def copyFiles():
	for file in source:
		shutil.copy("./copyFrom/" + file, destination)


def main():
	thread1 = ThreadPoolExecutor(3)
	thread1.submit(copyFiles)

if __name__ == '__main__':
  main()