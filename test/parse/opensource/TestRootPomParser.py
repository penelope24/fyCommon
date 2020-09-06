import unittest
from src.parse.opensource.pom.RootPomParser import RootPomParser


class TestRootPomParser(unittest.TestCase):

    def setUp(self):
        # a standard multi-module project
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1/spring-projects-spring-data-mongodb/" \
                     "spring-data-mongodb/pom.xml"

        # a multi-module project with large amount of modules
        # the sub-modules in the root pom are all not core
        # but there are some sub-modules that is core but not show in root pom, this part we choose to ignore
        # so we consider it has no core_artifact_paths
        self.path2 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1/spring-projects-spring-ide/spring-ide/pom.xml"

        # a single-module project
        self.path3 = "/home/qwe/zfy_lab/fyProgramAnalysis/pom.xml"

        # a project with a root pom.xml and many modules but none of these modules has a pom.xml, wtf
        self.path4 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1/DawnScience-scisoft-ui/scisoft-ui/pom.xml"

        # core root pom + core sub-module pom, but the root pom dont have any modules property
        # so it is considered as a single-module project
        self.path5 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1/OpenHFT-Chronicle-Queue/Chronicle-Queue/pom.xml"

        # deep level modules
        self.path6 = "/home/qwe/disk1/zfy_lab/bigcode_data/data1/speedment-speedment/speedment/pom.xml"

    def test_is_core(self):
        parser1 = RootPomParser(self.path1)
        parser2 = RootPomParser(self.path2)
        parser3 = RootPomParser(self.path3)
        parser4 = RootPomParser(self.path4)
        parser5 = RootPomParser(self.path5)
        self.assertFalse(parser1.is_core_pom())
        self.assertFalse(parser2.is_core_pom())
        self.assertTrue(parser3.is_core_pom())
        self.assertFalse(parser4.is_core_pom())
        self.assertTrue(parser5.is_core_pom())

    def test_get_core_artifact_paths(self):
        parser1 = RootPomParser(self.path1)
        parser2 = RootPomParser(self.path2)
        parser3 = RootPomParser(self.path3)
        parser4 = RootPomParser(self.path4)
        parser5 = RootPomParser(self.path5)
        parser6 = RootPomParser(self.path6)
        # print(parser5.get_core_paths())
        self.assertEqual(parser1.get_core_paths(), ['/home/qwe/disk1/zfy_lab/bigcode_data/data1/spring-projects-spring-data-mongodb/spring-data-mongodb/spring-data-mongodb$spring-data-mongodb-3.1.0-SNAPSHOT.jar'])
        self.assertEqual(parser2.get_core_paths(), [])
        self.assertEqual(parser3.get_core_paths(), ['/home/qwe/zfy_lab/fyProgramAnalysis$fyProgramAnalysis-1.0-SNAPSHOT.jar'])
        self.assertEqual(parser4.get_core_paths(), [])
        self.assertEqual(parser5.get_core_paths(), ['/home/qwe/disk1/zfy_lab/bigcode_data/data1/OpenHFT-Chronicle-Queue/Chronicle-Queue$chronicle-queue-5.19.76-SNAPSHOT.jar'])
        self.assertEqual(len(parser6.get_core_paths()), 40)

    def test_get_all_modules(self):
        parser1 = RootPomParser(self.path1)
        parser2 = RootPomParser(self.path2)
        parser3 = RootPomParser(self.path3)
        parser4 = RootPomParser(self.path4)
        parser5 = RootPomParser(self.path5)
        parser6 = RootPomParser(self.path6)
        self.assertEqual(len(parser1.get_all_submodules(parser1.root_build_path)), 2)
        self.assertEqual(parser3.get_all_submodules(parser3.root_build_path), [])
        self.assertEqual(parser4.get_all_submodules(parser4.root_build_path), [])
        self.assertEqual(parser5.get_all_submodules(parser5.root_build_path), [])
        self.assertEqual(len(parser6.get_all_submodules(parser6.root_build_path)), 52)


if __name__ == "__main__":
    unittest.main()
