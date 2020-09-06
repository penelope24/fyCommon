import os
from src.parse.opensource.project.ProjectParser import ProjectParser


base1 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data1"
base2 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data2"
base3 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data3"

path1 = '/home/qwe/disk1/zfy_lab/bigcode_data/projects/'
path2 = "/home/qwe/disk2/Repos/"
path3 = "/home/qwe/disk2/85_3000/repository"


all_projects = [path3 + "/" + p for p in os.listdir(path3)]
maven_projects = []
for project in all_projects:
    parser = ProjectParser(project)
    if parser.is_maven_project():
        # print(project)
        maven_projects.append(project)
print(len(all_projects), len(maven_projects))
