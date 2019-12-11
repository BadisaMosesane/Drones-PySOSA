import unittest
<<<<<<< HEAD
import pyobs_pyobs
import rdflib
from rdflib import Graph, URIRef, Literal
=======
from . import pyobs_pyobs
import rdflib
>>>>>>> 6b614c46346b96f235a84294ac1e0a9922c3a865


class MyTestCase(unittest.TestCase):

    def test_add_sensor(self):
<<<<<<< HEAD
        obs = pyobs_pyobs.ObservationCollection(comment="mycol")
=======
        obs = pyobs_pyobs.Platform(comment="mycol")
>>>>>>> 6b614c46346b96f235a84294ac1e0a9922c3a865
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_remove_sensor(self):
        obs = pyobs_pyobs.ObservationCollection(comment='mycol2')
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_Observation(self):
        obs = pyobs_pyobs.ObservationCollection(comment="mycol")
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))


    def test_Sensor(self):
        obs = pyobs_pyobs.ObservationCollection(comment='mycol3')
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))


if __name__ == '__main__':
    unittest.main()


