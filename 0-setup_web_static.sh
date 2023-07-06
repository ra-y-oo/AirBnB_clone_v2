#!/bin/bash
#Check if nginx is installed
if ! [-x "$(command -v nginx)"]; then
    echo "Installing Nginx..."

    #Update package list
    sudo apt update

    #Install Nginx
    sudo apt install nginx -y

    echo "Nginx installed"
else
    echo "Nginx already installed"
fi

#Checks if directory exists
if [ ! -d "./data/" ];then

    #Create the folder /data/ 
    mkdir -p "./data/"
else
    echo "Directory already exists"
fi

#Checks if directory exists
if [ ! -d "./data/web_static/" ];then

    #Create the folder /data/web_static/ 
    mkdir -p "./data/web_static/"
else
    echo "Directory already exists"
fi

#Checks if directory exists
if [ ! -d "./data/web_static/releases/" ];then

    #Create the folder /data/web_static/releases/ 
    mkdir -p "./data/web_static/releases//"
else
    echo "Directory already exists"
fi

#Checks if directory exists
if [ ! -d "./data/web_static/shared/" ];then

    #Create the folder /data/web_static/shared/ 
    mkdir -p "./data/web_static/shared//"
else
    echo "Directory already exists"
fi

#Checks if directory exists
if [ ! -d "./data/web_static/releases/test/" ];then

    #Create the folder /data/web_static/releases/test/ 
    mkdir -p "./data/web_static/releases/test//"
else
    echo "Directory already exists"
fi

# Define HTML content
html_content='<!DOCTYPE html>
<html>
<head>
  <title>My HTML Page</title>
</head>
<body>
  <h1>Welcome to my HTML page!</h1>
  <p>This is a sample HTML file created using a bash script.</p>
</body>
</html>'

#Define file path
html_path="./data/web_static/releases/test/index.html"

# Create HTML file
echo "$html_content" > "$html_path"

#!/bin/bash

# Define the target folder path
target_folder="./data/web_static/releases/test/"

# Define the symbolic link path
symbolic_link="./data/web_static/current"

# Check if the symbolic link already exists
if [ -L "$symbolic_link" ]; then
  echo "Symbolic link $symbolic_link already exists. Deleting..."
  rm "$symbolic_link"
fi

# Create the symbolic link
ln -s "$target_folder" "$symbolic_link"

echo "Symbolic link $symbolic_link created successfully."


#Define file path
folder_path="./data/"

#Define user
user="ubuntu"


#Change ownership of folder
sudo chown -R "$user" "$folder_path"
