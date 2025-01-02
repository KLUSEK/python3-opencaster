#!/bin/bash

if [ $# -lt 4 ]
then
    /bin/echo "Usage:"
    /bin/echo "ssu-update.sh dvbssu_section_directory dsmcc_pid padding_on"
    /bin/echo "	dvbssu_section_directory: the directory to marshal in an object carousel"
    /bin/echo "	association_tag aka common tag, referenced by PMTs and AITs, every carousel has its own"
    /bin/echo "	pid, referenced by PMTs using this carousel"
    /bin/echo "	padding_on, every section is padded, usuful with some buggy decoder, waste bandwith, default off"
    /bin/echo "	mount_frequency, set how often insert DII/DSI/SGW to speed up carousel mount, default is once per carousel period"
    /bin/echo
    /bin/echo "Example:"
    /bin/echo "ssu-update.sh dir1 2001 0 8"
    /bin/echo "	carousel_directory: dir1"
    /bin/echo "	pid: 2001"
    /bin/echo "	don't pad"
    /bin/echo "	insert DSI/DII/SGW eight times per carousel length"
    exit 65
fi

#Parameters passing
OCDIR=$1
PID=$2
PAD_ON=$3
MOUNT_PERIOD="1"
MOUNT_PERIOD=$4

# Check if it is necessary to pad every sections or not, unluckly we have found some decoders having buggy section filtering that needed this
if [ "$PAD_ON" = "1" ]
then
	file_number=0
	for file in $OCDIR/*.sec
	do
		let file_number=$file_number+1
	done
	echo "total carousel section number is $file_number"
	period=$(($file_number/$MOUNT_PERIOD))
	echo "carousel head period is every $period section"
	counter=-1
	
	for file in $OCDIR/*.sec
	do
		/usr/local/bin/sec2ts $PID < $file >> $OCDIR/temp_ts
		let counter=$counter-1
		if [ $counter -lt 0 ]; then
			let counter=$period
			/usr/local/bin/sec2ts $PID < $OCDIR/DSI.sec >> $OCDIR/temp_ts
			/usr/local/bin/sec2ts $PID < $OCDIR/DII-1.sec >> $OCDIR/temp_ts
			# /bin/cat $OCDIR/DSI.ts >> $OCDIR/temp_ts
			# /bin/cat $OCDIR/DII-1.ts >> $OCDIR/temp_ts
		fi
	done
	/usr/local/bin/tsfixcc $OCDIR/temp_ts > $OCDIR.ts
	rm $OCDIR/temp_ts
else
	file_number=0
	for file in $OCDIR/*.sec
	do
		let file_number=$file_number+1
	done
	echo "total carousel section number is $file_number"
	period=$(($file_number/$MOUNT_PERIOD))
	echo "carousel head period is every $period section"
	counter=-1
	for file in $OCDIR/*.sec
	do
		/bin/cat $file >> $OCDIR/temp_sec
		let counter=$counter-1
		if [ $counter -lt 0 ]; then
			let counter=$period
			/bin/cat $OCDIR/DSI.sec >> $OCDIR/temp_sec
			/bin/cat $OCDIR/DII-1.sec >> $OCDIR/temp_sec
		fi
	done
	/usr/local/bin/sec2ts $PID < $OCDIR/temp_sec > $OCDIR.ts
	rm $OCDIR/temp_sec
fi

