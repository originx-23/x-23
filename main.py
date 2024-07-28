#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
import socket

from cluster import create_app, socketio

# import os
# import sys
# Base_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(Base_DIR)


app = create_app()
hostname = socket.gethostname()

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=12138, debug=False, log_output=True,
                 use_reloader=True)
