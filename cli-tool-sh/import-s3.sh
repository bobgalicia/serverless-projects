#!/bin/bash

CLIHOME=$HOME/cli-movies
cd $CLIHOME

if [ $# -eq 1 ]
then
        var=`echo $1 | sed 's/ //g'`
        FICH=$var-`date +%Y%m%d`.json
        curl -o $FICH 'http://www.omdbapi.com/?apikey=12345ab&t='$1 > /dev/null 2>&1
        sum=`grep -n Title $FICH |cut -f1 -d:`
        if [ -n "$sum" ]
        then
                TIT=`cat $FICH | cut -d":" -f2 | cut -d"," -f1`
                echo "Subiendo "$TIT" a AWS S3"
                aws s3 cp $FICH s3://my-bucket/nuevos/movie.json
        else
                echo "No se ha encontrado la película"
        fi
else
        echo "Debe introducir solo el Titulo entre comillas"
        exit
fi
