#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import commands
import re

if sys.argv[1] == "-l":
        ip_concedidas=commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep lease.*.{ |sort |uniq | awk '{print $2}'")
        ip_reservadas=commands.getoutput("cat /etc/dhcp/dhcpd.conf |grep 'fixed-address' |sort |uniq | awk '{print $2}' | cut -d ';' -f 1")
        print "\n----------------"
        print " Ips concedidas"
        print "----------------"
        print ip_concedidas
        print "\n----------------"
        print " Ips reservadas"
        print "----------------"
        print ip_reservadas + "\n"

else:
        ip_concedidas = commands.getoutput("cat /var/lib/dhcp/dhcpd.leases |grep -A6 '%s' | grep hardware | awk '{print $3}' |sort |uniq" % sys.argv[1])
        ip_concedidas = ip_concedidas.replace(";", ".");
        check=re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
        if check.match(sys.argv[1]):
                if len(ip_concedidas) > 0:
                	print "La ip %s ha sido concedida y su MAC correspondiente es: %s" % (sys.argv[1],ip_concedidas)
                else:
                	print "La ip %s no tiene concesiones" % (sys.argv[1])

