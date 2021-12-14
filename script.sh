#!/bin/bash
if [ $1 ]
then    
    /spark/bin/spark-submit script.py $1 

else 
    /spark/bin/spark-submit script.py 10
fi 

