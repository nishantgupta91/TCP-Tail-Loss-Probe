config_measurement.py~                                                                              0000664 0001750 0001750 00000003524 12270762276 015411  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                import subprocess
import os
"""from time import sleep"""

def startMeasurement(tlpStatus):
    """ Measure all the possible configurations and save the output in files """

    print "tlpStatus : " + tlpStatus
    if "tlpDisabled" == tlpStatus:
	tlpFlag = 2
    elif "tlpEnabled" == tlpStatus:
	tlpFlag = 3
    subprocess.call(["sudo", "sysctl", "-w", "net.ipv4.tcp_early_retrans="+str(tlpFlag)])

    for linkConfig in ["fast", "moderate", "slow"]:
        for transferSize in ["short", "medium", "long"]:
            for packets_to_drop in [1, 2, 4, 8]:
		counter = 0
                for i in range(0, 10):
		    counter = counter + 1
		    tcpAnalysis = ''
                    subprocess.call(["python2", "mininet_tlp_measurement.py", linkConfig, linkConfig, 					transferSize, "tcpDump", str(packets_to_drop)])
                    try:
			tcpAnalysis = subprocess.check_output(["python", "tcp_analysis.py", 									"tcpDump.pcap"])
		    except:
			print "ERROR"
		    print "-----------------------------------------------------"
                    print "TLP_Case : " + tlpStatus
                    print "Link Configuration : " + linkConfig
		    print "Transfer Size : " + transferSize
                    print "Packets Dropped : " + str(packets_to_drop)
		    print "counter : " + str(counter)
                    print tcpAnalysis
		    print "-----------------------------------------------------"
		    if not os.path.exists("OutputFiles"):
		    	os.mkdir("OutputFiles")
		    fileName = tlpStatus + "_" + linkConfig + "_" + transferSize + "_" + 					str(packets_to_drop)
                    f = open("OutputFiles/" + fileName, 'a')
		    f.write(tcpAnalysis)
		    f.close()


if __name__ == "__main__":
    """ Start Measuring different configurations by disabling and enabling TLP """
    startMeasurement("tlpEnabled")
    startMeasurement("tlpDisabled")
                                                                                                                                                                            config_measurement.py$                                                                              0000664 0001750 0001750 00000000000 12270763457 015243  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                config_measurement_pylint                                                                           0000664 0001750 0001750 00000012522 12270763470 016156  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module config_measurement
W: 10,0: Found indentation with tabs instead of spaces
W: 12,0: Found indentation with tabs instead of spaces
C: 13,0: Line too long (89/80)
W: 18,0: Found indentation with tabs instead of spaces
W: 20,0: Found indentation with tabs instead of spaces
W: 21,0: Found indentation with tabs instead of spaces
C: 22,0: Line too long (154/80)
C: 24,0: Line too long (96/80)
W: 24,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
W: 26,0: Found indentation with tabs instead of spaces
W: 27,0: Found indentation with tabs instead of spaces
W: 30,0: Found indentation with tabs instead of spaces
W: 32,0: Found indentation with tabs instead of spaces
W: 34,0: Found indentation with tabs instead of spaces
W: 35,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
C: 37,0: Line too long (100/80)
W: 37,0: Found indentation with tabs instead of spaces
W: 39,0: Found indentation with tabs instead of spaces
W: 40,0: Found indentation with tabs instead of spaces
C: 44,0: Line too long (82/80)
C:  1,0: Missing docstring
W:  3,0: String statement has no effect
C:  5,0:startMeasurement: Invalid name "startMeasurement" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:  5,0:startMeasurement: Invalid name "tlpStatus" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:  5,21:startMeasurement: Invalid name "tlpStatus" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 10,1:startMeasurement: Invalid name "tlpFlag" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 12,1:startMeasurement: Invalid name "tlpFlag" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 15,8:startMeasurement: Invalid name "linkConfig" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 16,12:startMeasurement: Invalid name "transferSize" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 21,6:startMeasurement: Invalid name "tcpAnalysis" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
W: 25,6:startMeasurement: No exception type(s) specified
C: 24,3:startMeasurement: Invalid name "tcpAnalysis" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 37,6:startMeasurement: Invalid name "fileName" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 38,20:startMeasurement: Invalid name "f" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
W: 19,20:startMeasurement: Unused variable 'i'
W: 44,4: String statement has no effect


Report
======
41 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |1      |1          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |31     |70.45 |31       |=          |
+----------+-------+------+---------+-----------+
|docstring |9      |20.45 |9        |=          |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |0        |=          |
+----------+-------+------+---------+-----------+
|empty     |4      |9.09  |4        |=          |
+----------+-------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |17     |17       |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |21     |21       |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|W0312      |17          |
+-----------+------------+
|C0103      |11          |
+-----------+------------+
|C0301      |5           |
+-----------+------------+
|W0105      |2           |
+-----------+------------+
|W0702      |1           |
+-----------+------------+
|W0612      |1           |
+-----------+------------+
|C0111      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at 0.73/10 (previous run: 0.73/10)

                                                                                                                                                                              drop_tail.py                                                                                        0000664 0001750 0001750 00000005222 12270140647 013303  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                #!/usr/bin/python

""" Implementing tail loss """


import sys
import nfqueue

from socket import AF_INET

sys.path.append('python')
sys.path.append('build/python')
sys.path.append('dpkt-1.6')

import argparse
count = 0
lastPacketFlag = False


def cb(payload):
	""" Function for creating tail loss """
	global remainingDropCount
    	global lastPacketFlag
	global count
	print " "	
	count = count + 1
	print "count : " + str(count)
	if count > 1 and count <= int(segmentSize) + int(packetsToDrop) + 1:
		print "payload.get_length() : " + str(payload.get_length())
        	if remainingDropCount > 0:
            		if count > int(segmentSize) -int(packetsToDrop) + 1:
                		remainingDropCount = remainingDropCount - 1
			#	if remainingDropCount == 0:
			#		lastPacketFlag = True
				print "DROPPED..!!"
				print "Drop packets remaining : " + str(remainingDropCount)
                		payload.set_verdict(nfqueue.NF_DROP)
            		else:
				print "Drop packets remaining : " + str(remainingDropCount) + " .. ACCEPT....!!!!"
                		payload.set_verdict(nfqueue.NF_ACCEPT)
        	else:
			print "All drops packets dropped >> Retransmission"
            		payload.set_verdict(nfqueue.NF_ACCEPT)
    	elif lastPacketFlag is True:
		print "payload.get_length() : " + str(payload.get_length())
        	lastPacketFlag = False
		print "Tail Drop"
        	payload.set_verdict(nfqueue.NF_DROP)
    	else:
		print "payload.get_length() : " + str(payload.get_length())
		print "ELSE....!!!!"
        	payload.set_verdict(nfqueue.NF_ACCEPT)
	sys.stdout.flush()
	return 1


