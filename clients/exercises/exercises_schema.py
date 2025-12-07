from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка задания для курса.
    """
    model_config = ConfigDict(populate_by_name=True)
    courseId: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)
    title: str
    courseId: str = Field(alias="courseId")
    maxScore: int = Field(alias="maxScore")
    minScore: int = Field(alias="minScore")
    orderIndex: int = Field(alias="orderIndex")
    description: str
    estimatedTime: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None = Field(alias="maxScore")
    minScore: int | None = Field(alias="minScore")
    orderIndex: int | None = Field(alias="orderIndex")
    description: str | None
    estimatedTime: str | None = Field(alias="estimatedTime")

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение списка заданий.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
     Описание структуры ответа на получение задания..
     """
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema

class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema