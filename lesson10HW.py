mydict = {"蘋果" : "apple", "香蕉" : "banana", "貓咪" : "cat", "狗" : "dog", "大象" : "elephant"}

i = 0
while i == 0:
    choose = int(input('選擇功能: 1.列出所有單字 2.英翻中 3.中翻英 4.測驗學習成果 5.離開系統'))
    
    if choose == 1:  
        for x, y in mydict.items():
            print(x, y)
    
    if choose == 2:  
        english = input('請輸入要翻譯的英文?')
        for x, y in mydict.items():
            if y == english:
                print(y,'的中文是',x)
    
    if choose == 3: 
        chinese = input('請輸入要翻譯的中文?')
        english = mydict[chinese]
        print(chinese,'的英文是',english)
    
    if choose == 4: 
        TypeChoose = input('輸入(b)進入測驗')
        if TypeChoose == "b":  
            i = 0
            for x, y in mydict.items():
                print(y,'的中文是:')
                ans = input()
                if ans == x:
                    print('答對了,ㄏㄏ')
                    i = i + 1
                else:
                    print('答錯了,可憐哪')
            print('一共答對了:', i , '題')
    
    if choose == 5:                      
        i = 1                            
        print('系統已關閉,ㄅㄅ')

