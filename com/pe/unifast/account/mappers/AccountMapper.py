from ..schemas.AccountDto import AccountDto  as Dto
from ..schemas.AccountResponseDto import AccountResponseDto as ResponseDto
from ..domain.entities.Account import Account as Entity

class AccountMapper:
    #dto to entity
    @staticmethod
    def dto_to_entity(dto: Dto) -> Entity:
        return Entity(**dto)
    #entity to dto
    @staticmethod
    def entity_to_dto(entity: Entity) -> Dto:
        return Dto(**entity)
    #entity to response dto
    @staticmethod
    def entity_to_response_dto(entity: Entity) -> ResponseDto:
        return ResponseDto(**entity)
    #list of entities to list of dtos
    
    @staticmethod
    def list_entity_to_list_dto(entities: list[Entity]) -> list[Dto]:
        return [Dto(**entity) for entity in entities]
    #list of entities to list of response dtos
    @staticmethod
    def list_entity_to_list_response_dto(entities: list[Entity]) -> list[ResponseDto]:
        return [ResponseDto(**entity) for entity in entities]
    #list of dtos to list of entities
    @staticmethod
    def list_dto_to_list_entity(dtos: list[Dto]) -> list[Entity]:
        return [Entity(**dto) for dto in dtos]
    

