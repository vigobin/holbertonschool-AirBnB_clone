# AirBnB clone - The console

## Description
This partner project is the first step towards building a first full web application: the AirBnB clone.
It consists of a command interpreter, the base classes, file storage, and unit tests.

## Requirements
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
* The code should use the pycodestyle (version 2.7.*).
* All modulesand classes should have a documentation.

## Command Interpreter
The console works like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.
* Run the console using `./console.py`
* Quit the console with `(hbnb) quit`
* Display the help using `(hbnb) help`

## Models
The models folder contains the classes for the project.
* `base_model.py`: The BaseModel class for all the other classes.	
* `user.py`: The User class for future user information	email, password, first_name, last_name.
* `amenity.py`:	Amenity class for future amenity information.
* `city.py`: City class for future location information.
* `state.py`: State class for future location information.
* `place.py`: Place class for future accomodation information.
* `review.py`: Review class for future user/host review information.

## File Storage
The folder engine manages the serialization and deserialization of all the data, following a JSON format.
* `file_storage.py` contains the `FileStorage` class that serializes instances to a JSON file and deserializes JSON file to instances

## Tests
* All the code is tested with the unittest module. The test for the classes are in the test_models folder.

## Authors
* Darah Thomas <jdarahthomas@gmail.com>
* Vishal Gobin <5547@holbertonstudents.com>
