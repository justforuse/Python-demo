import random
secret = random.randint(1,10)
print("���һ������")

time=0
while time < 3:
	temp=input("������Ĵ�\n")
	#guess = int(temp)
	if temp == secret:
		print("��ϲ����¶���")
		print("�����Ҳ��ܸ����κν���")
		break
	else:
		time = time + 1
		if temp < secret:
			print("��Ĵ�̫С��")
		else:
			print("�е����")
if time == 3:
        print("3�λ�������")
print("��Ϸ�������ݰ�~")
