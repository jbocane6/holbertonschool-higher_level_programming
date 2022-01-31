#!/bin/bash
# Script that prints the content of catch_me
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
