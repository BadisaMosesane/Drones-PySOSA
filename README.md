
# Introduction - PySOSA
updated 2020.07.09


A python module for building SOSA  based RDF graphs


The LANDRS (Linked And Networked DRoneS) project amongst other things works to create an ontology and building an OpenAPI specification for creating a Restful API
for building linked data native drone data applications. LANDRS is a Sloan Foundation
funded project to build open source APIs for managing scientific data on drones through the
use of web standards and linked data technologies.

Updated PySOSA Design diagram is [here](https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA_Design.png)


The project endeavors to implement PySOSA: A python module for building SOSA  based RDF graphs.
Sensor, Observation, Sample, and Actuator (SOSA) ontology, provides a lightweight core for Semantic Sensor Network (SSN).
SOSA aims at broadening the target audience and application areas that can make use of Semantic Web ontologies.
To find out more about SOSA and SSN check out https://www.w3.org/TR/vocab-ssn/#SOSAPlatform  and https://www.w3.org/TR/vocab-ssn/ 

# Getting started

PySOSA is A python module for building RDF graphs using the W3C SOSA (Sensors, Observations, Samples,
and Actuators) ontology. For more see https://github.com/landrs-toolkit/PySOSA. In short PySOSA implements
a python-based Linked-Data API for Networked Drones.

Visit www.landrs.org or www.ld.landrs.org

# Requirements

We recommend Pycharm IDE, but this should work in any other IDE of choice.  To run this module successfully, ensure you have the pre-requisites correctly installed. You can install all the requirements by running
    
    $ pip install -r requirements.txt
    
See list of required libs here https://github.com/landrs-toolkit/PySOSA/blob/master/requirements.txt

The best way to install rdflib is to use pip. If the above install fails, install using pip as follows:
   
    $ pip install rdflib
    $ pip install PyLD
    $ pip install pytz
    $ pip -U install pylint
    $ install pyreverse
    


# How to install from Pypi

1. Pre Requisites. Before using, you must have the following: 
2. Installation. Install using pip: pip install pysosa [Link to pysosa pypi](https://github.com/landrs-toolkit/PySOSA)
3. Configuration. Configure all connection parameters on the IDE
4. Downloading the code! Run Your function
5. Checking your recently installed package.



# Generating Docs

How to generate the UML using Pycharm as a recommended IDE.

* cd into the directory of where the project resides
* Make sure pylint3 and graphviz are installed
* Run the command: $ pyreverse -S <modulename> to generate the dot files in the current folder
*       $ pyreverse -S <modulename>
* Once the dot files are generated use the following command to generate the output in one of the formats available
 *      $ dot -Tpdf <dotfilename> -o output
*     $ dot -Txxx shows all the available output formats

Install pylint3 from Install. If you have anaconda already installed use pip -U install pylint to update the pylint
so that pyreverse is added to the scripts folder.

Install Pyreverse

You need to install graphViz as the pyreverse generates the UML diagrams in dot format and needs the dot.exe
provided by Graphviz. Once GraphViz is installed make sure the bin folder is added to the PATH variable so that
pyreverse can find it at run time.

Install sphinx



# Running the Tests

The instructions for getting the project up and running on your local machine and testing purposes


E.g you can run tests for the platform class on the terminal as shown.

    $ python -m unittest test_Platform.py

Example for testing Sensor class:
*       $ python -m unittest test_Sensor.py
    


## Contributing

Pull requests and issue submissions are highly welcomed. This is an open project, published openly under Apache 2.0. We are
excited to have you contribute to this project!
See instructions on how you can contribute on this guide: https://github.com/landrs-toolkit/PySOSA/blob/master/CONTRIBUTING.md

    

# Issues
Navigate the git repo to find active issues. Some of the known issues include:
- Order of sensors and platform on the graph output to be fixed 
- The output of the graph needs to be formatted
- More tests needs to be done to cover all test cases
- Need to check if the function for adding objects to the graph does add and check duplicate
- Need a function that queries unit testing and code coverage
more unit testing needed

# License
This project is and always will be published openly under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)


## Contacts
 
* Get in touch with us on the [landrs website](https://www.landrs.org/)
* Email us at landrs@nd.edu
* Twitter Handle https://twitter.com/DroneData4Good




