#!/bin/bash
# script that displays all HTTP methods the server will accept
curl -sIX OPTIONS $1 | awk -F': ' '/Allow/ {print $2}'
