def maximumPerimeterTriangle(sticks):
    # Write your code here
    sort_s = sorted(sticks)

    for i in range((len(sort_s) - 1), 1, -1):

        if sort_s[i] < sort_s[i - 1] + sort_s[i - 2]:
            return (sort_s[i] + sort_s[i - 1] + sort_s[i - 2])
            break
    else:
        return -1


if __name__ == '__main__':

    # n = int(input().strip())
    j = [1, 2, 3]

    # sticks = list(map(int)

    result = maximumPerimeterTriangle(j)
    print(result)
