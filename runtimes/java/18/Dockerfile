FROM        --platform=$TARGETOS/$TARGETARCH eclipse-temurin:18-jdk-jammy

LABEL   	author="Jesper Richert" maintainer="contact@tnsjesper.xyz"

RUN 		apt update -y \
			&& apt -y upgrade

RUN  		apt install -y \
				curl \
				git \
				iproute2 \
				ipset \
				sqlite3 \
				tar \
				tzdata \
				libfreetype6

RUN     	useradd -m -d /home/container -s /bin/bash container
USER    	container
ENV     	USER=container HOME=/home/container
WORKDIR 	/home/container

COPY        ./../entrypoint.sh /entrypoint.sh
CMD         [ "/bin/bash", "/entrypoint.sh" ]