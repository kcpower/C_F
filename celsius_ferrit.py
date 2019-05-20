while True:
    select = input("攝𨍭華請按 1; 華轉攝請按 2; 結束請按 q:")
    if select == "q":
        break
    elif select == "1":
        select = int (select)
        C = input("請輸入攝氏度數:")
        Ferrit = 9/5 * float(C) + 32
        print("攝氏", C, "度為華氏", Ferrit, "度")
    elif select == "2":
        select = int(select)
        F = input("請輸入華氏度數:")
        Celsius = (float(F) - 32) * 5/9
        print("華氏", F, "度為攝氏", Celsius, "度")
    else:
        print("請輸入正確選項!")