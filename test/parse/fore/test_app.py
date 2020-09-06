import os
from src.parse.opensource.project.ProjectParser import ProjectParser


if __name__ == "__main__":
    base = "/home/qwe/disk2/Repos/"
    all_projects = [base + "/" + p for p in os.listdir(base)]
    maven_projects = []
    gradle_projects = []
    for project in all_projects:
        parser = ProjectParser(project)
        if parser.is_maven_project():
            maven_projects.append(project)
        if parser.is_gradle_project():
            gradle_projects.append(project)

    print(len(all_projects))
    print(len(maven_projects))
    print(len(gradle_projects))
