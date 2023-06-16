import os
import subprocess

def create_directory_structure():
    # Define the directory structure
    structure = {
        "global": {
            "iam": ["main.tf", "variables.tf", "outputs.tf"],
            "s3": ["main.tf", "variables.tf", "outputs.tf"]
        },
        "prod": {
            "services": {
                "ec2": ["main.tf", "variables.tf", "outputs.tf"]
            },
            "vpc": ["main.tf", "variables.tf", "outputs.tf"]
        },
        "uat": {
            "services": {
                "ec2": ["main.tf", "variables.tf", "outputs.tf"]
            },
            "vpc": ["main.tf", "variables.tf", "outputs.tf"]
        }
    }

    parent_folder = input("Enter the parent folder path to create the directory structure (press Enter to use current working directory): ")
    if not parent_folder:
        parent_folder = os.getcwd()

    if not os.path.exists(parent_folder):
        print(f"The specified folder '{parent_folder}' does not exist.")
        choice = input("Do you want to create the directory structure in the current working directory? (Y/N): ")
        if choice.lower() != 'y':
            print("Exiting the program.")
            return

    # Create the directories and files
    for directory, subitems in structure.items():
        parent_dir = os.path.join(parent_folder, directory)
        os.makedirs(parent_dir, exist_ok=True)
        create_files(parent_dir, subitems)

    print("Directory structure and files created successfully.")

    # Execute the tree command on the directory
    tree_command = ["tree", parent_folder]
    subprocess.run(tree_command, check=True)

def create_files(directory, subitems):
    for item, content in subitems.items():
        if isinstance(content, dict):
            subdir = os.path.join(directory, item)
            os.makedirs(subdir, exist_ok=True)
            create_files(subdir, content)
        elif isinstance(content, list):
            for file in content:
                filepath = os.path.join(directory, item, file)
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                if not os.path.exists(filepath):
                    open(filepath, 'w').close()

# Execute the script
create_directory_structure()