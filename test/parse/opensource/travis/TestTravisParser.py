import unittest
import json


class TestTravisParser(unittest.TestCase):

    def setUp(self) -> None:
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/eclipse-efxclipse-rt/efxclipse-rt"


# if __name__ == "__main__":
json_file = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/eclipse-efxclipse-rt/efxclipse-rt/.travis.yml"
with open(json_file) as json_data:
    data =json.load(json_data)
    print("json", data)
