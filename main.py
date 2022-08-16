def histogram(items):
    for i in items:
        times = i
        count = ''
        # print(times)

        while times > 0:
            count += '*'
            times -= 1
        print(count)


histogram([2, 3, 6, 5])
