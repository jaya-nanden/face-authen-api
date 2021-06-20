import json, requests

#url = 'https://ec-api-model.herokuapp.com/im_size' # change to your url

url = 'http://127.0.0.1:5000/im_size'

for i in range(1,5):
	path="./test"+str(i)+".jpg"
	my_img = {'image': open(path, 'rb')}
	r = requests.post(url, files=my_img)

	#print(r)
	print(r.json())