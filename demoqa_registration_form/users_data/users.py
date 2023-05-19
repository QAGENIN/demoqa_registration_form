import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: [str]
    subject: str
    hobby: str
    picture_file: str
    address: str
    state: str
    city: str


student = User(
    first_name='Test',
    last_name='Test',
    email='test@test.com',
    gender='Male',
    phone_number='1234567891',
    date_of_birth=['24', 'August', '1994'],
    subject='Maths',
    hobby='Sports',
    picture_file='test.png',
    address='Test-city, test street, test house 2',
    state='NCR',
    city='Delhi',
)
