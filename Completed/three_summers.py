def three_summers(items, goal):

    for x in range(len(items)-1):

        left = x+1
        right = len(items)-1

        while (left < right):

            tmp = items[left] + items[right] + items[x]

            if tmp > goal:
                right -= 1
            elif tmp < goal:
                left += 1
            else:
                return True

    return False
