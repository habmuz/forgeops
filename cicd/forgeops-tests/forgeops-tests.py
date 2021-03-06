#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from time import strftime, gmtime

import urllib3
urllib3.disable_warnings()

# root_dir : computed using relative position from this file
root_dir = os.path.abspath(os.path.dirname(__file__))

# Insert lib folder (as very first lib directory - rank 0) to python path
sys.path.insert(0, os.path.join(root_dir, 'lib'))

# Insert config folder (rank 1) to python path
sys.path.insert(0, os.path.join(root_dir, 'config'))

import pytest

if __name__ == '__main__':

    report_path = 'reports'
    if not os.path.exists(report_path):
        os.makedirs(report_path)

    html_report_name = 'forgeops_' + strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + '_report.html'
    html_report_path = os.path.join(report_path, html_report_name)
    allure_report_path = os.path.join(report_path, 'allure-files')

    custom_args = '--html=%s --self-contained-html --alluredir=%s' % (html_report_path, allure_report_path)
    args = sys.argv + custom_args.split()
    res = pytest.main(args=args)

    latest_link = os.path.join(report_path, 'latest.html')
    if os.path.lexists(latest_link):
        os.unlink(latest_link)
    if os.path.exists(latest_link):
        os.remove(latest_link)
    os.symlink(html_report_name, latest_link)

    sys.exit(res)
