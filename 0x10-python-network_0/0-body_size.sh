#!/bin/bash
# script that takes in URL, sends request to URL, and displays
# size of the body of the response

curl -sI $1 | grep Content-Length | awk '{print $2}'
