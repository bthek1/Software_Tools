import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.availability_block_business import AvailabilityBlockBusiness
    from ..models.availability_block_links import AvailabilityBlockLinks
    from ..models.availability_block_practitioner import AvailabilityBlockPractitioner
    from ..models.availability_block_repeat_rule_type_0 import AvailabilityBlockRepeatRuleType0


T = TypeVar("T", bound="AvailabilityBlock")


@_attrs_define
class AvailabilityBlock:
    """
    Attributes:
        business (Union[Unset, AvailabilityBlockBusiness]):
        created_at (Union[Unset, datetime.datetime]):
        ends_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, AvailabilityBlockLinks]):
        practitioner (Union[Unset, AvailabilityBlockPractitioner]):
        repeat_rule (Union['AvailabilityBlockRepeatRuleType0', None, Unset]):
        starts_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    business: Union[Unset, "AvailabilityBlockBusiness"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "AvailabilityBlockLinks"] = UNSET
    practitioner: Union[Unset, "AvailabilityBlockPractitioner"] = UNSET
    repeat_rule: Union["AvailabilityBlockRepeatRuleType0", None, Unset] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.availability_block_repeat_rule_type_0 import AvailabilityBlockRepeatRuleType0

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        ends_at: Union[Unset, str] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        repeat_rule: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeat_rule, Unset):
            repeat_rule = UNSET
        elif isinstance(self.repeat_rule, AvailabilityBlockRepeatRuleType0):
            repeat_rule = self.repeat_rule.to_dict()
        else:
            repeat_rule = self.repeat_rule

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business is not UNSET:
            field_dict["business"] = business
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if repeat_rule is not UNSET:
            field_dict["repeat_rule"] = repeat_rule
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.availability_block_business import AvailabilityBlockBusiness
        from ..models.availability_block_links import AvailabilityBlockLinks
        from ..models.availability_block_practitioner import AvailabilityBlockPractitioner
        from ..models.availability_block_repeat_rule_type_0 import AvailabilityBlockRepeatRuleType0

        d = src_dict.copy()
        _business = d.pop("business", UNSET)
        business: Union[Unset, AvailabilityBlockBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = AvailabilityBlockBusiness.from_dict(_business)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: Union[Unset, datetime.datetime]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = isoparse(_ends_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AvailabilityBlockLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AvailabilityBlockLinks.from_dict(_links)

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, AvailabilityBlockPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = AvailabilityBlockPractitioner.from_dict(_practitioner)

        def _parse_repeat_rule(data: object) -> Union["AvailabilityBlockRepeatRuleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeat_rule_type_0 = AvailabilityBlockRepeatRuleType0.from_dict(data)

                return repeat_rule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AvailabilityBlockRepeatRuleType0", None, Unset], data)

        repeat_rule = _parse_repeat_rule(d.pop("repeat_rule", UNSET))

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        availability_block = cls(
            business=business,
            created_at=created_at,
            ends_at=ends_at,
            id=id,
            links=links,
            practitioner=practitioner,
            repeat_rule=repeat_rule,
            starts_at=starts_at,
            updated_at=updated_at,
        )

        availability_block.additional_properties = d
        return availability_block

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
