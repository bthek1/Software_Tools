from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.concession_price import ConcessionPrice
    from ..models.list_concession_prices_get_response_200_links import ListConcessionPricesGetResponse200Links


T = TypeVar("T", bound="ListConcessionPricesGetResponse200")


@_attrs_define
class ListConcessionPricesGetResponse200:
    """
    Attributes:
        concession_prices (Union[Unset, List['ConcessionPrice']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListConcessionPricesGetResponse200Links]):
    """

    concession_prices: Union[Unset, List["ConcessionPrice"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListConcessionPricesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        concession_prices: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.concession_prices, Unset):
            concession_prices = []
            for concession_prices_item_data in self.concession_prices:
                concession_prices_item = concession_prices_item_data.to_dict()
                concession_prices.append(concession_prices_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concession_prices is not UNSET:
            field_dict["concession_prices"] = concession_prices
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.concession_price import ConcessionPrice
        from ..models.list_concession_prices_get_response_200_links import ListConcessionPricesGetResponse200Links

        d = src_dict.copy()
        concession_prices = []
        _concession_prices = d.pop("concession_prices", UNSET)
        for concession_prices_item_data in _concession_prices or []:
            concession_prices_item = ConcessionPrice.from_dict(concession_prices_item_data)

            concession_prices.append(concession_prices_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListConcessionPricesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListConcessionPricesGetResponse200Links.from_dict(_links)

        list_concession_prices_get_response_200 = cls(
            concession_prices=concession_prices,
            total_entries=total_entries,
            links=links,
        )

        list_concession_prices_get_response_200.additional_properties = d
        return list_concession_prices_get_response_200

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
