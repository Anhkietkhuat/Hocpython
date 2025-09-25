
#cú pháp
dic = {'name': 'Kiet','age': '20'}
print(dic)
#
#khởi tạo bằng constructor
dic = dict()
print(dic)
print(type(dic))

#khởi tạo bằng iterable
iter_ = [('name', 'Kiet'),('age', '20')]
dic = dict(iter_)
print(dic)
print(type(dic))

# khởi tạo bằng keyword arguments
dic = dict(name='kiet',age=20)
print(dic)
print(type(dic))

# sử dụng phương thức fromkey
iter_ = ('name','number', 56)
dic = dict.fromkeys(iter_,'hello')
print(dic)
print(type(dic))

# thay đổi nội dung Dict
iter_ = ('name','number', 56)
dic = dict.fromkeys(iter_,'hello')
dic['name']='kiet'
dic['number']= 47578
print(dic)
print(dic['name'])

dic=dict(A='Anh',K=97)
print(dic)
dic['K']=dic['K']+1
print(dic)

#thêm thủ công 1 phần tử vào dict
dic=dict(A='Anh',K='Kiet')
print(dic)
dic['K']=dic['K']+':Hello'
dic['A']=dic['A']+':Hello'
print(dic)

#phương thức copy
a={'name':'kiet',(1,2):87}
b=a.copy()
print(a)
print(b)

# phương thức clear
c = {'name':'kiet',(1,2):87}
print(c)
c.clear()
print(c)
#
# # #phương thức Get
e= {'name':'kiet',(1,2):87}
print(e)
value=e.get('name')
print(value)

# # phương thức itemp
s= {'name':'kiet',(1,2):87}
print(s)
value=s.items()
print(value)
value=list(s.items())
print(value[0][0])

# phương thức key
S= {'name':'kiet',(1,2):87}
print(S)
value=S.keys()
print(value)
value=S.values()
print(value)

#phương thức pop
f= {'name':'kiet',(1,2):87}
print(f)
value=f.pop('name')
print(value)
print(f)


# Setdefault
e= {'name':'kiet',(1,2):87}
print(e)
value=e.setdefault('Hello wolrd','Hi')
print(value)
print(e)


