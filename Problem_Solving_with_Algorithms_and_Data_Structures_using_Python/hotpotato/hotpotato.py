# run --> PYTHONPATH=$PYTHONPATH:queue python3 hotpotato/hotpotato.py

from queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

if __name__ == "__main__":
    namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(f"{namelist}=")
    print(f"{hotPotato(namelist, 17)=}")
    print(f"{hotPotato(namelist, 13)=}")
    print(f"{hotPotato(namelist, 11)=}")
    print(f"{hotPotato(namelist, 7)=}")
    print(f"{hotPotato(namelist, 5)=}")
    print(f"{hotPotato(namelist, 3)=}")
    print(f"{hotPotato(namelist, 2)=}")
