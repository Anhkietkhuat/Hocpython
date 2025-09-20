

#định dạng bằng phương thức format

# r = '1: {b}, 2: {a}'.format(b=555,a=86667)
# s = '1: {1}, 2: {0}'.format(5, 8)
# print(s)
# print(r)

#căn lề bằng phương thức format
a = '{:^20}'.format('Hello')    #căn giữa khoảng cách 20 kí tự
b = '{:*^50}'.format('Hello')

c = '{:@<50}'.format('Wolrd')  #căn lề trái

r = '{:*>30}'.format('Hello Wolrd')   #căn lề phải
s = '{:30'
print(a)
print(b)
print(c)
print(r)