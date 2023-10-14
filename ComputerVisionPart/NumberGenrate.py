def six_nine():
    import random
    numbers_car = [random.randint(100, 150) for _ in range(13)]
    numbers_bike = [random.randint(10, 40) for _ in range(13)]
    numbers_bus = [random.randint(20, 50) for _ in range(13)]
    numbers_truck = [random.randint(0, 5) for _ in range(13)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def Am11_1PM():
    import random
    numbers_car = [random.randint(20, 70) for _ in range(9)]
    numbers_bike = [random.randint(5, 10) for _ in range(9)]
    numbers_bus = [random.randint(3, 15) for _ in range(9)]
    numbers_truck = [random.randint(20, 30) for _ in range(9)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])
def pm4_pm630():
    import random
    numbers_car = [random.randint(100, 150) for _ in range(11)]
    numbers_bike = [random.randint(10, 40) for _ in range(11)]
    numbers_bus = [random.randint(20, 50) for _ in range(11)]
    numbers_truck = [random.randint(5, 10) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Pm10_4am():
    import random
    numbers_car = [random.randint(10, 20) for _ in range(25)]
    numbers_bike = [random.randint(0, 5) for _ in range(25)]
    numbers_bus = [random.randint(0, 1) for _ in range(25)]
    numbers_truck = [random.randint(10, 40) for _ in range(25)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])



# ------------------------------------------------------------------------------------------------------

def am415_545am():
    import random
    numbers_car = [random.randint(50, 120) for _ in range(7)]
    numbers_bike = [random.randint(0, 30) for _ in range(7)]
    numbers_bus = [random.randint(0, 10) for _ in range(7)]
    numbers_truck = [random.randint(0, 20) for _ in range(7)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])
def am915_1045pm():
    import random
    numbers_car = [random.randint(10, 100) for _ in range(7)]
    numbers_bike = [random.randint(1, 25) for _ in range(7)]
    numbers_bus = [random.randint(5, 40) for _ in range(7)]
    numbers_truck = [random.randint(5, 30) for _ in range(7)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])
def pm15_345pm():
    import random
    numbers_car = [random.randint(5, 120) for _ in range(11)]
    numbers_bike = [random.randint(10, 30) for _ in range(11)]
    numbers_bus = [random.randint(5, 40) for _ in range(11)]
    numbers_truck = [random.randint(5, 20) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])
def Pm645_945pm():
    import random
    numbers_car = [random.randint(50, 110) for _ in range(13)]
    numbers_bike = [random.randint(5, 25) for _ in range(13)]
    numbers_bus = [random.randint(10, 20) for _ in range(13)]
    numbers_truck = [random.randint(5, 35) for _ in range(13)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


# ---------------------------------------------- Friday

def Am415_9Am():
    import random
    numbers_car = [random.randint(25, 80) for _ in range(20)]
    numbers_bike = [random.randint(5, 20) for _ in range(20)]
    numbers_bus = [random.randint(0, 7) for _ in range(20)]
    numbers_truck = [random.randint(10, 15) for _ in range(20)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Am9_3Pm():
    import random
    numbers_car = [random.randint(130,180) for _ in range(24)]
    numbers_bike = [random.randint(40,70) for _ in range(24)]
    numbers_bus = [random.randint(10,30) for _ in range(24)]
    numbers_truck = [random.randint(0,4) for _ in range(24)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])


def Pm3_7Pm():
    import random
    numbers_car = [random.randint(50,90) for _ in range(16)]
    numbers_bike = [random.randint(20,30) for _ in range(16)]
    numbers_bus = [random.randint(0,25) for _ in range(16)]
    numbers_truck = [random.randint(0,2) for _ in range(16)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])

def Am7_10():
    import random
    numbers_car = [random.randint(20,50) for _ in range(11)]
    numbers_bike = [random.randint(1,11) for _ in range(11)]
    numbers_bus = [random.randint(0,7) for _ in range(11)]
    numbers_truck = [random.randint(0,15) for _ in range(11)]

    for i in range(len(numbers_car)):
        print(numbers_car[i], numbers_bike[i], numbers_bus[i], numbers_truck[i])










print("------------------ 6:9 --------------------")
six_nine()
# # am415_545am()
# Am415_9Am()
print("----------------- Am11_1PM---------------------")
# # am915_1045pm()
# Am9_3Pm()
Am11_1PM()
print("------------------- Pm4_6:30Pm ---------------------")
pm4_pm630()
# # pm15_345pm()
# Pm3_7Pm()

print("--------------- 10:00-4:00 -------------------------")
Pm10_4am()
# Pm645_945pm()
# Am7_10()

