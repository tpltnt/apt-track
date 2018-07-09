#!/usr/bin/env python3

with open("/var/log/dpkg.log") as infile:
    for line in infile:
        chunks = line.split(' ')
        data = {}

        # extracting data for each stage
        if 'install' == chunks[2]:
            data['state'] = 'preparing'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[3].split(':')[0]  # discard architecture
            data['version'] = chunks[5][:-1]
        if 'configure' == chunks[2]:
            data['state'] = 'configuring'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[3].split(':')[0]  # discard architecture
            data['version'] = chunks[4]
        if 'status' == chunks[2] and 'installed' == chunks[3]:
            data['state'] = 'installed'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[4].split(':')[0]  # discard architecture
            data['version'] = chunks[5]

        if data:
            print(data)
