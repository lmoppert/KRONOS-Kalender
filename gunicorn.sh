#!/bin/sh

killall gunicorn
wait
gunicorn -b 127.0.0.1:8765 kalender.wsgi &
