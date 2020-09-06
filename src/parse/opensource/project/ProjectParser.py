import os
from src.file.Traverse import Traverse
from src.parse.opensource.pom.PomParser import PomParser


class ProjectParser:

    def __init__(self, path):
        self.path = path  # project root path

    # def is_maven_project(self):
    #     """
    #     to judge if a project is maven project -> it has one ore more than one pom.xml files
    #     1. if it has only one pom.xml, that means the pom.xml should be a non-trivial pom:
    #         (1) it should have a /src dir as sibling (very strict, only standard project structure) # FIXME
    #         (2) it should have <dependencies> property
    #         (3) it's <packaging> should be default or jar
    #     2. if it has multiple pom files:
    #         (1) the root pom should have <modules> property.
    #     :return:
    #     """
    #     check_files = list_files_within_depth(self.path, 4)
    #     pom_files = []
    #     for file in check_files:
    #         if str(file).split("/")[-1] == "pom.xml":
    #             pom_files.append(file)
    #     if len(pom_files) == 1:
    #         pom = pom_files[0]
    #         current_dir = "/".join(pom.split("/")[:-1])
    #         if "src" in os.listdir(current_dir):
    #             parser = PomParser(pom)
    #             if parser.find_node(parser.root_node, "dependencies") is not None and parser.is_jar_pom():
    #                 return True
    #         return False
    #     elif len(pom_files) > 1:
    #         # for pom in pom_files:
    #         #     parser = PomParser(pom)
    #         #     if parser.find_node(parser.root_node, "modules") is not None:
    #         #         return True
    #         # return False
    #         return True
    #     else:
    #         return False

    def is_maven_project(self):
        t = Traverse(self.path)
        first_level = t.list_files_by_depth(0)
        second_level = t.list_files_by_depth(1)
        third_level = t.list_files_by_depth(2)
        if "pom.xml" in first_level or "pom.xml" in second_level or "pom.xml" in third_level:
            return True
        return False

    def is_gradle_project(self):
        t = Traverse(self.path)
        first_level = t.list_files_by_depth(0)
        second_level = t.list_files_by_depth(1)
        third_level = t.list_files_by_depth(2)
        if "build.gradle" in first_level or "build.gradle" in second_level or "build.gradle" in third_level:
            return True
        return False
