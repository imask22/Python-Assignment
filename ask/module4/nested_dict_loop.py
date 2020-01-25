people={1:{'name':'john','age':'27','sex':'male'},2:{'name':'Marie','age':'22','sex':'Female'} }
for p_id,p_info in people.items():
    print("Person ID",p_id)


for key in p_info:
    print(key+":"+p_info[key])
