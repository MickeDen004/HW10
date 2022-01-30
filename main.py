word = list(input("Enter: "))


def rep(lst: list) -> list:
    for item in range(len(lst)):
        lst[item] = ord(lst[item])


rep(word)
print(word)


# def calc(число1: float, действие: "function", число2: float = None) -> float:
#     if число2 is None:
#         результат = действие(число1)
#     else:
#         результат = действие(число1,число2)
#     return результат

def repair(x: str, action: "function") -> str:
    x = action(x)
    # if x == "лампочка":
    #     print("заменена лампочка")
    # elif x == "замок":
    #     print("смазан замок")
    # elif x == "ваза":
    #     print('ваза склеена')
    # elif x == "друзья":
    #     print('друзья помирились')
    # else:
    #     print('невозможно починить')
    return x


print(repair("лампочка", lambda x: x + " склеена"))
print(repair("friendship", lambda x: x + " is fixed"))

suits = ['\u2660', '\u2665', '\u2663', '\u2666']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(x, y) for x in suits for y in values]
deck.sort(key=lambda x:x[1])
deck.sort(key=lambda x:x[0])
