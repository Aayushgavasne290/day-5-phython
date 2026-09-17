def countdown(n):
    if n == 0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)