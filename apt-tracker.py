#!/usr/bin/env python3
"""
Read data from dpkg log and store it
into a database for documentation.
"""

with open("/var/log/dpkg.log") as infile:
    for line in infile:
        chunks = line.split(' ')
        data = {}

        # extracting data for each stage
        if chunks[2] == 'install':
            data['state'] = 'preparing'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[3].split(':')[0]  # discard architecture
            data['version'] = chunks[5][:-1]
        if chunks[2] == 'configure':
            data['state'] = 'configuring'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[3].split(':')[0]  # discard architecture
            data['version'] = chunks[4].strip()
        if chunks[2] == 'status' and chunks[3] == 'installed':
            data['state'] = 'installed'
            data['date'] = chunks[0]
            data['time'] = chunks[1]
            data['package'] = chunks[4].split(':')[0]  # discard architecture
            data['version'] = chunks[5].strip()

        if data:
            print(data)
