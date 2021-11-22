with open('ownercode.txt', 'w') as f:
	with open('container_2.txt', 'r', encoding = 'utf-8') as file:
		data = file.readlines()
		data1 = [i.replace('\n', '').split('\t')[0] for i in data]
		for k in data1:
			f.write(f'{k}\n')