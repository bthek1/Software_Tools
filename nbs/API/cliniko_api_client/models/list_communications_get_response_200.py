from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_communication import EmailCommunication
    from ..models.list_communications_get_response_200_links import ListCommunicationsGetResponse200Links
    from ..models.memo_communication import MemoCommunication
    from ..models.sms_communication import SmsCommunication


T = TypeVar("T", bound="ListCommunicationsGetResponse200")


@_attrs_define
class ListCommunicationsGetResponse200:
    """
    Attributes:
        communications (Union[Unset, List[Union['EmailCommunication', 'MemoCommunication', 'SmsCommunication']]]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListCommunicationsGetResponse200Links]):
    """

    communications: Union[Unset, List[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListCommunicationsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.email_communication import EmailCommunication
        from ..models.memo_communication import MemoCommunication

        communications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.communications, Unset):
            communications = []
            for communications_item_data in self.communications:
                communications_item: Dict[str, Any]
                if isinstance(communications_item_data, MemoCommunication):
                    communications_item = communications_item_data.to_dict()
                elif isinstance(communications_item_data, EmailCommunication):
                    communications_item = communications_item_data.to_dict()
                else:
                    communications_item = communications_item_data.to_dict()

                communications.append(communications_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communications is not UNSET:
            field_dict["communications"] = communications
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email_communication import EmailCommunication
        from ..models.list_communications_get_response_200_links import ListCommunicationsGetResponse200Links
        from ..models.memo_communication import MemoCommunication
        from ..models.sms_communication import SmsCommunication

        d = src_dict.copy()
        communications = []
        _communications = d.pop("communications", UNSET)
        for communications_item_data in _communications or []:

            def _parse_communications_item(
                data: object,
            ) -> Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_communication_type_0 = MemoCommunication.from_dict(data)

                    return componentsschemas_communication_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_communication_type_1 = EmailCommunication.from_dict(data)

                    return componentsschemas_communication_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_communication_type_2 = SmsCommunication.from_dict(data)

                return componentsschemas_communication_type_2

            communications_item = _parse_communications_item(communications_item_data)

            communications.append(communications_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListCommunicationsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListCommunicationsGetResponse200Links.from_dict(_links)

        list_communications_get_response_200 = cls(
            communications=communications,
            total_entries=total_entries,
            links=links,
        )

        list_communications_get_response_200.additional_properties = d
        return list_communications_get_response_200

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
