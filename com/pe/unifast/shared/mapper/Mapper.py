from typing import Type, TypeVar, Any
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta


T=TypeVar('T', bound=BaseModel)
E=TypeVar('E', bound=DeclarativeMeta)
R= TypeVar('R', bound=BaseModel)


class Mapper:
    #dto to entity
    @staticmethod
    def dto_to_entity(dto: T,entity_class:Type[E]) -> E:
        return entity_class(**dto)
    #entity to dto
    @staticmethod
    def entity_to_dto(entity: E,dto_class:Type[T]) -> T:
        return dto_class(**entity)
    #entity to response dto
    @staticmethod
    def entity_to_response_dto(entity: E,response_dto_class:Type[R]) -> R:
        return response_dto_class(**entity)
    #list of entities to list of dtos
    @staticmethod
    def list_entity_to_list_dto(entities: list[E],dto_class:Type[T]) -> list[T]:
        return [dto_class(**entity) for entity in entities]
    #list of entities to list of response dtos
    @staticmethod
    def list_entity_to_list_response_dto(entities: list[E],response_dto_class:Type[R]) -> list[R]:
        return [response_dto_class(**entity) for entity in entities]
    #list of dtos to list of entities
    @staticmethod
    def list_dto_to_list_entity(dtos: list[T],entity_class:Type[E]) -> list[E]:
        return [entity_class(**dto) for dto in dtos]
    

