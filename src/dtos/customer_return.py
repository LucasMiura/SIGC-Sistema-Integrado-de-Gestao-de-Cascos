from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class CustomerReturnOriginItemDTO:
    part_id: int
    part_code: str
    part_name: str

    outbound_quantity: int
    returned_quantity: int
    pending_quantity: int


@dataclass(
    frozen=True,
    slots=True,
)
class CustomerReturnOriginDTO:
    outbound_id: int

    return_type: str
    reference_number: str
    customer_name: str

    items: tuple[
        CustomerReturnOriginItemDTO,
        ...,
    ]

    total_outbound_quantity: int
    total_returned_quantity: int
    total_pending_quantity: int