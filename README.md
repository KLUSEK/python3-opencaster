# OpenCaster 

### About this fork
Fork done in order to:
 - Merge available patches & cherry-picked patches created by the community
 - Make it compatible with Python 3.10+

Please be aware that as of 2025, OpenCaster hasn't received any updates for more than 12 years, with last changes originating from 2013.  
In the meantime a lot of things have changed in the DVB world ...

Please also refer original [README](README.txt)

### Install dependenties
```
sudo apt install make gcc libgcc-12-dev zlib1g-dev bc python3 python3-pip python3-build python3-venv python3-crcmod -y
```

### Build and install
```
make
sudo make install
```