#!/bin/sh

sudo apt update && sudo apt install -y python3-qwt
pip3 install --upgrade pip
pip3 install PySide2 numpy opencv-python pyqtgraph
pip3 install protobuf grpcio grpcio-tools
pip3 install qdarkstyle