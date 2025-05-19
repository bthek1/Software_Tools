from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_block import AvailabilityBlock
    from ..models.list_availability_blocks_get_response_200_links import ListAvailabilityBlocksGetResponse200Links


T = TypeVar("T", bound="ListAvailabilityBlocksGetResponse200")


@_attrs_define
class ListAvailabilityBlocksGetResponse200:
    """
    Attributes:
        availability_blocks (Union[Unset, List['AvailabilityBlock']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListAvailabilityBlocksGetResponse200Links]):
    """

    availability_blocks: Union[Unset, List["AvailabilityBlock"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListAvailabilityBlocksGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability_blocks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.availability_blocks, Unset):
            availability_blocks = []
            for availability_blocks_item_data in self.availability_blocks:
                availability_blocks_item = availability_blocks_item_data.to_dict()
                availability_blocks.append(availability_blocks_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability_blocks is not UNSET:
            field_dict["availability_blocks"] = availability_blocks
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_block import AvailabilityBlock
        from ..models.list_availability_blocks_get_response_200_links import ListAvailabilityBlocksGetResponse200Links

        d = src_dict.copy()
        availability_blocks = []
        _availability_blocks = d.pop("availability_blocks", UNSET)
        for availability_blocks_item_data in _availability_blocks or []:
            availability_blocks_item = AvailabilityBlock.from_dict(availability_blocks_item_data)

            availability_blocks.append(availability_blocks_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListAvailabilityBlocksGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListAvailabilityBlocksGetResponse200Links.from_dict(_links)

        list_availability_blocks_get_response_200 = cls(
            availability_blocks=availability_blocks,
            total_entries=total_entries,
            links=links,
        )

        list_availability_blocks_get_response_200.additional_properties = d
        return list_availability_blocks_get_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
