#!/usr/bin/env python
""" MFW Common Lib """
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
# Include modules
# import json
import time
import datetime
import socket
import subprocess
# Import Ini Reader
import ConfigParser
import io
# Request
# import requests

# --------------------------------------------------------------------- #
# read_cfg_discrod

def read_cfg_discrod(cfg_filename):
    """ read_cfg_discrod """
    # Load the configuration file
    with open(cfg_filename) as file_tmp:
        sample_config = file_tmp.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(sample_config))
    return config

# --------------------------------------------------------------------- #
# get_network_ip

def get_network_ip():
    """ get_network_ip """
    socket_tmp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        #s.connect(('10.255.255.255', 1))
        socket_tmp.connect(("8.8.8.8", 80))
        ip_local = socket_tmp.getsockname()[0]
    except:
        # If no internet access, return loopback address
        ip_local = '127.0.0.1'
    finally:
        socket_tmp.close()
    return ip_local.rstrip('\n')

# --------------------------------------------------------------------- #
# get_timestamp

def get_timestamp():
    """ get_timestamp """
    today = datetime.datetime.fromtimestamp(time.time())
    today2 = today.strftime('%Y/%m/%d %H:%M')
    return today2.rstrip('\n')

# --------------------------------------------------------------------- #
# get_hostname

def get_hostname():
    """ get_hostname """
    return socket.gethostname().rstrip('\n')

# --------------------------------------------------------------------- #
# get_osversion

def get_osversion():
    """ get_osversion """
    ## call command ##
    process_tmp = subprocess.Popen("cat /etc/*release | grep \"PRETTY_NAME\" | head -n 1  | awk -F'=' '{print $2}' |  sed -e 's/^\"//' -e 's/\"$//'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_external_ip

def get_external_ip():
    """ get_external_ip """
    ## call command ##
    process_tmp = subprocess.Popen("wget -q -O - http://icanhazip.com/ | tail", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
