password = 'a123456'
x = 3
while x <= 3 and x > 0:
    user = input('Please enter your password :')
    if user != password:
        print('密碼錯誤! 還有', x - 1, '次機會!')
        x = x - 1
    else:
        print('登入成功!')
        break
