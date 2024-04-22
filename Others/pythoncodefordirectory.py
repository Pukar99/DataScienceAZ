import os

def create_directory_structure(project_directory):
    # Create the main project directory
    os.makedirs(project_directory, exist_ok=True)
    
    # Create subdirectories
    subdirectories = ['data/raw', 'data/processed', 'data/external',
                      'notebooks', 'scripts', 'models', 'reports']
    for subdir in subdirectories:
        os.makedirs(os.path.join(project_directory, subdir), exist_ok=True)
    
    # Create README.md file
    with open(os.path.join(project_directory, 'README.md'), 'w') as f:
        f.write("# Project Overview\n\nReplace this text with an overview of your project.")
    
    # Create requirements.txt file
    with open(os.path.join(project_directory, 'requirements.txt'), 'w') as f:
        f.write("# Project Requirements\n\nPut your project dependencies here.")
    
    # Create LICENSE file
    with open(os.path.join(project_directory, 'LICENSE'), 'w') as f:
        f.write("Put your license text here.")

# Example usage:
project_directory = 'my_data_science_project'
create_directory_structure(project_directory)
