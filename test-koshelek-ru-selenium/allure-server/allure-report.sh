#!/bin/bash
set -e

cd /home/vagrant/src/docker-results

FILE_NAME_ZIP=alluer-report.zip
IP_ADRESS=192.168.1.100
DATA=$(date '+%Y-%m-%d-%H:%M:%S')

zip -5 $FILE_NAME_ZIP * 2>&1

mv $FILE_NAME_ZIP /home/vagrant/src 2>&1

cd /home/vagrant/src 2>&1

RESULT=$(curl -X 'POST' \
          'http://'$IP_ADRESS':8080/api/result' \
          -H 'accept: */*' \
          -H 'Content-Type: multipart/form-data' \
          -F 'allureResults=@'$FILE_NAME_ZIP';type=application/zip' | \
          python3 -c "import sys, json; print(json.load(sys.stdin)['uuid'])")



curl -X 'POST' \
  'http://'$IP_ADRESS':8080/api/report' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "reportSpec": {
    "path": [
      "master",
      "'$DATA'"
    ],
    "executorInfo": {
      "name": "string",
      "type": "string",
      "url": "string",
      "buildOrder": 0,
      "buildName": "#'$DATA'",
      "buildUrl": "string",
      "reportName": "string",
      "reportUrl": "string"
    }
  },
  "results": [
    "'$RESULT'"
  ],
  "deleteResults": true
}'
