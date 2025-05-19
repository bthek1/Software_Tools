from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_communication_invoice_links import SmsCommunicationInvoiceLinks


T = TypeVar("T", bound="SmsCommunicationInvoice")


@_attrs_define
class SmsCommunicationInvoice:
    """
    Attributes:
        links (Union[Unset, SmsCommunicationInvoiceLinks]):
    """

    links: Union[Unset, "SmsCommunicationInvoiceLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sms_communication_invoice_links import SmsCommunicationInvoiceLinks

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, SmsCommunicationInvoiceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SmsCommunicationInvoiceLinks.from_dict(_links)

        sms_communication_invoice = cls(
            links=links,
        )

        sms_communication_invoice.additional_properties = d
        return sms_communication_invoice

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
