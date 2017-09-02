FROM tensorflow/tensorflow:1.3.0-devel
MAINTAINER Curtis Kim <ildoo@ildoo.net>

RUN apt update -yq && apt install -yq curl wget unzip vim cmake sudo && \
useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo && \
pip3 install pysc2 && \
mkdir -p ~/StarCraftII/

RUN mkdir /opencv && \
curl -fsSL http://bit.ly/OpenCV-Latest | bash -s /opencv

RUN wget http://blzdistsc2-a.akamaihd.net/Linux/SC2.3.16.1.zip && \
unzip -P iagreetotheeula SC2.3.16.1.zip -d ~/StarCraftII/ && \
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season1.zip && \
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season2.zip && \
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Ladder2017Season3.zip && \
wget http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip && \
wget http://blzdistsc2-a.akamaihd.net/ReplayPacks/3.16.1-Pack_1-fix.zip && \
unzip Ladder2017Season1.zip ~/StarCraftII/Maps && \
unzip Ladder2017Season2.zip ~/StarCraftII/Maps && \
unzip Ladder2017Season3.zip ~/StarCraftII/Maps && \
unzip Melle.zip ~/StarCraftII/Maps && \
unzip 3.16.1-Pack_1-fix.zip ~/StarCraftII/Replays && \
rm *.zip 

ENV PYTHONPATH=$PYTHONPATH:$HOME/.opencv/lib/python3.2/dist-package

USER docker
ENTRYPOINT ["/bin/bash"]
