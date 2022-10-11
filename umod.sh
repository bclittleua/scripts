sudo useradd -m -p <be201440#> -s /bin/bash user01
sudo useradd -m -p <be201440#> -s /bin/bash user02
sudo useradd -m -p <be201440#> -s /bin/bash user03
sudo useradd -m -p <be201440#> -s /bin/bash user04
sudo usermod user01 -a -G user00,adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,spi,i2c,gpio
sudo usermod user02 -a -G user00,adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,spi,i2c,gpio
sudo usermod user03 -a -G user00,adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,spi,i2c,gpio
sudo usermod user04 -a -G user00,adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,spi,i2c,gpio
