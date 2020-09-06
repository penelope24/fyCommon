import unittest
from src.file.Traverse import Traverse


class TestTraverse(unittest.TestCase):

    def setUp(self) -> None:
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/"

    def test_list_dirs_by_depth(self):
        t = Traverse(self.path1)
        self.assertEqual(t.list_dirs_by_depth(0), ['spring-data-mongodb'])
        self.assertEqual(t.list_dirs_by_depth(1), ['spring-data-mongodb-benchmarks', 'spring-data-mongodb-distribution', 'spring-data-mongodb', 'ci', 'src', 'deps'])
        self.assertEqual(t.list_dirs_by_depth(0, abs=True), ['/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb'])

    def test_list_files_by_depth(self):
        t = Traverse(self.path1)
        self.assertEqual(t.list_files_by_depth(1), ['CONTRIBUTING.adoc', 'lombok.config', 'mvnw.cmd', 'Jenkinsfile', 'SECURITY.adoc', 'mvnw', 'CI.adoc', 'pom.xml', 'README.adoc'])
        self.assertEqual(t.list_files_by_depth(1, True), ['/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/CONTRIBUTING.adoc', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/lombok.config', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/mvnw.cmd', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/Jenkinsfile', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/SECURITY.adoc', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/mvnw', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/CI.adoc', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/pom.xml', '/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/spring-data-mongodb/README.adoc'])

    def test_find_files_by_depth(self):
        t = Traverse(self.path1)
        self.assertEqual(len(t.find_files_by_depth("pom.xml", 0)), 0)
        self.assertEqual(len(t.find_files_by_depth("pom.xml", 1)), 1)
        self.assertEqual(len(t.find_files_by_depth("pom.xml", 2)), 3)


if __name__ == "__main__":
    unittest.main()