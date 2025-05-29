from typing import List
from xml.etree import ElementTree as ET

from app.models import TestCase, TestSuite


def parse_testsuite_element(elem) -> TestSuite:
    name = elem.attrib.get("name")
    time = float(elem.attrib.get("time", "0"))

    testcases = []
    children = []

    for child in elem:
        if child.tag == "testcase":
            status = "passed"
            failure_message = None
            failure = child.find("failure")
            if failure is not None:
                status = "failed"
                failure_message = failure.attrib.get("message", "")

            testcases.append(
                TestCase(
                    name=child.attrib["name"],
                    classname=child.attrib.get("classname", ""),
                    time=float(child.attrib.get("time", "0")),
                    status=status,
                    failure_message=failure_message,
                )
            )
        elif child.tag == "testsuite":
            children.append(parse_testsuite_element(child))

    return TestSuite(name=name, time=time, testcases=testcases, children=children)


def parse_junit_xml(xml_path: str) -> List[TestSuite]:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    return [parse_testsuite_element(ts) for ts in root.findall("testsuite")]
