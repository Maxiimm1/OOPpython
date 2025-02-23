import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True




    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:+^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Cat(name="Nick")

for day in range(3650):
    if nick.alive == False:
        break



    def divider(a, b):
        if a < b:
            raise ValueError('Good A')
        if b > 100:
            raise IndexError('Good B')
        return a / b


    for key in data:
        try:
            res = divider(key, data[key])
            result.append(res)
        except Exception as e:
            print(f"Exception occurred: {type(e).__name__}: {e}")

    print(result)

    # nick.live(day)
    # if kate.alive == False:
    #     break
    # kate.live(day)
    # if bohdan.alive == False:
    #     break
    # bohdan.live(day)