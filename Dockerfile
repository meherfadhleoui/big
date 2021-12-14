FROM bde2020/spark-master:3.0.1-hadoop3.2 

COPY ./access.log ./
COPY script.py ./

COPY script.sh ./

RUN pip install termcolor && chmod +x script.sh 










