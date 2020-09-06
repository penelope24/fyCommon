from src.parse.opensource.project.MavenProjectParser import MavenProjectParser
from src.parse.opensource.pom.RootPomParser import RootPomParser
import xml.etree.ElementTree as ET


"""
input: 
    a project path as an command line argument
output: 
    1. the build root path
    2. all target jars' absolute path
process:
    1. check the project is maven
    2. find root pom & build root path
    3. find all core poms from root pom
    4. generate all absolute jar names from core pom
"""

if __name__ == "__main__":
    path1 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data1/maven_projects"
    target1 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data1/build_property"

    path2 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data2/maven_projects"
    target2 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data2/build_property"

    path3 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data3/maven_projects"
    target3 = "/home/qwe/disk1/zfy_lab/fy_ipvnb/inf/data3/build_property"

    empty_count1 = 0
    true_count1 = 0
    with open(path1, "r") as f1:
        with open(target1, "w") as f2:
            for line in f1.readlines():
                project_path = line.strip()
                project_parser = MavenProjectParser(project_path)
                build_path = project_parser.root_build_path
                pom_parser = RootPomParser(project_parser.root_pom)
                target_paths = pom_parser.get_core_paths()
                if target_paths is not None:
                    target_path_str = "##".join(target_paths) if len(target_paths) > 0 else ""
                    total_str = build_path + ":::" + target_path_str
                    if len(target_paths) == 0:
                        empty_count1 += 1
                        print(total_str)
                    else:
                        f2.write(total_str + "\n")
                        true_count1 += 1

    empty_count2 = 0
    true_count2 = 0
    with open(path2, "r") as f1:
        with open(target2, "w") as f2:
            for line in f1.readlines():
                project_path = line.strip()
                project_parser = MavenProjectParser(project_path)
                build_path = project_parser.root_build_path
                pom_parser = RootPomParser(project_parser.root_pom)
                target_paths = pom_parser.get_core_paths()
                if target_paths is not None:
                    target_path_str = "##".join(target_paths) if len(target_paths) > 0 else ""
                    total_str = build_path + ":::" + target_path_str
                    if len(target_paths) == 0:
                        empty_count2 += 1
                        print(total_str)
                    else:
                        f2.write(total_str + "\n")
                        true_count2 += 1
    empty_count3 = 0
    true_count3 = 0
    with open(path3, "r") as f1:
        with open(target3, "w") as f2:
            for line in f1.readlines():
                try:
                    project_path = line.strip()
                    project_parser = MavenProjectParser(project_path)
                    build_path = project_parser.root_build_path
                    pom_parser = RootPomParser(project_parser.root_pom)
                    target_paths = pom_parser.get_core_paths()
                    if target_paths is not None:
                        target_path_str = "##".join(target_paths) if len(target_paths) > 0 else ""
                        total_str = build_path + ":::" + target_path_str
                        if len(target_paths) == 0:
                            empty_count3 += 1
                            print(total_str)
                        else:
                            f2.write(total_str + "\n")
                            true_count3 += 1
                except ET.ParseError as e:
                    continue
    print(empty_count1, empty_count2, empty_count3)
    print(true_count1, true_count2, true_count3)
