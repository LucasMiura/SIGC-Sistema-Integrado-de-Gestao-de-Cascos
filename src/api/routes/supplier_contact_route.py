from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    status,
)
from sqlalchemy.orm import Session

from src.api.dependencies.authorization import (
    AdminOrBuyerUserDependency,
)
from src.database.connection import get_session
from src.repositories.supplier_contact_repository import (
    SupplierContactRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.supplier_contact_schema import (
    SupplierContactCreateRequest,
    SupplierContactResponse,
    SupplierContactUpdateRequest,
)
from src.services.supplier_contact_service import (
    SupplierContactService,
)


router = APIRouter(
    prefix="/suppliers/{supplier_id}/contacts",
    tags=["Supplier Contacts"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_supplier_contact_service(
    session: SessionDependency,
) -> SupplierContactService:
    """
    Monta o serviço de contatos de fornecedores
    com seus repositórios.
    """

    contact_repository = (
        SupplierContactRepository(
            session
        )
    )

    supplier_repository = (
        SupplierRepository(
            session
        )
    )

    return SupplierContactService(
        repository=contact_repository,
        supplier_repository=(
            supplier_repository
        ),
    )


SupplierContactServiceDependency = Annotated[
    SupplierContactService,
    Depends(get_supplier_contact_service),
]


def handle_contact_error(
    error: ValueError,
) -> HTTPException:
    """
    Converte erros de negócio
    em respostas HTTP.
    """

    message = str(error)

    not_found_messages = {
        "Fornecedor não encontrado.",
        "Contato não encontrado.",
    }

    if message in not_found_messages:
        return HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        )

    if message == (
        "O contato não pertence ao "
        "fornecedor informado."
    ):
        return HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        )

    return HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    )


@router.post(
    "",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar contato de fornecedor",
)
def create_supplier_contact(
    request: SupplierContactCreateRequest,
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierContactResponse:
    """
    Cadastra um novo contato.

    Operação permitida ao Administrador Master
    e ao Comprador.
    """

    try:
        contact = service.create(
            supplier_id=supplier_id,
            name=request.name,
            email=request.email,
            phone=request.phone,
            position=request.position,
            is_primary=request.is_primary,
        )

        session.commit()

        session.refresh(
            contact
        )

        return (
            SupplierContactResponse.model_validate(
                contact
            )
        )

    except ValueError as error:
        session.rollback()

        raise handle_contact_error(
            error
        ) from error

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[
        SupplierContactResponse
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar contatos de um fornecedor",
)
def list_supplier_contacts(
    service: SupplierContactServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> list[SupplierContactResponse]:
    """
    Lista todos os contatos do fornecedor.
    """

    try:
        contacts = service.list_by_supplier(
            supplier_id
        )

        return [
            SupplierContactResponse.model_validate(
                contact
            )
            for contact in contacts
        ]

    except ValueError as error:
        raise handle_contact_error(
            error
        ) from error


@router.get(
    "/{contact_id}",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar contato de fornecedor",
)
def get_supplier_contact(
    service: SupplierContactServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """
    Consulta um contato específico.
    """

    try:
        contact = service.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        return (
            SupplierContactResponse.model_validate(
                contact
            )
        )

    except ValueError as error:
        raise handle_contact_error(
            error
        ) from error


@router.put(
    "/{contact_id}",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar contato de fornecedor",
)
def update_supplier_contact(
    request: SupplierContactUpdateRequest,
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """
    Atualiza somente os campos enviados.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        contact = service.update(
            supplier_id=supplier_id,
            contact_id=contact_id,
            **update_data,
        )

        session.commit()

        session.refresh(
            contact
        )

        return (
            SupplierContactResponse.model_validate(
                contact
            )
        )

    except ValueError as error:
        session.rollback()

        raise handle_contact_error(
            error
        ) from error

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{contact_id}/activate",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar contato de fornecedor",
)
def activate_supplier_contact(
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """
    Ativa um contato inativo.
    """

    try:
        contact = service.activate(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        session.commit()

        session.refresh(
            contact
        )

        return (
            SupplierContactResponse.model_validate(
                contact
            )
        )

    except ValueError as error:
        session.rollback()

        raise handle_contact_error(
            error
        ) from error

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{contact_id}/deactivate",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar contato de fornecedor",
)
def deactivate_supplier_contact(
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """
    Desativa um contato sem eliminar
    seu histórico.
    """

    try:
        contact = service.deactivate(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        session.commit()

        session.refresh(
            contact
        )

        return (
            SupplierContactResponse.model_validate(
                contact
            )
        )

    except ValueError as error:
        session.rollback()

        raise handle_contact_error(
            error
        ) from error

    except Exception:
        session.rollback()
        raise