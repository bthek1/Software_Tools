from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_unavailable_blocks_get_response_200_links import ListUnavailableBlocksGetResponse200Links
    from ..models.unavailable_block import UnavailableBlock


T = TypeVar("T", bound="ListUnavailableBlocksGetResponse200")


@_attrs_define
class ListUnavailableBlocksGetResponse200:
    """
    Attributes:
        unavailable_blocks (Union[Unset, List['UnavailableBlock']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListUnavailableBlocksGetResponse200Links]):
    """

    unavailable_blocks: Union[Unset, List["UnavailableBlock"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListUnavailableBlocksGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unavailable_blocks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unavailable_blocks, Unset):
            unavailable_blocks = []
            for unavailable_blocks_item_data in self.unavailable_blocks:
                unavailable_blocks_item = unavailable_blocks_item_data.to_dict()
                unavailable_blocks.append(unavailable_blocks_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unavailable_blocks is not UNSET:
            field_dict["unavailable_blocks"] = unavailable_blocks
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_unavailable_blocks_get_response_200_links import ListUnavailableBlocksGetResponse200Links
        from ..models.unavailable_block import UnavailableBlock

        d = src_dict.copy()
        unavailable_blocks = []
        _unavailable_blocks = d.pop("unavailable_blocks", UNSET)
        for unavailable_blocks_item_data in _unavailable_blocks or []:
            unavailable_blocks_item = UnavailableBlock.from_dict(unavailable_blocks_item_data)

            unavailable_blocks.append(unavailable_blocks_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListUnavailableBlocksGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListUnavailableBlocksGetResponse200Links.from_dict(_links)

        list_unavailable_blocks_get_response_200 = cls(
            unavailable_blocks=unavailable_blocks,
            total_entries=total_entries,
            links=links,
        )

        list_unavailable_blocks_get_response_200.additional_properties = d
        return list_unavailable_blocks_get_response_200

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