def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	print "!!!!!!!!!!!!!!!!!!!!! drop_tail.py !!!!!!!!!!!!!!!!!!!!!!!!"
	parser = argparse.ArgumentParser()
	parser.add_argument("payloadSize",
		help="Enter payload size : " +
		"1) short 2) medium 3) long",
		type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	return args

def tailDrop(segmentSize, packetsToDrop):
		q = nfqueue.queue()

		print "setting callback"
		q.set_callback(cb)

		print "open"
		q.fast_open(0, AF_INET)

		q.set_queue_maxlen(50000)

		print "trying to run"
		try:
			q.try_run()
		except KeyboardInterrupt, e:
			print "interrupted"+str(e)

		print "%d packets handled" % count

		print "unbind"
		q.unbind(AF_INET)

		print "close"
		q.close()

if __name__ == '__main__':
	arguments = parseArguments()
	payloadSize = arguments.payloadSize
	segmentSize = int(payloadSize)/1448
	packetsToDrop = arguments.packetsToDrop
	remainingDropCount = int(packetsToDrop)
	tailDrop(segmentSize, packetsToDrop)
                                                                                                                                                                                                                                                                                                                                                                              drop_tail.py~                                                                                       0000664 0001750 0001750 00000005252 12270140232 013472  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                #!/usr/bin/python

""" Implementing tail loss """


import sys
import nfqueue

from socket import AF_INET

sys.path.append('python')
sys.path.append('build/python')
sys.path.append('dpkt-1.6')

import argparse
count = 0
lastPacketFlag = False


def cb(payload):
	""" Function for creating tail loss """
	global remainingDropCount
    	global lastPacketFlag
	global count
	print " "	
	count = count + 1
	print "count : " + str(count)
	if count > 1 and count <= int(segmentSize) + int(packetsToDrop) + 1:
		print "payload.get_length() : " + str(payload.get_length())
        	if remainingDropCount > 0:
            		if count > int(segmentSize) -int(packetsToDrop) + 1:
                		remainingDropCount = remainingDropCount - 1
			#	if remainingDropCount == 0:
			#		lastPacketFlag = True
				print "DROPPED..!!"
				print "Drop packets remaining : " + str(remainingDropCount)
                		payload.set_verdict(nfqueue.NF_DROP)
            		else:
				print "Drop packets remaining : " + str(remainingDropCount) + " .. ACCEPT....!!!!"
                		payload.set_verdict(nfqueue.NF_ACCEPT)
        	else:
			print "All drops packets dropped >> Retransmission"
            		payload.set_verdict(nfqueue.NF_ACCEPT)
    	elif lastPacketFlag is True:
		print "payload.get_length() : " + str(payload.get_length())
        	lastPacketFlag = False
		print "Tail Drop"
        	payload.set_verdict(nfqueue.NF_DROP)
    	else:
		print "payload.get_length() : " + str(payload.get_length())
		print "ELSE....!!!!"
        	payload.set_verdict(nfqueue.NF_ACCEPT)
	sys.stdout.flush()
	return 1


def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	print "!!!!!!!!!!!!!!!!!!!!! drop_tail.py !!!!!!!!!!!!!!!!!!!!!!!!"
	parser = argparse.ArgumentParser()
	parser.add_argument("payloadSize",
		help="Enter payload size : " +
		"1) short 2) medium 3) long",
		type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	print "args : " + args
	return args

def tailDrop(segmentSize, packetsToDrop):
		q = nfqueue.queue()

		print "setting callback"
		q.set_callback(cb)

		print "open"
		q.fast_open(0, AF_INET)

		q.set_queue_maxlen(50000)

		print "trying to run"
		try:
			q.try_run()
		except KeyboardInterrupt, e:
			print "interrupted"+str(e)

		print "%d packets handled" % count

		print "unbind"
		q.unbind(AF_INET)

		print "close"
		q.close()

if __name__ == '__main__':
	arguments = parseArguments()
	payloadSize = arguments.payloadSize
	segmentSize = int(payloadSize)/1448
	packetsToDrop = arguments.packetsToDrop
	remainingDropCount = int(packetsToDrop)
	tailDrop(segmentSize, packetsToDrop)
                                                                                                                                                                                                                                                                                                                                                      drop_tail.py1804_17122013                                                                           0000664 0001750 0001750 00000005226 12266437330 014607  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                #!/usr/bin/python

# need root privileges

import struct
import sys
import time

from socket import AF_INET, AF_INET6, inet_ntoa

sys.path.append('python')
sys.path.append('build/python')
import nfqueue

sys.path.append('dpkt-1.6')
from dpkt import ip

import argparse
count = 0
lastPacketFlag = False

# Function for creating tail loss
def cb(payload):
	global remainingDropCount
    	global lastPacketFlag
	global count
	print " "	
	count = count + 1
	print "count : " + str(count)
	if count > 1 and count <= int(segmentSize) + int(packetsToDrop) + 1:
		print "payload.get_length() : " + str(payload.get_length())
        	if remainingDropCount > 0:
            		if count > int(segmentSize) -int(packetsToDrop) + 1:
                		remainingDropCount = remainingDropCount - 1
                		if remainingDropCount == 0:
                    			lastPacketFlag = True
				print "DROPPED..!!"
				print "Drop packets remaining : " + str(remainingDropCount)
                		payload.set_verdict(nfqueue.NF_DROP)
            		else:
				print "Drop packets remaining : " + str(remainingDropCount) + " .. Count not in drop_range"
                		payload.set_verdict(nfqueue.NF_ACCEPT)
        	else:
			print "All drops packets dropped >> Retransmission"
            		payload.set_verdict(nfqueue.NF_ACCEPT)
    	elif lastPacketFlag is True:
		print "payload.get_length() : " + str(payload.get_length())
        	lastPacketFlag = False
		print "Tail Drop"
        	payload.set_verdict(nfqueue.NF_DROP)
    	else:
		print "payload.get_length() : " + str(payload.get_length())
		print "ELSE....!!!!"
        	payload.set_verdict(nfqueue.NF_ACCEPT)
	sys.stdout.flush()
	return 1

# Function for adding and parsing the arguments passed as userinput in CLI
def parseArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("payloadSize",
		help="Enter payload size : " +
		"1) short 2) medium 3) long",
		type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	return args

def tailDrop(segmentSize,packetsToDrop):
		q = nfqueue.queue()

		print "setting callback"
		q.set_callback(cb)

		print "open"
		q.fast_open(0, AF_INET)

		q.set_queue_maxlen(50000)

		print "trying to run"
		try:
			q.try_run()
		except KeyboardInterrupt, e:
			print "interrupted"

		print "%d packets handled" % count

		print "unbind"
		q.unbind(AF_INET)

		print "close"
		q.close()

if __name__ == '__main__':
	arguments = parseArguments()
	payloadSize = arguments.payloadSize
	segmentSize = int(payloadSize)/1448
	packetsToDrop = arguments.packetsToDrop
	remainingDropCount = int(packetsToDrop)
	tailDrop(segmentSize,packetsToDrop)
                                                                                                                                                                                                                                                                                                                                                                          drop_tail.pyc                                                                                       0000644 0001750 0001750 00000005251 12266437330 013451  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                �
�/�Rc           @   s  d  d l  Z  d  d l Z d  d l Z d  d l m Z m Z m Z e j j d � e j j d � d  d l	 Z	 e j j d � d  d l
 m Z d  d l Z d a e a d �  Z d	 �  Z d
 �  Z e d k re �  Z e j Z e e � d Z e j Z e e � a e e e � n  d S(   i����N(   t   AF_INETt   AF_INET6t	   inet_ntoat   pythons   build/pythons   dpkt-1.6(   t   ipi    c         C   s�  d GHt  d a  d t t  � GHt  d k rt  t t � t t � d k rd t |  j �  � GHt d k r� t  t t � t t � d k r� t d a t d k r� t a n  d GHd t t � GH|  j	 t
 j � qd t t � d GH|  j	 t
 j � qxd	 GH|  j	 t
 j � ni t t k rNd t |  j �  � GHt a d
 GH|  j	 t
 j � n* d t |  j �  � GHd GH|  j	 t
 j � t j j �  d S(   Nt    i   s   count : s   payload.get_length() : i    s   DROPPED..!!s   Drop packets remaining : s    .. Count not in drop_ranges+   All drops packets dropped >> Retransmissions	   Tail Drops   ELSE....!!!!(   t   countt   strt   intt   segmentSizet   packetsToDropt
   get_lengtht   remainingDropCountt   Truet   lastPacketFlagt   set_verdictt   nfqueuet   NF_DROPt	   NF_ACCEPTt   Falset   syst   stdoutt   flush(   t   payload(    (    s   /home/mininet/exp/drop_tail.pyt   cb   s6    
, 
	c          C   sR   t  j �  }  |  j d d d d d t �|  j d d d d t �|  j �  } | S(   Nt   payloadSizet   helps   Enter payload size : s   1) short 2) medium 3) longt   typeR
   s)   Enter the number of packets to be dropped(   t   argparset   ArgumentParsert   add_argumentR   t
   parse_args(   t   parsert   args(    (    s   /home/mininet/exp/drop_tail.pyt   parseArguments;   s    c         C   s�   t  j �  } d GH| j t � d GH| j d t � | j d � d GHy | j �  Wn t k
 rm } d GHn Xd t	 GHd GH| j
 t � d	 GH| j �  d  S(
   Ns   setting callbackt   openi    iP�  s   trying to runt   interrupteds   %d packets handledt   unbindt   close(   R   t   queuet   set_callbackR   t	   fast_openR    t   set_queue_maxlent   try_runt   KeyboardInterruptR   R%   R&   (   R	   R
   t   qt   e(    (    s   /home/mininet/exp/drop_tail.pyt   tailDropG   s     		t   __main__i�  (   t   structR   t   timet   socketR    R   R   t   patht   appendR   t   dpktR   R   R   R   R   R   R"   R/   t   __name__t	   argumentsR   R   R	   R
   R   (    (    (    s   /home/mininet/exp/drop_tail.pyt   <module>   s*   	$					                                                                                                                                                                                                                                                                                                                                                       drop_tail_pylint_analysis                                                                           0000664 0001750 0001750 00000020412 12270756426 016164  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module drop_tail
W: 21,0: Found indentation with tabs instead of spaces
W: 22,0: Found indentation with tabs instead of spaces
W: 23,0: Found indentation with tabs instead of spaces
W: 24,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
W: 26,0: Found indentation with tabs instead of spaces
W: 27,0: Found indentation with tabs instead of spaces
W: 28,0: Found indentation with tabs instead of spaces
W: 29,0: Found indentation with tabs instead of spaces
W: 30,0: Found indentation with tabs instead of spaces
W: 31,0: Found indentation with tabs instead of spaces
W: 32,0: Found indentation with tabs instead of spaces
W: 35,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
W: 37,0: Found indentation with tabs instead of spaces
W: 38,0: Found indentation with tabs instead of spaces
C: 39,0: Line too long (86/80)
W: 39,0: Found indentation with tabs instead of spaces
W: 40,0: Found indentation with tabs instead of spaces
W: 41,0: Found indentation with tabs instead of spaces
W: 42,0: Found indentation with tabs instead of spaces
W: 43,0: Found indentation with tabs instead of spaces
W: 44,0: Found indentation with tabs instead of spaces
W: 45,0: Found indentation with tabs instead of spaces
W: 46,0: Found indentation with tabs instead of spaces
W: 47,0: Found indentation with tabs instead of spaces
W: 48,0: Found indentation with tabs instead of spaces
W: 49,0: Found indentation with tabs instead of spaces
W: 50,0: Found indentation with tabs instead of spaces
W: 51,0: Found indentation with tabs instead of spaces
W: 52,0: Found indentation with tabs instead of spaces
W: 53,0: Found indentation with tabs instead of spaces
W: 54,0: Found indentation with tabs instead of spaces
C: 58,0: Line too long (81/80)
W: 58,0: Found indentation with tabs instead of spaces
W: 59,0: Found indentation with tabs instead of spaces
W: 60,0: Found indentation with tabs instead of spaces
W: 61,0: Found indentation with tabs instead of spaces
W: 65,0: Found indentation with tabs instead of spaces
W: 68,0: Found indentation with tabs instead of spaces
W: 69,0: Found indentation with tabs instead of spaces
W: 72,0: Found indentation with tabs instead of spaces
W: 74,0: Found indentation with tabs instead of spaces
W: 75,0: Found indentation with tabs instead of spaces
W: 77,0: Found indentation with tabs instead of spaces
W: 78,0: Found indentation with tabs instead of spaces
W: 80,0: Found indentation with tabs instead of spaces
W: 82,0: Found indentation with tabs instead of spaces
W: 83,0: Found indentation with tabs instead of spaces
W: 84,0: Found indentation with tabs instead of spaces
W: 85,0: Found indentation with tabs instead of spaces
W: 86,0: Found indentation with tabs instead of spaces
W: 88,0: Found indentation with tabs instead of spaces
W: 90,0: Found indentation with tabs instead of spaces
W: 91,0: Found indentation with tabs instead of spaces
W: 93,0: Found indentation with tabs instead of spaces
W: 94,0: Found indentation with tabs instead of spaces
W: 97,0: Found indentation with tabs instead of spaces
W: 98,0: Found indentation with tabs instead of spaces
W: 99,0: Found indentation with tabs instead of spaces
W:100,0: Found indentation with tabs instead of spaces
W:101,0: Found indentation with tabs instead of spaces
W:102,0: Found indentation with tabs instead of spaces
C: 16,0: Invalid name "count" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 17,0: Invalid name "lastPacketFlag" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 20,0:cb: Invalid name "cb" for type function (should match [a-z_][a-z0-9_]{2,30}$)
W: 22,1:cb: Using the global statement
W: 23,5:cb: Using the global statement
W: 24,1:cb: Using the global statement
C: 57,0:parseArguments: Invalid name "parseArguments" for type function (should match [a-z_][a-z0-9_]{2,30}$)
W: 71,26:tailDrop: Redefining name 'packetsToDrop' from outer scope (line 100)
W: 71,13:tailDrop: Redefining name 'segmentSize' from outer scope (line 99)
C: 71,0:tailDrop: Invalid name "tailDrop" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 71,0:tailDrop: Invalid name "segmentSize" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C: 71,0:tailDrop: Invalid name "packetsToDrop" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C: 71,0:tailDrop: Missing docstring
C: 71,13:tailDrop: Invalid name "segmentSize" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 71,26:tailDrop: Invalid name "packetsToDrop" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 72,2:tailDrop: Invalid name "q" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 85,28:tailDrop: Invalid name "e" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
W: 71,26:tailDrop: Unused argument 'packetsToDrop'
W: 71,13:tailDrop: Unused argument 'segmentSize'
C: 97,1: Invalid name "arguments" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 98,1: Invalid name "payloadSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 99,1: Invalid name "segmentSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:100,1: Invalid name "packetsToDrop" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:101,1: Invalid name "remainingDropCount" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


Report
======
70 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |19     |31       |-12.00     |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |68     |62       |+6.00      |
+-----------+-------+---------+-----------+
|error      |0      |9        |-9.00      |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|W0312      |61          |
+-----------+------------+
|C0103      |16          |
+-----------+------------+
|W0603      |3           |
+-----------+------------+
|W0621      |2           |
+-----------+------------+
|W0613      |2           |
+-----------+------------+
|C0301      |2           |
+-----------+------------+
|C0111      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -2.43/10 (previous run: -10.00/10)

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |70     |79.55 |69       |+1.00      |
+----------+-------+------+---------+-----------+
|docstring |10     |11.36 |6        |+4.00      |
+----------+-------+------+---------+-----------+
|comment   |2      |2.27  |5        |-3.00      |
+----------+-------+------+---------+-----------+
|empty     |6      |6.82  |5        |+1.00      |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |3      |3          |=          |66.67       |100.00   |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    nfqueue (drop_tail)



                                                                                                                                                                                                                                                      drop_tail_report                                                                                    0000664 0001750 0001750 00000020477 12266437330 014263  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module drop_tail
W: 21,0: Found indentation with tabs instead of spaces
W: 22,0: Found indentation with tabs instead of spaces
W: 23,0: Found indentation with tabs instead of spaces
W: 24,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
W: 26,0: Found indentation with tabs instead of spaces
W: 27,0: Found indentation with tabs instead of spaces
W: 28,0: Found indentation with tabs instead of spaces
W: 29,0: Found indentation with tabs instead of spaces
W: 30,0: Found indentation with tabs instead of spaces
W: 31,0: Found indentation with tabs instead of spaces
W: 32,0: Found indentation with tabs instead of spaces
W: 33,0: Found indentation with tabs instead of spaces
W: 34,0: Found indentation with tabs instead of spaces
W: 35,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
W: 37,0: Found indentation with tabs instead of spaces
W: 38,0: Found indentation with tabs instead of spaces
C: 39,0: Line too long (95/80)
W: 39,0: Found indentation with tabs instead of spaces
W: 40,0: Found indentation with tabs instead of spaces
W: 41,0: Found indentation with tabs instead of spaces
W: 42,0: Found indentation with tabs instead of spaces
W: 43,0: Found indentation with tabs instead of spaces
W: 44,0: Found indentation with tabs instead of spaces
W: 45,0: Found indentation with tabs instead of spaces
W: 46,0: Found indentation with tabs instead of spaces
W: 47,0: Found indentation with tabs instead of spaces
W: 48,0: Found indentation with tabs instead of spaces
W: 49,0: Found indentation with tabs instead of spaces
W: 50,0: Found indentation with tabs instead of spaces
W: 51,0: Found indentation with tabs instead of spaces
W: 52,0: Found indentation with tabs instead of spaces
W: 53,0: Found indentation with tabs instead of spaces
W: 54,0: Found indentation with tabs instead of spaces
C: 58,0: Line too long (81/80)
W: 58,0: Found indentation with tabs instead of spaces
W: 59,0: Found indentation with tabs instead of spaces
W: 60,0: Found indentation with tabs instead of spaces
W: 64,0: Found indentation with tabs instead of spaces
W: 67,0: Found indentation with tabs instead of spaces
W: 68,0: Found indentation with tabs instead of spaces
W: 71,0: Found indentation with tabs instead of spaces
W: 73,0: Found indentation with tabs instead of spaces
W: 74,0: Found indentation with tabs instead of spaces
W: 76,0: Found indentation with tabs instead of spaces
W: 77,0: Found indentation with tabs instead of spaces
W: 79,0: Found indentation with tabs instead of spaces
W: 81,0: Found indentation with tabs instead of spaces
W: 82,0: Found indentation with tabs instead of spaces
W: 83,0: Found indentation with tabs instead of spaces
W: 84,0: Found indentation with tabs instead of spaces
W: 85,0: Found indentation with tabs instead of spaces
W: 87,0: Found indentation with tabs instead of spaces
W: 89,0: Found indentation with tabs instead of spaces
W: 90,0: Found indentation with tabs instead of spaces
W: 92,0: Found indentation with tabs instead of spaces
W: 93,0: Found indentation with tabs instead of spaces
W: 96,0: Found indentation with tabs instead of spaces
W: 97,0: Found indentation with tabs instead of spaces
W: 98,0: Found indentation with tabs instead of spaces
W: 99,0: Found indentation with tabs instead of spaces
W:100,0: Found indentation with tabs instead of spaces
W:101,0: Found indentation with tabs instead of spaces
C: 16,0: Invalid name "count" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 17,0: Invalid name "lastPacketFlag" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 20,0:cb: Invalid name "cb" for type function (should match [a-z_][a-z0-9_]{2,30}$)
W: 22,1:cb: Using the global statement
W: 23,5:cb: Using the global statement
W: 24,1:cb: Using the global statement
C: 57,0:parseArguments: Invalid name "parseArguments" for type function (should match [a-z_][a-z0-9_]{2,30}$)
W: 70,26:tailDrop: Redefining name 'packetsToDrop' from outer scope (line 99)
W: 70,13:tailDrop: Redefining name 'segmentSize' from outer scope (line 98)
C: 70,0:tailDrop: Invalid name "tailDrop" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 70,0:tailDrop: Invalid name "segmentSize" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C: 70,0:tailDrop: Invalid name "packetsToDrop" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C: 70,0:tailDrop: Missing docstring
C: 70,13:tailDrop: Invalid name "segmentSize" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 70,26:tailDrop: Invalid name "packetsToDrop" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 71,2:tailDrop: Invalid name "q" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 84,28:tailDrop: Invalid name "e" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
W: 70,26:tailDrop: Unused argument 'packetsToDrop'
W: 70,13:tailDrop: Unused argument 'segmentSize'
C: 96,1: Invalid name "arguments" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 97,1: Invalid name "payloadSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 98,1: Invalid name "segmentSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 99,1: Invalid name "packetsToDrop" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:100,1: Invalid name "remainingDropCount" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


Report
======
71 statements analysed.

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |72     |82.76 |72       |=          |
+----------+-------+------+---------+-----------+
|docstring |9      |10.34 |9        |=          |
+----------+-------+------+---------+-----------+
|comment   |1      |1.15  |1        |=          |
+----------+-------+------+---------+-----------+
|empty     |5      |5.75  |5        |=          |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |3      |3          |=          |66.67       |100.00   |
+---------+-------+-----------+-----------+------------+---------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |19     |19       |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |69     |69       |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|W0312      |62          |
+-----------+------------+
|C0103      |16          |
+-----------+------------+
|W0603      |3           |
+-----------+------------+
|W0621      |2           |
+-----------+------------+
|W0613      |2           |
+-----------+------------+
|C0301      |2           |
+-----------+------------+
|C0111      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -2.39/10 (previous run: -2.39/10)

External dependencies
---------------------
::

    nfqueue (drop_tail)



                                                                                                                                                                                                 mininet_tlp_measurement.py                                                                          0000664 0001750 0001750 00000013656 12270151112 016254  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                """

Two hosts connected through another host which is configured as router:

   host A --- host B (router) --- host C

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.link import TCLink
from time import sleep
import argparse


# Topology
class Router_Topo(Topo):
    """ Main class which sets up the topology and helps in communication with the hosts """
    def __init__(self):
		Topo.__init__(self)
        	# Add hosts
        	hostA = self.addHost( 'hostA' )
        	hostB = self.addHost( 'hostB' )
	        hostC = self.addHost( 'hostC' )

        	# Add links
	        self.addLink( hostA, hostB, bw=bw1, delay=delay1, use_tbf=True )
        	self.addLink( hostB, hostC, bw=bw2, delay=delay2, use_tbf=True )

# Function for Starting and Testing Topology
def simpleTest():
	topo = Router_Topo()
	net = Mininet(topo, link=TCLink)
	
	hostA = net.get('hostA')
	hostB = net.get('hostB')
	hostC = net.get('hostC')

	# Setting IP Address to various interfaces of hosts
	hostA.cmd('ifconfig hostA-eth0 10.0.1.1 netmask 255.255.255.0')
	hostC.cmd('ifconfig hostC-eth0 10.0.2.1 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth0 10.0.1.2 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth1 10.0.2.2 netmask 255.255.255.0')

	# Setting Default Gateway
	hostA.cmd('route add default gw 10.0.1.2')
	hostC.cmd('route add default gw 10.0.2.2')
	hostB.setHostRoute(ip="10.0.1.1/24", intf="hostB-eth0")
	hostB.setHostRoute(ip="10.0.2.1/24", intf="hostB-eth1")
	
	# Enabling IP Forwarding
	hostB.cmd('sysctl net.ipv4.ip_forward=1')

	# Sending packets to netfilter queue
	hostB.cmd('iptables -A FORWARD -i hostB-eth0 -o hostB-eth1 -p tcp -j NFQUEUE --queue-num 0')
	
	#Start Network
	net.start()

	# wait for the network
	sleep(1)

	# Capturing network activities
	tcpDump(hostB)

	# wait for tcpdump to start up
	sleep(1)

	#command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+' >successLogs_1 2>errorLogs &'
	command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+'  &'
	print "command : " + command
	hostB.cmd(command)

	#hostA.cmd('ping -c2 hostC')
	# TCP Transfer
	tcpTransfer(hostA, hostC)	

	# stop capturing
	hostB.sendInt()
	tcpDumpStop(hostB)

	# kill drop_tail.py
	hostB.cmd("pkill -9 -f drop_tail.py")

	# give the network some time
	sleep(1)
	
	#Run CLI
	#CLI(net)
	#Stop Network
	net.stop()

# Function for adding and parsing the arguments passed as userinput in CLI
def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	parser = argparse.ArgumentParser()
	parser.add_argument("linkConfig1",
		help="Choose the configuration for  link 1 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("linkConfig2",
		help="Choose the configuration for  link 2 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("segmentSize", help="TCP Segment Size : 1) short 2) medium 3) long", type=str)
	parser.add_argument("logFile", help="Set Log File's Name generated from tcpdump", type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	return args

# Function for setting the bandwidth and delay of links according to the link configuration
def setConfiguration():
	global bw1, delay1, bw2, delay2
	if "fast" == linkConfig1:
		print "### FAST connection at link 1 ###"
		bw1 = 1
		delay1 = "5ms"
	elif "moderate" == linkConfig1:
		print "### MODERATE connection at link 1 ###"
		bw1 = 0.5
		delay1 = "10ms"
	elif "slow" == linkConfig1:
		print "### SLOW connection at link 1 ###"
		bw1 = 0.1
		delay1 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)

	if "fast" == linkConfig2:
		print "### FAST connection at link 2 ###"
		bw2 = 1
		delay2 = "5ms"
	elif "moderate" == linkConfig2:
		print "### MODERATE connection at link 2 ###"
		bw2 = 0.5
		delay2 = "10ms"
	elif "slow" == linkConfig2:
		print "### SLOW connection at link 2 ###"
		bw2 = 0.1
		delay2 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	
# Function for setting transfer size of TCP Segments
def setSegmentSize():
	tcpSegments=(1500-18)*256
	if "short" == segment:
		print "### Short segments ###"
		tcpSegments = 64
	elif "medium" == segment:
		print "### Medium segments ###"
		tcpSegments = 128
	elif "long" == segment:
		print "### Long segments ###"
		tcpSegments = 256
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	return tcpSegments

# Function for creating dump file (.pcap) which can be analysed in Wireshark
def tcpDump(hostB):
	LogFile = logFile + '.pcap'
	hostB.cmd('tcpdump -p -s 68 -w ' + LogFile + ' -i hostB-eth0 &')
	print "### TCP Dump generated with name " + LogFile + " ###"

def tcpDumpStop(hostB):
	hostB.cmd("killall tcpdump 2> errorDUMP.txt")

def tcpTransfer(hostA, hostC):	
	""" Function for transferring segments from Host A to Host C """
	print "### tcp transfer begins ###"
	hostA.cmd('dd if=/dev/zero count=' + str(segmentsSize) + ' bs=1448 | nc6 -X -l -p 7777 &')
	hostC.cmd('nc6 -X 10.0.1.1 7777 > /dev/null')
	#hostC.cmd('nc6 -X 10.0.1.1 7777 > target ')
	print "### Total Bytes transferred : " + str(segmentsSize) + " bytes ###"

if __name__ == '__main__':
	setLogLevel('info')
	arguments = parseArguments()

	linkConfig1 = arguments.linkConfig1
	linkConfig2 = arguments.linkConfig2
	segment = arguments.segmentSize
	logFile = arguments.logFile
	packetsToDrop = arguments.packetsToDrop

	setConfiguration()
	segmentsSize = setSegmentSize()
	payloadSize = str(segmentsSize * 1448)

	simpleTest()

                                                                                  mininet_tlp_measurement.py~                                                                         0000664 0001750 0001750 00000013733 12270150716 016457  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                """

Two hosts connected through another host which is configured as router:

   host A --- host B (router) --- host C

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.link import TCLink
from time import sleep
import argparse


# Topology
class Router_Topo(Topo):
    """ Main class which sets up the topology and helps in communication with the hosts """
    def __init__(self):
		Topo.__init__(self)
        	# Add hosts
        	hostA = self.addHost( 'hostA' )
        	hostB = self.addHost( 'hostB' )
	        hostC = self.addHost( 'hostC' )

        	# Add links
	        self.addLink( hostA, hostB, bw=bw1, delay=delay1, use_tbf=True )
        	self.addLink( hostB, hostC, bw=bw2, delay=delay2, use_tbf=True )

# Function for Starting and Testing Topology
def simpleTest():
	topo = Router_Topo()
	net = Mininet(topo, link=TCLink)
	
	hostA = net.get('hostA')
	hostB = net.get('hostB')
	hostC = net.get('hostC')

	# Setting IP Address to various interfaces of hosts
	hostA.cmd('ifconfig hostA-eth0 10.0.1.1 netmask 255.255.255.0')
	hostC.cmd('ifconfig hostC-eth0 10.0.2.1 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth0 10.0.1.2 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth1 10.0.2.2 netmask 255.255.255.0')

	# Setting Default Gateway
	hostA.cmd('route add default gw 10.0.1.2')
	hostC.cmd('route add default gw 10.0.2.2')
	hostB.setHostRoute(ip="10.0.1.1/24", intf="hostB-eth0")
	hostB.setHostRoute(ip="10.0.2.1/24", intf="hostB-eth1")
	
	# Enabling IP Forwarding
	hostB.cmd('sysctl net.ipv4.ip_forward=1')

	# Sending packets to netfilter queue
	hostB.cmd('iptables -A FORWARD -i hostB-eth0 -o hostB-eth1 -p tcp -j NFQUEUE --queue-num 0')
	
	#Start Network
	net.start()

	# wait for tcpdump to start up
	sleep(1)

	# Capturing network activities
	tcpDump(hostB)

	#command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+' >successLogs_1 2>errorLogs &'
	command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+'  &'
	print "command : " + command
	hostB.cmd(command)

	# wait for the network
	#sleep(1)

	# wait for tcpdump to start up
	#sleep(1)

	#hostA.cmd('ping -c2 hostC')
	# TCP Transfer
	tcpTransfer(hostA, hostC)	

	# stop capturing
	hostB.sendInt()
	tcpDumpStop(hostB)

	# kill drop_tail.py
	hostB.cmd("pkill -9 -f drop_tail.py")

	# give the network some time
	sleep(1)
	
	#Run CLI
	#CLI(net)
	#Stop Network
	net.stop()

# Function for adding and parsing the arguments passed as userinput in CLI
def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	parser = argparse.ArgumentParser()
	parser.add_argument("linkConfig1",
		help="Choose the configuration for  link 1 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("linkConfig2",
		help="Choose the configuration for  link 2 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("segmentSize", help="TCP Segment Size : 1) short 2) medium 3) long", type=str)
	parser.add_argument("logFile", help="Set Log File's Name generated from tcpdump", type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	return args

# Function for setting the bandwidth and delay of links according to the link configuration
def setConfiguration():
	global bw1, delay1, bw2, delay2
	if "fast" == linkConfig1:
		print "### FAST connection at link 1 ###"
		bw1 = 1
		delay1 = "5ms"
	elif "moderate" == linkConfig1:
		print "### MODERATE connection at link 1 ###"
		bw1 = 0.5
		delay1 = "10ms"
	elif "slow" == linkConfig1:
		print "### SLOW connection at link 1 ###"
		bw1 = 0.1
		delay1 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)

	if "fast" == linkConfig2:
		print "### FAST connection at link 2 ###"
		bw2 = 1
		delay2 = "5ms"
	elif "moderate" == linkConfig2:
		print "### MODERATE connection at link 2 ###"
		bw2 = 0.5
		delay2 = "10ms"
	elif "slow" == linkConfig2:
		print "### SLOW connection at link 2 ###"
		bw2 = 0.1
		delay2 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	
# Function for setting transfer size of TCP Segments
def setSegmentSize():
	tcpSegments=(1500-18)*256
	if "short" == segment:
		print "### Short segments ###"
		tcpSegments = 64
	elif "medium" == segment:
		print "### Medium segments ###"
		tcpSegments = 128
	elif "long" == segment:
		print "### Long segments ###"
		tcpSegments = 256
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	return tcpSegments

# Function for creating dump file (.pcap) which can be analysed in Wireshark
def tcpDump(hostB):
	LogFile = logFile + '.pcap'
	hostB.cmd('tcpdump -p -s 68 -w ' + LogFile + ' -i hostB-eth0 &')
	print "### TCP Dump generated with name " + LogFile + " ###"

def tcpDumpStop(hostB):
	hostB.cmd("killall tcpdump 2> errorDUMP.txt")

def tcpTransfer(hostA, hostC):	
	""" Function for transferring segments from Host A to Host C """
	print "### tcp transfer begins ###"
	hostA.cmd('dd if=/dev/zero count=' + str(segmentsSize) + ' bs=1448 | nc6 -X -l -p 7777 &')
	hostC.cmd('nc6 -X 10.0.1.1 7777 > /dev/null')
	#hostC.cmd('nc6 -X 10.0.1.1 7777 > target ')
	print "### Total Bytes transferred : " + str(segmentsSize) + " bytes ###"

if __name__ == '__main__':
	setLogLevel('info')
	arguments = parseArguments()

	linkConfig1 = arguments.linkConfig1
	linkConfig2 = arguments.linkConfig2
	segment = arguments.segmentSize
	logFile = arguments.logFile
	packetsToDrop = arguments.packetsToDrop

	setConfiguration()
	segmentsSize = setSegmentSize()
	payloadSize = str(segmentsSize * 1448)

	simpleTest()

                                     mininet_tlp_measurement.py1734_17122013                                                             0000664 0001750 0001750 00000013500 12266437330 017555  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                """

Two hosts connected through another host which is configured as router:

   host A --- host B (router) --- host C

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import Host
from time import sleep
from mininet.node import Node
import argparse
from drop_tail import tailDrop

# Topology
class Router_Topo(Topo):
	def __init__(self):
		Topo.__init__(self)
        	# Add hosts
        	hostA = self.addHost( 'hostA' )
        	hostB = self.addHost( 'hostB' )
	        hostC = self.addHost( 'hostC' )

        	# Add links
	        self.addLink( hostA, hostB, bw=bw1, delay=delay1, use_tbf=True )
        	self.addLink( hostB, hostC, bw=bw2, delay=delay2, use_tbf=True )

# Function for Starting and Testing Topology
def simpleTest():
	topo = Router_Topo()
	net = Mininet(topo, link=TCLink)

	#Start Network
	net.start()

	hostA = net.get('hostA')
	hostB = net.get('hostB')
	hostC = net.get('hostC')

	# Setting IP Address to various interfaces of hosts
	hostA.cmd('ifconfig hostA-eth0 10.0.1.1 netmask 255.255.255.0')
	hostC.cmd('ifconfig hostC-eth0 10.0.2.1 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth0 10.0.1.2 netmask 255.255.255.0')
	hostB.cmd('ifconfig hostB-eth1 10.0.2.2 netmask 255.255.255.0')

	# Setting Default Gateway
	hostA.cmd('route add default gw 10.0.1.2')
	hostC.cmd('route add default gw 10.0.2.2')
	hostB.setHostRoute(ip="10.0.1.1/24", intf="hostB-eth0")
	hostB.setHostRoute(ip="10.0.2.1/24", intf="hostB-eth1")
	
	# Enabling IP Forwarding
	hostB.cmd('sysctl net.ipv4.ip_forward=1')

	# Sending packets to netfilter queue
	hostB.cmd('iptables -A FORWARD -i hostB-eth0 -o hostB-eth1 -p tcp -j NFQUEUE --queue-num 0')
	#command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+' >successLogs_1 2>errorLogs &'
	command = 'python drop_tail.py '+payloadSize+' '+packetsToDrop+'  &'
	print "command : " + command
	hostB.cmd(command)

	# wait for the network
	sleep(1)
	
	# Capturing network activities
	tcpDump(hostB)

	# wait for tcpdump to start up
	sleep(1)

	#hostA.cmd('ping -c2 hostC')
	# TCP Transfer
	tcpTransfer(hostA,hostC)	

	# stop capturing
	hostB.sendInt()

	# give the network some time
	sleep(1)
	
	#Run CLI
	#CLI(net)
	#Stop Network
	net.stop()

# Function for adding and parsing the arguments passed as userinput in CLI
def parseArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("linkConfig1",
		help="Choose the configuration for  link 1 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("linkConfig2",
		help="Choose the configuration for  link 2 to set the desired Bandwidth & Delay : " +
		"1) fast 2) moderate 3) slow",
		type=str)
	parser.add_argument("segmentSize", help="TCP Segment Size : 1) short 2) medium 3) long",type=str)
	parser.add_argument("logFile", help="Set Log File's Name generated from tcpdump", type=str)
	parser.add_argument("packetsToDrop",
		help="Enter the number of packets to be dropped",
		type=str)
	args = parser.parse_args()
	return args

# Function for setting the bandwidth and delay of links according to the link configuration
def setConfiguration():
	global bw1, delay1, bw2, delay2
	if "fast"==linkConfig1:
		print "### FAST connection at link 1 ###"
		bw1 = 1
		delay1 = "5ms"
	elif "moderate"==linkConfig1:
		print "### MODERATE connection at link 1 ###"
		bw1 = 0.5
		delay1 = "10ms"
	elif "slow"==linkConfig1:
		print "### SLOW connection at link 1 ###"
		bw1 = 0.1
		delay1 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)

	if "fast"==linkConfig2:
		print "### FAST connection at link 2 ###"
		bw2 = 1
		delay2 = "5ms"
	elif "moderate"==linkConfig2:
		print "### MODERATE connection at link 2 ###"
		bw2 = 0.5
		delay2 = "10ms"
	elif "slow"==linkConfig2:
		print "### SLOW connection at link 2 ###"
		bw2 = 0.1
		delay2 = "20ms"
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	
# Function for setting transfer size of TCP Segments
def setSegmentSize():
	tcpSegments=(1500-18)*256
	if "short"==segment:
		print "### Short segments ###"
		tcpSegments = 64
	elif "medium"==segment:
		print "### Medium segments ###"
		tcpSegments = 128
	elif "long"==segment:
		print "### Long segments ###"
		tcpSegments = 256
	else:
		print "ERROR! Wrong Input! Please try again. For help please type"
		print "python mininet_tlp_measurement.py --help"
		exit(0)
	return tcpSegments

# Function for creating dump file (.pcap) which can be analysed in Wireshark
def tcpDump(hostB):
	LogFile = logFile + '.pcap'
	hostB.sendCmd('tcpdump -p -s 68 -w ' + LogFile + ' -i hostB-eth0')
	print "### TCP Dump generated with name " + LogFile + " ###"

# Function for transferring segments from Host A to Host C
def tcpTransfer(hostA,hostC):	
	print "### tcp transfer begins ###"
	#hostA.cmd("dd if=/dev/zero of=sourceFile count=" + str(segmentsSize) + " bs=1448")
	hostA.cmd('dd if=/dev/zero count=' + str(segmentsSize) + ' bs=1448 | nc6 -X -l -p 7777 &')
	hostC.cmd('nc6 -X 10.0.1.1 7777 > /dev/null')
	#hostC.cmd('nc6 -X 10.0.1.1 7777 > target ')
	print "### Total Bytes transferred : " + str(segmentsSize) + " bytes ###"

if __name__ == '__main__':
	setLogLevel('info')
	arguments = parseArguments()

	linkConfig1 = arguments.linkConfig1
	linkConfig2 = arguments.linkConfig2
	segment = arguments.segmentSize
	logFile = arguments.logFile
	packetsToDrop = arguments.packetsToDrop

	setConfiguration()
	segmentsSize = setSegmentSize()
	payloadSize = str(segmentsSize * 1448)

	simpleTest()

                                                                                                                                                                                                mininet_tlp_measurement_report                                                                      0000664 0001750 0001750 00000032013 12266437330 017222  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module mininet_tlp_measurement
C: 21,0: Line too long (91/80)
W: 23,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
W: 26,0: Found indentation with tabs instead of spaces
W: 27,0: Found indentation with tabs instead of spaces
W: 30,0: Found indentation with tabs instead of spaces
W: 31,0: Found indentation with tabs instead of spaces
W: 35,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
W: 39,0: Found indentation with tabs instead of spaces
W: 41,0: Found indentation with tabs instead of spaces
W: 42,0: Found indentation with tabs instead of spaces
W: 43,0: Found indentation with tabs instead of spaces
W: 46,0: Found indentation with tabs instead of spaces
W: 47,0: Found indentation with tabs instead of spaces
W: 48,0: Found indentation with tabs instead of spaces
W: 49,0: Found indentation with tabs instead of spaces
W: 52,0: Found indentation with tabs instead of spaces
W: 53,0: Found indentation with tabs instead of spaces
W: 54,0: Found indentation with tabs instead of spaces
W: 55,0: Found indentation with tabs instead of spaces
W: 58,0: Found indentation with tabs instead of spaces
C: 61,0: Line too long (93/80)
W: 61,0: Found indentation with tabs instead of spaces
C: 62,0: Line too long (96/80)
W: 63,0: Found indentation with tabs instead of spaces
W: 64,0: Found indentation with tabs instead of spaces
W: 65,0: Found indentation with tabs instead of spaces
W: 68,0: Found indentation with tabs instead of spaces
W: 71,0: Found indentation with tabs instead of spaces
W: 74,0: Found indentation with tabs instead of spaces
W: 78,0: Found indentation with tabs instead of spaces
W: 81,0: Found indentation with tabs instead of spaces
W: 84,0: Found indentation with tabs instead of spaces
W: 89,0: Found indentation with tabs instead of spaces
C: 93,0: Line too long (81/80)
W: 93,0: Found indentation with tabs instead of spaces
W: 94,0: Found indentation with tabs instead of spaces
W: 95,0: Found indentation with tabs instead of spaces
C: 96,0: Line too long (87/80)
W: 99,0: Found indentation with tabs instead of spaces
C:100,0: Line too long (87/80)
C:103,0: Line too long (99/80)
W:103,0: Found indentation with tabs instead of spaces
C:104,0: Line too long (92/80)
W:104,0: Found indentation with tabs instead of spaces
W:105,0: Found indentation with tabs instead of spaces
W:108,0: Found indentation with tabs instead of spaces
W:109,0: Found indentation with tabs instead of spaces
C:111,0: Line too long (91/80)
W:113,0: Found indentation with tabs instead of spaces
W:114,0: Found indentation with tabs instead of spaces
W:115,0: Found indentation with tabs instead of spaces
W:116,0: Found indentation with tabs instead of spaces
W:117,0: Found indentation with tabs instead of spaces
W:118,0: Found indentation with tabs instead of spaces
W:119,0: Found indentation with tabs instead of spaces
W:120,0: Found indentation with tabs instead of spaces
W:121,0: Found indentation with tabs instead of spaces
W:122,0: Found indentation with tabs instead of spaces
W:123,0: Found indentation with tabs instead of spaces
W:124,0: Found indentation with tabs instead of spaces
W:125,0: Found indentation with tabs instead of spaces
W:126,0: Found indentation with tabs instead of spaces
W:127,0: Found indentation with tabs instead of spaces
W:128,0: Found indentation with tabs instead of spaces
W:129,0: Found indentation with tabs instead of spaces
W:131,0: Found indentation with tabs instead of spaces
W:132,0: Found indentation with tabs instead of spaces
W:133,0: Found indentation with tabs instead of spaces
W:134,0: Found indentation with tabs instead of spaces
W:135,0: Found indentation with tabs instead of spaces
W:136,0: Found indentation with tabs instead of spaces
W:137,0: Found indentation with tabs instead of spaces
W:138,0: Found indentation with tabs instead of spaces
W:139,0: Found indentation with tabs instead of spaces
W:140,0: Found indentation with tabs instead of spaces
W:141,0: Found indentation with tabs instead of spaces
W:142,0: Found indentation with tabs instead of spaces
W:143,0: Found indentation with tabs instead of spaces
W:144,0: Found indentation with tabs instead of spaces
W:145,0: Found indentation with tabs instead of spaces
W:146,0: Found indentation with tabs instead of spaces
W:150,0: Found indentation with tabs instead of spaces
W:151,0: Found indentation with tabs instead of spaces
W:152,0: Found indentation with tabs instead of spaces
W:153,0: Found indentation with tabs instead of spaces
W:154,0: Found indentation with tabs instead of spaces
W:155,0: Found indentation with tabs instead of spaces
W:156,0: Found indentation with tabs instead of spaces
W:157,0: Found indentation with tabs instead of spaces
W:158,0: Found indentation with tabs instead of spaces
W:159,0: Found indentation with tabs instead of spaces
W:160,0: Found indentation with tabs instead of spaces
W:161,0: Found indentation with tabs instead of spaces
W:162,0: Found indentation with tabs instead of spaces
W:163,0: Found indentation with tabs instead of spaces
W:164,0: Found indentation with tabs instead of spaces
W:168,0: Found indentation with tabs instead of spaces
W:169,0: Found indentation with tabs instead of spaces
W:170,0: Found indentation with tabs instead of spaces
W:174,0: Found indentation with tabs instead of spaces
W:175,0: Found indentation with tabs instead of spaces
C:176,0: Line too long (84/80)
C:177,0: Line too long (91/80)
W:177,0: Found indentation with tabs instead of spaces
W:178,0: Found indentation with tabs instead of spaces
W:180,0: Found indentation with tabs instead of spaces
W:183,0: Found indentation with tabs instead of spaces
W:184,0: Found indentation with tabs instead of spaces
W:186,0: Found indentation with tabs instead of spaces
W:187,0: Found indentation with tabs instead of spaces
W:188,0: Found indentation with tabs instead of spaces
W:189,0: Found indentation with tabs instead of spaces
W:190,0: Found indentation with tabs instead of spaces
W:192,0: Found indentation with tabs instead of spaces
W:193,0: Found indentation with tabs instead of spaces
W:194,0: Found indentation with tabs instead of spaces
W:196,0: Found indentation with tabs instead of spaces
C: 20,0:Router_Topo: Invalid name "Router_Topo" for type class (should match [A-Z_][a-zA-Z0-9]+$)
C: 25,9:Router_Topo.__init__: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 26,9:Router_Topo.__init__: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 27,9:Router_Topo.__init__: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 34,0:simpleTest: Invalid name "simpleTest" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 34,0:simpleTest: Missing docstring
C: 41,1:simpleTest: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 42,1:simpleTest: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 43,1:simpleTest: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 92,0:parseArguments: Invalid name "parseArguments" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:112,0:setConfiguration: Invalid name "setConfiguration" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:112,0:setConfiguration: Missing docstring
W:113,1:setConfiguration: Global variable 'bw1' undefined at the module level
W:113,1:setConfiguration: Global variable 'delay1' undefined at the module level
W:113,1:setConfiguration: Global variable 'bw2' undefined at the module level
W:113,1:setConfiguration: Global variable 'delay2' undefined at the module level
C:149,0:setSegmentSize: Invalid name "setSegmentSize" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:149,0:setSegmentSize: Missing docstring
C:150,1:setSegmentSize: Operator not preceded by a space
	tcpSegments=(1500-18)*256
            ^
C:150,1:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:153,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:156,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:159,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:167,0:tcpDump: Invalid name "tcpDump" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:167,0:tcpDump: Invalid name "hostB" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:167,0:tcpDump: Missing docstring
C:167,12:tcpDump: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:168,1:tcpDump: Invalid name "LogFile" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:173,0:tcpTransfer: Invalid name "tcpTransfer" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:173,0:tcpTransfer: Invalid name "hostA" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:173,0:tcpTransfer: Invalid name "hostC" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:173,16:tcpTransfer: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:173,23:tcpTransfer: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:184,1: Invalid name "arguments" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:186,1: Invalid name "linkConfig1" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:187,1: Invalid name "linkConfig2" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:188,1: Invalid name "segment" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:189,1: Invalid name "logFile" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:190,1: Invalid name "packetsToDrop" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:193,1: Invalid name "segmentsSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:194,1: Invalid name "payloadSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


Report
======
119 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |48     |48       |=          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |112    |112      |=          |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|W0312      |108         |
+-----------+------------+
|C0103      |32          |
+-----------+------------+
|C0301      |11          |
+-----------+------------+
|W0601      |4           |
+-----------+------------+
|C0111      |4           |
+-----------+------------+
|C0322      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -3.45/10 (previous run: -3.45/10)

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |1      |1          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+
|method   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |6      |6          |=          |33.33       |100.00   |
+---------+-------+-----------+-----------+------------+---------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |120    |69.77 |120      |=          |
+----------+-------+------+---------+-----------+
|docstring |22     |12.79 |22       |=          |
+----------+-------+------+---------+-----------+
|comment   |22     |12.79 |22       |=          |
+----------+-------+------+---------+-----------+
|empty     |8      |4.65  |8        |=          |
+----------+-------+------+---------+-----------+



External dependencies
---------------------
::

    mininet 
      \-link 
      | \-TCLink (mininet_tlp_measurement)
      \-log 
      | \-setLogLevel (mininet_tlp_measurement)
      \-net 
      | \-Mininet (mininet_tlp_measurement)
      \-topo 
        \-Topo (mininet_tlp_measurement)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     mininet_tlp_pylint_analysis                                                                         0000664 0001750 0001750 00000032745 12270755660 016544  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module mininet_tlp_measurement
C: 21,0: Line too long (91/80)
W: 23,0: Found indentation with tabs instead of spaces
W: 25,0: Found indentation with tabs instead of spaces
W: 26,0: Found indentation with tabs instead of spaces
W: 27,0: Found indentation with tabs instead of spaces
W: 30,0: Found indentation with tabs instead of spaces
W: 31,0: Found indentation with tabs instead of spaces
W: 35,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
W: 38,0: Found indentation with tabs instead of spaces
W: 39,0: Found indentation with tabs instead of spaces
W: 40,0: Found indentation with tabs instead of spaces
W: 43,0: Found indentation with tabs instead of spaces
W: 44,0: Found indentation with tabs instead of spaces
W: 45,0: Found indentation with tabs instead of spaces
W: 46,0: Found indentation with tabs instead of spaces
W: 49,0: Found indentation with tabs instead of spaces
W: 50,0: Found indentation with tabs instead of spaces
W: 51,0: Found indentation with tabs instead of spaces
W: 52,0: Found indentation with tabs instead of spaces
W: 55,0: Found indentation with tabs instead of spaces
C: 58,0: Line too long (93/80)
W: 58,0: Found indentation with tabs instead of spaces
W: 61,0: Found indentation with tabs instead of spaces
W: 64,0: Found indentation with tabs instead of spaces
W: 67,0: Found indentation with tabs instead of spaces
W: 70,0: Found indentation with tabs instead of spaces
C: 72,0: Line too long (96/80)
W: 73,0: Found indentation with tabs instead of spaces
W: 74,0: Found indentation with tabs instead of spaces
W: 75,0: Found indentation with tabs instead of spaces
W: 79,0: Found indentation with tabs instead of spaces
W: 82,0: Found indentation with tabs instead of spaces
W: 83,0: Found indentation with tabs instead of spaces
W: 86,0: Found indentation with tabs instead of spaces
W: 89,0: Found indentation with tabs instead of spaces
W: 94,0: Found indentation with tabs instead of spaces
C: 98,0: Line too long (81/80)
W: 98,0: Found indentation with tabs instead of spaces
W: 99,0: Found indentation with tabs instead of spaces
W:100,0: Found indentation with tabs instead of spaces
C:101,0: Line too long (87/80)
W:104,0: Found indentation with tabs instead of spaces
C:105,0: Line too long (87/80)
C:108,0: Line too long (99/80)
W:108,0: Found indentation with tabs instead of spaces
C:109,0: Line too long (92/80)
W:109,0: Found indentation with tabs instead of spaces
W:110,0: Found indentation with tabs instead of spaces
W:113,0: Found indentation with tabs instead of spaces
W:114,0: Found indentation with tabs instead of spaces
C:116,0: Line too long (91/80)
W:118,0: Found indentation with tabs instead of spaces
W:119,0: Found indentation with tabs instead of spaces
W:120,0: Found indentation with tabs instead of spaces
W:121,0: Found indentation with tabs instead of spaces
W:122,0: Found indentation with tabs instead of spaces
W:123,0: Found indentation with tabs instead of spaces
W:124,0: Found indentation with tabs instead of spaces
W:125,0: Found indentation with tabs instead of spaces
W:126,0: Found indentation with tabs instead of spaces
W:127,0: Found indentation with tabs instead of spaces
W:128,0: Found indentation with tabs instead of spaces
W:129,0: Found indentation with tabs instead of spaces
W:130,0: Found indentation with tabs instead of spaces
W:131,0: Found indentation with tabs instead of spaces
W:132,0: Found indentation with tabs instead of spaces
W:133,0: Found indentation with tabs instead of spaces
W:134,0: Found indentation with tabs instead of spaces
W:136,0: Found indentation with tabs instead of spaces
W:137,0: Found indentation with tabs instead of spaces
W:138,0: Found indentation with tabs instead of spaces
W:139,0: Found indentation with tabs instead of spaces
W:140,0: Found indentation with tabs instead of spaces
W:141,0: Found indentation with tabs instead of spaces
W:142,0: Found indentation with tabs instead of spaces
W:143,0: Found indentation with tabs instead of spaces
W:144,0: Found indentation with tabs instead of spaces
W:145,0: Found indentation with tabs instead of spaces
W:146,0: Found indentation with tabs instead of spaces
W:147,0: Found indentation with tabs instead of spaces
W:148,0: Found indentation with tabs instead of spaces
W:149,0: Found indentation with tabs instead of spaces
W:150,0: Found indentation with tabs instead of spaces
W:151,0: Found indentation with tabs instead of spaces
W:155,0: Found indentation with tabs instead of spaces
W:156,0: Found indentation with tabs instead of spaces
W:157,0: Found indentation with tabs instead of spaces
W:158,0: Found indentation with tabs instead of spaces
W:159,0: Found indentation with tabs instead of spaces
W:160,0: Found indentation with tabs instead of spaces
W:161,0: Found indentation with tabs instead of spaces
W:162,0: Found indentation with tabs instead of spaces
W:163,0: Found indentation with tabs instead of spaces
W:164,0: Found indentation with tabs instead of spaces
W:165,0: Found indentation with tabs instead of spaces
W:166,0: Found indentation with tabs instead of spaces
W:167,0: Found indentation with tabs instead of spaces
W:168,0: Found indentation with tabs instead of spaces
W:169,0: Found indentation with tabs instead of spaces
W:173,0: Found indentation with tabs instead of spaces
W:174,0: Found indentation with tabs instead of spaces
W:175,0: Found indentation with tabs instead of spaces
W:178,0: Found indentation with tabs instead of spaces
W:181,0: Found indentation with tabs instead of spaces
W:182,0: Found indentation with tabs instead of spaces
C:183,0: Line too long (91/80)
W:183,0: Found indentation with tabs instead of spaces
W:184,0: Found indentation with tabs instead of spaces
W:186,0: Found indentation with tabs instead of spaces
W:189,0: Found indentation with tabs instead of spaces
W:190,0: Found indentation with tabs instead of spaces
W:192,0: Found indentation with tabs instead of spaces
W:193,0: Found indentation with tabs instead of spaces
W:194,0: Found indentation with tabs instead of spaces
W:195,0: Found indentation with tabs instead of spaces
W:196,0: Found indentation with tabs instead of spaces
W:198,0: Found indentation with tabs instead of spaces
W:199,0: Found indentation with tabs instead of spaces
W:200,0: Found indentation with tabs instead of spaces
W:202,0: Found indentation with tabs instead of spaces
C: 20,0:Router_Topo: Invalid name "Router_Topo" for type class (should match [A-Z_][a-zA-Z0-9]+$)
C: 25,9:Router_Topo.__init__: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 26,9:Router_Topo.__init__: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 27,9:Router_Topo.__init__: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 34,0:simpleTest: Invalid name "simpleTest" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 34,0:simpleTest: Missing docstring
C: 38,1:simpleTest: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 39,1:simpleTest: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 40,1:simpleTest: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 97,0:parseArguments: Invalid name "parseArguments" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:117,0:setConfiguration: Invalid name "setConfiguration" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:117,0:setConfiguration: Missing docstring
W:118,1:setConfiguration: Global variable 'bw1' undefined at the module level
W:118,1:setConfiguration: Global variable 'delay1' undefined at the module level
W:118,1:setConfiguration: Global variable 'bw2' undefined at the module level
W:118,1:setConfiguration: Global variable 'delay2' undefined at the module level
C:154,0:setSegmentSize: Invalid name "setSegmentSize" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:154,0:setSegmentSize: Missing docstring
C:155,1:setSegmentSize: Operator not preceded by a space
	tcpSegments=(1500-18)*256
            ^
C:155,1:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:158,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:161,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:164,2:setSegmentSize: Invalid name "tcpSegments" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:172,0:tcpDump: Invalid name "tcpDump" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:172,0:tcpDump: Invalid name "hostB" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:172,0:tcpDump: Missing docstring
C:172,12:tcpDump: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:173,1:tcpDump: Invalid name "LogFile" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:177,0:tcpDumpStop: Invalid name "tcpDumpStop" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:177,0:tcpDumpStop: Invalid name "hostB" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:177,0:tcpDumpStop: Missing docstring
C:177,16:tcpDumpStop: Invalid name "hostB" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:180,0:tcpTransfer: Invalid name "tcpTransfer" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:180,0:tcpTransfer: Invalid name "hostA" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:180,0:tcpTransfer: Invalid name "hostC" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:180,16:tcpTransfer: Invalid name "hostA" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:180,23:tcpTransfer: Invalid name "hostC" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:190,1: Invalid name "arguments" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:192,1: Invalid name "linkConfig1" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:193,1: Invalid name "linkConfig2" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:194,1: Invalid name "segment" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:195,1: Invalid name "logFile" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:196,1: Invalid name "packetsToDrop" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:199,1: Invalid name "segmentsSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C:200,1: Invalid name "payloadSize" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


Report
======
123 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |1      |1          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+
|method   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|function |7      |6          |+1.00      |28.57       |100.00   |
+---------+-------+-----------+-----------+------------+---------+



Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |124    |70.86 |125      |-1.00      |
+----------+-------+------+---------+-----------+
|docstring |22     |12.57 |19       |+3.00      |
+----------+-------+------+---------+-----------+
|comment   |24     |13.71 |23       |+1.00      |
+----------+-------+------+---------+-----------+
|empty     |5      |2.86  |5        |=          |
+----------+-------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |51     |61       |-10.00     |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |115    |116      |-1.00      |
+-----------+-------+---------+-----------+
|error      |0      |0        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|W0312      |111         |
+-----------+------------+
|C0103      |35          |
+-----------+------------+
|C0301      |10          |
+-----------+------------+
|C0111      |5           |
+-----------+------------+
|W0601      |4           |
+-----------+------------+
|C0322      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -3.50/10 (previous run: -4.27/10)

External dependencies
---------------------
::

    mininet 
      \-link 
      | \-TCLink (mininet_tlp_measurement)
      \-log 
      | \-setLogLevel (mininet_tlp_measurement)
      \-net 
      | \-Mininet (mininet_tlp_measurement)
      \-topo 
        \-Topo (mininet_tlp_measurement)



                           nohup.out                                                                                           0000600 0001750 0001750 00000000000 12266437330 012614  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                OutputFiles/                                                                                        0000755 0000000 0000000 00000000000 12270533750 012043  5                                                                                                    ustar   root                            root                                                                                                                                                                                                                   OutputFiles/tlpEnabled_fast_short_1                                                                 0000644 0000000 0000000 00000000436 12270452135 016514  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.34905910492	0.689700126648
1.37340903282	0.692317962646
1.3730969429	0.691863059998
2.34819412231	0.689645051956
2.34271812439	0.68577504158
2.352227211	0.689740180969
2.34828996658	0.689802885056
2.34804201126	0.689723014832
1.37042403221	0.689399957657
2.35454797745	0.693047046661
                                                                                                                                                                                                                                  OutputFiles/tlpEnabled_fast_short_2                                                                 0000644 0000000 0000000 00000000440 12270452232 016506  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.45015597343	0.68966794014
2.44933891296	0.689789056778
1.42403483391	0.64310002327
2.44740700722	0.689745903015
2.45018005371	0.689774036407
2.44767308235	0.689872026443
2.45043110847	0.689695835114
2.44980716705	0.689640045166
2.44889307022	0.689754009247
1.47036910057	0.689292907715
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_short_1                                                                0000644 0000000 0000000 00000000441 12270452326 016667  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.46548199654	0.789895057678
2.44773292542	0.789717912674
1.46869111061	0.787477970123
1.47632694244	0.795136928558
2.44347882271	0.785693883896
2.4490840435	0.789767980576
1.46664619446	0.785621166229
2.44661402702	0.789841890335
2.44767999649	0.789024829865
2.44983410835	0.789718151093
                                                                                                                                                                                                                               OutputFiles/tlpDisabled_fast_short_2                                                                0000644 0000000 0000000 00000000440 12270452424 016666  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.57694005966	0.833759069443
2.57983183861	0.83385181427
1.51956605911	0.830041885376
2.5934779644	0.833998918533
2.58063411713	0.833820104599
2.57773709297	0.833854913712
2.57604002953	0.829855918884
1.51596212387	0.826522827148
2.58292794228	0.837902069092
2.57676005363	0.829789161682
                                                                                                                                                                                                                                OutputFiles/tlpEnabled_fast_short_4                                                                 0000644 0000000 0000000 00000000440 12270453071 016512  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.3483850956	0.649797916412
2.29915308952	0.585067033768
1.36907505989	0.647099018097
2.34007906914	0.641647815704
2.34805679321	0.649832963943
1.36994194984	0.647429943085
2.34830307961	0.649734973907
2.34794592857	0.64971113205
1.30867886543	0.586053848267
2.34851288795	0.649770021439
                                                                                                                                                                                                                                OutputFiles/tlpEnabled_fast_short_8                                                                 0000644 0000000 0000000 00000000437 12270453163 016526  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.27996897697	0.561194896698
2.28417897224	0.565823078156
1.24693202972	0.504389047623
2.28912401199	0.569719076157
2.28471493721	0.565713882446
1.30151581764	0.558681964874
1.30806112289	0.56568312645
2.2853679657	0.565667867661
2.2900621891	0.569125175476
2.28931498528	0.569794178009
                                                                                                                                                                                                                                 OutputFiles/tlpDisabled_fast_short_4                                                                0000644 0000000 0000000 00000000437 12270453261 016676  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.56156802177	0.822008132935
2.56413507462	0.82133603096
1.45881223679	0.773192882538
1.51506710052	0.829442977905
2.56208205223	0.821985006332
2.5658121109	0.825464010239
2.56163406372	0.821295022964
2.56589508057	0.826125860214
2.57052993774	0.829359054565
2.5655939579	0.826141119003
                                                                                                                                                                                                                                 OutputFiles/tlpDisabled_fast_short_8                                                                0000644 0000000 0000000 00000000437 12270453357 016710  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.51718902588	0.802495002747
2.52029085159	0.806450128555
2.51389288902	0.802685022354
2.51193094254	0.7984790802
2.5237929821	0.810642004013
2.51838684082	0.806623935699
1.48456811905	0.811794996262
2.52506303787	0.810580968857
2.51892185211	0.806594133377
1.46443200111	0.806046009064
                                                                                                                                                                                                                                 OutputFiles/tlpEnabled_fast_medium_1                                                                0000644 0000000 0000000 00000000442 12270454221 016630  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.25176095963	0.818531036377
3.20141983032	0.765963792801
2.20723199844	0.751024007797
2.27057409286	0.814301967621
3.20217108727	0.766631126404
3.19982290268	0.766672849655
2.22073984146	0.764551877975
3.20170807838	0.766698122025
3.20677685738	0.774477958679
2.22376704216	0.767479896545
                                                                                                                                                                                                                              OutputFiles/tlpEnabled_fast_medium_2                                                                0000644 0000000 0000000 00000000440 12270454330 016630  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.34402108192	0.794697999954
3.34308004379	0.79464507103
3.34411001205	0.794527053833
3.30724406242	0.757834911346
3.34641909599	0.794567108154
3.31551814079	0.762531995773
3.34568881989	0.794528007507
3.31706595421	0.762471914291
3.34330415726	0.794542074203
2.33873701096	0.76253080368
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_medium_1                                                               0000644 0000000 0000000 00000000440 12270454436 017013  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.19981384277	0.766551971436
3.19893193245	0.766533136368
3.2511510849	0.818439006805
2.21584510803	0.759659051895
3.20672988892	0.774472951889
3.20193696022	0.76668381691
3.19878387451	0.766708850861
3.20782208443	0.774466991425
3.19947910309	0.766680002213
3.25318288803	0.817838907242
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_medium_2                                                               0000644 0000000 0000000 00000000442 12270454543 017015  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.21042609215	0.766815900803
3.21898603439	0.774618864059
2.24286603928	0.778167963028
3.24785399437	0.806699037552
3.25404906273	0.773800134659
3.21751594543	0.774644851685
3.21704292297	0.774616003036
3.21562409401	0.774639844894
3.20977497101	0.766800880432
3.20762205124	0.766652107239
                                                                                                                                                                                                                              OutputFiles/tlpEnabled_fast_medium_4                                                                0000644 0000000 0000000 00000000441 12270454755 016646  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.24392580986	0.770531892776
3.20785307884	0.734519958496
2.22692894936	0.729577064514
2.23687911034	0.739067077637
3.24341201782	0.766638994217
3.20890903473	0.734519004822
3.23612093925	0.762557983398
3.20685982704	0.730520009995
2.2168200016	0.719599962234
3.24215102196	0.766561985016
                                                                                                                                                                                                                               OutputFiles/tlpEnabled_fast_medium_8                                                                0000644 0000000 0000000 00000000440 12270455062 016641  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.27651309967	0.743417978287
3.23887610435	0.741965055466
3.20224022865	0.706404209137
3.20296001434	0.706549882889
3.2361869812	0.742526054382
3.23771882057	0.742623090744
3.23812294006	0.74180316925
3.23985695839	0.742686986923
3.23959493637	0.742668151855
2.26052093506	0.742287158966
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_medium_4                                                               0000644 0000000 0000000 00000000442 12270455171 017015  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.24831986427	0.770956993103
3.25158500671	0.774118900299
3.24866008759	0.770880937576
3.32662606239	0.810153961182
3.32928586006	0.810158967972
3.24756097794	0.770727157593
3.32597589493	0.810147047043
3.21150398254	0.770080804825
3.20860791206	0.770889997482
3.32349896431	0.806871891022
                                                                                                                                                                                                                              OutputFiles/tlpDisabled_fast_medium_8                                                               0000644 0000000 0000000 00000000441 12270455274 017024  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.34496998787	0.855324029922
3.34497904778	0.854765176773
2.23508882523	0.802072048187
2.29423689842	0.861666917801
2.2887840271	0.855193853378
3.26794290543	0.819406986237
2.22298598289	0.789441823959
3.34226083755	0.854607820511
3.34507918358	0.855479955673
3.26911878586	0.819144964218
                                                                                                                                                                                                                               OutputFiles/tlpEnabled_fast_long_4                                                                  0000644 0000000 0000000 00000000437 12270455653 016330  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.76884484291	0.74359703064
4.76846504211	0.743693113327
3.79298090935	0.745439052582
3.75214982033	0.703962802887
4.7289249897	0.703002929688
4.72754788399	0.703022003174
4.7250828743	0.699039936066
4.72520303726	0.699067831039
4.72430896759	0.699588060379
3.75004506111	0.701735973358
                                                                                                                                                                                                                                 OutputFiles/tlpEnabled_fast_long_8                                                                  0000644 0000000 0000000 00000000437 12270456000 016317  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.6975069046	0.651039123535
3.71695303917	0.649108886719
4.7022330761	0.655776977539
4.69899487495	0.651519060135
4.69799399376	0.651047945023
4.69959902763	0.651042938232
4.69297194481	0.647003889084
4.69771909714	0.650979042053
4.69990086555	0.651065826416
4.73660087585	0.69170999527
                                                                                                                                                                                                                                 OutputFiles/tlpDisabled_fast_long_4                                                                 0000644 0000000 0000000 00000000441 12270456123 016471  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.77590799332	0.747354030609
3.75001692772	0.738748073578
4.76534199715	0.740051031113
4.84645485878	0.778488874435
3.79468512535	0.782662153244
4.84525799751	0.779986858368
4.84695005417	0.779312133789
3.74589204788	0.734354972839
4.76685404778	0.739324092865
4.7635641098	0.736058950424
                                                                                                                                                                                                                               OutputFiles/tlpDisabled_fast_long_8                                                                 0000644 0000000 0000000 00000000432 12270456251 016477  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.73594403267	0.735889911652
4.81480002403	0.776440858841
3.71827316284	0.735266923904
4.72999286652	0.732455968857
4.7301940918	0.732522010803
4.73738408089	0.7357878685
4.73512291908	0.7358481884
4.73273801804	0.732553005219
4.8140809536	0.77635884285
4.8193860054	0.780453920364
                                                                                                                                                                                                                                      OutputFiles/tlpEnabled_fast_long_1                                                                  0000644 0000000 0000000 00000000436 12270456450 016320  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.75080299377	0.743546009064
4.72294306755	0.739496946335
4.77415895462	0.786886930466
4.76271390915	0.77970290184
4.76847219467	0.782065153122
4.72965502739	0.74371099472
3.78910398483	0.781868934631
4.76433300972	0.779653072357
4.76347398758	0.778948068619
4.727257967	0.743641138077
                                                                                                                                                                                                                                  OutputFiles/tlpEnabled_fast_long_2                                                                  0000644 0000000 0000000 00000000440 12270456571 016320  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.89507603645	0.775002002716
3.8638420105	0.724358081818
3.86476182938	0.725539922714
3.86548805237	0.722163915634
4.88668084145	0.766954898834
4.84383893013	0.727697134018
3.8757519722	0.732958078384
3.86274504662	0.724276065826
4.84564399719	0.727755069733
3.86674904823	0.728286027908
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_long_1                                                                 0000644 0000000 0000000 00000000440 12270456717 016476  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.74666118622	0.740045070648
4.74403691292	0.743637800217
4.74264001846	0.742866039276
4.76291680336	0.779631853104
4.73047399521	0.742959022522
4.72749996185	0.743620872498
4.72802901268	0.743502140045
4.76323795319	0.779758930206
4.741492033	0.738945960999
4.77152180672	0.786964893341
                                                                                                                                                                                                                                OutputFiles/tlpDisabled_fast_long_2                                                                 0000644 0000000 0000000 00000000441 12270457043 016471  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.80069303513	0.785804986954
4.85462999344	0.783791065216
4.77275705338	0.743830919266
4.85600018501	0.78299498558
4.86039400101	0.786916017532
4.86202692986	0.791707992554
4.77001285553	0.739171028137
4.77525997162	0.743849039078
4.85064411163	0.779000043869
3.75291490555	0.738082170486
                                                                                                                                                                                                                               OutputFiles/tlpEnabled_moderate_long_1                                                              0000644 0000000 0000000 00000000426 12270462115 017155  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.63001894951	1.61498379707
7.57700610161	1.56078696251
7.57348418236	1.55856919289
7.62671780586	1.61182904243
7.57029700279	1.55397796631
7.56052207947	1.54553198814
7.62620306015	1.6096329689
7.62378096581	1.60897707939
7.55762910843	1.54285907745
7.57433986664	1.5609369278
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_moderate_long_2                                                              0000644 0000000 0000000 00000000427 12270462302 017155  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.91641688347	1.58153295517
7.89699006081	1.56469416618
7.91655015945	1.58301186562
7.89695596695	1.56470298767
7.83910894394	1.51235079765
7.89830803871	1.56740999222
7.86178302765	1.53100895882
7.8638279438	1.52896499634
7.88914108276	1.55835199356
7.86248683929	1.53168010712
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_moderate_long_1                                                             0000644 0000000 0000000 00000000426 12270462465 017342  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.61924099922	1.60421299934
7.56094193459	1.5461230278
7.63080811501	1.61604809761
7.63557600975	1.62214112282
7.63495898247	1.62011790276
7.62320113182	1.60843801498
7.62570381165	1.60928487778
7.56676793098	1.55041003227
7.58110308647	1.5662920475
7.62992620468	1.61368322372
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_moderate_long_2                                                             0000644 0000000 0000000 00000000425 12270462650 017336  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.58245205879	1.55287289619
7.58679914474	1.55696582794
7.63742399216	1.60475301743
7.58601593971	1.55499005318
7.63273501396	1.6002600193
7.58170986176	1.55060315132
7.57950782776	1.54976987839
7.58123803139	1.54864501953
7.58642506599	1.55544018745
7.586550951	1.55533003807
                                                                                                                                                                                                                                           OutputFiles/tlpEnabled_moderate_long_4                                                              0000644 0000000 0000000 00000000420 12270463147 017160  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.60126590729	1.50691199303
7.56624102592	1.47035384178
7.6054019928	1.51080513
7.54232597351	1.44629216194
7.56770014763	1.47320985794
7.5692460537	1.4745850563
7.56772112846	1.4733080864
7.62368416786	1.52924990654
7.55267906189	1.45806598663
7.54043197632	1.4448029995
                                                                                                                                                                                                                                                OutputFiles/tlpEnabled_moderate_long_8                                                              0000644 0000000 0000000 00000000426 12270463331 017165  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.53972887993	1.40213298798
7.48793196678	1.35188603401
7.47022986412	1.33397603035
7.53197479248	1.39402985573
7.53186011314	1.39564394951
7.49657988548	1.35995697975
7.49488782883	1.36006617546
7.53610897064	1.40121293068
7.4814620018	1.3436999321
7.49635696411	1.36142683029
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_moderate_long_4                                                             0000644 0000000 0000000 00000000424 12270465335 017342  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.61484098434	1.59180688858
7.57488512993	1.55305504799
7.5720140934	1.55021691322
7.52025914192	1.49567985535
7.57655000687	1.5518219471
7.60173606873	1.57736206055
7.57291007042	1.54819703102
7.56822896004	1.5464720726
7.5717959404	1.54847002029
7.55660295486	1.53333306313
                                                                                                                                                                                                                                            OutputFiles/tlpDisabled_moderate_long_8                                                             0000644 0000000 0000000 00000000426 12270465517 017352  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   7.52752304077	1.56003308296
7.52255702019	1.55600595474
7.48827791214	1.52142095566
7.52651000023	1.55975103378
7.49406194687	1.52733778954
7.46913194656	1.5036919117
7.47343397141	1.50811290741
7.49537014961	1.5286450386
7.48921298981	1.52262377739
7.48233699799	1.51573300362
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_moderate_medium_1                                                           0000644 0000000 0000000 00000000424 12270474426 017661  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   5.3978998661	1.53012895584
4.42479801178	1.5131649971
4.42861509323	1.51561713219
4.44160914421	1.52998805046
4.44650602341	1.53474998474
4.44628596306	1.53467702866
4.44638204575	1.53471708298
4.40000510216	1.48835206032
4.449395895	1.53790688515
4.44178390503	1.52878499031
                                                                                                                                                                                                                                            OutputFiles/tlpDisabled_moderate_medium_2                                                           0000644 0000000 0000000 00000000430 12270474551 017656  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.40740609169	1.47962903976
4.40687918663	1.47759103775
4.40887093544	1.48108291626
4.40603613853	1.47670388222
4.40269303322	1.47483611107
4.40704298019	1.47760796547
4.41140913963	1.48196697235
4.36878395081	1.44089484215
4.38602280617	1.45816421509
4.40641498566	1.47839403152
                                                                                                                                                                                                                                        OutputFiles/tlpDisabled_moderate_medium_4                                                           0000644 0000000 0000000 00000000425 12270474674 017672  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.45717787743	1.53570604324
4.39483308792	1.47501397133
4.38067293167	1.4608361721
4.39088487625	1.46971011162
4.3858101368	1.46438312531
4.39102506638	1.47103500366
4.39590406418	1.47586202621
4.40299606323	1.48317193985
4.38236904144	1.46249985695
4.39486598969	1.4735019207
                                                                                                                                                                                                                                           OutputFiles/tlpDisabled_moderate_medium_8                                                           0000644 0000000 0000000 00000000427 12270475017 017670  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.47969508171	1.61638903618
4.47921800613	1.61442112923
4.47450590134	1.6109828949
4.47913384438	1.61579489708
4.47936010361	1.61444187164
4.47933483124	1.61592817307
4.47812008858	1.61184000969
4.47899699211	1.61544394493
4.47428894043	1.60809087753
4.46993613243	1.60505604744
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_moderate_short_1                                                            0000644 0000000 0000000 00000000426 12270475123 017535  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   3.00102615356	1.63988804817
2.93112897873	1.5699930191
2.93422198296	1.57297801971
3.01182889938	1.64911603928
2.93110394478	1.56984901428
3.01136112213	1.6502161026
2.99679398537	1.63549804688
2.93416810036	1.57292819023
2.94219613075	1.58085513115
3.01183199883	1.65055298805
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_moderate_short_2                                                            0000644 0000000 0000000 00000000427 12270475230 017536  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.96800684929	1.59046220779
2.94630384445	1.56852602959
3.00733399391	1.62831282616
2.96457195282	1.58553791046
2.99469304085	1.61700201035
2.96817111969	1.5904250145
2.96029686928	1.58002614975
2.99075102806	1.61307811737
2.95371389389	1.57468605042
3.00340485573	1.62585997581
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_moderate_short_4                                                            0000644 0000000 0000000 00000000427 12270475334 017545  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.97117400169	1.60153579712
2.94502091408	1.57544898987
2.97885203362	1.60796403885
2.94522595406	1.5755469799
2.97446107864	1.60486793518
2.97867798805	1.60913896561
2.98335909843	1.61389017105
2.97472596169	1.60523486137
2.92621302605	1.55681490898
2.98359513283	1.61415195465
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_moderate_short_8                                                            0000644 0000000 0000000 00000000427 12270475440 017547  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.84196400642	1.52898216248
2.88033890724	1.56720495224
2.85435295105	1.54130887985
2.86119103432	1.54823088646
2.8873360157	1.57415890694
2.84191799164	1.52903604507
2.89122009277	1.57801604271
2.84282708168	1.52958583832
2.89630913734	1.58330702782
2.84267687798	1.52951407433
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_moderate_medium_1                                                            0000644 0000000 0000000 00000000427 12270475701 017504  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.44175410271	1.53015708923
4.42369008064	1.51209998131
4.42869305611	1.51710104942
4.42154312134	1.50979208946
4.44179916382	1.52885508537
4.42933297157	1.51617884636
4.44628310204	1.5347840786
4.42538690567	1.51368689537
4.44694900513	1.53541707993
4.42914509773	1.51729011536
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_moderate_medium_2                                                            0000644 0000000 0000000 00000000426 12270476026 017505  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.59773302078	1.44864296913
4.60680985451	1.45910692215
4.60629487038	1.45725798607
4.58748078346	1.43995594978
4.59916400909	1.44870281219
4.59233283997	1.44340205193
4.60227203369	1.45464706421
4.6068239212	1.4591012001
4.59792280197	1.45042991638
4.56514596939	1.42006397247
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_moderate_medium_4                                                            0000644 0000000 0000000 00000000427 12270476151 017507  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.44882416725	1.45615196228
4.39897894859	1.4050450325
4.39524388313	1.40264415741
4.38167500496	1.38901591301
4.39913678169	1.40656304359
4.38056993484	1.38810300827
4.39545297623	1.40126609802
4.45400905609	1.46132516861
4.38069796562	1.38809895515
4.38141489029	1.38886117935
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_moderate_medium_8                                                            0000644 0000000 0000000 00000000424 12270476274 017516  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   4.44864392281	1.41559910774
4.45174217224	1.41853189468
4.44341397285	1.4089589119
4.44254803658	1.40800499916
4.45253896713	1.41807103157
4.43392395973	1.40082907677
4.4429910183	1.41004300117
4.4511911869	1.4182138443
4.45088291168	1.41782689095
4.45183110237	1.41741394997
                                                                                                                                                                                                                                            OutputFiles/tlpEnabled_moderate_short_1                                                             0000644 0000000 0000000 00000000426 12270476376 017373  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.74021697044	1.37893509865
2.66696000099	1.30558800697
2.74094080925	1.37967681885
2.7411301136	1.37978410721
2.69118094444	1.32991409302
2.68979310989	1.3286280632
2.73283910751	1.37143707275
2.69404816628	1.33136796951
2.69411897659	1.33274888992
2.69031906128	1.32906699181
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_moderate_short_2                                                             0000644 0000000 0000000 00000000426 12270476501 017362  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.92667508125	1.36142778397
2.84032607079	1.27896094322
2.84490704536	1.28373599052
2.92694401741	1.36151003838
2.91753387451	1.35230898857
2.83353614807	1.27225899696
2.8451769352	1.2838408947
2.84415388107	1.28285288811
2.91784787178	1.35252285004
2.84487104416	1.28372907639
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_moderate_short_4                                                             0000644 0000000 0000000 00000000427 12270476603 017370  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.72680807114	1.28305220604
2.72335100174	1.28109407425
2.65216207504	1.21001005173
2.7001888752	1.25798606873
2.65247893333	1.21020793915
2.65439295769	1.21217393875
2.71622395515	1.27400183678
2.65322184563	1.21118688583
2.73125696182	1.28758406639
2.64545297623	1.20307683945
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_moderate_short_8                                                             0000644 0000000 0000000 00000000427 12270476703 017375  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   2.53383207321	1.05130004883
2.60400390625	1.11985111237
2.53303098679	1.05043315887
2.54422211647	1.05859398842
2.60462903976	1.12185692787
2.60384011269	1.1196911335
2.53276920319	1.05031704903
2.60300898552	1.12037706375
2.59663295746	1.11406493187
2.58839702606	1.10578894615
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_slow_short_1                                                                 0000644 0000000 0000000 00000000426 12270500132 016531  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   13.3401899338	6.67308402061
13.3586659431	6.6987888813
13.3135540485	6.66095113754
13.333466053	6.68087887764
13.3380792141	6.68524599075
13.3357150555	6.68312597275
13.3607208729	6.70809602737
13.3206551075	6.65533304214
13.3289990425	6.67078399658
13.3478200436	6.68951702118
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_slow_short_1                                                                0000644 0000000 0000000 00000000425 12270500772 016717  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   14.4320158958	7.77942991257
14.4407758713	7.76811695099
14.4451270103	7.77961397171
14.429213047	7.77654409409
14.4833650589	7.82489490509
14.4431889057	7.78347802162
14.4659459591	7.80059909821
14.4596610069	7.80146193504
14.41877985	7.75334787369
14.4409170151	7.77552890778
                                                                                                                                                                                                                                           OutputFiles/tlpEnabled_slow_short_2                                                                 0000644 0000000 0000000 00000000426 12270501362 016540  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   14.3374447823	6.7592921257
14.3160889149	6.73475885391
14.3355369568	6.7572851181
14.2922570705	6.72357797623
14.2789061069	6.69980096817
14.2926421165	6.71129894257
14.2729139328	6.70096302032
14.3002130985	6.73146605492
14.3049690723	6.71629810333
13.8549399376	6.31105089188
                                                                                                                                                                                                                                          OutputFiles/tlpDisabled_slow_short_2                                                                0000644 0000000 0000000 00000000424 12270501653 016716  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   14.5644409657	7.95243096352
14.5498700142	7.93777894974
14.5534591675	7.92867612839
14.555781126	7.9365439415
14.5490710735	7.92976403236
14.5495898724	7.92469406128
14.5587010384	7.9338581562
14.5737478733	7.94730114937
14.6077311039	7.97556686401
14.5781509876	7.9659049511
                                                                                                                                                                                                                                            OutputFiles/tlpEnabled_slow_short_4                                                                 0000644 0000000 0000000 00000000426 12270503067 016546  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   13.1974740028	6.3766849041
13.1877510548	6.36858916283
13.1702809334	6.35660195351
13.199865818	6.38065481186
13.2093141079	6.38278508186
13.2040381432	6.37760710716
13.1741080284	6.36045789719
13.2007520199	6.37434411049
13.1387269497	6.31800103188
13.1551978588	6.34168505669
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_short_8                                                                 0000644 0000000 0000000 00000000427 12270503333 016547  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   12.0433521271	5.14916086197
12.4600300789	5.55293989182
12.4895260334	5.59550189972
12.482052803	5.58246207237
12.0482778549	5.15395903587
12.4944498539	5.59473419189
12.4770870209	5.57744693756
12.5019140244	5.59489297867
12.4859519005	5.57889389992
12.4839968681	5.58415913582
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_slow_short_4                                                                0000644 0000000 0000000 00000000426 12270504357 016726  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   14.361219883	7.90370512009
14.3378968239	7.88751506805
14.3688120842	7.90562486649
14.3429760933	7.87834906578
14.1962058544	7.74598813057
14.3538520336	7.90350604057
14.3489820957	7.8916258812
14.3497180939	7.89928197861
14.3525371552	7.89518594742
14.3190531731	7.86314201355
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_medium_1                                                                0000644 0000000 0000000 00000000426 12270505145 016663  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   23.5359928608	9.11318588257
23.5205559731	9.09065008163
23.5363559723	9.10642910004
23.5203859806	9.0904610157
23.5296468735	9.0997300148
23.5367388725	9.10693788528
23.5324831009	9.10988807678
23.5005729198	9.07796502113
23.5310370922	9.10122919083
23.5400080681	9.12420892715
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_medium_2                                                                0000644 0000000 0000000 00000000430 12270505602 016655  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   24.5161941051	8.78155589104
24.5033729076	8.76524019241
24.4832630157	8.74542093277
24.4954369068	8.76078820229
24.5165610313	8.77080893517
24.5047688484	8.76280903816
24.5076060295	8.76566696167
24.7325048447	8.98250699043
24.7139439583	8.96392893791
24.4905970097	8.74878287315
                                                                                                                                                                                                                                        OutputFiles/tlpEnabled_slow_medium_4                                                                0000644 0000000 0000000 00000000426 12270506220 016661  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   23.0652070045	8.47415208817
23.0418410301	8.45808887482
23.0497360229	8.46583104134
23.0453810692	8.45438599586
23.0203371048	8.42897486687
23.250674963	8.65998387337
23.0472018719	8.4562318325
23.0581998825	8.47451806068
23.0545880795	8.47784996033
23.0701208115	8.47929787636
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_medium_8                                                                0000644 0000000 0000000 00000000430 12270506631 016666  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   22.7233228683	8.05190300941
22.5179340839	7.85384678841
22.5075609684	7.83635187149
22.5079460144	7.83673191071
22.4991219044	7.82752990723
22.5061779022	7.83478999138
22.5139560699	7.84247708321
22.5339341164	7.86236786842
22.5055868626	7.84867596626
22.7033338547	8.03176498413
                                                                                                                                                                                                                                        OutputFiles/tlpDisabled_slow_medium_1                                                               0000644 0000000 0000000 00000000423 12270507674 017046  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   23.5548009872	9.12500190735
23.5299098492	9.10008192062
23.528824091	9.09889507294
23.5099608898	9.0799767971
23.5264101028	9.09617590904
23.37657094	8.95369791985
23.552312851	9.12961888313
23.5044059753	9.07436203957
23.5048649311	9.07482981682
23.5156130791	9.08576607704
                                                                                                                                                                                                                                             OutputFiles/tlpDisabled_slow_short_8                                                                0000644 0000000 0000000 00000000425 12270510700 016716  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   13.8042879105	7.75796890259
13.8057050705	7.7596051693
13.7600359917	7.71342492104
13.8095991611	7.76333498955
13.7975599766	7.75137400627
13.8054618835	7.7589969635
13.8195719719	7.77336001396
13.5241639614	7.47775006294
13.6385159492	7.59238910675
13.785449028	7.73188710213
                                                                                                                                                                                                                                           OutputFiles/tlpDisabled_slow_medium_2                                                               0000644 0000000 0000000 00000000427 12270513745 017047  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   23.2566699982	8.86747312546
23.2810661793	8.89899802208
23.5071280003	9.1177740097
23.2704048157	8.88109278679
23.2683458328	8.87904596329
23.2854838371	8.89609909058
23.4863638878	9.09711480141
23.2836358547	8.89439606667
23.2725269794	8.88327217102
23.2609639168	8.87168312073
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_slow_medium_4                                                               0000644 0000000 0000000 00000000427 12270515627 017052  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   23.0713849068	8.84379410744
23.0484509468	8.82097816467
23.0442111492	8.82377791405
23.0067231655	8.78611898422
23.0288238525	8.80847907066
23.0288529396	8.80115699768
23.2605650425	9.03303289413
23.0693800449	8.84156608582
23.0272231102	8.8068780899
23.0626890659	8.83514308929
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_slow_medium_8                                                               0000644 0000000 0000000 00000000430 12270516752 017050  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   22.7114350796	8.88792800903
22.4884440899	8.66468191147
22.4979240894	8.68152999878
22.4959611893	8.67941904068
22.5289931297	8.70556592941
22.4883811474	8.67216396332
22.5000259876	8.67662405968
22.7327511311	8.90928196907
22.4926831722	8.66899299622
22.5189938545	8.69557595253
                                                                                                                                                                                                                                        OutputFiles/tlpDisabled_slow_long_1                                                                 0000644 0000000 0000000 00000000427 12270522124 016514  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   41.6762089729	11.7429590225
41.6796579361	11.7464399338
46.4767739773	16.5472819805
41.736041069	11.8099520206
41.6751539707	11.7418510914
41.6444180012	11.7111551762
41.4805250168	11.5471701622
46.4840528965	16.5506999493
41.6299669743	11.6967070103
46.4621291161	16.5288860798
                                                                                                                                                                                                                                         OutputFiles/tlpDisabled_slow_long_2                                                                 0000644 0000000 0000000 00000000463 12270523537 016526  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   41.4622881413	11.5766530037
41.6573879719	11.7646231651
45.8274531364	15.9314911366
41.5779440403	11.6924190521
41.3652980328	11.4725041389
41.4309868813	11.5455429554
41.3818490505	11.4961531162
41.4468448162	11.554224968
41.7449719906	11.8520851135
41.6866109371	11.7938389778
41.6717228889	11.7790079117
                                                                                                                                                                                                             OutputFiles/tlpDisabled_slow_long_4                                                                 0000644 0000000 0000000 00000000430 12270525137 016520  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   41.4992909431	11.7682628632
41.3887829781	11.6650319099
41.1852490902	11.4543988705
41.1760809422	11.4525499344
41.5273869038	11.7964699268
41.1686689854	11.4449391365
41.2090959549	11.4782290459
46.7122910023	16.9814860821
41.1804680824	11.4566800594
41.1888608932	11.4577031136
                                                                                                                                                                                                                                        OutputFiles/tlpDisabled_slow_long_8                                                                 0000644 0000000 0000000 00000000605 12270527453 016533  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   40.648113966	11.3211779594
44.6804339886	15.3607211113
40.6713819504	11.3515350819
40.7183401585	11.391354084
40.8819360733	11.5622889996
40.6583678722	11.3314988613
40.6504840851	11.3237581253
40.6474571228	11.3276810646
40.6493449211	11.3297040462
40.6611819267	11.3342809677
40.926543951	11.5996661186
40.6928122044	11.3660540581
40.6706140041	11.3437018394
40.6354031563	11.3154270649
                                                                                                                           OutputFiles/tlpEnabled_slow_long_1                                                                  0000644 0000000 0000000 00000000426 12270531063 016340  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   41.6503958702	11.7172150612
41.6681411266	11.7349469662
41.6684439182	11.7352619171
41.6270258427	11.6937019825
43.8671059608	13.940928936
45.8564801216	15.9198830128
41.6626670361	11.7366979122
41.5709960461	11.6377310753
41.5560698509	11.637185812
41.8168070316	11.8835301399
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_long_2                                                                  0000644 0000000 0000000 00000000427 12270532017 016342  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   43.9098570347	11.7446708679
43.8261020184	11.6767969131
43.7487008572	11.6073219776
43.6412541866	11.4982569218
43.5755341053	11.441505909
43.5430929661	11.4162170887
43.5310049057	11.3898031712
43.5632939339	11.4292151928
43.4997851849	11.3666229248
43.5154521465	11.3822190762
                                                                                                                                                                                                                                         OutputFiles/tlpEnabled_slow_long_4                                                                  0000644 0000000 0000000 00000000426 12270532730 016345  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   41.1970100403	11.1027429104
41.3764829636	11.2821729183
45.5366141796	15.4423120022
41.2370231152	11.1425950527
41.4561421871	11.361675024
41.1896998882	11.1025528908
41.2020730972	11.1150281429
41.1818978786	11.0874919891
42.4065458775	12.3121528625
41.181625843	11.0874569416
                                                                                                                                                                                                                                          OutputFiles/tlpEnabled_slow_long_8                                                                  0000644 0000000 0000000 00000000425 12270533640 016351  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   40.6578330994	10.4831118584
40.6859009266	10.511398077
40.6692950726	10.5016679764
40.6402301788	10.4655930996
40.6649599075	10.4902410507
40.6524348259	10.4775409698
40.6786391735	10.5035262108
43.441106081	13.2736828327
47.0497751236	16.874861002
41.0271799564	10.8522398472
                                                                                                                                                                                                                                           tcp_analysis.py                                                                                     0000664 0001750 0001750 00000004232 12270761652 014024  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                import dpkt
import argparse

completionTime = 0
def filterPackets(pcapReader):
    """Filters the packets of the transmission being observed"""
    pktsToObserve = []
    count = 0;
    for ts, data in pcapReader:
        ether = dpkt.ethernet.Ethernet(data)
	#print ts
        ip = ether.data
        tcp = ip.data
        if type(tcp) == dpkt.tcp.TCP:
            if tcp.sport == 7777 or tcp.dport == 7777:
		pktsToObserve.append((ts, ether))
		#print "--------------------------------------------------------------------"
		#print pktsToObserve[count]
		#print "--------------------------------------------------------------------"
		count = count + 1

    """Calculate Completion Time"""
    global completionTime
    completionTime = pktsToObserve[count-1][0] - pktsToObserve[0][0]
    #print "completionTime : " + str(completionTime)
    #print "Total packets transmitted : " + str(count)
    return pktsToObserve

def retransmissionTime(pktsToObserve):
    """ Calculate Retransmission time """
    pktsArray = []
    retransmissionCount = 0
    for ts, pkt in pktsToObserve:
        if pkt.data.len == 1500 and pkt.data.data.sport == 7777	:
            for ts1, packet in pktsArray:
		retransmissionCount = retransmissionCount + 1
                if pkt.data.data.seq == packet.data.data.seq:
		    #print "Packets retransmitted : " + str(retransmissionCount)
                    return (ts - ts1)
            pktsArray.append((ts, pkt))
    return 0

def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	parser = argparse.ArgumentParser()
	parser.add_argument("pcapFile",
		help="Enter the name of pcap file to be analyzed : ",
		type=str)
	args = parser.parse_args()
	return args

if __name__ == "__main__":
    arguments = parseArguments()
    f = open(arguments.pcapFile)
    pcapReader = dpkt.pcap.Reader(f)
    pktsToObserve = filterPackets(pcapReader)
    retransmission_time = retransmissionTime(pktsToObserve)
    #print "-----------------------------------------------------------------"
    print(str(completionTime) + "\t" + str(retransmission_time))
    #print "-----------------------------------------------------------------"
                                                                                                                                                                                                                                                                                                                                                                      tcp_analysis.py~                                                                                    0000664 0001750 0001750 00000004231 12270152126 014207  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                import dpkt
import argparse

completionTime = 0
def filterPackets(pcapReader):
    """Filters the packets of the transmission being observed"""
    pktsToObserve = []
    count = 0;
    for ts, data in pcapReader:
        ether = dpkt.ethernet.Ethernet(data)
	#print ts
        ip = ether.data
        tcp = ip.data
        if type(tcp) == dpkt.tcp.TCP:
            if tcp.sport == 7777 or tcp.dport == 7777:
		pktsToObserve.append((ts,ether))
		#print "--------------------------------------------------------------------"
		#print pktsToObserve[count]
		#print "--------------------------------------------------------------------"
		count = count + 1

    """Calculate Completion Time"""
    global completionTime
    completionTime = pktsToObserve[count-1][0] - pktsToObserve[0][0]
    #print "completionTime : " + str(completionTime)
    #print "Total packets transmitted : " + str(count)
    return pktsToObserve

def retransmissionTime(pktsToObserve):
    """ Calculate Retransmission time """
    pktsArray = []
    retransmissionCount = 0
    for ts, pkt in pktsToObserve:
        if pkt.data.len == 1500 and pkt.data.data.sport == 7777	:
            for ts1, packet in pktsArray:
		retransmissionCount = retransmissionCount + 1
                if pkt.data.data.seq == packet.data.data.seq:
		    #print "Packets retransmitted : " + str(retransmissionCount)
                    return (ts - ts1)
            pktsArray.append((ts, pkt))
    return 0

def parseArguments():
	""" Function for adding and parsing the arguments passed as userinput in CLI """
	parser = argparse.ArgumentParser()
	parser.add_argument("pcapFile",
		help="Enter the name of pcap file to be analyzed : ",
		type=str)
	args = parser.parse_args()
	return args

if __name__ == "__main__":
    arguments = parseArguments()
    f = open(arguments.pcapFile)
    pcapReader = dpkt.pcap.Reader(f)
    pktsToObserve = filterPackets(pcapReader)
    retransmission_time = retransmissionTime(pktsToObserve)
    #print "-----------------------------------------------------------------"
    print(str(completionTime) + "\t" + str(retransmission_time))
    #print "-----------------------------------------------------------------"
                                                                                                                                                                                                                                                                                                                                                                       tcp_analysis_pylint                                                                                 0000664 0001750 0001750 00000014336 12270761700 014774  0                                                                                                    ustar   mininet                         mininet                                                                                                                                                                                                                ************* Module tcp_analysis
W:  8,0: Unnecessary semicolon
W: 16,0: Found indentation with tabs instead of spaces
W: 20,0: Found indentation with tabs instead of spaces
W: 36,0: Found indentation with tabs instead of spaces
C: 44,0: Line too long (81/80)
W: 44,0: Found indentation with tabs instead of spaces
W: 45,0: Found indentation with tabs instead of spaces
W: 46,0: Found indentation with tabs instead of spaces
W: 49,0: Found indentation with tabs instead of spaces
W: 50,0: Found indentation with tabs instead of spaces
C:  1,0: Missing docstring
C:  4,0: Invalid name "completionTime" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
W:  7,4:filterPackets: Redefining name 'pktsToObserve' from outer scope (line 56)
W:  5,18:filterPackets: Redefining name 'pcapReader' from outer scope (line 55)
C:  5,0:filterPackets: Invalid name "filterPackets" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C:  5,0:filterPackets: Invalid name "pcapReader" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C:  5,18:filterPackets: Invalid name "pcapReader" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:  7,4:filterPackets: Invalid name "pktsToObserve" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C:  9,8:filterPackets: Invalid name "ts" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 12,8:filterPackets: Invalid name "ip" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
E: 15,15:filterPackets: Instance of 'str' has no 'sport' member (but some types could not be inferred)
E: 15,36:filterPackets: Instance of 'str' has no 'dport' member (but some types could not be inferred)
W: 22,4:filterPackets: String statement has no effect
W: 23,4:filterPackets: Using the global statement
W: 29,23:retransmissionTime: Redefining name 'pktsToObserve' from outer scope (line 56)
C: 29,0:retransmissionTime: Invalid name "retransmissionTime" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 29,0:retransmissionTime: Invalid name "pktsToObserve" for type argument (should match [a-z_][a-z0-9_]{2,30}$)
C: 29,23:retransmissionTime: Invalid name "pktsToObserve" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 31,4:retransmissionTime: Invalid name "pktsArray" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 32,4:retransmissionTime: Invalid name "retransmissionCount" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 33,8:retransmissionTime: Invalid name "ts" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 36,2:retransmissionTime: Invalid name "retransmissionCount" for type variable (should match [a-z_][a-z0-9_]{2,30}$)
C: 43,0:parseArguments: Invalid name "parseArguments" for type function (should match [a-z_][a-z0-9_]{2,30}$)
C: 53,4: Invalid name "arguments" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 54,4: Invalid name "f" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 55,4: Invalid name "pcapReader" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 56,4: Invalid name "pktsToObserve" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)
C: 57,4: Invalid name "retransmission_time" for type constant (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


Report
======
42 statements analysed.

Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |=          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |22     |23       |-1.00      |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |=          |
+-----------+-------+---------+-----------+
|warning    |14     |14       |=          |
+-----------+-------+---------+-----------+
|error      |2      |2        |=          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+
|C0103      |20          |
+-----------+------------+
|W0312      |8           |
+-----------+------------+
|W0621      |3           |
+-----------+------------+
|E1103      |2           |
+-----------+------------+
|W0603      |1           |
+-----------+------------+
|W0301      |1           |
+-----------+------------+
|W0105      |1           |
+-----------+------------+
|C0301      |1           |
+-----------+------------+
|C0111      |1           |
+-----------+------------+



Global evaluation
-----------------
Your code has been rated at -0.95/10 (previous run: -1.19/10)

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |44     |78.57 |44       |=          |
+----------+-------+------+---------+-----------+
|docstring |3      |5.36  |3        |=          |
+----------+-------+------+---------+-----------+
|comment   |3      |5.36  |3        |=          |
+----------+-------+------+---------+-----------+
|empty     |6      |10.71 |6        |=          |
+----------+-------+------+---------+-----------+



Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |0.00        |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |0          |=          |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |3      |3          |=          |100.00      |100.00   |
+---------+-------+-----------+-----------+------------+---------+



External dependencies
---------------------
::

    dpkt (tcp_analysis)



                                                                                                                                                                                                                                                                                                  tcpDump.pcap                                                                                        0000644 0000000 0000000 00000107656 12270533637 012064  0                                                                                                    ustar   root                            root                                                                                                                                                                                                                   �ò�          D      v��R� D   Z   33   �����`    $ ��      쨷������             :    � @�  v��R�_ *   *   ���������   ���
       
 v��R0� *   *   ����T��H   �T��H
 ���
 v��R�� D   J   �T��H��� E  <��@ ?�

 
 �aG�p�    �r0  �
 �b  v��R%K	 D   J   ����T��H E  <  @ @#�
 
 a��-udG�pӠq 0  �
 �� v��R7
 B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-ue� :(  
 �� ��v��R߆
 D   �  ����T��H E ܃�@ @�)
 
 a��-ueG�pӀ 9�  
 �� ��  v��R��
 D   �  ����T��H E ܃�@ @�(
 
 a��-{G�pӀ 9�  
 �� ��  v��R��
 D   �  ����T��H E ܃�@ @�'
 
 a��-��G�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�&
 
 a��-�]G�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�%
 
 a��-�G�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�$
 
 a��-��G�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�#
 
 a��-�UG�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�"
 
 a��-��G�pӀ 9�  
 �� ��  v��R�
 D   �  ����T��H E ܃�@ @�!
 
 a��-��G�pӀ 9�  
 �� ��  v��R޲
 D   �  ����T��H E ܃�@ @� 
 
 a��-�MG�pӀ 9�  
 �� ��  v��Rwr B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-{� ?(  
 �� ��v��R�r B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-��� E(  
 �� ��v��R.s B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�]� J(  
 �� ��v��R;s B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�� P(  
 �� ��v��R=s B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-��� V(  
 �� ��v��R?s B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�U� Y(  
 �� ��v��RAs B   B   �T��H��� E  4��@ ?�

 
 �aG�pӑ-��� Y(  
 �� ��v��R�s B   B   �T��H��� E  4��@ ?�	
 
 �aG�pӑ-��� Y(  
 �� ��v��R�s B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�M� Y(  
 �� ��v��R[� B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-��� Y(  
 �� ��v��R�� D   �  ����T��H E ܃�@ @�
 
 a��-��G�pӀ 9�  
 �� ��  v��R�w B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-��� Y(  
 �� ��v��Re D   �  ����T��H E ܃�@ @�
 
 a��-��G�pӀ 9�  
 �� ��  w��R�  B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�E� Y(  
 �� ��w��R��  D   �  ����T��H E ܃�@ @�
 
 a��-�EG�pӀ 9�  
 �� ��  w��R�� B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�� Y(  
 �� ��w��R#� D   �  ����T��H E ܃�@ @�
 
 a��-��G�pӀ 9�  
 �� ��  w��R�� B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-ĕ� Y(  
 � ��w��R<� D   �  ����T��H E ܃�@ @�
 
 a��-ĕG�pӀ 9�  
 �� ��  w��R� B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�=� Y(  
 �9 ��w��R`� D   �  ����T��H E ܄ @ @�
 
 a��-�=G�pӀ 9�  
 �� ��  w��Rs B   B   �T��H��� E  4��@ ?�
 
 �aG�pӑ-�� Y(  
 �W ��w��R}` D   �  ����T��H E ܄@ @�
 
 a��-��G�pӀ 9�  
 �� ��  w��R��	 B   B   �T��H��� E  4��@ ?� 
 
 �aG�pӑ-Ս� Y(  
 � ��w��R�9
 D   �  ����T��H E ܄@ @�
 
 a��-ՍG�pӀ 9�  
 �� ��  w��R� D   �  ����T��H E ܄@ @�
 
 a��-�5G�pӀ 9�  
 �� ��  w��R�N B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ-�5� Y(  
 �� ��w��R�� D   �  ����T��H E ܄@ @�
 
 a��-��G�pӀ 9�  
 �� ��  w��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ-慀 Y(  
 �� ��x��R��  D   �  ����T��H E ܄@ @�
 
 a��-�G�pӀ 9�  
 �� ��  x��R�[ D   �  ����T��H E ܄@ @�
 
 a��-�-G�pӀ 9�  
 �� ��  x��R}G B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ-�Հ Y(  
 � ��x��R�4 D   �  ����T��H E ܄@ @�
 
 a��-��G�pӀ 9�  
 �� ��  x��R& D   �  ����T��H E ܄@ @�
 
 a��-�}G�pӀ 9�  
 �� ��  x��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ-�%� Y(  
 �I ��x��R>� D   �  ����T��H E ܄	@ @�
 
 a��-�%G�pӀ 9�  
 �� ��  x��R]�	 D   �  ����T��H E ܄
@ @�
 
 a��.�G�pӀ 9�  
 �� ��  x��R��
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.u� Y(  
 �� ��x��R� D   �  ����T��H E ܄@ @�
 
 a��.uG�pӀ 9�  
 �� ��  x��R�r D   �  ����T��H E ܄@ @�
 
 a��.G�pӀ 9�  
 �� ��  x��RD^ B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.ŀ Y(  
 �� ��y��R�	  D   �  ����T��H E ܄@ @�
 
 a��.�G�pӀ 9�  
 �� ��  y��R�� D   �  ����T��H E ܄@ @�
 
 a��.mG�pӀ 9�  
 �� ��  y��RG� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.� Y(  
 �� ��y��R�� D   �  ����T��H E ܄@ @�
 
 a��.G�pӀ 9�  
 �� ��  y��R!_ D   F   33   �����`    :���      쨷������             � �q    �y��R� D   �  ����T��H E ܄@ @�

 
 a��.$�G�pӀ 9�  
 �� ��  y��R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.*e� Y(  
 �; ��y��Rn D   �  ����T��H E ܄@ @�	
 
 a��.*eG�pӀ 9�  
 �� ��  y��RG	 D   �  ����T��H E ܄@ @�
 
 a��.0G�pӀ 9�  
 �� ��  y��R�H
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.5�� Y(  
 �y ��y��R<  D   �  ����T��H E ܄@ @�
 
 a��.5�G�pӀ 9�  
 �$ �  y��Re� D   �  ����T��H E ܄@ @�
 
 a��.;]G�pӀ 9�  
 �$ �  y��R�	 D   Z   33   �����`    $ ��      쨷������             :    � >�  y��R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.A� ^(  
 �� �$y��R�� D   �  ����T��H E ܄@ @�
 
 a��.AG�pӀ 9�  
 �$ �  z��Rԭ  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.F�� a(  
 �� �$z��R^i D   �  ����T��H E ܄@ @�
 
 a��.F�G�pӀ 9�  
 �$ �  z��RP B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.LU� a(  
 �� �$z��RwB D   �  ����T��H E ܄@ @�
 
 a��.LUG�pӀ 9�  
 �a �W  z��R� D   �  ����T��H E ܄@ @�
 
 a��.Q�G�pӀ 9�  
 �a �W  z��R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.Q�� a(  
 �' �az��R�� D   �  ����T��H E ܄@ @�
 
 a��.W�G�pӀ 9�  
 �a �W  z��R_ B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.]M� a(  
 �O �az��R�� D   �  ����T��H E ܄@ @� 
 
 a��.]MG�pӀ 9�  
 �a �W  z��R��
 D   �  ����T��H E ܄@ @��
 
 a��.b�G�pӀ 9�  
 �� ��  z��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.h�� a(  
 �� �az��R� D   �  ����T��H E ܄@ @��
 
 a��.h�G�pӀ 9�  
 �� ��  z��R?Y D   �  ����T��H E ܄@ @��
 
 a��.nEG�pӀ 9�  
 �� ��  {��R�4  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.s� a(  
 �� ��{��R�  D   �  ����T��H E ܄@ @��
 
 a��.s�G�pӀ 9�  
 �� ��  {��R=� D   �  ����T��H E ܄@ @��
 
 a��.y�G�pӀ 9�  
 � �  {��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.=� a(  
 � ��{��R`� D   �  ����T��H E ܄ @ @��
 
 a��.=G�pӀ 9�  
 � �  {��R~{ D   �  ����T��H E ܄!@ @��
 
 a��.��G�pӀ 9�  
 � �  {��R(� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.��� a(  
 �A �{��R�T D   �  ����T��H E ܄"@ @��
 
 a��.��G�pӀ 9�  
 � �  {��R�-
 D   �  ����T��H E ܄#@ @��
 
 a��.�5G�pӀ 9�  
 � �  {��RuX B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�݀ a(  
 � �{��R� D   �  ����T��H E ܄$@ @��
 
 a��.��G�pӀ 9�  
 � �  {��R�� D   �  ����T��H E ܄%@ @��
 
 a��.��G�pӀ 9�  
 �S �I  {��R�
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�-� a(  
 �� �|��R�v  D   �  ����T��H E ܄&@ @��
 
 a��.�-G�pӀ 9�  
 �S �I  |��RP D   �  ����T��H E ܄'@ @��
 
 a��.��G�pӀ 9�  
 �� ��  |��R�z B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�}� a(  
 �� �S|��R) D   �  ����T��H E ܄(@ @��
 
 a��.�}G�pӀ 9�  
 �� ��  |��R> D   �  ����T��H E ܄)@ @��
 
 a��.�%G�pӀ 9�  
 �� ��  |��R$- B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�̀ a(  
 �4 ��|��Rd� D   �  ����T��H E ܄*@ @��
 
 a��.��G�pӀ 9�  
 �� ��  |��Ry� D   Z   33   �T��H��`    $ ��      �T����H�             :    � �4  |��Rk D   F   33   �T��H��`    :���      �T����H�             � '�    �T�|��R��	 D   �  ����T��H E ܄+@ @��
 
 a��.�uG�pӀ 9�  
 �E �;  |��RT�
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�� a(  
 �q ��|��R�� D   �  ����T��H E ܄,@ @��
 
 a��.�G�pӀ 9�  
 �E �;  |��RØ D   �  ����T��H E ܄-@ @��
 
 a��.��G�pӀ 9�  
 �E �;  |��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�m� a(  
 �� �E}��R�/  D   �  ����T��H E ܄.@ @��
 
 a��.�mG�pӀ 9�  
 �E �;  }��R� D   �  ����T��H E ܄/@ @��
 
 a��.�G�pӀ 9�  
 �� ��  }��R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.ٽ� a(  
 �� �E}��R�� D   �  ����T��H E ܄0@ @��
 
 a��.ٽG�pӀ 9�  
 �� ��  }��R�~ D   F   33   �����`    :���      쨷������             � �q    �}��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�e� f(  
 �
 ��}��R� D   �  ����T��H E ܄1@ @��
 
 a��.�eG�pӀ 9�  
 �� ��  }��R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�� l(  
 �( ��}��R(� D   �  ����T��H E ܄2@ @��
 
 a��.�G�pӀ 9�  
 �� ��  }��R
� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.굀 r(  
 �G ��}��R=m	 D   �  ����T��H E ܄3@ @��
 
 a��.�G�pӀ 9�  
 � ��  }��R�
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�]� w(  
 �f �}��RiF D   �  ����T��H E ܄4@ @��
 
 a��.�]G�pӀ 9�  
 � ��  }��R.q B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.�� }(  
 �� �}��R� D   �  ����T��H E ܄5@ @��
 
 a��.�G�pӀ 9�  
 � ��  }��RxJ B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ.��� �(  
 �� �}��R�� D   �  ����T��H E ܄6@ @��
 
 a��.��G�pӀ 9�  
 �Y �O  ~��R��  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/U� �(  
 �� �Y~��R�� D   �  ����T��H E ܄7@ @��
 
 a��/UG�pӀ 9�  
 �Y �O  ~��RP� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 �� �Y~��R�h D   �  ����T��H E ܄8@ @��
 
 a��/�G�pӀ 9�  
 �Y �O  ~��Rn� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 �� �Y~��R�A D   �  ����T��H E ܄9@ @��
 
 a��/�G�pӀ 9�  
 �� ��  ~��R�l B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/M� �(  
 � ��~��R� D   �  ����T��H E ܄:@ @��
 
 a��/MG�pӀ 9�  
 �� ��  ~��R�E B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 �: ��~��R� D   �  ����T��H E ܄;@ @��
 
 a��/�G�pӀ 9�  
 �� ��  ~��R��
 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 �c ��~��R�
 D   �  ����T��H E ܄<@ @��
 
 a��/�G�pӀ 9�  
 �� ��  ~��RJ� D   �  ����T��H E ܄=@ @��
 
 a��/#EG�pӀ 9�  
 �� ��  ~��R�) B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/#E� �(  
 �� ��~��R` D   �  ����T��H E ܄>@ @��
 
 a��/(�G�pӀ 9�  
 �K �A  ��R�g  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/.�� �(  
 �� ����RF D   �  ����T��H E ܄?@ @��
 
 a��/.�G�pӀ 9�  
 �K �A  ��Rj� D   �  ����T��H E ܄@@ @��
 
 a��/4=G�pӀ 9�  
 �K �A  ��R: B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/9� �(  
 �� �K��R�� D   �  ����T��H E ܄A@ @��
 
 a��/9�G�pӀ 9�  
 �K �A  ��R�� D   �  ����T��H E ܄B@ @��
 
 a��/?�G�pӀ 9�  
 �K �A  ��Rm� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/E5� �(  
 �- �K��R�z D   �  ����T��H E ܄C@ @��
 
 a��/E5G�pӀ 9�  
 �� �  ��R�S
 D   �  ����T��H E ܄D@ @��
 
 a��/J�G�pӀ 9�  
 �� �  ��R�~ B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/P�� �(  
 �i ����R�, D   �  ����T��H E ܄E@ @��
 
 a��/P�G�pӀ 9�  
 � ��  ��R' D   �  ����T��H E ܄F@ @��
 
 a��/V-G�pӀ 9�  
 � ��  ��R�0 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/[Հ �(  
 �� ����R �  D   �  ����T��H E ܄G@ @��
 
 a��/[�G�pӀ 9�  
 � ��  ���R#v D   �  ����T��H E ܄H@ @��
 
 a��/a}G�pӀ 9�  
 � ��  ���R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/g%� �(  
 �� ����RFO D   �  ����T��H E ܄I@ @��
 
 a��/g%G�pӀ 9�  
 � ��  ���Rd( D   �  ����T��H E ܄J@ @��
 
 a��/l�G�pӀ 9�  
 �{ �q  ���R6S B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/ru� �(  
   ����Ry D   �  ����T��H E ܄K@ @��
 
 a��/ruG�pӀ 9�  
 �{ �q  ���R��	 D   �  ����T��H E ܄L@ @��
 
 a��/xG�pӀ 9�  
 �{ �q  ���R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/}ŀ �(  
  [ �{���Rų D   �  ����T��H E ܄M@ @��
 
 a��/}�G�pӀ 9�  
 �{ �q  ���R� D   �  ����T��H E ܄N@ @��
 
 a��/�mG�pӀ 9�  
 �� ��  ���R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
  � �{���R�#  D   �  ����T��H E ܄O@ @��
 
 a��/�G�pӀ 9�  
 �� ��  ���R�� D   �  ����T��H E ܄P@ @��
 
 a��/��G�pӀ 9�  
 �� ��  ���R�' B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�e� �(  
  � �����R� D   �  ����T��H E ܄Q@ @��
 
 a��/�eG�pӀ 9�  
 �� ��  ���R�  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
  � �����R� D   �  ����T��H E ܄R@ @��
 
 a��/�G�pӀ 9�  
 � �
  ���R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/��� �(  
  ����RH� D   �  ����T��H E ܄S@ @��
 
 a��/��G�pӀ 9�  
 � �
  ���R� D   F   33   �T��H��`    :���      �T����H�             � '�    �TÁ��R� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�]� �(  
 / ����R?w	 D   �  ����T��H E ܄T@ @��
 
 a��/�]G�pӀ 9�  
 �3 �(  ���R�% B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 X �3���R^P D   �  ����T��H E ܄U@ @��
 
 a��/�G�pӀ 9�  
 �3 �(  ���R�) D   �  ����T��H E ܄V@ @��
 
 a��/��G�pӀ 9�  
 �3 �(  ���R�E D   Z   33   �T��H��`    $ ��      �T����H�             :    � �4  ���Rϖ B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/��� �(  
 � �3���R� D   �  ����T��H E ܄W@ @��
 
 a��/�UG�pӀ 9�  
 �p �f  ���RF�  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/��� �(  
 � �3���R�� D   �  ����T��H E ܄X@ @��
 
 a��/��G�pӀ 9�  
 �p �f  ���RÎ D   �  ����T��H E ܄Y@ @��
 
 a��/��G�pӀ 9�  
 �p �f  ���R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�M� �(  
 � �p���R�g D   �  ����T��H E ܄Z@ @��
 
 a��/�MG�pӀ 9�  
 �� ��  ���RA D   �  ����T��H E ܄[@ @��
 
 a��/��G�pӀ 9�  
 �� ��  ���R�9 B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/ҝ� �(  
 " �����R"	 D   �  ����T��H E ܄\@ @��
 
 a��/ҝG�pӀ 9�  
 �� ��  ���RD�
 D   �  ����T��H E ܄]@ @��
 
 a��/�EG�pӀ 9�  
 �� ��  ���R
� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�� �(  
 ^ �����Re� D   �  ����T��H E ܄^@ @��
 
 a��/��G�pӀ 9�  
 �� ��  ���R�� D   �  ����T��H E ܄_@ @��
 
 a��/�G�pӀ 9�  
 �� ��  ���R8\  B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�=� �(  
 � �ꃷ�Rc< D   �  ����T��H E ܄`@ @��
 
 a��/�=G�pӀ 9�  
 �& �  ���R� D   �  ����T��H E ܄a@ @��
 
 a��/��G�pӀ 9�  
 �& �  ���RK B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/� �(  
 � �&���R�� D   �  ����T��H E ܄b@ @��
 
 a��/�G�pӀ 9�  
 �& �  ���R�� D   �  ����T��H E ܄c@ @��
 
 a��/�5G�pӀ 9�  
 �m �c  ���R�� B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ/�݀ �(  
  �&���R� D   �  ����T��H E ܄d@ @��
 
 a��/��G�pӀ 9�  
 �m �c  ���Rz
 D   �  ����T��H E ܄e@ @��
 
 a��0�G�pӀ 9�  
 �m �c  ���R�r B   B   �T��H��� E  4��@ ?��
 
 �aG�pӑ0-� �(  
 P �m���R S D   �  ����T��H E ܄f@ @��
 
 a��0-G�pӀ 9�  
 �� ��  ���R>, D   �  ����T��H E ܄g@ @��
 
 a��0�G�pӀ 9�  
 �� ��  ���R&% B   B   �T��H��� E  4� @ ?��
 
 �aG�pӑ0}� �(  
 � �����R-�  D   �  ����T��H E ܄h@ @��
 
 a��0}G�pӀ 9�  
 �� ��  ���RN� D   �  ����T��H E ܄i@ @��
 
 a��0%G�pӀ 9�  
 �� ��  ���R*� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0!̀ �(  
 � �����Rdu D   �  ����T��H E ܄j@ @��
 
 a��0!�G�pӀ 9�  
 �7 �-  ���R�N D   �  ����T��H E ܄k@ @��
 
 a��0'uG�pӀ 9�  
 �7 �-  ���RYG B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0-� �(  
  �7���R�' D   �  ����T��H E ܄l@ @��
 
 a��0-G�pӀ 9�  
 �7 �-  ���R� 
 D   �  ����T��H E ܄m@ @��
 
 a��02�G�pӀ 9�  
 �7 �-  ���R��
 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ08m� �(  
 C �7���R�� D   �  ����T��H E ܄n@ @��
 
 a��08mG�pӀ 9�  
 �7 �-  ���R� D   �  ����T��H E ܄o@ @��
 
 a��0>G�pӀ 9�  
 �� ��  ���R� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0C�� �(  
  �7���R�I  D   �  ����T��H E ܄p@ @��
 
 a��0C�G�pӀ 9�  
 �� ��  ���R# D   �  ����T��H E ܄q@ @��
 
 a��0IeG�pӀ 9�  
 �� ��  ���R� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0O� �(  
 � �����R"� D   �  ����T��H E ܄r@ @��
 
 a��0OG�pӀ 9�  
 �� ��  ���RH� D   �  ����T��H E ܄s@ @��
 
 a��0T�G�pӀ 9�  
 �� ��  ���R� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0Z]� �(  
 � �����R]� D   �  ����T��H E ܄t@ @��
 
 a��0Z]G�pӀ 9�  
  )    ���R��	 D   �  ����T��H E ܄u@ @��
 
 a��0`G�pӀ 9�  
  )    ���RK�
 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0e�� �(  
 5  )���R�` D   �  ����T��H E ܄v@ @��
 
 a��0e�G�pӀ 9�  
  )    ���R�9 D   �  ����T��H E ܄w@ @��
 
 a��0kUG�pӀ 9�  
  )    ���R�2 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0p�� �(  
 q  )���R� D   �  ����T��H E ܄x@ @��
 
 a��0p�G�pӀ 9�  
  )    ���R�� D   �  ����T��H E ܄y@ @��
 
 a��0v�G�pӀ 9�  
  �  �  ���R�� B   B   �T��H��� E  4�	@ ?��
 
 �aG�pӑ0|M� �(  
 �  )���R� D   �  ����T��H E ܄z@ @��
 
 a��0|MG�pӀ 9�  
  �  �  ���R\ D   �  ����T��H E ܄{@ @��
 
 a��0��G�pӀ 9�  
  �  �  ���R�T B   B   �T��H��� E  4�
@ ?��
 
 �aG�pӑ0��� �(  
 �  ����R5 D   �  ����T��H E ܄|@ @��
 
 a��0��G�pӀ 9�  
  �  �  ���R�- B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�E� �(  
 	  ����RA	 D   �  ����T��H E ܄}@ @��
 
 a��0�EG�pӀ 9�  
  �  �  ���R
 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�� �(  
 '  ����Rd�
 D   �  ����T��H E ܄~@ @��
 
 a��0��G�pӀ 9�  
  �  �  ���R4� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0��� �(  
 E  ����R�� D   �  ����T��H E ܄@ @��
 
 a��0��G�pӀ 9�  
  �  �  ���R?� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�=� �(  
 d  ����R�� D   �  ����T��H E ܄�@ @��
 
 a��0�=G�pӀ 9�  
  �  �  ���R.P  B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�� �(  
 �  ����R�0 D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
  �  �  ���R[) B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0��� �(  
 �  ����R�	 D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 9 /  ���Rt B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�5� �(  
 � 9���R�� D   �  ����T��H E ܄�@ @��
 
 a��0�5G�pӀ 9�  
 9 /  ���R�� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�݀ �(  
 � 9���R� D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 9 /  ���R�� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0��� �(  
 � 9���R� D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 � �  ���R܍	 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�-� �(  
  ����Rn
 D   �  ����T��H E ܄�@ @��
 
 a��0�-G�pӀ 9�  
 � �  ���R�f B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�Հ �(  
 8 ����RFG D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 � �  ���R@ B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�}� �(  
 V ����Rh  D   �  ����T��H E ܄�@ @��
 
 a��0�}G�pӀ 9�  
 � �  ���R�g  B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�%� �(  
 ~ �RC�  D   �  ����T��H E ܄�@ @��
 
 a��0�%G�pӀ 9�  
 � �  ���Ra� D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 � �  ���Rs� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�̀ �(  
 � �R�i D   �  ����T��H E ܄�@ @��
 
 a��0�uG�pӀ 9�  
 � �  ���RXb B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�� �(  
 � �R�B D   �  ����T��H E ܄�@ @��
 
 a��0�G�pӀ 9�  
 � �  ���R� D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 h ^  ���R�	 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0�m� �(  
  �R��	 D   �  ����T��H E ܄�@ @��
 
 a��0�mG�pӀ 9�  
 h ^  ���R� D   �  ����T��H E ܄�@ @��
 
 a��0�G�pӀ 9�  
 h ^  ���R�� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ0��� �(  
 H h���R� D   �  ����T��H E ܄�@ @��
 
 a��0��G�pӀ 9�  
 h ^  ���R>  D   �  ����T��H E ܄�@ @��
 
 a��0�eG�pӀ 9�  
 h ^  ���R�6 B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ1� �(  
 � h���R! D   �  ����T��H E ܄�@ @��
 
 a��1G�pӀ 9�  
 � �  ���R@� D   �  ����T��H E ܄�@ @��
 
 a��1	�G�pӀ 9�  
 � �  ���R� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ1]� �(  
 � ቷ�R`� D   �  ����T��H E ܄�@ @��
 
 a��1]G�pӀ 9�  
 � �  ���R�� D   �  ����T��H E ܄�@ @��
 
 a��1G�pӀ 9�  
 � �  ���RX� B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ1�� �(  
 � ቷ�R�{	 D   �  ����T��H E ܄�@ @��
 
 a��1�G�pӀ 9�  
    ���R�T D   �  ����T��H E ܄�@ @��
 
 a��1 UG�pӀ 9�  
    ���R�M B   B   �T��H��� E  4�@ ?��
 
 �aG�pӑ1%�� �(  
 	: ���R�- D   �  ����T��H E ܄�@ @��
 
 a��1%�G�pӀ 9�  
    ���R D   �  ����T��H E ܄�@ @��
 
 a��1+�G�pӀ 9�  
    ���R��  B   B   �T��H��� E  4� @ ?��
 
 �aG�pӑ11M� �(  
 	w ���R� D   �  ����T��H E ܄�@ @��
 
 a��11MG�pӀ 9�  
 � �  ���Rw D   �  ����T��H E ܄�@ @�
 
 a��16�G�pӀ 9�  
 � �  ���R�o B   B   �T��H��� E  4�!@ ?��
 
 �aG�pӑ1<�� �(  
 	� ����R"P D   �  ����T��H E ܄�@ @�~
 
 a��1<�G�pӀ 9�  
 � �  ���R0) D   �  ����T��H E ܄�@ @�}
 
 a��1BEG�pӀ 9�  
 � �  ���R" B   B   �T��H��� E  4�"@ ?��
 
 �aG�pӑ1G� �(  
 	� ����R^	 D   �  ����T��H E ܄�@ @�|
 
 a��1G�G�pӀ 9�  
 � �  ���R��
 D   �  ����T��H E ܄�@ @�{
 
 a��1M�G�pӀ 9�  
    ���RK� B   B   �T��H��� E  4�#@ ?��
 
 �aG�pӑ1S=� �(  
 
- ����R�� D   �  ����T��H E ܄�@ @�z
 
 a��1S=G�pӀ 9�  
    ���R�� D   �  ����T��H E ܄�@ @�y
 
 a��1X�G�pӀ 9�  
    ���RUD  B   B   �T��H��� E  4�$@ ?��
 
 �aG�pӑ1^�� �(  
 
i ���R�$ D   �  ����T��H E ܄�@ @�x
 
 a��1^�G�pӀ 9�  
    ���R�� D   �  ����T��H E ܄�@ @�w
 
 a��1d5G�pӀ 9�  
    ���R� B   B   �T��H��� E  4�%@ ?��
 
 �aG�pӑ1i݀ �(  
 
� ���R�� D   �  ����T��H E ܄�@ @�v
 
 a��1i�G�pӀ 9�  
 �   ���R�� D   �  ����T��H E ܄�@ @�u
 
 a��1o�G�pӀ 9�  
 �   ���RҨ B   B   �T��H��� E  4�&@ ?��
 
 �aG�pӑ1u-� �(  
 
� ����R"� D   �  ����T��H E ܄�@ @�t
 
 a��1u-G�pӀ 9�  
 �   ���R=b
 D   �  ����T��H E ܄�@ @�s
 
 a��1z�G�pӀ 9�  
 �   ���R�Z B   B   �T��H��� E  4�'@ ?��
 
 �aG�pӑ1�}� �(  
  ����R\; D   �  ����T��H E ܄�@ @�r
 
 a��1�}G�pӀ 9�  
 �   ���Rz D   �  ����T��H E ܄�@ @�q
 
 a��1�%G�pӀ 9�  
  �  ���R? B   B   �T��H��� E  4�(@ ?��
 
 �aG�pӑ1�̀ �(  
 [ ����R]�  D   �  ����T��H E ܄�@ @�p
 
 a��1��G�pӀ 9�  
  �  ���R�� D   �  ����T��H E ܄�@ @�o
 
 a��1�uG�pӀ 9�  
  �  ���RS} B   B   �T��H��� E  4�)@ ?��
 
 �aG�pӑ1�� �(  
 � ���R�] D   �  ����T��H E ܄�@ @�n
 
 a��1�G�pӀ 9�  
  �  ���R�6 D   �  ����T��H E ܄�@ @�m
 
 a��1��G�pӀ 9�  
  �  ���R�/ B   B   �T��H��� E  4�*@ ?��
 
 �aG�pӑ1�m� �(  
 � ���R� D   �  ����T��H E ܄�@ @�l
 
 a��1�mG�pӀ 9�  
 | q  ���R��	 D   �  ����T��H E ܄�@ @�k
 
 a��1�G�pӀ 9�  
 | q  ���R��
 B   B   �T��H��� E  4�+@ ?��
 
 �aG�pӑ1��� �(  
  |���R� D   �  ����T��H E ܄�@ @�j
 
 a��1��G�pӀ 9�  
 | q  ���RQ� D   �  ����T��H E ܄�@ @�i
 
 a��1�eG�pӀ 9�  
 | q  ���R� B   B   �T��H��� E  4�,@ ?��
 
 �aG�pӑ1�� �(  
 N |���R'2  D   �  ����T��H E ܄�@ @�h
 
 a��1�G�pӀ 9�  
 � �  ���RA D   �  ����T��H E ܄�@ @�g
 
 a��1��G�pӀ 9�  
 � �  ���R� B   B   �T��H��� E  4�-@ ?��
 
 �aG�pӑ1�]� �(  
 � ����R\� D   �  ����T��H E ܄�@ @�f
 
 a��1�]G�pӀ 9�  
 � �  ���R�� D   �  ����T��H E ܄�@ @�e
 
 a��1�G�pӀ 9�  
  	  ���RJ� B   B   �T��H��� E  4�.@ ?��
 
 �aG�pӑ1ϭ� �(  
 � ����R�� D   �  ����T��H E ܄�@ @�d
 
 a��1ϭG�pӀ 9�  
  	  ���RU� B   B   �T��H��� E  4�/@ ?��
 
 �aG�pӑ1�U�(  
 � ���R�o	 D   �  ����T��H E ܄�@ @�c
 
 a��1�UG�pӀ 9�  
  	  ���Rqh
 B   B   �T��H��� E  4�0@ ?��
 
 �aG�pӑ1���
(  
  ���R�H D   �  ����T��H E ܄�@ @�b
 
 a��1��G�pӀ 9�  
  	  ���R�A B   B   �T��H��� E  4�1@ ?��
 
 �aG�pӑ1ी(  
 " ���R�! D   �  ����T��H E ܄�@ @�a
 
 a��1�G�pӀ 9�  
 O E  ���R� B   B   �T��H��� E  4�2@ ?��
 
 �aG�pӑ1�M�(  
 @ O���R� D   �  ����T��H E ܄�@ @�`
 
 a��1�MG�pӀ 9�  
 O E  ���R��  B   B   �T��H��� E  4�3@ ?��
 
 �aG�pӑ1���(  
 ^ O���R�� D   �  ����T��H E ܄�@ @�_
 
 a��1��G�pӀ 9�  
 O E  ���RÊ B   B   �T��H��� E  4�4@ ?��
 
 �aG�pӑ1�!(  
 } O���R k D   �  ����T��H E ܄�@ @�^
 
 a��1�G�pӀ 9�  
 � �  ���R�c B   B   �T��H��� E  4�5@ ?��
 
 �aG�pӑ1�E�'(  
 � ����RED D   �  ����T��H E ܄�@ @�]
 
 a��1�EG�pӀ 9�  
 � �  ���R�< B   B   �T��H��� E  4�6@ ?��
 
 �aG�pӑ1��,(  
 � ����Rd D   �  ����T��H E ܄�@ @�\
 
 a��1��G�pӀ 9�  
 � �  ���R B   B   �T��H��� E  4�7@ ?��
 
 �aG�pӑ2��2(  
 � ����R}� D   �  ����T��H E ܄�@ @�[
 
 a��2�G�pӀ 9�  
 � �  ���R8�	 B   B   �T��H��� E  4�8@ ?��
 
 �aG�pӑ2=�8(  
 � Ɏ��R��
 D   �  ����T��H E ܄�@ @�Z
 
 a��2=G�pӀ 9�  
 � �  ���R^� B   B   �T��H��� E  4�9@ ?��
 
 �aG�pӑ2�=(  
  Ɏ��R�� D   �  ����T��H E ܄�@ @�Y
 
 a��2�G�pӀ 9�  
 � �  ���R~� B   B   �T��H��� E  4�:@ ?��
 
 �aG�pӑ2��C(  
 2 Ɏ��R߁ D   �  ����T��H E ܄�@ @�X
 
 a��2�G�pӀ 9�  
  �  ���R|�  B   B   �T��H��� E  4�;@ ?��
 
 �aG�pӑ25�C(  
 Z ���R� D   �  ����T��H E ܄�@ @�W
 
 a��25G�pӀ 9�  
  �  ���R�� D   �  ����T��H E ܄�@ @�V
 
 a��2�G�pӀ 9�  
  �  ���REF B   B   �T��H��� E  4�<@ ?��
 
 �aG�pӑ2݀C(  
 � ���R�� D   �  ����T��H E ܄�@ @�U
 
 a��2$�G�pӀ 9�  
 B 8  ���R�� B   B   �T��H��� E  4�=@ ?��
 
 �aG�pӑ2*-�C(  
 � ���R'� D   �  ����T��H E ܄�@ @�T
 
 a��2*-G�pӀ 9�  
 B 8  ���R<} D   �  ����T��H E ܄�@ @�S
 
 a��2/�G�pӀ 9�  
 B 8  ���R�u	 B   B   �T��H��� E  4�>@ ?��
 
 �aG�pӑ25}�C(  
 � B���RbV
 D   �  ����T��H E ܄�@ @�R
 
 a��25}G�pӀ 9�  
 � ~  ���R{/ D   �  ����T��H E ܄�@ @�Q
 
 a��2;%G�pӀ 9�  
 � ~  ���R1( B   B   �T��H��� E  4�?@ ?��
 
 �aG�pӑ2@̀C(  
 $ ����R� D   �  ����T��H E ܄�@ @�P
 
 a��2@�G�pӀ 9�  
 � ~  ���R��  D   �  ����T��H E ܄�@ @�O
 
 a��2FuG�pӀ 9�  
 � �  ���R0� B   B   �T��H��� E  4�@@ ?��
 
 �aG�pӑ2L�C(  
 a ����R�x D   �  ����T��H E ܄�@ @�N
 
 a��2LG�pӀ 9�  
 � �  ���R�Q D   �  ����T��H E ܄�@ @�M
 
 a��2Q�G�pӀ 9�  
 � �  ���R�J B   B   �T��H��� E  4�A@ ?��
 
 �aG�pӑ2Wm�C(  
 � ِ��R�* D   �  ����T��H E ܄�@ @�L
 
 a��2WmG�pӀ 9�  
 � �  ���R D   �  ����T��H E ܄�@ @�K
 
 a��2]G�pӀ 9�  
    ���R�� B   B   �T��H��� E  4�B@ ?��
 
 �aG�pӑ2b��C(  
 � ِ��R�	 D   �  ����T��H E ܄�@ @�J
 
 a��2b�G�pӀ 9�  
    ���RG� D   �  ����T��H E ܄�@ @�I
 
 a��2heG�pӀ 9�  
    ���R� B   B   �T��H��� E  4�C@ ?�
 
 �aG�pӑ2n�C(  
  ���R_� D   �  ����T��H E ܄�@ @�H
 
 a��2nG�pӀ 9�  
 R H  ���R>&  D   �  ����T��H E ܄�@ @�G
 
 a��2s�G�pӀ 9�  
 R H  ���R� B   B   �T��H��� E  4�D@ ?�~
 
 �aG�pӑ2y]�C(  
 S R���R[� D   �  ����T��H E ܄�@ @�F
 
 a��2y]G�pӀ 9�  
 � �  ���R{� D   �  ����T��H E ܄�@ @�E
 
 a��2G�pӀ 9�  
 � �  ���R'� B   B   �T��H��� E  4�E@ ?�}
 
 �aG�pӑ2���C(  
 � ����R�� D   �  ����T��H E ܄�@ @�D
 
 a��2��G�pӀ 9�  
 � �  ���RŊ D   �  ����T��H E ܄�@ @�C
 
 a��2�UG�pӀ 9�  
 � �  ���R~� B   B   �T��H��� E  4�F@ ?�|
 
 �aG�pӑ2���C(  
 � ����R�c	 D   �  ����T��H E ܄�@ @�B
 
 a��2��G�pӀ 9�  
 � �  ���R
= D   �  ����T��H E ܄�@ @�A
 
 a��2��G�pӀ 9�  
 	 �  ���R�5 B   B   �T��H��� E  4�G@ ?�{
 
 �aG�pӑ2�M�C(  
 	 ˑ��R  D   �  ����T��H E ܄�@ @�@
 
 a��2�MG�pӀ 9�  
 	 �  ���R?� D   �  ����T��H E ܄�@ @�?
 
 a��2��G�pӀ 9�  
 	 �  ���Rɥ  B   B   �T��H��� E  4�H@ ?�z
 
 �aG�pӑ2���C(  
 E 	���R� D   �  ����T��H E ܄�@ @�>
 
 a��2��G�pӀ 9�  
 	D 	:  ���R?_ D   �  ����T��H E ܄�@ @�=
 
 a��2�EG�pӀ 9�  
 	D 	:  ���R�W B   B   �T��H��� E  4�I@ ?�y
 
 �aG�pӑ2��C(  
 � 	D���Rg8 D   �  ����T��H E ܄�@ @�<
 
 a��2��G�pӀ 9�  
 	� 	w  ���R� D   �  ����T��H E ܄�@ @�;
 
 a��2��G�pӀ 9�  
 	� 	w  ���RB
 B   B   �T��H��� E  4�J@ ?�x
 
 �aG�pӑ2�=�C(  
 � 	����R�� D   �  ����T��H E ܄�@ @�:
 
 a��2�=G�pӀ 9�  
 	� 	w  ���R��
 D   �  ����T��H E ܄�@ @�9
 
 a��2��G�pӀ 9�  
 	� 	�  ���R�� B   B   �T��H��� E  4�K@ ?�w
 
 �aG�pӑ2ȍ�C(  
 � 	����R� D   �  ����T��H E ܄�@ @�8
 
 a��2ȍG�pӀ 9�  
 	� 	�  ���R�u D   �  ����T��H E ܄�@ @�7
 
 a��2�5G�pӀ 9�  
 	� 	�  ���R�,  B   B   �T��H��� E  4�L@ ?�v
 
 �aG�pӑ2�݀C(  
 8 	����R� D   �  ����T��H E ܄�@ @�6
 
 a��2��G�pӀ 9�  
 	� 	�  ���R�� D   �  ����T��H E ܄�@ @�5
 
 a��2مG�pӀ 9�  
 	� 	�  ���R�� B   B   �T��H��� E  4�M@ ?�u
 
 �aG�pӑ2�-�C(  
 t 	����R+� D   �  ����T��H E ܄�@ @�4
 
 a��2�-G�pӀ 9�  
 
7 
-  ���R9� D   �  ����T��H E ܄�@ @�3
 
 a��2��G�pӀ 9�  
 
7 
-  ���R�� B   B   �T��H��� E  4�N@ ?�t
 
 �aG�pӑ2�}�C(  
 � 
7���R\q D   �  ����T��H E ܄�@ @�2
 
 a��2�}G�pӀ 9�  
 
s 
i  ���R{J
 D   �  ����T��H E ܄�@ @�1
 
 a��2�%G�pӀ 9�  
 
s 
i  ���R�� B   B   �T��H��� E  4�O@ ?�s
 
 �aG�pӑ2�%�C(  
 � 
s���R�# D   �  ����T��H E ܄�@ @�0
 
 a��2��G�pӀ 9�  
 
s 
i  ���R�� D   �  ����T��H E ܄�@ @�/
 
 a��2�uG�pӀ 9�  
 
� 
�  ���R��  D   �  ����T��H E ܄�@ @�.
 
 a��3G�pӀ 9�  
 
� 
�  ���R�l D   �  ����T��H E ܄�@ @�-
 
 a��3�G�pӀ 9�  
 
� 
�  ���R�E D   �  ����T��H E ܄�@ @�,
 
 a��3mG�pӀ 9�  
 
� 
�  ���R D   �  ����T��H E ܄�@ @�+
 
 a��3G�pӀ 9�  
 
� 
�  ���R� D   �  ����T��H E ܄�@ @�*
 
 a��3�G�pӀ 9�  
 
� 
�  ���R� D   �  ����T��H E ܄�@ @�)
 
 a��3�G�pӀ 9�  
 P �  ���R� D   N   �T��H��� E  @�P@ ?�f
 
 �aG�pӑ2�%�C4  
 Z 
s���Rv� D   �  ����T��H E ܄�@ @�(
 
 a��2�%G�pӀ 9�  
 d Z  ���Rx� D   �  ����T��H E ܄�@ @�'
 
 a��2��G�pӀ 9�  
 d Z  ���R�� D   N   �T��H��� E  @�Q@ ?�e
 
 �aG�pӑ2�ͰC4  
 n d���RT� D   N   �T��H��� E  @�R@ ?�d
 
 �aG�pӑ2�u�C4  
 n d���R?, D   �  ����T��H E ܄�@ @�&
 
 a��2�uG�pӀ 9�  
 x n  ���R@, D   �  ����T��H E ܄�@ @�%
 
 a��3G�pӀ 9�  
 x n  ���R�, D   �  ����T��H E ܄�@ @�$
 
 a��3�G�pӀ 9�  
 x n  ���R�, D   �  ����T��H E ܄�@ @�#
 
 a��3mG�pӀ 9�  
 x n  ���R&	 D   N   �T��H��� E  @�S@ ?�c
 
 �aG�pӑ3�C4  
 � x���R<	 D   N   �T��H��� E  @�T@ ?�b
 
 �aG�pӑ3ŰC4  
 � x���R�	 D   N   �T��H��� E  @�U@ ?�a
 
 �aG�pӑ3m�C4  
 � x���R�	 D   N   �T��H��� E  @�V@ ?�`
 
 �aG�pӑ3�C4  
 � x���R�f	 D   �  ����T��H E ܄�@ @�"
 
 a��3G�pӀ 9�  
 � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    