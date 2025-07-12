import random

def guess_number_game():
    number = random.randint(1, 100)
    attempts = 0
    print("欢迎来到猜数字游戏！我已经选好了一个 1 到 100 之间的数字。")
    while True:
        try:
            guess = int(input("请输入你的猜测: "))
            attempts += 1
            if guess < number:
                print("太小了！")
            elif guess > number:
                print("太大了！")
            else:
                print(f"恭喜你猜对了！答案是 {number}，你一共猜了 {attempts} 次。")
                break
        except ValueError:
            print("请输入有效的整数！")

if __name__ == "__main__":
    guess_number_game()
