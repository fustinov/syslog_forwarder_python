# syslog_forwarder_python
This script is a basic implementation of a syslog relay/proxy. I tested this with python3.9 and rsyslogd. 

## Usage

```
usage: syslog_forwarder.py [-h] -t TARGET [-p PORT] [-l LISTEN]

This is syslog forwarder written in Python

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Destination server
  -p PORT, --port PORT  Target port. Default - 514
  -l LISTEN, --listen LISTEN
                        Interface to listen on. Default - all
```
