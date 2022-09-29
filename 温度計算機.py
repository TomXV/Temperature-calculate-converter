import os
from time import sleep


def main():
    print("""
変換したい先を選んでください。
------------------------------
摂氏から、華氏に変換: F
華氏から、摂氏に変換: C
""")
    sel = str(input(">>> ").upper())

    if sel == "F":
        clearConsole()
        calc_temp_to_F()
    elif sel == "C":
        clearConsole()
        calc_temp_to_C()
    else:
        print("入力された値が正しくありません。")
        sleep(3)
        clearConsole()
        main()

def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def calc_temp_to_F():
    try:
        temp = float(input("摂氏: "))
        calc_result = temp * 9 / 5 + 32

        print(f"{round(temp, 1)}℃は、{round(calc_result, 1)}℉です。")
    except ValueError:
        print("計算エラーです。入力された値が、間違っています。")
        sleep(3)
        clearConsole()
        calc_temp_to_F()


def calc_temp_to_C():
    try:
        temp = float(input("華氏: "))
        calc_result = 5 / 9 * (temp -32)
        print(f"{round(temp, 1)}℉は、{round(calc_result, 1)}℃です。")
    except ValueError:
        print("計算エラーです。入力された値が、間違っています。")
        sleep(3)
        clearConsole()
        calc_temp_to_C()


if __name__ == "__main__":
    main()


    print("続けて計算したい場合は、Yを入力してください")
    con = input("プログラムを終了するには、Enterキーを押してください: ").upper()

    if con == "Y":
        main()
    else:
        exit()
