import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unavailable_block_business import UnavailableBlockBusiness
    from ..models.unavailable_block_conflicts_type_0 import UnavailableBlockConflictsType0
    from ..models.unavailable_block_links import UnavailableBlockLinks
    from ..models.unavailable_block_practitioner import UnavailableBlockPractitioner
    from ..models.unavailable_block_repeat_rule_type_0 import UnavailableBlockRepeatRuleType0
    from ..models.unavailable_block_repeated_from import UnavailableBlockRepeatedFrom
    from ..models.unavailable_block_repeats_type_0 import UnavailableBlockRepeatsType0


T = TypeVar("T", bound="UnavailableBlock")


@_attrs_define
class UnavailableBlock:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        business (Union[Unset, UnavailableBlockBusiness]):
        conflicts (Union['UnavailableBlockConflictsType0', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        ends_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, UnavailableBlockLinks]):
        notes (Union[None, Unset, str]):
        practitioner (Union[Unset, UnavailableBlockPractitioner]):
        repeat_rule (Union['UnavailableBlockRepeatRuleType0', None, Unset]):
        repeated_from (Union[Unset, UnavailableBlockRepeatedFrom]):
        repeats (Union['UnavailableBlockRepeatsType0', None, Unset]):
        starts_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    business: Union[Unset, "UnavailableBlockBusiness"] = UNSET
    conflicts: Union["UnavailableBlockConflictsType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "UnavailableBlockLinks"] = UNSET
    notes: Union[None, Unset, str] = UNSET
    practitioner: Union[Unset, "UnavailableBlockPractitioner"] = UNSET
    repeat_rule: Union["UnavailableBlockRepeatRuleType0", None, Unset] = UNSET
    repeated_from: Union[Unset, "UnavailableBlockRepeatedFrom"] = UNSET
    repeats: Union["UnavailableBlockRepeatsType0", None, Unset] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.unavailable_block_conflicts_type_0 import UnavailableBlockConflictsType0
        from ..models.unavailable_block_repeat_rule_type_0 import UnavailableBlockRepeatRuleType0
        from ..models.unavailable_block_repeats_type_0 import UnavailableBlockRepeatsType0

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        conflicts: Union[Dict[str, Any], None, Unset]
        if isinstance(self.conflicts, Unset):
            conflicts = UNSET
        elif isinstance(self.conflicts, UnavailableBlockConflictsType0):
            conflicts = self.conflicts.to_dict()
        else:
            conflicts = self.conflicts

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        ends_at: Union[Unset, str] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        repeat_rule: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeat_rule, Unset):
            repeat_rule = UNSET
        elif isinstance(self.repeat_rule, UnavailableBlockRepeatRuleType0):
            repeat_rule = self.repeat_rule.to_dict()
        else:
            repeat_rule = self.repeat_rule

        repeated_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeated_from, Unset):
            repeated_from = self.repeated_from.to_dict()

        repeats: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeats, Unset):
            repeats = UNSET
        elif isinstance(self.repeats, UnavailableBlockRepeatsType0):
            repeats = self.repeats.to_dict()
        else:
            repeats = self.repeats

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if business is not UNSET:
            field_dict["business"] = business
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if notes is not UNSET:
            field_dict["notes"] = notes
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if repeat_rule is not UNSET:
            field_dict["repeat_rule"] = repeat_rule
        if repeated_from is not UNSET:
            field_dict["repeated_from"] = repeated_from
        if repeats is not UNSET:
            field_dict["repeats"] = repeats
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.unavailable_block_business import UnavailableBlockBusiness
        from ..models.unavailable_block_conflicts_type_0 import UnavailableBlockConflictsType0
        from ..models.unavailable_block_links import UnavailableBlockLinks
        from ..models.unavailable_block_practitioner import UnavailableBlockPractitioner
        from ..models.unavailable_block_repeat_rule_type_0 import UnavailableBlockRepeatRuleType0
        from ..models.unavailable_block_repeated_from import UnavailableBlockRepeatedFrom
        from ..models.unavailable_block_repeats_type_0 import UnavailableBlockRepeatsType0

        d = src_dict.copy()

        def _parse_archived_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = isoparse(data)

                return archived_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        _business = d.pop("business", UNSET)
        business: Union[Unset, UnavailableBlockBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = UnavailableBlockBusiness.from_dict(_business)

        def _parse_conflicts(data: object) -> Union["UnavailableBlockConflictsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conflicts_type_0 = UnavailableBlockConflictsType0.from_dict(data)

                return conflicts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UnavailableBlockConflictsType0", None, Unset], data)

        conflicts = _parse_conflicts(d.pop("conflicts", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: Union[Unset, datetime.datetime]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = isoparse(_ends_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, UnavailableBlockLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UnavailableBlockLinks.from_dict(_links)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, UnavailableBlockPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = UnavailableBlockPractitioner.from_dict(_practitioner)

        def _parse_repeat_rule(data: object) -> Union["UnavailableBlockRepeatRuleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeat_rule_type_0 = UnavailableBlockRepeatRuleType0.from_dict(data)

                return repeat_rule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UnavailableBlockRepeatRuleType0", None, Unset], data)

        repeat_rule = _parse_repeat_rule(d.pop("repeat_rule", UNSET))

        _repeated_from = d.pop("repeated_from", UNSET)
        repeated_from: Union[Unset, UnavailableBlockRepeatedFrom]
        if isinstance(_repeated_from, Unset):
            repeated_from = UNSET
        else:
            repeated_from = UnavailableBlockRepeatedFrom.from_dict(_repeated_from)

        def _parse_repeats(data: object) -> Union["UnavailableBlockRepeatsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeats_type_0 = UnavailableBlockRepeatsType0.from_dict(data)

                return repeats_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UnavailableBlockRepeatsType0", None, Unset], data)

        repeats = _parse_repeats(d.pop("repeats", UNSET))

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

        unavailable_block = cls(
            archived_at=archived_at,
            business=business,
            conflicts=conflicts,
            created_at=created_at,
            deleted_at=deleted_at,
            ends_at=ends_at,
            id=id,
            links=links,
            notes=notes,
            practitioner=practitioner,
            repeat_rule=repeat_rule,
            repeated_from=repeated_from,
            repeats=repeats,
            starts_at=starts_at,
            updated_at=updated_at,
        )

        unavailable_block.additional_properties = d
        return unavailable_block

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
