#!/bin/bash

if [ -z "$1" ]
    then
        echo "You forgot to enter ip address"
        echo "Syntax: ./ping.sh 192.168.1"
    else
      for ip in `seq 1 254`:
          do
             ping -c 1 $1.$ip | sed -n 's/.*from \([0-9.]*\).*/\1/p' &
          done
fi
