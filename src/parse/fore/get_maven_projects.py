import os
from src.parse.opensource.project.ProjectParser import ProjectParser

# dataset 1
path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1"
target1 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data1/maven_projects"

# dataset 2
path2 = "/home/qwe/disk2/Repos"
target2 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data2/maven_projects"

# dataset 3
path3 = "/home/qwe/disk2/85_3000/repository"
target3 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data3/maven_projects"

new_base1 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1"
new_base2 = "/home/qwe/disk1/zfy_lab/bigcode_data/data2"
new_base3 = "/home/qwe/disk1/zfy_lab/bigcode_data/data3"

if __name__ == "__main__":
    with open(target1, "w") as f:
        base = path1
        all_projects1 = os.listdir(base)
        maven_projects1 = []
        for project in all_projects1:
            parser = ProjectParser(base + "/" + project)
            if parser.is_maven_project():
                # print(project)
                maven_projects1.append(new_base1 + "/" + project)
                f.write(new_base1 + "/" + project)
                f.write("\n")

    with open(target2, "w") as f:
        base = path2
        all_projects2 = os.listdir(base)
        maven_projects2 = []
        for project in all_projects2:
            parser = ProjectParser(base + "/" + project)
            if parser.is_maven_project():
                # print(project)
                maven_projects2.append(new_base2 + "/" + project)
                f.write(new_base2 + "/" + project)
                f.write("\n")

    with open(target3, "w") as f:
        base = path3
        all_projects3 = os.listdir(base)
        maven_projects3 = []
        for project in all_projects3:
            parser = ProjectParser(base + "/" + project)
            if parser.is_maven_project():
                # print(project)
                maven_projects3.append(new_base3 + "/" + project)
                f.write(new_base3 + "/" + project)
                f.write("\n")

    print(len(all_projects1), len(maven_projects1))
    print(len(all_projects2), len(maven_projects2))
    print(len(all_projects3), len(maven_projects3))
    """
    329 175
    4164 511
    3792 2174
    """
