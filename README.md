# pyPerfRecord
Automatically record perf utility output when large avgs elevate.

This is information for pyPerf.py.

The script collects `perf` utility output when the 1 minute load averages elevate sharply, to the point defined in the script. 
It will record 30 seconds * <intervals> set in the script, and then rename the file according to the time stamp.

