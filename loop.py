password = 'a123456'
x = 3
while x > 0:
    x = x - 1
    user = input('Please enter your password :')
    if user != password:
        if x > 0:
            print('密碼錯誤! 還有', x, '次機會!') 
        if x == 0:
            print('密碼錯誤! 沒機會了歐~')            
    else:
        print('登入成功!')
        break
