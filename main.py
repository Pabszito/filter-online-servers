#!/usr/bin/python

import sys
from mcstatus import JavaServer

if len(sys.argv) <= 2:
    print("")
    print("Usage: test.py servers.txt servers-clean.txt")
    print("")
    print("Where 'servers.txt' is the initial list of servers")
    print("and 'servers-clean.txt' is where online servers should")
    print("be written to.")
    exit(0)

online = []

# Open input file and read it
with open(sys.argv[1]) as f:
    for line in f.readlines():
        try:
            # Get server status
            address = line.strip('\n')
            server = JavaServer.lookup(address)
            status = server.status()
                
            # Print that server is online and write it to a new file
            print(f"Server {address} has {status.players.online} online players and has replied in {round(status.latency)} ms.")
            online.append(address)
        except Exception:
            # Server is offline, remove it
            print(f"Server {address} seems to be offline! Removing from final list.")

# Write online servers to a new file
with open(sys.argv[2], 'w') as f:
    f.write('\n'.join(online))
