<<<<<<< HEAD
import pyobs_pyobs
=======
from . import pyobs_pyobs


>>>>>>> 6b614c46346b96f235a84294ac1e0a9922c3a865
import rdflib


def test_Observation():
    obs = pyobs_pyobs.ObservationCollection(comment="mycol")
    this_graph = pyobs_pyobs.get_graph()
    print(this_graph.serialize(format='turtle'))


if __name__ == '__main__':
    test_Observation()
