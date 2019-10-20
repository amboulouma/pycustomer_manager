# Customer manager program

import logging

logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
fh = logging.FileHandler('customer_manager.log', 'w')
fh.setFormatter(formatter)

logger.addHandler(fh)

# The customer class
class Customer():
    # Initialization with parameters and exceptions
    def __init__(self, name, age, height, zipcode, city):
        logging.info(f'Creating customer ({name}, {age}, {height}, {zipcode}, {city})')
        if not isinstance(name, str):
            raise TypeError('"' + str(name) + '" : ' + 'name must be a string')
        if len(name) < 2 or len(name) > 25:
            raise AttributeError('"' + str(name) + '" : ' + 'name length should be at least 2 character and at most 25 characters')
        if any(list(map(lambda c:c.isdigit(), list(name)))):
            raise AttributeError('"' + str(name) + '" : ' + 'name shouldn\'t contain any digits')
        self.name = name
        
        if not isinstance(age, int):
            raise TypeError('"' + str(age) + '" : ' + 'age must be an integer')
        if age < 0 or age > 150:
            raise AttributeError('"' + str(age) + '" : ' + 'age should be greater or equal to 0 and smaller or equal to 150')
        self.age = age

        if not isinstance(height, int):
            raise TypeError('"' + str(height) + '" : ' + 'height must be an integer')
        if height < 20 or height > 250:
            raise AttributeError('"' + str(height) + '" : ' + 'height should be greater or equal to 20 and smaller or equal to 250')
        self.height = height

        if not isinstance(zipcode, int):
            raise TypeError('"' + str(zipcode) + '" : ' + 'zipcode must be an integer')
        if zipcode < 0 or zipcode > 100000:
            raise AttributeError('"' + str(zipcode) + '" : ' + 'zipcode should be greater or equal to 0 and smaller or equal to 100000')
        self.zipcode = zipcode

        if not isinstance(city, str):
            raise TypeError('"' + str(city) + '" : ' + 'city must be a string')
        if len(city) < 2 or len(city) > 25:
            raise AttributeError('"' + str(city) + '" : ' + 'city length should contain at least 2 character and at most 25 characters')
        if any(list(map(lambda c:c.isdigit(), list(city)))):
            raise AttributeError('"' + str(city) + '" : ' + 'city shouldn\'t contain any digits')
        self.city = city
        logging.info(f'Customer {self.__dict__} has been created')

    # Setters with error handling for each value on set
    def _set_name(self, name):
        logging.info(f'Setting the new name ({name}) to the customer {self.__dict__}')
        if not isinstance(name, str):
            raise TypeError('"' + str(name) + '" : ' + 'name must be a string')
        if len(name) < 2 or len(name) > 25:
            raise AttributeError('"' + str(name) + '" : ' + 'name length should be at least 2 character and at most 25 characters')
        if any(list(map(lambda c:c.isdigit(), list(name)))):
            raise AttributeError('"' + str(name) + '" : ' + 'name shouldn\'t contain any digits')
        self.name = name
        logging.info(f'New name ({name}) to the customer {self.__dict__} set')

    def _set_age(self, age):
        logging.info(f'Setting the new age ({age}) to the customer {self.__dict__}')
        if not isinstance(age, int):
            raise TypeError('"' + str(age) + '" : ' + 'age must be an integer')
        if age < 0 or age > 150:
            raise AttributeError('"' + str(age) + '" : ' + 'age should be greater or equal to 0 and smaller or equal to 150')
        self.age = age
        logging.info(f'New age ({age}) to the customer {self.__dict__} set')

    def _set_height(self, height):
        logging.info(f'Setting the new height ({height}) to the customer {self.__dict__}')
        if not isinstance(height, int):
            raise TypeError('"' + str(height) + '" : ' + 'height must be an integer')
        if height < 20 or height > 250:
            raise AttributeError('"' + str(height) + '" : ' + 'height should be greater or equal to 20 and smaller or equal to 250')
        self.height = height
        logging.info(f'New height ({height}) to the customer {self.__dict__} set')

    def _set_zipcode(self, zipcode):
        logging.info(f'Setting the new zipcode ({zipcode}) to the customer {self.__dict__}')
        if not isinstance(zipcode, int):
            raise TypeError('"' + str(zipcode) + '" : ' + 'zipcode must be an integer')
        if zipcode < 0 or zipcode > 100000:
            raise AttributeError('"' + str(zipcode) + '" : ' + 'zipcode should be greater or equal to 0 and smaller or equal to 100000')
        self.zipcode = zipcode
        logging.info(f'New zipcode ({zipcode}) to the customer {self.__dict__} set')

    def _set_city(self, city):
        logging.info(f'Setting the new city ({city}) to the customer {self.__dict__}')
        if not isinstance(city, str):
            raise TypeError('"' + str(city) + '" : ' + 'city must be a string')
        if len(city) < 2 or len(city) > 25:
            raise AttributeError('"' + str(city) + '" : ' + 'city length should contain at least 2 character and at most 25 characters')
        if any(list(map(lambda c:c.isdigit(), list(city)))):
            raise AttributeError('"' + str(city) + '" : ' + 'city shouldn\'t contain any digits')
        self.city = city
        logging.info(f'New city ({city}) to the customer {self.__dict__} set')
    

