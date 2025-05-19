from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_medical_alerts_get_response_200_links import ListMedicalAlertsGetResponse200Links
    from ..models.medical_alert import MedicalAlert


T = TypeVar("T", bound="ListMedicalAlertsGetResponse200")


@_attrs_define
class ListMedicalAlertsGetResponse200:
    """
    Attributes:
        medical_alerts (Union[Unset, List['MedicalAlert']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListMedicalAlertsGetResponse200Links]):
    """

    medical_alerts: Union[Unset, List["MedicalAlert"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListMedicalAlertsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        medical_alerts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.medical_alerts, Unset):
            medical_alerts = []
            for medical_alerts_item_data in self.medical_alerts:
                medical_alerts_item = medical_alerts_item_data.to_dict()
                medical_alerts.append(medical_alerts_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if medical_alerts is not UNSET:
            field_dict["medical_alerts"] = medical_alerts
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_medical_alerts_get_response_200_links import ListMedicalAlertsGetResponse200Links
        from ..models.medical_alert import MedicalAlert

        d = src_dict.copy()
        medical_alerts = []
        _medical_alerts = d.pop("medical_alerts", UNSET)
        for medical_alerts_item_data in _medical_alerts or []:
            medical_alerts_item = MedicalAlert.from_dict(medical_alerts_item_data)

            medical_alerts.append(medical_alerts_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListMedicalAlertsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListMedicalAlertsGetResponse200Links.from_dict(_links)

        list_medical_alerts_get_response_200 = cls(
            medical_alerts=medical_alerts,
            total_entries=total_entries,
            links=links,
        )

        list_medical_alerts_get_response_200.additional_properties = d
        return list_medical_alerts_get_response_200

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
