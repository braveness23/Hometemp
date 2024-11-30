#!/bin/bash
sqlite3 /home/pi/hometemp/hometemp.db << EOF
.mode tabs
.headers off
SELECT strftime('%s', datetime), temperature FROM readings WHERE datetime >= datetime('now', '-1 day');
EOF