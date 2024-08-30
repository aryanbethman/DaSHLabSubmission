#!/bin/bash
python Level1.py ;
python Level2_server.py &
python Level2_client.py &
wait