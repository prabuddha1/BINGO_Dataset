import cv2
import sys
import os
import argparse



if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='')
	parser.add_argument('-i', '--inputPath', type=str, nargs=1, help='inputPath.')
	parser.add_argument('-o', '--outputPath',type=str, nargs=1, help='outputPath.')
	parser.add_argument('-intSkip', '--intSkip',type=str, nargs=1, help='intSkip.')

	args = parser.parse_args()

	inputPath = args.inputPath[0]
	outputPath = args.outputPath[0]
	intSkip = int(args.intSkip[0])
	os.system("mkdir -p "+outputPath)

	vid = cv2.VideoCapture(inputPath)
	res,img = vid.read()
	count = 0
	while res:
		if intSkip > 0:
			intSkip = intSkip - 1
		else:
			cv2.imwrite(outputPath+"%d.jpg" % count, img)     # save frame as JPEG file
			count = count + 1      
		res,img = vid.read()
		print('Read a new frame: ', res)
		