# Find the oldest customer of a list of customers
def find_oldest_customer(customers):
    logging.info(f'Finding oldest customer in {[c.__dict__ for c in customers]}')
    logging.info(f'Oldest customer found is {max(customers, key=lambda custumer:custumer.age).__dict__}')
    return max(customers, key=lambda custumer:custumer.age)

# Find the youngest customer of a list of customers
def find_youngest_customer(customers):
    logging.info(f'Finding youngest customer in {[c.__dict__ for c in customers]}')
    logging.info(f'Youngest customer found is {min(customers, key=lambda custumer:custumer.age).__dict__}')
    return min(customers, key=lambda custumer:custumer.age)

# Compare two customers
def compare_customers(customer_1, customer_2):
    logging.info(f'Comparing {customer_1.__dict__} to {customer_2.__dict__}')
    for ((key_1, value_1), (key_2, value_2)) in zip(customer_1.__dict__.items(), customer_2.__dict__.items()):
        if value_1 != value_2:
            logging.info(f'''The customer {customer_1.name} and the customer {customer_2.name} have different {key_1} attributes : {value_1} not equal {value_2}''')        
        else:
            logging.info(f'''The customer {customer_1.name} and the customer {customer_2.name} have the same {key_1} attribute''')

# Generate customers data
def generate_no_errors_customers_data_list():
    logging.info(f'Generating a list of no errors cuctomers')
    customers_names     = ['Ted', 'Jack', 'Med', 'Line', 'Missy']
    customers_ages      = [21, 34, 53, 31, 76]
    customers_heights   = [181, 179, 161, 158, 178]
    customers_zipcodes  = [1010, 1050, 28100, 69100, 1070]
    customers_cities    = ['Vienna', 'Vienna', 'Mohammedia', 'Lyon', 'Vienna']
    customers_data_list = [c for c in zip(customers_names, customers_ages, customers_heights, customers_zipcodes, customers_cities)]
    logging.info(f'The list {customers_data_list} has been created')
    return customers_data_list

def generate_errors_customers_data_list():
    logging.info(f'Generating a list of errors cuctomers')
    error_customers_names     = ['Ted1', 'k', 'a'*26, 1]
    error_customers_ages      = ['a', -1, -1, 200]
    error_customers_heights   = ['a', -1, -1, 300]
    error_customers_zipcodes  = ['a', -1, -1, 100001]
    error_customers_cities    = ['Vienna1', 'k', 'a'*26, 1]
    error_customers_data_list = [c for c in zip(error_customers_names, error_customers_ages, error_customers_heights, error_customers_zipcodes, error_customers_cities)]
    logging.info(f'The list {error_customers_data_list} has been created')
    return error_customers_data_list

# Create customers
def create_customers():
    logging.info(f'Creating a list of customers')
    customers = [Customer(*c) for c in generate_no_errors_customers_data_list()]
    logging.info(f'Customers {[c.__dict__ for c in customers]} have been created')
    return customers

# Error based customers instanciation
def test_error_customers_entries():
    logging.info(f'Testing error customers entries')
    error_customers_data_list = generate_errors_customers_data_list()
    customer = Customer('test', 0, 100, 0, 'test')
    for c in error_customers_data_list:
        try:
            customer._set_name(c[0])
        except Exception as e:
            logging.error(e)
        try:
            customer._set_age(c[1])
        except Exception as e:
            logging.error(e)
        try:
            customer._set_height(c[2])
        except Exception as e:
            logging.error(e)
        try:
            customer._set_zipcode(c[3])
        except Exception as e:
            logging.error(e)
        try:
            customer._set_city(c[4])
        except Exception as e:
            logging.error(e)
    logging.info(f'All error customers entries have been tested')

# Testing functions
def test_functions():
    customers = [Customer(*c) for c in generate_no_errors_customers_data_list()]
    logging.info(f'Testing find the oldest customer function')
    find_oldest_customer(customers)
    logging.info(f'Testing find the youngest customer function')
    find_youngest_customer(customers)
    logging.info(f'Testing the compare customers function')
    for c_1 in range(4):
        for c_2 in range(4):
            compare_customers(customers[c_1], customers[c_2])

# Running the functions and the tests
create_customers()
test_error_customers_entries()
test_functions()
