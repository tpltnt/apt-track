#!/usr/bin/env python3

with open("/var/log/dpkg.log") as infile:
    for line in infile:
        chunks = line.split(' ')
        if 'install' == chunks[2]:
            date = chunks[0]
            time = chunks[1]
            package = chunks[3].split(':')[0]  # discard architecture
            version = chunks[5][:-1]
            print(package, version)
