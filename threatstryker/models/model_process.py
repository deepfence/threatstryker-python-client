from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_connection import ModelConnection


T = TypeVar("T", bound="ModelProcess")


@_attrs_define
class ModelProcess:
    """
    Attributes:
        active_cves (Union[None, list[str]]):
        active_malwares (Union[None, list[str]]):
        active_secrets (Union[None, list[str]]):
        cmdline (str):
        cpu_max (float):
        cpu_usage (float):
        host_name (str):
        inbound_connections (Union[None, list['ModelConnection']]):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        open_files (Union[None, list[str]]):
        open_files_count (int):
        outbound_connections (Union[None, list['ModelConnection']]):
        pid (int):
        ppid (int):
        short_name (str):
        threads (int):
    """

    active_cves: Union[None, list[str]]
    active_malwares: Union[None, list[str]]
    active_secrets: Union[None, list[str]]
    cmdline: str
    cpu_max: float
    cpu_usage: float
    host_name: str
    inbound_connections: Union[None, list["ModelConnection"]]
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    open_files: Union[None, list[str]]
    open_files_count: int
    outbound_connections: Union[None, list["ModelConnection"]]
    pid: int
    ppid: int
    short_name: str
    threads: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_cves: Union[None, list[str]]
        if isinstance(self.active_cves, list):
            active_cves = self.active_cves

        else:
            active_cves = self.active_cves

        active_malwares: Union[None, list[str]]
        if isinstance(self.active_malwares, list):
            active_malwares = self.active_malwares

        else:
            active_malwares = self.active_malwares

        active_secrets: Union[None, list[str]]
        if isinstance(self.active_secrets, list):
            active_secrets = self.active_secrets

        else:
            active_secrets = self.active_secrets

        cmdline = self.cmdline

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        host_name = self.host_name

        inbound_connections: Union[None, list[dict[str, Any]]]
        if isinstance(self.inbound_connections, list):
            inbound_connections = []
            for inbound_connections_type_0_item_data in self.inbound_connections:
                inbound_connections_type_0_item = inbound_connections_type_0_item_data.to_dict()
                inbound_connections.append(inbound_connections_type_0_item)

        else:
            inbound_connections = self.inbound_connections

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        node_id = self.node_id

        node_name = self.node_name

        open_files: Union[None, list[str]]
        if isinstance(self.open_files, list):
            open_files = self.open_files

        else:
            open_files = self.open_files

        open_files_count = self.open_files_count

        outbound_connections: Union[None, list[dict[str, Any]]]
        if isinstance(self.outbound_connections, list):
            outbound_connections = []
            for outbound_connections_type_0_item_data in self.outbound_connections:
                outbound_connections_type_0_item = outbound_connections_type_0_item_data.to_dict()
                outbound_connections.append(outbound_connections_type_0_item)

        else:
            outbound_connections = self.outbound_connections

        pid = self.pid

        ppid = self.ppid

        short_name = self.short_name

        threads = self.threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active_cves": active_cves,
                "active_malwares": active_malwares,
                "active_secrets": active_secrets,
                "cmdline": cmdline,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "host_name": host_name,
                "inbound_connections": inbound_connections,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "open_files": open_files,
                "open_files_count": open_files_count,
                "outbound_connections": outbound_connections,
                "pid": pid,
                "ppid": ppid,
                "short_name": short_name,
                "threads": threads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_connection import ModelConnection

        d = dict(src_dict)

        def _parse_active_cves(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_cves_type_0 = cast(list[str], data)

                return active_cves_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        active_cves = _parse_active_cves(d.pop("active_cves"))

        def _parse_active_malwares(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_malwares_type_0 = cast(list[str], data)

                return active_malwares_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        active_malwares = _parse_active_malwares(d.pop("active_malwares"))

        def _parse_active_secrets(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                active_secrets_type_0 = cast(list[str], data)

                return active_secrets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        active_secrets = _parse_active_secrets(d.pop("active_secrets"))

        cmdline = d.pop("cmdline")

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        host_name = d.pop("host_name")

        def _parse_inbound_connections(data: object) -> Union[None, list["ModelConnection"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inbound_connections_type_0 = []
                _inbound_connections_type_0 = data
                for inbound_connections_type_0_item_data in _inbound_connections_type_0:
                    inbound_connections_type_0_item = ModelConnection.from_dict(inbound_connections_type_0_item_data)

                    inbound_connections_type_0.append(inbound_connections_type_0_item)

                return inbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelConnection"]], data)

        inbound_connections = _parse_inbound_connections(d.pop("inbound_connections"))

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        def _parse_open_files(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                open_files_type_0 = cast(list[str], data)

                return open_files_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        open_files = _parse_open_files(d.pop("open_files"))

        open_files_count = d.pop("open_files_count")

        def _parse_outbound_connections(data: object) -> Union[None, list["ModelConnection"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outbound_connections_type_0 = []
                _outbound_connections_type_0 = data
                for outbound_connections_type_0_item_data in _outbound_connections_type_0:
                    outbound_connections_type_0_item = ModelConnection.from_dict(outbound_connections_type_0_item_data)

                    outbound_connections_type_0.append(outbound_connections_type_0_item)

                return outbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelConnection"]], data)

        outbound_connections = _parse_outbound_connections(d.pop("outbound_connections"))

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
            host_name=host_name,
            inbound_connections=inbound_connections,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            open_files=open_files,
            open_files_count=open_files_count,
            outbound_connections=outbound_connections,
            pid=pid,
            ppid=ppid,
            short_name=short_name,
            threads=threads,
        )

        model_process.additional_properties = d
        return model_process

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
