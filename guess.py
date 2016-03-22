import random
secret = random.randint(1,10)
print("请猜一个数字")

time=0
while time < 3:
	temp=input("输入你的答案\n")
	#guess = int(temp)
	if temp == secret:
		print("恭喜，你猜对了")
		print("但是我不能给你任何奖励")
		break
	else:
		time = time + 1
		if temp < secret:
			print("你的答案太小了")
		else:
			print("有点大了")
if time == 3:
        print("3次机会用完")
print("游戏结束，拜拜~")
