You need to generate a API key at http://www.omdbapi.com/apikey.aspx (you can select the FREE account type).
Once you have the key you need to replace it in import-s3.sh script, where "12345ab" write your generated apikey:
  "curl -o $FICH 'http://www.omdbapi.com/?apikey=12345ab&t='$1 > /dev/null 2>&1"
You also need to configure your bucket and key at:
  " aws s3 cp $FICH s3://my-bucket/nuevos/movie.json"
  
This script will copy the generated json into your S3 bucket
