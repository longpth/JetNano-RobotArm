MYIP=ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
docker run -it -p 1880:1880 --ip=$MYIP -v ~/JetNano-RobotArm:/data -v /dev:/dev --name mynodered --rm --privileged longpth/rbtln:latest 
