import math
import numpy as np
from obspy import UTCDateTime, Trace, Stream, read
from obspy.io.segy.segy import _read_segy, _read_su, SEGYTraceHeader
from obspy import Trace, Stream
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter, lfilter, freqs, iirfilter
import sys


filename = 'C:/Users/pedro/Documents/projects/AR3D1044-1266.su'
##filename = 'E:/zshared/ssView/Coj1XP-orig.sgy'
print(filename)


try:
    filename = str(sys.argv[1])
except:
    print('Please enter a valid filename')
    print("Use the following command to run this script")
    print("python SEGY_filter_panels_multi.py \"[filename]\" [initial trace] [number of traces]")
    exit(0)

try:
    init_trace = int(sys.argv[2])
except:
    print('Please enter a valid integer for the initial trace:')
    print("Use the following command to run this script")
    print("python SEGY_filter_panels_multi.py \"[filename]\" [initial trace] [number of traces]")
    exit(0)

try:
    num_trace = int(sys.argv[3])
except:
    print('Please enter a valid integer for the number of traces:')
    print("Use the following command to run this script")
    print("python SEGY_filter_panels_multi.py \"[filename]\" [initial trace] [number of traces]")
    exit(0)

try:
    min_amp = float(sys.argv[4])
except:
    print('Please enter a valid integer for the minimum amplitude:')
    print("Use the following command to run this script")
    print("python SEGY_filter_panels_multi.py \"[filename]\" [initial trace] [number of traces] [min amp] [max amp]")
    min_amp = -1
    # exit(0)

try:
    max_amp = float(sys.argv[5])
except:
    print('Please enter a valid integer for the maximum amplitude:')
    print("Use the following command to run this script")
    print("python SEGY_filter_panels_multi.py \"[filename]\" [initial trace] [number of traces] [min amp] [max amp]")
    max_amp = 1
    # exit(0)











#just reading the SEGY
# #----------------------------------------------------------------------------------------
# stream = _read_su(filename,headonly=True)
stream = _read_segy(filename,headonly=True)
# stream = read(filename,format='segy')
# print(stream.textual_file_header)
# exit(0)

#print(stream)
print(stream.textual_file_header.decode())
#print(stream.binary_file_header)


print("Trace Length=",stream.traces[0].npts, \
          'sampling interval=',stream.traces[0].header.sample_interval_in_ms_for_this_trace)
# init_trace=0
# num_trace=20
tlen=stream.traces[0].npts
dt=stream.traces[0].header.sample_interval_in_ms_for_this_trace
fs=(1/dt)*1e6
print('Sampling frequency [Hz]=',fs)

data=np.zeros((num_trace,tlen))
print(data.shape[0],data.shape[1])  # traces, time samples

k=0
for i in range(init_trace,init_trace+num_trace):
    data[k][:]=stream.traces[i].data
    # print('TRace header=',stream.traces[i].header)
    print('Trace header ID code=',stream.traces[i].header.trace_identification_code)
    k=k+1

print("Reading done!")


plt.figure(figsize=(7,8))
plt.imshow(data.T,cmap='Greys',interpolation='nearest',vmin=min_amp,vmax=max_amp,aspect='auto')
plt.xlabel('Trace number')
plt.ylabel('Time [ms]')
plt.colorbar()
plt.show(block=True)
# #----------------------------------------------------------------------------------------













# if we want to separate the components
# #----------------------------------------------------------------------------------------
stream = read(filename,format='segy')
# dataV=Stream()
dataH1=Stream()
dataH2=Stream()
print(len(stream))
exit(0)
#
for i in range(len(stream)):
#     # print(len(stream),i,stream[i].stats.segy.trace_header.trace_identification_code)
    if stream[i].stats.segy.trace_header.trace_identification_code == 11:
        dataH2 = dataH2 + stream[i]
    elif stream[i].stats.segy.trace_header.trace_identification_code == 12:
        dataH1 = dataH1 + stream[i]
#     elif stream[i].stats.segy.trace_header.trace_identification_code == 22:
#         dataV = dataV + stream[i]
# dataV.write(filename.split('.')[0] + "_V.sgy", format="segy")
dataH1.write(filename.split('.')[0] + "_H1.sgy", format="segy")
dataH2.write(filename.split('.')[0] + "_H2.sgy", format="segy")
# #----------------------------------------------------------------------------------------






















































##import numpy as np
##import math
##import string
##
##
##
##def _read_ebcdic(fp):
##    buf = fp.read(3200)
##
##
##def _read_binary(fp):
##    buf = fp.read(400)
##
##
##
##def _read_tr_head(fp):
##    buf = fp.read(240)
##
##
####def _read_tr_data(fp):
##
##
##
##def _decode_bcd(bytes_in):
##    """Decode arbitrary length binary code decimals."""
##    v = 0
##    if isinstance(bytes_in, int):
##        bytes_in = bytes([bytes_in])
##    n = len(bytes_in)
##    n = n*2 - 1  # 2 values per byte
##    for byte in bytes_in:
##        v1, v2 = _bcd(byte)
##        v += v1*10**n + v2*10**(n-1)
##        n -= 2
##    return v
##
##
##
##def _decode_dbl(bytes_in):
##    """Decode double-precision floats."""
##    return unpack('>d', bytes_in)[0]
##
##
##
##def _decode_asc(bytes_in):
##    """Decode ascii."""
##    if PY2:
##        # transform bytes_in to a list of ints
##        bytes_ord = map(ord, bytes_in)
##    else:
##        # in PY3 this is already the case
##        bytes_ord = bytes_in
##    printable = map(ord, string.printable)
##    s = ''.join(chr(x) for x in bytes_ord if x in printable)
##    if not s:
##        s = None
##    return s
##
##
##    
##
##
##filename = 'E:\zshared\ssView\d_sg_stratton3d.sgy' #filename
##fb=open(filename,'rb')
## _read_ebcdic(fb)
## _read_binary




