## A program to demonstrate how to handle None values in a list of projects.

projects = ["website", "mobile app", "data analysis", None, "game development"]

for project in projects:
    if project is None:
        print("Project name is missing.")
    else:
        print(project)