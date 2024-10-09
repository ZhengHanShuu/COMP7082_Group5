from pydantic import BaseModel, Field
from typing import List, Optional


class Exercise(BaseModel):
    """
    Represents a single exercise within a workout routine.

    Attributes:
        name (str): The name of the exercise.
        duration (Optional[int]): The duration of the exercise in seconds.
        repetitions (Optional[int]): The number of repetitions for the exercise.
        sets (Optional[int]): The number of sets for the exercise.
    """
    name: str
    duration: Optional[int] = Field(
        default=None, description="Duration in seconds")
    repetitions: Optional[int] = Field(
        default=None, description="Number of repetitions")
    sets: Optional[int] = Field(default=None, description="Number of sets")


class Routine(BaseModel):
    """
    Represents a workout routine containing multiple exercises.

    Attributes:
        id (str): The id of the workout routine.
        name (str): The name of the workout routine.
        exercises (List[Exercise]): A list of exercises included in the routine.
        difficulty (Optional[str]): The difficulty level of the workout, defaults to "Intermediate".
        total_duration (Optional[int]): The total duration of the workout in minutes.
    """
    id: Optional[str] = None
    name: str
    exercises: List[Exercise]
    difficulty: Optional[str] = Field(
        default="Intermediate", description="Difficulty level of the workout")
    total_duration: Optional[int] = Field(
        default=None, description="Total duration of the workout in minutes")
