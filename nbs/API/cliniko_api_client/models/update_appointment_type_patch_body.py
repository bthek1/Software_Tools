from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_appointment_type_patch_body_online_bookings_lead_time_hours import (
    UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours,
    check_update_appointment_type_patch_body_online_bookings_lead_time_hours,
)
from ..models.update_appointment_type_patch_body_online_payments_mode import (
    UpdateAppointmentTypePatchBodyOnlinePaymentsMode,
    check_update_appointment_type_patch_body_online_payments_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppointmentTypePatchBody")


@_attrs_define
class UpdateAppointmentTypePatchBody:
    """
    Attributes:
        add_deposit_to_account_credit (Union[None, Unset, bool]):
        billable_item_id (Union[Unset, str]): billable item id Example: 1.
        category (Union[None, Unset, str]):
        color (Union[Unset, str]):
        deposit_price (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        duration_in_minutes (Union[Unset, int]):
        online_bookings_lead_time_hours (Union[Unset, UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours]):
        online_payments_mode (Union[Unset, UpdateAppointmentTypePatchBodyOnlinePaymentsMode]):
        max_attendees (Union[Unset, int]):
        name (Union[Unset, str]):
        product_id (Union[Unset, str]): product id Example: 1.
        show_in_online_bookings (Union[None, Unset, bool]):
        telehealth_enabled (Union[None, Unset, bool]):
        treatment_note_template_id (Union[Unset, str]): treatment note template id Example: 1.
        appointment_confirmation_template_ids (Union[List[str], None, Unset]):
        appointment_reminder_template_ids (Union[List[str], None, Unset]):
        business_ids (Union[Unset, List[str]]):
        practitioner_ids (Union[Unset, List[str]]): Practitioner ids
    """

    add_deposit_to_account_credit: Union[None, Unset, bool] = UNSET
    billable_item_id: Union[Unset, str] = UNSET
    category: Union[None, Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    deposit_price: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    duration_in_minutes: Union[Unset, int] = UNSET
    online_bookings_lead_time_hours: Union[Unset, UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours] = UNSET
    online_payments_mode: Union[Unset, UpdateAppointmentTypePatchBodyOnlinePaymentsMode] = UNSET
    max_attendees: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    show_in_online_bookings: Union[None, Unset, bool] = UNSET
    telehealth_enabled: Union[None, Unset, bool] = UNSET
    treatment_note_template_id: Union[Unset, str] = UNSET
    appointment_confirmation_template_ids: Union[List[str], None, Unset] = UNSET
    appointment_reminder_template_ids: Union[List[str], None, Unset] = UNSET
    business_ids: Union[Unset, List[str]] = UNSET
    practitioner_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_deposit_to_account_credit: Union[None, Unset, bool]
        if isinstance(self.add_deposit_to_account_credit, Unset):
            add_deposit_to_account_credit = UNSET
        else:
            add_deposit_to_account_credit = self.add_deposit_to_account_credit

        billable_item_id = self.billable_item_id

        category: Union[None, Unset, str]
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        color = self.color

        deposit_price: Union[None, Unset, str]
        if isinstance(self.deposit_price, Unset):
            deposit_price = UNSET
        else:
            deposit_price = self.deposit_price

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        duration_in_minutes = self.duration_in_minutes

        online_bookings_lead_time_hours: Union[Unset, int] = UNSET
        if not isinstance(self.online_bookings_lead_time_hours, Unset):
            online_bookings_lead_time_hours = self.online_bookings_lead_time_hours

        online_payments_mode: Union[Unset, str] = UNSET
        if not isinstance(self.online_payments_mode, Unset):
            online_payments_mode = self.online_payments_mode

        max_attendees = self.max_attendees

        name = self.name

        product_id = self.product_id

        show_in_online_bookings: Union[None, Unset, bool]
        if isinstance(self.show_in_online_bookings, Unset):
            show_in_online_bookings = UNSET
        else:
            show_in_online_bookings = self.show_in_online_bookings

        telehealth_enabled: Union[None, Unset, bool]
        if isinstance(self.telehealth_enabled, Unset):
            telehealth_enabled = UNSET
        else:
            telehealth_enabled = self.telehealth_enabled

        treatment_note_template_id = self.treatment_note_template_id

        appointment_confirmation_template_ids: Union[List[str], None, Unset]
        if isinstance(self.appointment_confirmation_template_ids, Unset):
            appointment_confirmation_template_ids = UNSET
        elif isinstance(self.appointment_confirmation_template_ids, list):
            appointment_confirmation_template_ids = self.appointment_confirmation_template_ids

        else:
            appointment_confirmation_template_ids = self.appointment_confirmation_template_ids

        appointment_reminder_template_ids: Union[List[str], None, Unset]
        if isinstance(self.appointment_reminder_template_ids, Unset):
            appointment_reminder_template_ids = UNSET
        elif isinstance(self.appointment_reminder_template_ids, list):
            appointment_reminder_template_ids = self.appointment_reminder_template_ids

        else:
            appointment_reminder_template_ids = self.appointment_reminder_template_ids

        business_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.business_ids, Unset):
            business_ids = self.business_ids

        practitioner_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.practitioner_ids, Unset):
            practitioner_ids = self.practitioner_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_deposit_to_account_credit is not UNSET:
            field_dict["add_deposit_to_account_credit"] = add_deposit_to_account_credit
        if billable_item_id is not UNSET:
            field_dict["billable_item_id"] = billable_item_id
        if category is not UNSET:
            field_dict["category"] = category
        if color is not UNSET:
            field_dict["color"] = color
        if deposit_price is not UNSET:
            field_dict["deposit_price"] = deposit_price
        if description is not UNSET:
            field_dict["description"] = description
        if duration_in_minutes is not UNSET:
            field_dict["duration_in_minutes"] = duration_in_minutes
        if online_bookings_lead_time_hours is not UNSET:
            field_dict["online_bookings_lead_time_hours"] = online_bookings_lead_time_hours
        if online_payments_mode is not UNSET:
            field_dict["online_payments_mode"] = online_payments_mode
        if max_attendees is not UNSET:
            field_dict["max_attendees"] = max_attendees
        if name is not UNSET:
            field_dict["name"] = name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if show_in_online_bookings is not UNSET:
            field_dict["show_in_online_bookings"] = show_in_online_bookings
        if telehealth_enabled is not UNSET:
            field_dict["telehealth_enabled"] = telehealth_enabled
        if treatment_note_template_id is not UNSET:
            field_dict["treatment_note_template_id"] = treatment_note_template_id
        if appointment_confirmation_template_ids is not UNSET:
            field_dict["appointment_confirmation_template_ids"] = appointment_confirmation_template_ids
        if appointment_reminder_template_ids is not UNSET:
            field_dict["appointment_reminder_template_ids"] = appointment_reminder_template_ids
        if business_ids is not UNSET:
            field_dict["business_ids"] = business_ids
        if practitioner_ids is not UNSET:
            field_dict["practitioner_ids"] = practitioner_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_add_deposit_to_account_credit(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        add_deposit_to_account_credit = _parse_add_deposit_to_account_credit(
            d.pop("add_deposit_to_account_credit", UNSET)
        )

        billable_item_id = d.pop("billable_item_id", UNSET)

        def _parse_category(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category = _parse_category(d.pop("category", UNSET))

        color = d.pop("color", UNSET)

        def _parse_deposit_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deposit_price = _parse_deposit_price(d.pop("deposit_price", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        duration_in_minutes = d.pop("duration_in_minutes", UNSET)

        _online_bookings_lead_time_hours = d.pop("online_bookings_lead_time_hours", UNSET)
        online_bookings_lead_time_hours: Union[Unset, UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours]
        if isinstance(_online_bookings_lead_time_hours, Unset):
            online_bookings_lead_time_hours = UNSET
        else:
            online_bookings_lead_time_hours = check_update_appointment_type_patch_body_online_bookings_lead_time_hours(
                _online_bookings_lead_time_hours
            )

        _online_payments_mode = d.pop("online_payments_mode", UNSET)
        online_payments_mode: Union[Unset, UpdateAppointmentTypePatchBodyOnlinePaymentsMode]
        if isinstance(_online_payments_mode, Unset):
            online_payments_mode = UNSET
        else:
            online_payments_mode = check_update_appointment_type_patch_body_online_payments_mode(_online_payments_mode)

        max_attendees = d.pop("max_attendees", UNSET)

        name = d.pop("name", UNSET)

        product_id = d.pop("product_id", UNSET)

        def _parse_show_in_online_bookings(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_in_online_bookings = _parse_show_in_online_bookings(d.pop("show_in_online_bookings", UNSET))

        def _parse_telehealth_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        telehealth_enabled = _parse_telehealth_enabled(d.pop("telehealth_enabled", UNSET))

        treatment_note_template_id = d.pop("treatment_note_template_id", UNSET)

        def _parse_appointment_confirmation_template_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                appointment_confirmation_template_ids_type_0 = cast(List[str], data)

                return appointment_confirmation_template_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        appointment_confirmation_template_ids = _parse_appointment_confirmation_template_ids(
            d.pop("appointment_confirmation_template_ids", UNSET)
        )

        def _parse_appointment_reminder_template_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                appointment_reminder_template_ids_type_0 = cast(List[str], data)

                return appointment_reminder_template_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        appointment_reminder_template_ids = _parse_appointment_reminder_template_ids(
            d.pop("appointment_reminder_template_ids", UNSET)
        )

        business_ids = cast(List[str], d.pop("business_ids", UNSET))

        practitioner_ids = cast(List[str], d.pop("practitioner_ids", UNSET))

        update_appointment_type_patch_body = cls(
            add_deposit_to_account_credit=add_deposit_to_account_credit,
            billable_item_id=billable_item_id,
            category=category,
            color=color,
            deposit_price=deposit_price,
            description=description,
            duration_in_minutes=duration_in_minutes,
            online_bookings_lead_time_hours=online_bookings_lead_time_hours,
            online_payments_mode=online_payments_mode,
            max_attendees=max_attendees,
            name=name,
            product_id=product_id,
            show_in_online_bookings=show_in_online_bookings,
            telehealth_enabled=telehealth_enabled,
            treatment_note_template_id=treatment_note_template_id,
            appointment_confirmation_template_ids=appointment_confirmation_template_ids,
            appointment_reminder_template_ids=appointment_reminder_template_ids,
            business_ids=business_ids,
            practitioner_ids=practitioner_ids,
        )

        update_appointment_type_patch_body.additional_properties = d
        return update_appointment_type_patch_body

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
