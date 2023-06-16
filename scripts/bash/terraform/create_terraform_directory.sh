#!/bin/bash

## simple bash script to create a default directory and .tf files for terraform - edit this to suit your environment.

# Create the directories
mkdir -p global/iam
mkdir -p global/s3
mkdir -p prod/services/ec2
mkdir -p prod/vpc
mkdir -p uat/services/ec2
mkdir -p uat/vpc

# Create the files
touch global/iam/main.tf global/iam/variables.tf global/iam/outputs.tf
touch global/s3/main.tf global/s3/variables.tf global/s3/outputs.tf
touch prod/services/ec2/main.tf prod/services/ec2/variables.tf prod/services/ec2/outputs.tf
touch prod/vpc/main.tf prod/vpc/variables.tf prod/vpc/outputs.tf
touch uat/services/ec2/main.tf uat/services/ec2/variables.tf uat/services/ec2/outputs.tf
touch uat/vpc/main.tf uat/vpc/variables.tf uat/vpc/outputs.tf

# Display success message
echo "Directory structure and files created successfully."
