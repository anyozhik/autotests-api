from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client()

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()

# Отправляем POST запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

files_client = get_files_client(authentication_user)
courses_client= get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)


create_file_request = CreateFileRequestSchema(upload_file="./testdata/files/image.jpg")

create_file_response = files_client.create_file(create_file_request)
print(f"Create file data: {create_file_response}")

create_course_dict = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_dict)
print(f"Create course data {create_course_response}")

create_exercise_request = CreateExerciseRequestSchema(courseId = create_course_response.course.id)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print(f"Create exercise data: {create_exercise_response}")



