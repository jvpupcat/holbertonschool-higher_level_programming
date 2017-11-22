#!/bin/bash
curl -sH "Content-Type: application/json" -X POST "$1" -d "@$2"
