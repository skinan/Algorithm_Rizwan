#Greedy Algorithm, used to determine the amount of money to be paid to bus drivers for over time.

def call(num):
    final = int(0)
    morning_route = input().split(" ")

    evening_route = input().split(" ")

    morning_route.sort()
    evening_route.sort(reverse=True)

    for i in range(0, int(num[0])):
        total_hours = int(morning_route[i]) + int(evening_route[i])

        if total_hours > 20:
            over_time = total_hours - 20
            count = over_time * int(num[2])
            final = final + count
    return final


z = True
ans = ""

while z != False:
    num = input().split(" ")
    if 1 <= int(num[0]) <= 100 and 1 <= int(num[1]) <= 10000 and 1 <= int(num[2]) <= 5:
        value = str(call(num = num))
        ans = ans + value + "\n"
    if int(num[0]) == 0 and int(num[1]) == 0 and int(num[2]) == 0:
        break
    del num

print(ans)





