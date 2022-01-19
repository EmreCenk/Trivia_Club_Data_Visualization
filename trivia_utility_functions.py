from time import sleep
import matplotlib.pyplot as plt

def loop_through_weeks(a):
    a = a.split("\n")
    current_week = []
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    for i in range(len(a)):
        b = a[i].split("\t")

        if len(b[0].split(" ")) > 4: continue
        b_0 = b[0].lower()
        inmonth = False
        for month in months:
            if month in b_0:
                if len(current_week) == 0: continue
                yield current_week
                current_week = []
                inmonth = True
                break
        if inmonth: current_week.append(b)
        if "team" in b[0].lower() or len(b) <= 1: continue
        current_week.append(b)
def process_points(a):
    a = a.split("\n")
    nums = {}
    occurences = {}
    for i in range(len(a)):
        b = a[i].split("\t")

        if len(b) <= 1 or "team" in b[0].lower():
            continue

        if b[0] not in nums:
            nums[b[0]] = int(b[1])
            occurences[b[0]] = 1
        else:
            nums[b[0]] += int(b[1])
            occurences[b[0]] += 1
    asdf = sorted(nums, key = lambda element: nums[element], reverse = True)

    return asdf, nums, occurences
def trivia_copy(a, countdown = True, time_between_name_reveals = 1):
    sorted_names, nums, occurences = process_points(a)

    print("and now, the moment of truth...")
    if countdown:
        for i in range(5, 0, -1):
            print(i)
            sleep(1)
    print("TOTAL POINT RANKINGS:")

    for i in range(len(sorted_names)):
        print(str(i + 1) + ".\t" + sorted_names[i] + "\t" + str(nums[sorted_names[i]]))
        sleep(time_between_name_reveals)

    print("\n")
    print("POINTS PER GAME RANKNIGS:")
    sorted_names = sorted(nums, key = lambda element: nums[element] / occurences[element], reverse=True)
    for i in range(len(sorted_names)):
        print(str(i + 1) + ".\t" + sorted_names[i] + "\t" + str(round(nums[sorted_names[i]]/occurences[sorted_names[i]], 2)))
        sleep(time_between_name_reveals)

def histogram_of_points(a, exclude=None):
    """
    Generates a histogram of points per game distribution
    :param a: file to read from
    :param exclude: list of people to exclude
    :return:
    """
    if exclude is None:
        exclude = []

    sorted_names, points, occurences = process_points(a)
    sorted_names.remove(exclude)
    for person in exclude:
        if person in points: points[person] = 0

    point_values = [points[x]/occurences[x] for x in points]
    num_bins = 7
    n, bins, patches = plt.hist(point_values, num_bins, facecolor='blue', alpha=0.5)
    plt.xlabel("Points per game")
    plt.ylabel("Number of people")
    plt.show()

def plot_personal_progress(a):
    plots = {} #{"name": [ [x1,x2], [y1, y2] ], "name2": [[...] ... ], ... }
    for week_number, week in enumerate(loop_through_weeks(a)):
        date = week.pop(0)
        for name, points in week:
            try: points = int(points)
            except: continue

            if name in plots:
                plots[name][0].append(points)
                plots[name][1].append(week_number)
            else:
                plots[name] = [[points], [week_number]]

    for person in plots:
        xs, ys = plots[person]
        plt.plot(ys, xs, label = person)

    plt.legend()
    plt.show()



if __name__ == '__main__':
    with open("results.txt", "r") as file:
        a = file.read()

    plot_personal_progress(a)
    # histogram_of_points(a, exclude = ["Ali"])