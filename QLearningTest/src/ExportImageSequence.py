import cv2

def make_video():
	fourcc = cv2.VideoWriter_fourcc(*'XVID')

	out = cv2.VideoWriter('qlearn.mp4', fourcc, 60.0, (1200, 900))

	for i in range(0, 12050, 10):
		img_path = f"C:\_My Files\Python\QLearningTest\QLearningTest\qtable_charts\{i}.png"
		print(img_path)
		frame = cv2.imread(img_path)
		out.write(frame)

	out.release()


make_video()
