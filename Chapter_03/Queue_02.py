from pythonds.basic import Queue

def hot_potato(name_list, num):
    simqueue = Queue()
    for name in name_list:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))