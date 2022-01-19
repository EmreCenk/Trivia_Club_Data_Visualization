from time import sleep
import matplotlib.pyplot as plt

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

def histogram_of_points(a, exclude = "Ali"):
    sorted_names, points, occurences = process_points(a)
    sorted_names.remove(exclude)
    points["Ali"] = 0
    point_values = [points[x]/occurences[x] for x in points]
    num_bins = 7
    n, bins, patches = plt.hist(point_values, num_bins, facecolor='blue', alpha=0.5)
    plt.xlabel("Points per game")
    plt.ylabel("Number of people")
    plt.show()



if __name__ == '__main__':
    with open("results.txt", "r") as file:
        a = file.read()

    histogram_of_points(a)