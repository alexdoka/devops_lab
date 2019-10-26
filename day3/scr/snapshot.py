#!/usr/bin/env python
import psutil
import json
import time
from datetime import datetime

# load settings
with open('settings.json', 'r') as f:
    datastore = json.load(f)
    outputformat = datastore['output']
    timeinterval = datastore['interval']
    iteration = datastore['iteration']


class SystemStateSlice():

    def __init__(self):
        self.CpuPercent()
        self.VirtMemUsed()
        self.VirtMemUsage()
        self.ioinfo()
        self.net()

    """Common information about system"""

    def CpuPercent(self):
        self.cpu = str(psutil.cpu_percent())

    def VirtMemUsed(self):
        self.vmem_used = str(psutil.virtual_memory().used)

    def VirtMemUsage(self):
        self.vmem_active = str(psutil.virtual_memory().used)

    def ioinfo(self):
        self.io = str(psutil.disk_io_counters().read_bytes)

    def net(self):
        self.net_cntr = str(psutil.net_io_counters().bytes_sent)


if outputformat == 'txt':
    textfile = open("systemlog.txt", "w")
    for i in range(iteration):
        sysstate = SystemStateSlice()
        textfile.write('\nSNAPSHOT{0}: {1}'.format(i, datetime.now()))
        textfile.write("\n{0:{width}} {1:{width}} {2:{width}} {3:{width}} \
        {4:{width}}".format("CpuPercent", "Mem.usage", "Virt.mem.usage", "IO info", "NetInfo",
                            width=20))
        textfile.write("\n{0:{width}} {1:{width}} {2:{width}} {3:{width}} \
        {4:{width}}".format(sysstate.cpu, sysstate.vmem_used, sysstate.vmem_active, sysstate.io,
                            sysstate.net_cntr, width=20))
        time.sleep(timeinterval)
    textfile.close()
elif outputformat == 'json':
    SysDict = {}
    for i in range(iteration):
        sysstate = SystemStateSlice()
        FirstField = "Snapshot{0}: {1}".format(i, datetime.now())
        SysDict.update({FirstField: [sysstate.__dict__]})
        with open('data.json', 'w') as outfile:
            json.dump(SysDict, outfile, indent=4)
        time.sleep(timeinterval)
