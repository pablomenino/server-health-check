#!/usr/bin/env python
""" MFW Status Report """
# pylint: disable=invalid-name
# pylint: disable=C0301
# -*- coding: utf-8 -*- 

#----------------------------------------------------------------------------------------
# server-health-check
# Version: 0.6
# 
# WebSite:
# https://github.com/pablomenino/server-health-check/
# 
# Copyright 2019 - Pablo Menino <pablo.menino@gmail.com>
#----------------------------------------------------------------------------------------

# --------------------------------------------------------------------- #
# Import General modules
import sys
import os
# import datetime
# import time
import platform

# --------------------------------------------------------------------- #
# Add local lib path
pathname = os.path.dirname(sys.argv[0])
sys.path.append(os.path.abspath(pathname) + "/modules/")

# Import MFW Lib General
from mfw_lib_general import get_network_ip
from mfw_lib_general import get_timestamp
from mfw_lib_general import get_hostname
from mfw_lib_general import get_osversion
from mfw_lib_general import get_external_ip
from mfw_lib_general import read_cfg_discrod

# Import MFW Status
from mfw_lib_status import get_uptime
from mfw_lib_status import get_cpuload
from mfw_lib_status import get_memfree
from mfw_lib_status import get_memused
from mfw_lib_status import get_memtotal
from mfw_lib_status import get_memfreeb
from mfw_lib_status import get_memusedb
from mfw_lib_status import get_memtotalb
from mfw_lib_status import get_uptimedays
from mfw_lib_status import get_uptimehours
from mfw_lib_status import get_uptimeminutes
from mfw_lib_status import get_uptimeseconds
from mfw_lib_status import get_sessioncount
from mfw_lib_status import get_processcount
# from mfw_lib_status import get_processmax
from mfw_lib_status import get_swapfreeb
from mfw_lib_status import get_swaptotalb
from mfw_lib_status import get_swapusedb
from mfw_lib_status import get_swapfree
from mfw_lib_status import get_swapused
from mfw_lib_status import get_swaptotal
from mfw_lib_status import get_rootfreeb
from mfw_lib_status import get_rootusedb
from mfw_lib_status import get_roottotalb
from mfw_lib_status import get_rootfree
from mfw_lib_status import get_rootused
from mfw_lib_status import get_roottotal
from mfw_lib_status import get_rootusedperc
from mfw_lib_status import get_rootfreeperc
from mfw_lib_status import get_phpversion
from mfw_lib_status import get_httpversion
from mfw_lib_status import get_neofetch

# --------------------------------------------------------------------- #
# Import Discord Webhook module
from mfw_lib_discord import Webhook

# --------------------------------------------------------------------- #
# Read Discord Configuration
discord_config = read_cfg_discrod(os.path.abspath(pathname) + "/config/discord.cfg")

# --------------------------------------------------------------------- #
# Define allowed hostname to run
HOST_ERIC = "eric-ws"
HOST_NORC = "norc"
HOST_XPS = "xps13"
HOST_NORCCluster01 = "raspi"
HOST_NORCCluster02 = "raspi-standby"

# WebHook Discord Key
norc_webhook = discord_config.get('discord_webhook', 'norc')
xps13_webhook = discord_config.get('discord_webhook', 'xps13')
NORC_Cluster_01_webhook = discord_config.get('discord_webhook', 'norc-cluster-r01')
NORC_Cluster_02_webhook = discord_config.get('discord_webhook', 'norc-cluster-r02')
eric_webhook = discord_config.get('discord_webhook', 'eric')

# --------------------------------------------------------------------- #
def gather_info():
    """ gather_info """
    msg_desc = "Generated date = " + get_timestamp() + "\n"
    msg_desc += "Ip = " + get_network_ip() + "\n"
    msg_desc += "Ip External = " + get_external_ip() + "\n"
    msg_desc += "System = " + platform.system() + "\n"
    msg_desc += "Operating System = " + get_osversion() + "\n"
    msg_desc += "Kernel = " + platform.release() + "\n"
    msg_desc += "CPU Load = " + get_cpuload() +  "\n"
    msg_desc += "Memory = Free: " + get_memfree(get_memfreeb()) + " GB, Used: " + get_memused(get_memusedb(get_memtotalb(), get_memfreeb())) + " GB, Total: " + get_memtotal(get_memtotalb()) + " GB \n"
    msg_desc += "Swap = Free: " + get_swapfree(get_swapfreeb()) + " GB, Used: " + get_swapused(get_swapusedb(get_swaptotalb(), get_swapfreeb())) + " GB, Total: " + get_swaptotal(get_swaptotalb()) + " GB \n"
    msg_desc += "Root = Free: " + get_rootfree(get_rootfreeb()) + " GB (" + get_rootfreeperc(get_rootusedperc()) + "%), Used: " + get_rootused(get_rootusedb()) + " GB (" + get_rootusedperc() + "%), Total: " + get_roottotal(get_roottotalb()) + " GB \n"
    msg_desc += "Sessions = " + get_sessioncount() + " sessions \n"
    # msg_desc += "Processes = " + get_processcount() + " running processes of " + get_processmax() + " maximum processes \n"
    msg_desc += "Processes = " + get_processcount() + " \n"
    php_version = get_phpversion()
    if php_version != "ERROR":
        msg_desc += "PHP Info = Version: " + php_version + "\n"
    http_version = get_httpversion()
    if http_version != "ERROR":
        msg_desc += "Apache Info = Version: " + http_version + "\n"
    msg_desc += "Uptime = " + get_uptimedays() + " day(s). " + get_uptimehours() + ":" + get_uptimeminutes() + ":" + get_uptimeseconds()
    return msg_desc

# --------------------------------------------------------------------- #
def send_report_discord(discord_Webhook, msg_desc):
    """ send_report_discord """
    embed = Webhook(discord_Webhook, color=1234123, msg='`Server Status Report:`')
    embed.set_title(title='System Overview - '+get_hostname(), url='http://www.mfwlab.com/')
    embed.set_desc(msg_desc)
    embed.set_thumbnail('http://www.pngmart.com/files/3/Health-PNG-File.png')
    embed.set_footer(text='Time Stamp: ' + get_timestamp(), ts=False)
    embed.post()

# --------------------------------------------------------------------- #
# Main

if get_hostname() == HOST_ERIC:
    print("ServerName: " + HOST_ERIC)
    print("Running: ")
    msg_desc = gather_info()
    send_report_discord(eric_webhook, msg_desc)
elif get_hostname() == HOST_NORC:
    print("ServerName: " + HOST_NORC)
    print("Running: ")
    msg_desc = gather_info()
    send_report_discord(norc_webhook, msg_desc)
elif get_hostname() == HOST_XPS:
    print("ServerName: " + HOST_XPS)
    print("Running: ")
    msg_desc = gather_info()
    send_report_discord(xps13_webhook, msg_desc)
elif get_hostname() == HOST_NORCCluster01:
    print("ServerName: " + HOST_NORCCluster01)
    print("Running: ")
    msg_desc = gather_info()
    send_report_discord(NORC_Cluster_01_webhook, msg_desc)
elif get_hostname() == HOST_NORCCluster02:
    print("ServerName: " + HOST_NORCCluster02)
    print("Running: ")
    msg_desc = gather_info()
    send_report_discord(NORC_Cluster_02_webhook, msg_desc)

# --------------------------------------------------------------------- #
