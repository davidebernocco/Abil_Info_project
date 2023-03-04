#!/bin/bash

echo "Hello dear user, if you still haven't done it yet, PLEASE SPECIFY THE PATH IN THE BASH FILE"

# SPECIFY THE LOCATION WHERE YOU WOULD LIKE THE FOLDER TO BE CREATED:
path=/home/utente/University/AbilInfo22_23/Data

# Make the directory 'Bernocco_AbilInfo' in the specified location
mkdir $path/Bernocco_AbilInfo

# Download the 'perAbInf.tgz' folder from the given link
wget -P $path/Bernocco_AbilInfo/ https://adlibitum.oats.inaf.it/monaco/etc/perAbInf.tgz

# Extract the compressed file in the same folder and delete the compressed one
tar -xzf $path/Bernocco_AbilInfo/perAbInf.tgz -C $path/Bernocco_AbilInfo/
rm -r $path/Bernocco_AbilInfo/perAbInf.tgz

# Move the 'MockMeasures_2PCF_Test{i}' files to the parent directory Bernocco_AbilInfo delitin the useless subfolder 'data'
cd $path/Bernocco_AbilInfo/data/
mv * ../
rm -d $path/Bernocco_AbilInfo/data/
   