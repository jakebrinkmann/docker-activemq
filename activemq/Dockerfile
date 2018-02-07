FROM openjdk:8

ENV ACTIVEMQ_VERSION="5.15.3"
ENV ACTIVEMQ_HOME="/usr/local/activemq"
ENV ACTIVEMQ_DATA_DIR="/usr/local/data/activemq"

RUN mkdir -p ${ACTIVEMQ_HOME} \
	&& cd /usr/src \
	&& curl -L http://apache.mirrors.ovh.net/ftp.apache.org/dist/activemq/${ACTIVEMQ_VERSION}/apache-activemq-${ACTIVEMQ_VERSION}-bin.tar.gz | tar -xvz \
	&& mv apache-activemq-${ACTIVEMQ_VERSION}/* ${ACTIVEMQ_HOME} \
	&& rm -rf /usr/src/*

RUN mkdir -p ${ACTIVEMQ_DATA_DIR} \
	&& groupadd activemq \
	&& useradd --system --home ${ACTIVEMQ_HOME} -g activemq activemq \
	&& chown -R activemq:activemq ${ACTIVEMQ_DATA_DIR}

ENV PATH=${ACTIVEMQ_HOME}/bin:${PATH}

ENTRYPOINT ["activemq", "console"]


