from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_all_available_times_get_response_200_links import GetAllAvailableTimesGetResponse200Links


T = TypeVar("T", bound="GetAllAvailableTimesGetResponse200")


@_attrs_define
class GetAllAvailableTimesGetResponse200:
    """
    Attributes:
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, GetAllAvailableTimesGetResponse200Links]):
        available_times (Union[Unset, Any]):
    """

    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "GetAllAvailableTimesGetResponse200Links"] = UNSET
    available_times: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        available_times = self.available_times

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links
        if available_times is not UNSET:
            field_dict["available_times"] = available_times

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_all_available_times_get_response_200_links import GetAllAvailableTimesGetResponse200Links

        d = src_dict.copy()
        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, GetAllAvailableTimesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GetAllAvailableTimesGetResponse200Links.from_dict(_links)

        available_times = d.pop("available_times", UNSET)

        get_all_available_times_get_response_200 = cls(
            total_entries=total_entries,
            links=links,
            available_times=available_times,
        )

        get_all_available_times_get_response_200.additional_properties = d
        return get_all_available_times_get_response_200

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
