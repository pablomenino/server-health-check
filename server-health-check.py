#!/usr/bin/env python3

#----------------------------------------------------------------------------------------
# server-health-check
# Version: 0.1
# 
# WebSite:
# https://github.com/pablomenino/server-health-check/
# 
# Copyright © 2017 - Pablo Meniño <pablo.menino@gmail.com>
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
# Import modules
 
import sys
import os
# import datetime
# import time
# import platform

# --------------------------------------------------------------------- #
# Add local lib path
pathname = os.path.dirname(sys.argv[0])
sys.path.append(os.path.abspath(pathname) + "/lib/")

# Import MFW Lib General
from general import get_timestamp
from general import get_hostname

print("\n\n");
print(get_timestamp());
print(get_hostname());

