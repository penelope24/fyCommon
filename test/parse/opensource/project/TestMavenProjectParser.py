import unittest
from src.parse.opensource.project.MavenProjectParser import MavenProjectParser


class TestMavenProjectParser(unittest.TestCase):

    def setUp(self):
        # a standard multi-module project
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/" \
                    "spring-data-mongodb/"

        # a project with many modules
        self.path2 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-ide/spring-ide"

        # a single-module projects
        self.path3 = "/home/qwe/zfy_lab/fyProgramAnalysis"

        # a maven project with deep pom files (pom.xml not appear in top 2 level dirs)
        self.path4 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/eclipse-efxclipse-rt"

    def test_get_root_pom(self):
        parser1 = MavenProjectParser(self.path1)
        parser3 = MavenProjectParser(self.path3)
        parser4 = MavenProjectParser(self.path4)
        self.assertEqual(parser1._get_root_pom(), "/home/qwe/disk1/zfy_lab/bigcode_data/projects/"
                                                  "spring-projects-spring-data-mongodb/spring-data-mongodb/pom.xml")
        self.assertEqual(parser3._get_root_pom(), "/home/qwe/zfy_lab/fyProgramAnalysis/pom.xml")
        self.assertEqual(parser4._get_root_pom(), "/home/qwe/disk1/zfy_lab/bigcode_data/projects/eclipse-efxclipse-rt/efxclipse-rt/modules/pom.xml")

    def test_get_all_child_poms(self):
        parser1 = MavenProjectParser(self.path1)
        parser3 = MavenProjectParser(self.path3)
        self.assertEqual(len(parser1.get_all_poms()), 4)
        self.assertEqual(len(parser3.get_all_poms()), 1)


if __name__ == "__main__":
    unittest.main()