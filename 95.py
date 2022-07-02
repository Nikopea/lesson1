import random
import math

start = 10000
stop = 60000
step = 1
random_list = [10420, 11462, 11861, 13514, 17999, 21011, 21730, 22195, 23183, 23731, 24538, 28840, 29630, 33892, 34018, 35183, 36850, 37273, 40368, 42785, 43360, 50376, 51826, 53975, 54008, 65700, 66200, 69900, 72500, 80000]
percent_95_1 = math.ceil((len(random_list) / 100) * 95)
percent_95_2 = math.floor((len(random_list) / 100) * 95)
x = (random_list[percent_95_1 - 1] - random_list[percent_95_2 - 1]) / 2
print(x)
y = (72500 / 100) + (69900 / 100)
result = random_list[percent_95_1 - 1] - y
print(result)
# for i in range(30):
#     random_list.append(random.randrange(start, stop, step))
# random_list = sorted(random_list)
# print(random_list[percent_95_1 - 1])
# print(random_list[percent_95_2 - 1])