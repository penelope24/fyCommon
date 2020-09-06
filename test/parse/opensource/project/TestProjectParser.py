import unittest
from src.parse.opensource.project.ProjectParser import ProjectParser


class TestProjectParser(unittest.TestCase):

    def setUp(self):
        # a standard maven project
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/"
        # an ant project
        self.path2 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/calint-a/"
        # a maven project with many modules
        self.path3 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-ide"
        # a maven project with deep pom files (pom.xml not appear in top 2 level dirs)
        self.path4 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/eclipse-efxclipse-rt"
        # a maven project with single pom file
        self.path5 = "/home/qwe/zfy_lab/fyProgramAnalysis"
        # a maven project, but its root dir has many files
        self.path6 = "/home/qwe/disk2/Repos/zoopaper"

    def test_is_maven_project(self):
        parser1 = ProjectParser(self.path1)
        parser2 = ProjectParser(self.path2)
        parser3 = ProjectParser(self.path3)
        parser4 = ProjectParser(self.path4)
        parser5 = ProjectParser(self.path5)
        parser6 = ProjectParser(self.path6)
        self.assertTrue(parser1.is_maven_project())
        self.assertFalse(parser2.is_maven_project())
        self.assertTrue(parser3.is_maven_project())
        self.assertTrue(parser4.is_maven_project())
        self.assertTrue(parser5.is_maven_project())
        self.assertTrue(parser6.is_maven_project())


if __name__ == "__main__":
    unittest.main()