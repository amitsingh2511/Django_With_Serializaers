# Django_With_Serializaers

# Backend is the project Name And Api is the App Name

# DevelopingApi Three Api 2 Post Api and 1 Get Api.

# Compliance Post Api Curls
curl --location 'localhost:8000/api/compliances/' \
--header 'Content-Type: application/json' \
--data '{
  "name": "AS"
}'


# Application Post Api Curls
curl --location 'localhost:8000/api/applications/' \
--header 'Content-Type: application/json' \
--data '{
  "name": "app4",
  "product_name": "product4",
  "compliance": 3
}'

# Get Compliance Details with Application Details Api
curl --location 'localhost:8000/api/compliances/with-application/'


# Thank You 