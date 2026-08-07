from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
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
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.supplier_schema import (
    SupplierCreateRequest,
    SupplierResponse,
    SupplierUpdateRequest,
)
from src.services.supplier_service import (
    SupplierService,
)


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_supplier_service(
    session: SessionDependency,
) -> SupplierService:
    """
    Cria o serviço de fornecedores
    com suas dependências.
    """

    repository = SupplierRepository(
        session
    )

    return SupplierService(
        repository
    )


SupplierServiceDependency = Annotated[
    SupplierService,
    Depends(get_supplier_service),
]


def raise_supplier_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio
    em respostas HTTP.
    """

    message = str(error)

    if message == "Fornecedor não encontrado.":
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    if message == (
        "Já existe um fornecedor com este "
        "documento."
    ):
        raise HTTPException(
            status_code=(
                status.HTTP_409_CONFLICT
            ),
            detail=message,
        ) from error

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.post(
    "",
    response_model=SupplierResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar fornecedor",
)
def create_supplier(
    request: Annotated[
        SupplierCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
) -> SupplierResponse:
    """
    Cadastra um novo fornecedor.

    Operação permitida ao Administrador Master
    e ao Comprador.
    """

    try:
        supplier = service.create(
            name=request.name,
            document=request.document,
            address=request.address,
            notes=request.notes,
        )

        session.commit()

        session.refresh(
            supplier
        )

        return SupplierResponse.model_validate(
            supplier
        )

    except ValueError as error:
        session.rollback()

        raise_supplier_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[SupplierResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar fornecedores",
)
def list_suppliers(
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
) -> list[SupplierResponse]:
    """
    Retorna todos os fornecedores cadastrados.

    A listagem contém fornecedores ativos
    e inativos.
    """

    suppliers = service.list_all()

    return [
        SupplierResponse.model_validate(
            supplier
        )
        for supplier in suppliers
    ]


@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar fornecedor",
)
def get_supplier(
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Consulta um fornecedor pelo identificador.
    """

    try:
        supplier = service.get_required(
            supplier_id
        )

        return SupplierResponse.model_validate(
            supplier
        )

    except ValueError as error:
        raise_supplier_http_exception(
            error
        )


@router.put(
    "/{supplier_id}",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar fornecedor",
)
def update_supplier(
    request: Annotated[
        SupplierUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Atualiza somente os campos enviados.

    Operação permitida ao Administrador Master
    e ao Comprador.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True,
        )

        supplier = service.update(
            supplier_id,
            **update_data,
        )

        session.commit()

        session.refresh(
            supplier
        )

        return SupplierResponse.model_validate(
            supplier
        )

    except ValueError as error:
        session.rollback()

        raise_supplier_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{supplier_id}/activate",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar fornecedor",
)
def activate_supplier(
    session: SessionDependency,
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Ativa um fornecedor que está inativo.
    """

    try:
        supplier = service.activate(
            supplier_id
        )

        session.commit()

        session.refresh(
            supplier
        )

        return SupplierResponse.model_validate(
            supplier
        )

    except ValueError as error:
        session.rollback()

        raise_supplier_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{supplier_id}/deactivate",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar fornecedor",
)
def deactivate_supplier(
    session: SessionDependency,
    service: SupplierServiceDependency,
    _current_user: AdminOrBuyerUserDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Desativa um fornecedor sem excluir
    seu histórico.
    """

    try:
        supplier = service.deactivate(
            supplier_id
        )

        session.commit()

        session.refresh(
            supplier
        )

        return SupplierResponse.model_validate(
            supplier
        )

    except ValueError as error:
        session.rollback()

        raise_supplier_http_exception(
            error
        )

    except Exception:
        session.rollback()
        raise