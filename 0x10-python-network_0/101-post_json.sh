#!/bin/bash
# script that sends POST request with contents of file
curl -sH "Content-Type: application/json" -X POST "$1" -d "@$2"
