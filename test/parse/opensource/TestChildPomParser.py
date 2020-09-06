from src.parse.opensource.pom.ChildPomParser import ChildPomParser
import unittest


class TestChildPomParser(unittest.TestCase):
    def setUp(self):
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/svn2github-aTunes/" \
                     "aTunes/plugins/instantmessaging/pom.xml"

    def test_get_installing_name(self):
        parser = ChildPomParser(self.path1)
        print(parser.get_jar_name())


if __name__ == "__main__":
    unittest.main()