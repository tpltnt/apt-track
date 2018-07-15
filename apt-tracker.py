#!/usr/bin/env python3
"""
Read data from dpkg log and store it
into a database for documentation.
"""

def read_logs(logfile):
    """
    Read the relevant data from the dpkg log file.

    :param logfile: file (path) to read from
    :type logfile: str
    :returns: list of dict (may be empty)
    :raises: TypeError
    """
    if not isinstance(logfile, str):
        raise TypeError("given 'logfile' not of type 'str'")
    # TODO: check for existence?
    logs = []
    with open(logfile) as infile:
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
                logs.append(data)
    return logs


for d in read_logs("/var/log/dpkg.log"):
    print(d)
