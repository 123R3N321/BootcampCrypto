import re

def parse_requirements(file_path):
    """
    Parse a requirements.txt file and return a dictionary of package name -> version.
    """
    requirements = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            # Strip spaces and ignore comments
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Handle versioned requirements
            match = re.match(r'([a-zA-Z0-9\-_.]+)(==[^#]*)?', line)
            if match:
                package = match.group(1)
                version = match.group(2) if match.group(2) else ""
                requirements[package] = version

    return requirements

def update_requirements():
    '''
    will :
    1. update server requirement based on local
    2. check if gunicorn is in there. If not:
        - ask for version preferred, if empty, default 23.0.0
        - add to the server requirements
    '''
    # Define the file paths
    root_requirements_path = '../requirements.txt'
    server_requirements_path = '../server/requirements.txt'

    # Parse both requirements files into dictionaries
    root_requirements = parse_requirements(root_requirements_path)
    server_requirements = parse_requirements(server_requirements_path)

    # Find the dependencies from root_requirements that are not in server_requirements
    new_requirements = {pkg: version for pkg, version in root_requirements.items() if pkg not in server_requirements or server_requirements[pkg] != version}

    if "gunicorn" not in server_requirements:
        print("gunicorn missing from server side requirements. Adding it...")
        ver = str(input("specify gunicon version needed. (Suggested: 23.0.0): "))
        if not ver:
            ver = "23.0.0"
        new_requirements["gunicorn"] = ver

    # If there are new dependencies, append them to the server requirements.txt
    if new_requirements:
        with open(server_requirements_path, 'a') as file:
            for pkg, version in new_requirements.items():
                if version:
                    file.write(f"{pkg}{version}\n")
                else:
                    file.write(f"{pkg}\n")
        print(f"Added {len(new_requirements)} new dependencies to {server_requirements_path}.")
    else:
        print("No new dependencies to add.")

if __name__ == '__main__':
    update_requirements()