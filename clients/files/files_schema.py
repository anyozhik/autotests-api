from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake

class FileSchema(BaseModel):  # Добавили структуру с токенами аутентификации
    """
    Описание структуры файла.
    """

    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """

    filename: str = Field(default_factory=lambda: f"{fake.uuid64()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema