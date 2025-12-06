from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request['email'],
    password=create_user_request['password']
)
private_users_client = get_private_users_client(authentication_user)

files_client = get_files_client(authentication_user)
courses_client= get_courses_client(authentication_user)


create_file_request = CreateFileRequestDict(
    filename="image.jpg",
    directory="courses",
    upload_file="./testdata/files/image.jpg"
)

create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

create_course_dict = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_dict)
print(f"Create course data {create_course_response}")