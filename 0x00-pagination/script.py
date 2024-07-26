#!\usr\bin\ python 3
import requests

# URL of the file
url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240726%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240726T195457Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=83dafd97d3e28af644a48ceabf5e93fcfa49937d86ccdb40fa2204088ac30675'

# Send a HTTP request to the URL
response = requests.get(url)

# Save the content to a file
file_name = 'Popular_Baby_Names.csv'
with open(file_name, 'wb') as file:
    file.write(response.content)

print(f"File '{file_name}' downloaded successfully.")
