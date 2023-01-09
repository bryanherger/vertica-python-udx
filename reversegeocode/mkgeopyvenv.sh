#!/bin/bash
rm -rf /tmp/venv_geocode
/opt/vertica/oss/python3/bin/python3 -m venv /tmp/venv_geocode
source /tmp/venv_geocode/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade geopy

