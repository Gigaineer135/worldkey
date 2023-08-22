#!/bin/bash
#apt installs
apt install gpsd
#making a dir and executable 
mkdir /bin/worldkey
mv WorldKey.py /bin/worldkey/
echo "#!/bin/bash" >> /bin/worldkey
echo "python3 /bin/worldkey/Worldkey.py" >> /bin/worldkey
echo "To use the command just type worldkey in to your terminal"