# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 17:28:22 2025

@author: Ronyt
"""

# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io 

# For security reasons, never expose your password
#password = open('password','r').readline()

# Create a connection
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="sa1234",
	database="world_x" # Name of the database
)

# Create a cursor object
cursor = mydb.cursor()

# Prepare the query
query = 'SELECT doc FROM world_x.countryinfo where doc like "%8287%";'

# Execute the query to get the file
cursor.execute(query)

data = cursor.fetchall()

# The returned data will be a list of list
image = data[0][0]

# Decode the string
binary_data = base64.b64decode(image)

# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))

# Display the image
image.show()
