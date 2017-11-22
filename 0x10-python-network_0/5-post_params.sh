#!/bin/bash
# script that POST request
curl -s "$1" -X POST -F 'email=hr@holbertonschool.com' -F 'subject=I will always be here for PLD'
