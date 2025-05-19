import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_appointment_appointment_type import GroupAppointmentAppointmentType
    from ..models.group_appointment_attendees import GroupAppointmentAttendees
    from ..models.group_appointment_business import GroupAppointmentBusiness
    from ..models.group_appointment_conflicts_type_0 import GroupAppointmentConflictsType0
    from ..models.group_appointment_links import GroupAppointmentLinks
    from ..models.group_appointment_practitioner import GroupAppointmentPractitioner
    from ..models.group_appointment_repeat_rule_type_0 import GroupAppointmentRepeatRuleType0
    from ..models.group_appointment_repeated_from import GroupAppointmentRepeatedFrom
    from ..models.group_appointment_repeats_type_0 import GroupAppointmentRepeatsType0


T = TypeVar("T", bound="GroupAppointment")


@_attrs_define
class GroupAppointment:
    """
    Attributes:
        appointment_type (Union[Unset, GroupAppointmentAppointmentType]):
        archived_at (Union[None, Unset, datetime.datetime]):
        attendees (Union[Unset, GroupAppointmentAttendees]):
        business (Union[Unset, GroupAppointmentBusiness]):
        conflicts (Union['GroupAppointmentConflictsType0', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        ends_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, GroupAppointmentLinks]):
        max_attendees (Union[Unset, int]):
        notes (Union[None, Unset, str]):
        patient_ids (Union[List[str], None, Unset]):
        practitioner (Union[Unset, GroupAppointmentPractitioner]):
        repeat_rule (Union['GroupAppointmentRepeatRuleType0', None, Unset]):
        repeated_from (Union[Unset, GroupAppointmentRepeatedFrom]):
        repeats (Union['GroupAppointmentRepeatsType0', None, Unset]):
        starts_at (Union[Unset, datetime.datetime]):
        telehealth_url (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    appointment_type: Union[Unset, "GroupAppointmentAppointmentType"] = UNSET
    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    attendees: Union[Unset, "GroupAppointmentAttendees"] = UNSET
    business: Union[Unset, "GroupAppointmentBusiness"] = UNSET
    conflicts: Union["GroupAppointmentConflictsType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "GroupAppointmentLinks"] = UNSET
    max_attendees: Union[Unset, int] = UNSET
    notes: Union[None, Unset, str] = UNSET
    patient_ids: Union[List[str], None, Unset] = UNSET
    practitioner: Union[Unset, "GroupAppointmentPractitioner"] = UNSET
    repeat_rule: Union["GroupAppointmentRepeatRuleType0", None, Unset] = UNSET
    repeated_from: Union[Unset, "GroupAppointmentRepeatedFrom"] = UNSET
    repeats: Union["GroupAppointmentRepeatsType0", None, Unset] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    telehealth_url: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group_appointment_conflicts_type_0 import GroupAppointmentConflictsType0
        from ..models.group_appointment_repeat_rule_type_0 import GroupAppointmentRepeatRuleType0
        from ..models.group_appointment_repeats_type_0 import GroupAppointmentRepeatsType0

        appointment_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_type, Unset):
            appointment_type = self.appointment_type.to_dict()

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        attendees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = self.attendees.to_dict()

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        conflicts: Union[Dict[str, Any], None, Unset]
        if isinstance(self.conflicts, Unset):
            conflicts = UNSET
        elif isinstance(self.conflicts, GroupAppointmentConflictsType0):
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

        max_attendees = self.max_attendees

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        patient_ids: Union[List[str], None, Unset]
        if isinstance(self.patient_ids, Unset):
            patient_ids = UNSET
        elif isinstance(self.patient_ids, list):
            patient_ids = self.patient_ids

        else:
            patient_ids = self.patient_ids

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        repeat_rule: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeat_rule, Unset):
            repeat_rule = UNSET
        elif isinstance(self.repeat_rule, GroupAppointmentRepeatRuleType0):
            repeat_rule = self.repeat_rule.to_dict()
        else:
            repeat_rule = self.repeat_rule

        repeated_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeated_from, Unset):
            repeated_from = self.repeated_from.to_dict()

        repeats: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeats, Unset):
            repeats = UNSET
        elif isinstance(self.repeats, GroupAppointmentRepeatsType0):
            repeats = self.repeats.to_dict()
        else:
            repeats = self.repeats

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        telehealth_url: Union[None, Unset, str]
        if isinstance(self.telehealth_url, Unset):
            telehealth_url = UNSET
        else:
            telehealth_url = self.telehealth_url

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type is not UNSET:
            field_dict["appointment_type"] = appointment_type
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
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
        if max_attendees is not UNSET:
            field_dict["max_attendees"] = max_attendees
        if notes is not UNSET:
            field_dict["notes"] = notes
        if patient_ids is not UNSET:
            field_dict["patient_ids"] = patient_ids
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
        if telehealth_url is not UNSET:
            field_dict["telehealth_url"] = telehealth_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_appointment_appointment_type import GroupAppointmentAppointmentType
        from ..models.group_appointment_attendees import GroupAppointmentAttendees
        from ..models.group_appointment_business import GroupAppointmentBusiness
        from ..models.group_appointment_conflicts_type_0 import GroupAppointmentConflictsType0
        from ..models.group_appointment_links import GroupAppointmentLinks
        from ..models.group_appointment_practitioner import GroupAppointmentPractitioner
        from ..models.group_appointment_repeat_rule_type_0 import GroupAppointmentRepeatRuleType0
        from ..models.group_appointment_repeated_from import GroupAppointmentRepeatedFrom
        from ..models.group_appointment_repeats_type_0 import GroupAppointmentRepeatsType0

        d = src_dict.copy()
        _appointment_type = d.pop("appointment_type", UNSET)
        appointment_type: Union[Unset, GroupAppointmentAppointmentType]
        if isinstance(_appointment_type, Unset):
            appointment_type = UNSET
        else:
            appointment_type = GroupAppointmentAppointmentType.from_dict(_appointment_type)

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

        _attendees = d.pop("attendees", UNSET)
        attendees: Union[Unset, GroupAppointmentAttendees]
        if isinstance(_attendees, Unset):
            attendees = UNSET
        else:
            attendees = GroupAppointmentAttendees.from_dict(_attendees)

        _business = d.pop("business", UNSET)
        business: Union[Unset, GroupAppointmentBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = GroupAppointmentBusiness.from_dict(_business)

        def _parse_conflicts(data: object) -> Union["GroupAppointmentConflictsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conflicts_type_0 = GroupAppointmentConflictsType0.from_dict(data)

                return conflicts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupAppointmentConflictsType0", None, Unset], data)

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
        links: Union[Unset, GroupAppointmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GroupAppointmentLinks.from_dict(_links)

        max_attendees = d.pop("max_attendees", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_patient_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                patient_ids_type_0 = cast(List[str], data)

                return patient_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        patient_ids = _parse_patient_ids(d.pop("patient_ids", UNSET))

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, GroupAppointmentPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = GroupAppointmentPractitioner.from_dict(_practitioner)

        def _parse_repeat_rule(data: object) -> Union["GroupAppointmentRepeatRuleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeat_rule_type_0 = GroupAppointmentRepeatRuleType0.from_dict(data)

                return repeat_rule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupAppointmentRepeatRuleType0", None, Unset], data)

        repeat_rule = _parse_repeat_rule(d.pop("repeat_rule", UNSET))

        _repeated_from = d.pop("repeated_from", UNSET)
        repeated_from: Union[Unset, GroupAppointmentRepeatedFrom]
        if isinstance(_repeated_from, Unset):
            repeated_from = UNSET
        else:
            repeated_from = GroupAppointmentRepeatedFrom.from_dict(_repeated_from)

        def _parse_repeats(data: object) -> Union["GroupAppointmentRepeatsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeats_type_0 = GroupAppointmentRepeatsType0.from_dict(data)

                return repeats_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GroupAppointmentRepeatsType0", None, Unset], data)

        repeats = _parse_repeats(d.pop("repeats", UNSET))

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        def _parse_telehealth_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        telehealth_url = _parse_telehealth_url(d.pop("telehealth_url", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        group_appointment = cls(
            appointment_type=appointment_type,
            archived_at=archived_at,
            attendees=attendees,
            business=business,
            conflicts=conflicts,
            created_at=created_at,
            deleted_at=deleted_at,
            ends_at=ends_at,
            id=id,
            links=links,
            max_attendees=max_attendees,
            notes=notes,
            patient_ids=patient_ids,
            practitioner=practitioner,
            repeat_rule=repeat_rule,
            repeated_from=repeated_from,
            repeats=repeats,
            starts_at=starts_at,
            telehealth_url=telehealth_url,
            updated_at=updated_at,
        )

        group_appointment.additional_properties = d
        return group_appointment

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
