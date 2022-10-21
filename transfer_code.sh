#!/bin/bash
#Arg 1 is the "old file" (e.g. file.c.orig)
#Arg 2 is the "new file" (e.g. file.c)
#Must be run from the location the file.c is created || things get whacky

#Find dir one up from file we're making changes from. E.G. if we're editing /etc/hosts, this will find just "/etc"
OrigDir=`find /freebsd_ports/* -iname $1 -print -quit | sed 's|/[^/]*$||' | rev | cut -f2- -d"/" | rev`

#Then we'll run the diff to create a file using the "new" filename dynamically
diff -u $1 $2 > /free-bsdports/net/frr7/files/patch-$2

echo "File `/free-bsdports/net/frr7/files/patch-$2` created successfully"

#Check to see if backup work dir exists - if so, copy work over to work_backup. If not, create it, then copy over to it.
#Version 0.2 might have some better error handling
[ -d "/free-bsdports/net/frr7/work_backup" ] && mv /free-bsdports/net/frr7/work /free-bsdports/net/frr7/work_backup || mkdir /free-bsdports/net/frr7/work_backup && mv /free-bsdports/net/frr7/work /free-bsdports/net/frr7/work_backup


#Make it
cd ${OrigDir} && echo "" | make

#Now, grab the shiny new binary and pitch it to dev

binary=`echo ${1} | cut -f 1 -d "."`

scp /free-bsdports/net/frr7/work/stage/usr/local/sbin/${binary} root@172.16.1.1:/usr/local/sbin || echo "SCP failed. Sad pandas :( "
