from abc import ABC, abstractmethod
from typing import List, Optional

from pymongo import MongoClient
from bson import ObjectId

from infra.models import Routine


class IRoutineRepository(ABC):
    """
    Interface for the Workout Routine repository, defining the methods for data operations.
    """
    @abstractmethod
    def add(self, routine: Routine) -> str:
        """
        Add a new workout routine and return its ID.

        Args:
            routine (Routine): The workout routine to create.

        Returns:
            str: The ID of the created workout routine.
        """
        pass

    @abstractmethod
    def get(self, routine_id: str) -> Optional[Routine]:
        """
        Retrieve a workout routine by its ID.

        Args:
            routine_id (str): The ID of the routine to retrieve.

        Returns:
            Optional[Routine]: The retrieved workout routine, or None if not found.
        """
        pass

    @abstractmethod
    def list(self) -> List[Routine]:
        """
        List all workout routines.

        Returns:
            List[Routine]: A list of all workout routines. 
                                 This list may be empty if no routines are available.
       """
        pass

    @abstractmethod
    def update(self, routine_id: str, routine: Routine) -> bool:
        """
        Update a workout routine by its ID and return success status.

        Args:
            routine_id (str): The ID of the routine to update.
            routine (Routine): The updated workout routine object containing the new data.

        Returns:
            bool: True if the removal was successful, False otherwise.
        """
        pass

    @abstractmethod
    def remove(self, routine_id: str) -> bool:
        """
        Remove a workout routine by its ID and return success status.

        Args:
            routine_id (str): The ID of the routine to remove.

        Returns:
            bool: True if the removal was successful, False otherwise.
        """


class RoutineRepository(IRoutineRepository):
    def __init__(self, mongo_uri: str, db_name: str):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db["routines"]

    def add(self, routine: Routine) -> str:
        routine_dict = routine.model_dump(exclude={"id"})
        result = self.collection.insert_one(routine_dict)
        return str(result.inserted_id)

    def get(self, routine_id: str) -> Optional[Routine]:
        routine_dict = self.collection.find_one({"_id": ObjectId(routine_id)})
        if routine_dict:
            routine_dict["id"] = str(routine_dict.pop("_id"))
            return Routine(**routine_dict)
        return None

    def list(self) -> List[Routine]:
        routines = []
        for routine_dict in self.collection.find():
            routine_dict["id"] = str(routine_dict.pop("_id"))
            routines.append(Routine(**routine_dict))
        return routines

    def update(self, routine_id: str, routine: Routine) -> bool:
        update_data = routine.model_dump(exclude={"id"})
        result = self.collection.update_one(
            {"_id": ObjectId(routine_id)}, {"$set": update_data})
        return result.modified_count > 0

    def remove(self, routine_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(routine_id)})
        return result.deleted_count > 0
