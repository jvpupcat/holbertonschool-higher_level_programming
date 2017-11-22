#!/bin/bash
# script that takes in URL, sends request to URL, and displays
curl -sI "$1" | grep Content-Length | awk '{print $2}'
