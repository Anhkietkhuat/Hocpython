
# while
a = 5
while a > 0:
    print('a =', a)
    a -= 1
    # a += 1




# sử dụng vòng lặp While để xử lí chuỗi ,list ,tuple
a = 'Hello world'
idx = 0       #vị trí bắt đầu muốn sử lí chuỗi
length = len(a)  #lấy độ dài chuỗi làm mốc kết thúc

while idx < length:
    print(idx,'....',a[idx])
    idx +=1    # di chuyển đến vị trị tiếp theo

# break: thoát khỏi vòng lặp ngay lập tức
five_even_numbers = []   #tạo ra 5 số chẵn
k_number = 1



while True:                        # vòng lặp vô hạn
    if k_number % 2 == 0:          # nếu k_number là một số chẵn
        five_even_numbers.append(k_number)            # thêm giá trị của k_number vào list
        if len(five_even_numbers) == 5:               # độ dài =5
            break # thì kết thúc vòng lặp
    k_number += 1
print(k_number)
print(five_even_numbers)
# từ 1 trở lên lấy ra 5 phần tử chẵn đầu tiên




# Continue :bỏ qua vòng lặp hiện tại, sang lần lặp tiếp theo
k_number=0
while k_number < 10:
    k_number+= 1        #tăng 1 đơn vị cho k_number và tiếp tục
    if k_number %2 == 0:     #nếu k_number là số chẵn
        continue           # tiếp tục vòng lặp
    print(k_number,'is old number')
print(k_number)




# while - else
k=0
while k < 5:
    print('value of k is', k)
    k += 1
else:
    print('k is not less than 3 anymore')




length = 5
iter_ = (x for x in range(length))
c = 0
while c < length:
    print(next(iter_))
    c += 1

