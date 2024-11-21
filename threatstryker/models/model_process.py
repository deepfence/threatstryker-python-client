from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelProcess")


@_attrs_define
class ModelProcess:
    """
    Example:
        {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}

    Attributes:
        active_cves (Union[List[str], None]):
        active_malwares (Union[List[str], None]):
        active_secrets (Union[List[str], None]):
        cmdline (str):
        cpu_max (float):
        cpu_usage (float):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        open_files_count (int):
        pid (int):
        ppid (int):
        short_name (str):
        threads (int):
    """

    active_cves: Union[List[str], None]
    active_malwares: Union[List[str], None]
    active_secrets: Union[List[str], None]
    cmdline: str
    cpu_max: float
    cpu_usage: float
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    open_files_count: int
    pid: int
    ppid: int
    short_name: str
    threads: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_cves: Union[List[str], None]
        if isinstance(self.active_cves, list):
            active_cves = self.active_cves

        else:
            active_cves = self.active_cves

        active_malwares: Union[List[str], None]
        if isinstance(self.active_malwares, list):
            active_malwares = self.active_malwares

        else:
            active_malwares = self.active_malwares

        active_secrets: Union[List[str], None]
        if isinstance(self.active_secrets, list):
            active_secrets = self.active_secrets

        else:
            active_secrets = self.active_secrets

        cmdline = self.cmdline

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        node_id = self.node_id

        node_name = self.node_name

        open_files_count = self.open_files_count

        pid = self.pid

        ppid = self.ppid

        short_name = self.short_name

        threads = self.threads

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_cves": active_cves,
                "active_malwares": active_malwares,
                "active_secrets": active_secrets,
                "cmdline": cmdline,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "open_files_count": open_files_count,
                "pid": pid,
                "ppid": ppid,
                "short_name": short_name,
                "threads": threads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_active_cves(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_cves_type_0 = cast(List[str], data)

                return active_cves_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        active_cves = _parse_active_cves(d.pop("active_cves"))

        def _parse_active_malwares(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_malwares_type_0 = cast(List[str], data)

                return active_malwares_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        active_malwares = _parse_active_malwares(d.pop("active_malwares"))

        def _parse_active_secrets(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_secrets_type_0 = cast(List[str], data)

                return active_secrets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        active_secrets = _parse_active_secrets(d.pop("active_secrets"))

        cmdline = d.pop("cmdline")

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        open_files_count = d.pop("open_files_count")

        pid = d.pop("pid")

        ppid = d.pop("ppid")

        short_name = d.pop("short_name")

        threads = d.pop("threads")

        model_process = cls(
            active_cves=active_cves,
            active_malwares=active_malwares,
            active_secrets=active_secrets,
            cmdline=cmdline,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            open_files_count=open_files_count,
            pid=pid,
            ppid=ppid,
            short_name=short_name,
            threads=threads,
        )

        model_process.additional_properties = d
        return model_process

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
