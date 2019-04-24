#!/usr/bin/python

import sys, time, os

clients = []
servers = []
counter = {}

TIME_TO_PRINT = 60
SEEK = TIME_TO_PRINT + 5

def print_results(host_cl, host_sr):
    print("")
    print("Host Client " + host_cl +  " connects to: ")
    print(*servers)
    print("")
    print("Host Server " + host_sr + " connected from: ")
    print(*clients)
    print("")
    print("Clients' connections:")
    for keys, values in counter.items():
        print(keys + ":")
        print(values)


def addHosts(line, host_cl, host_sr, ts0):
    fields = line.split(" ")
    ts = float(fields[0])
    cl = fields[1]
    sr = fields[2]
    tsc = time.time()
    diff = (tsc - ts) / 60
    if (cl == host_cl and diff <= TIME_TO_PRINT):
        servers.append(sr)
    if (sr == host_sr and diff <= TIME_TO_PRINT):
        clients.append(cl)
    if (cl in counter and diff <= TIME_TO_PRINT):
        counter[cl] = counter.get(cl) + 1
    else:
        counter[cl] = 1

    return  tsc - ts0 >= TIME_TO_PRINT

def main(argv):
    filelog = open(argv[0])
    ts0 = time.time()
    first_exec = True
    follow = True
    while follow:
        line = filelog.readline()
        if not line:
            follow = False
        else:
            ts = float(line.split(" ")[0])
            diff = (ts0 - ts) / 60
            follow = diff > SEEK
    while True:
        if not line:
            if first_exec:
                print_results(argv[1], argv[2])
                first_exec = False
            time.sleep(0.2)
        elif addHosts(line, argv[1], argv[2], ts0):
            print_results(argv[1], argv[2])
            ts0 = time.time()
        line = filelog.readline()


if len(sys.argv) > 3 :
    main(sys.argv[1:])