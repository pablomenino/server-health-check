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
import subprocess

# --------------------------------------------------------------------- #
# get_cpuload

def get_cpuload():
    """ get_cpuload """
    ## call command ##
    process_tmp = subprocess.Popen("uptime | grep -ohe '[s:][: ].*' | awk '{ print \"1m: \"$2 \" 5m: \"$3 \" 15m: \" $4}'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_memfreeb

def get_memfreeb():
    """ get_memfreeb """
    ## call command ##
    process_tmp = subprocess.Popen("cat /proc/meminfo | grep MemFree | awk {'print $2'}", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_memtotalb

def get_memtotalb():
    """ get_memtotalb """
    ## call command ##
    process_tmp = subprocess.Popen("cat /proc/meminfo | grep MemTotal | awk {'print $2'}", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_memusedb

def get_memusedb(memtotalb, memfreeb):
    """ get_memusedb """
    ## call command ##
    process_tmp = subprocess.Popen("echo \"" + memtotalb + " - " + memfreeb + "\" | bc", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_memfree

def get_memfree(memfreeb):
    """ get_memfree """
    ## call command ##
    memfreeb_round = str(round((int(memfreeb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + memfreeb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return memfreeb_round

# --------------------------------------------------------------------- #
# get_memused

def get_memused(memusedb):
    """ get_memused """
    ## call command ##
    memusedb_round = str(round((int(memusedb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + memusedb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return memusedb_round

# --------------------------------------------------------------------- #
# get_memtotal

def get_memtotal(memtotalb):
    """ get_memtotal """
    ## call command ##
    memtotalb_round = str(round((int(memtotalb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + memtotalb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return memtotalb_round

# --------------------------------------------------------------------- #
# get_uptime

def get_uptime():
    """ get_uptime """
    ## call command ##
    process_tmp = subprocess.Popen("awk '{print int($1/86400)\" day(s) \"int($1%86400/3600)\":\"int(($1%3600)/60)\":\"int($1%60)}' /proc/uptime", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_uptimedays

def get_uptimedays():
    """ get_uptimedays """
    ## call command ##
    process_tmp = subprocess.Popen("awk '{print int($1/86400)}' /proc/uptime", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_uptimehours

def get_uptimehours():
    """ get_uptimehours """
    ## call command ##
    process_tmp = subprocess.Popen("awk '{print int($1%86400/3600)}' /proc/uptime", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_uptimeminutes

def get_uptimeminutes():
    """ get_uptimeminutes """
    ## call command ##
    process_tmp = subprocess.Popen("awk '{print int(($1%3600)/60)}' /proc/uptime", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_uptimeseconds

def get_uptimeseconds():
    """ get_uptimeseconds """
    ## call command ##
    process_tmp = subprocess.Popen("awk '{print int($1%60)}' /proc/uptime", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_sessioncount

def get_sessioncount():
    """ get_sessioncount """
    ## call command ##
    process_tmp = subprocess.Popen("who | wc -l", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_processcount

def get_processcount():
    """ get_processcount """
    ## call command ##
    process_tmp = subprocess.Popen("ps -Afl | wc -l", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_processmax

def get_processmax():
    """ get_processmax """
    ## call command ##
    process_tmp = subprocess.Popen("ulimit -u", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_swapfreeb

def get_swapfreeb():
    """ get_swapfreeb """
    ## call command ##
    process_tmp = subprocess.Popen("cat /proc/meminfo | grep SwapFree | awk {'print $2'}", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_swaptotalb

def get_swaptotalb():
    """ get_swaptotalb """
    ## call command ##
    process_tmp = subprocess.Popen("cat /proc/meminfo | grep SwapTotal | awk {'print $2'}", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_swapusedb

def get_swapusedb(swaptotalb, swapfreeb):
    """ get_swapusedb """
    ## call command ##
    process_tmp = subprocess.Popen("echo \"" + swaptotalb + " - " + swapfreeb + "\" | bc", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_swapfree

def get_swapfree(swapfreeb):
    """ get_swapfree """
    ## call command ##
    swapfreeb_round = str(round((int(swapfreeb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + swapfreeb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return swapfreeb_round

# --------------------------------------------------------------------- #
# get_swapused

def get_swapused(swapusedb):
    """ get_swapused """
    ## call command ##
    swapusedb_round = str(round((int(swapusedb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + swapusedb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return swapusedb_round

# --------------------------------------------------------------------- #
# get_swaptotal

def get_swaptotal(swaptotalb):
    """ get_swaptotal """
    ## call command ##
    swaptotalb_round = str(round((int(swaptotalb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + swaptotalb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return swaptotalb_round

# --------------------------------------------------------------------- #
# get_rootfreeb

def get_rootfreeb():
    """ get_rootfreeb """
    ## call command ##
    process_tmp = subprocess.Popen("df -kP / | tail -1 | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_rootusedb

def get_rootusedb():
    """ get_rootusedb """
    ## call command ##
    process_tmp = subprocess.Popen("df -kP / | tail -1 | awk '{print $3}'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_roottotalb

def get_roottotalb():
    """ get_roottotalb """
    ## call command ##
    process_tmp = subprocess.Popen("df -kP / | tail -1 | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_rootfree

def get_rootfree(rootfreeb):
    """ get_rootfree """
    rootfreeb_round = str(round((int(rootfreeb) / 1024 / 1024), 2))
    ## call command ##
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + rootfreeb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return rootfreeb_round

# --------------------------------------------------------------------- #
# get_rootused

def get_rootused(rootusedb):
    """ get_rootused """
    ## call command ##
    rootusedb_round = str(round((int(rootusedb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + rootusedb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return rootusedb_round

# --------------------------------------------------------------------- #
# get_roottotal

def get_roottotal(roottotalb):
    """ get_roottotal """
    ## call command ##
    roottotalb_round = str(round((int(roottotalb) / 1024 / 1024), 2))
    #process_tmp = subprocess.Popen("printf \"%0.2f\" $(bc -q <<< scale=2\;" + roottotalb + "/1024/1024)", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    #(output, err) = process_tmp.communicate()
    #p_status = process_tmp.wait()

    #if p_status == 0:
    #    return output.rstrip('\n')
    #else:
    #    return "ERROR"
    return roottotalb_round

# --------------------------------------------------------------------- #
# get_rootusedperc

def get_rootusedperc():
    """ get_rootusedperc """
    ## call command ##
    process_tmp = subprocess.Popen("df -kP / | tail -1 | awk '{print $5}'| sed s'/%$//'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_rootfreeperc

def get_rootfreeperc(rootusedperc):
    """ get_rootfreeperc """
    ## call command ##
    process_tmp = subprocess.Popen("echo \"100 - " + rootusedperc + "\" | bc", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_phpversion

def get_phpversion():
    """ get_phpversion """
    ## call command ##
    process_tmp = subprocess.Popen("/usr/bin/php -v 2>/dev/null | grep -oE '^PHP\\s[0-9]+\\.[0-9]+\\.[0-9]+' | awk '{ print $2}'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0 and output.rstrip('\n'):
        return output.rstrip('\n')
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_httpversion_ext

def get_httpversion_ext(http_path):
    """ get_httpversion_ext """
    ## call command ##
    process_tmp = subprocess.Popen(http_path + " -v  | grep \"Server version\"  | sed -e 's/.*[^0-9]\\([0-9].[0-9]\\+.[0-9]\\+\\)[^0-9]*$/\\1/'", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0 and output.rstrip('\n'):
        return output.rstrip('\n')
    else:
        return "ERROR"


# --------------------------------------------------------------------- #
# get_httpversion

def get_httpversion():
    """ get_httpversion """
    ## call command ##
    process_tmp = subprocess.Popen("which httpd 2>/dev/null", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0 and output.rstrip('\n'):
        http_ver = get_httpversion_ext(output.rstrip('\n'))
        return http_ver
    else:
        return "ERROR"

# --------------------------------------------------------------------- #
# get_neofetch

def get_neofetch():
    """ get_neofetch """
    ## call command ##
    process_tmp = subprocess.Popen("neofetch --config ~/bin/neofetch.conf 2>/dev/null", stdout=subprocess.PIPE, shell=True)
    ## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0 and output.rstrip('\n'):
        neostatus = output.rstrip('\n')
        return neostatus
    else:
        return "ERROR"

# --------------------------------------------------------------------- #

