r'''
# `docker_container`

Refer to the Terraform Registry for docs: [`docker_container`](https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class Container(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.Container",
):
    '''Represents a {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container docker_container}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        image: builtins.str,
        name: builtins.str,
        attach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        capabilities: typing.Optional[typing.Union["ContainerCapabilities", typing.Dict[builtins.str, typing.Any]]] = None,
        cgroupns_mode: typing.Optional[builtins.str] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
        cpu_set: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        destroy_grace_seconds: typing.Optional[jsii.Number] = None,
        devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
        domainname: typing.Optional[builtins.str] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        gpus: typing.Optional[builtins.str] = None,
        group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union["ContainerHealthcheck", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        init: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_driver: typing.Optional[builtins.str] = None,
        log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_retry_count: typing.Optional[jsii.Number] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        must_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        networks_advanced: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        publish_all_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remove_volumes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restart: typing.Optional[builtins.str] = None,
        rm: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        runtime: typing.Optional[builtins.str] = None,
        security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        start: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stdin_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        stop_timeout: typing.Optional[jsii.Number] = None,
        storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        upload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[builtins.str] = None,
        userns_mode: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_timeout: typing.Optional[jsii.Number] = None,
        working_dir: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container docker_container} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param image: The ID of the image to back this container. The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#image Container#image}
        :param name: The name of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        :param attach: If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#attach Container#attach}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#capabilities Container#capabilities}
        :param cgroupns_mode: Cgroup namespace mode to use for the container. Possible values are: ``private``, ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cgroupns_mode Container#cgroupns_mode}
        :param command: The command to use to start the container. For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-f","baz.con"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#command Container#command}
        :param container_read_refresh_timeout_milliseconds: The total number of milliseconds to wait for the container to reach status 'running'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        :param cpu_set: A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_set Container#cpu_set}
        :param cpu_shares: CPU shares (relative weight) for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_shares Container#cpu_shares}
        :param destroy_grace_seconds: If defined will attempt to stop the container before destroying. Container will be destroyed after ``n`` seconds or on successful stop. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#destroy_grace_seconds Container#destroy_grace_seconds}
        :param devices: devices block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#devices Container#devices}
        :param dns: DNS servers to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns Container#dns}
        :param dns_opts: DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_opts Container#dns_opts}
        :param dns_search: DNS search domains that are used when bare unqualified hostnames are used inside of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_search Container#dns_search}
        :param domainname: Domain name of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#domainname Container#domainname}
        :param entrypoint: The command to use as the Entrypoint for the container. The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#entrypoint Container#entrypoint}
        :param env: Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#env Container#env}
        :param gpus: GPU devices to add to the container. Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#gpus Container#gpus}
        :param group_add: Additional groups for the container user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#group_add Container#group_add}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#healthcheck Container#healthcheck}
        :param host: host block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host Container#host}
        :param hostname: Hostname of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#hostname Container#hostname}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#id Container#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param init: Configured whether an init process should be injected for this container. If unset this will default to the ``dockerd`` defaults. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#init Container#init}
        :param ipc_mode: IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipc_mode Container#ipc_mode}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        :param links: Set of links for link based connectivity between containers that are running on the same host. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#links Container#links}
        :param log_driver: The logging driver to use for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_driver Container#log_driver}
        :param log_opts: Key/value pairs to use as options for the logging driver. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_opts Container#log_opts}
        :param logs: Save the container logs (``attach`` must be enabled). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#logs Container#logs}
        :param max_retry_count: The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#max_retry_count Container#max_retry_count}
        :param memory: The memory limit for the container in MBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory Container#memory}
        :param memory_swap: The total memory limit (memory + swap) for the container in MBs. This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory_swap Container#memory_swap}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mounts Container#mounts}
        :param must_run: If ``true``, then the Docker container will be kept running. If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#must_run Container#must_run}
        :param network_alias: Set an alias for the container in all specified networks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_alias Container#network_alias}
        :param network_mode: Network mode of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_mode Container#network_mode}
        :param networks: ID of the networks in which the container is. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks Container#networks}
        :param networks_advanced: networks_advanced block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks_advanced Container#networks_advanced}
        :param pid_mode: he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#pid_mode Container#pid_mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ports Container#ports}
        :param privileged: If ``true``, the container runs in privileged mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#privileged Container#privileged}
        :param publish_all_ports: Publish all ports of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#publish_all_ports Container#publish_all_ports}
        :param read_only: If ``true``, the container will be started as readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        :param remove_volumes: If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#remove_volumes Container#remove_volumes}
        :param restart: The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#restart Container#restart}
        :param rm: If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#rm Container#rm}
        :param runtime: Runtime to use for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#runtime Container#runtime}
        :param security_opts: List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#security_opts Container#security_opts}
        :param shm_size: Size of ``/dev/shm`` in MBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#shm_size Container#shm_size}
        :param start: If ``true``, then the Docker container will be started after creation. If ``false``, then the container is only created. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start Container#start}
        :param stdin_open: If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stdin_open Container#stdin_open}
        :param stop_signal: Signal to stop a container (default ``SIGTERM``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_signal Container#stop_signal}
        :param stop_timeout: Timeout (in seconds) to stop a container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_timeout Container#stop_timeout}
        :param storage_opts: Key/value pairs for the storage driver options, e.g. ``size``: ``120G``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#storage_opts Container#storage_opts}
        :param sysctls: A map of kernel parameters (sysctls) to set in the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#sysctls Container#sysctls}
        :param tmpfs: A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tmpfs Container#tmpfs}
        :param tty: If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tty Container#tty}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ulimit Container#ulimit}
        :param upload: upload block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#upload Container#upload}
        :param user: User used for run the first process. Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#user Container#user}
        :param userns_mode: Sets the usernamespace mode for the container when usernamespace remapping option is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#userns_mode Container#userns_mode}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volumes Container#volumes}
        :param wait: If ``true``, then the Docker container is waited for being healthy state after creation. If ``false``, then the container health state is not checked. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait Container#wait}
        :param wait_timeout: The timeout in seconds to wait the container to be healthy after creation. Defaults to ``60``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait_timeout Container#wait_timeout}
        :param working_dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#working_dir Container#working_dir}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8420f4ec8afb941e149518b118f3a35ee97ce4675e62b891354bfb9a0048c7dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContainerConfig(
            image=image,
            name=name,
            attach=attach,
            capabilities=capabilities,
            cgroupns_mode=cgroupns_mode,
            command=command,
            container_read_refresh_timeout_milliseconds=container_read_refresh_timeout_milliseconds,
            cpu_set=cpu_set,
            cpu_shares=cpu_shares,
            destroy_grace_seconds=destroy_grace_seconds,
            devices=devices,
            dns=dns,
            dns_opts=dns_opts,
            dns_search=dns_search,
            domainname=domainname,
            entrypoint=entrypoint,
            env=env,
            gpus=gpus,
            group_add=group_add,
            healthcheck=healthcheck,
            host=host,
            hostname=hostname,
            id=id,
            init=init,
            ipc_mode=ipc_mode,
            labels=labels,
            links=links,
            log_driver=log_driver,
            log_opts=log_opts,
            logs=logs,
            max_retry_count=max_retry_count,
            memory=memory,
            memory_swap=memory_swap,
            mounts=mounts,
            must_run=must_run,
            network_alias=network_alias,
            network_mode=network_mode,
            networks=networks,
            networks_advanced=networks_advanced,
            pid_mode=pid_mode,
            ports=ports,
            privileged=privileged,
            publish_all_ports=publish_all_ports,
            read_only=read_only,
            remove_volumes=remove_volumes,
            restart=restart,
            rm=rm,
            runtime=runtime,
            security_opts=security_opts,
            shm_size=shm_size,
            start=start,
            stdin_open=stdin_open,
            stop_signal=stop_signal,
            stop_timeout=stop_timeout,
            storage_opts=storage_opts,
            sysctls=sysctls,
            tmpfs=tmpfs,
            tty=tty,
            ulimit=ulimit,
            upload=upload,
            user=user,
            userns_mode=userns_mode,
            volumes=volumes,
            wait=wait,
            wait_timeout=wait_timeout,
            working_dir=working_dir,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a Container resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Container to import.
        :param import_from_id: The id of the existing Container that should be imported. Refer to the {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Container to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bff20b73f4c2823f238498715191cbc5bf3c5d91dc13bd09dd0a2603bfe1dd4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCapabilities")
    def put_capabilities(
        self,
        *,
        add: typing.Optional[typing.Sequence[builtins.str]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param add: List of linux capabilities to add. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#add Container#add}
        :param drop: List of linux capabilities to drop. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#drop Container#drop}
        '''
        value = ContainerCapabilities(add=add, drop=drop)

        return typing.cast(None, jsii.invoke(self, "putCapabilities", [value]))

    @jsii.member(jsii_name="putDevices")
    def put_devices(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8fa5cf0cf94c147e100eef20d33f2fcdfca770dfb20e57cd4209a35184a1f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDevices", [value]))

    @jsii.member(jsii_name="putHealthcheck")
    def put_healthcheck(
        self,
        *,
        test: typing.Sequence[builtins.str],
        interval: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        start_period: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param test: Command to run to check health. For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#test Container#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#interval Container#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#retries Container#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start_period Container#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#timeout Container#timeout}
        '''
        value = ContainerHealthcheck(
            test=test,
            interval=interval,
            retries=retries,
            start_period=start_period,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthcheck", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa3e43a2c0d98ad294ed60f8954e449ea89afb7dce4a39392d1102723b6b48b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f1cf00f1f2f04c6c6c119c90dd9cb5fa90b120204f498923b2d0d275dee13e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="putMounts")
    def put_mounts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bead9498abea885f6ee8c0ce07bcaa2e41c9e045e6e6b377a05dc8d1c95fa45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMounts", [value]))

    @jsii.member(jsii_name="putNetworksAdvanced")
    def put_networks_advanced(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c023832501ced51e1c1dae71003e9c891751a451cba47d3a2f10e56d1a2ded4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworksAdvanced", [value]))

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a2e770611d581eec5f2ef261891a38186749a307b528a0af90889e947f0e28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="putUlimit")
    def put_ulimit(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ed5ad0ad26c56f4143aa4e1a9aa2d3afda343a32849363c488b9d69d867bd99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUlimit", [value]))

    @jsii.member(jsii_name="putUpload")
    def put_upload(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a07c651ea4569f2fdc9faaa78f877c74dfaa6119debd5302558eadf58a07fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUpload", [value]))

    @jsii.member(jsii_name="putVolumes")
    def put_volumes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d025bdf12a5d1e7872240f5983d8fcbde3fdd44a68734ea4f1e9900ff4057904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolumes", [value]))

    @jsii.member(jsii_name="resetAttach")
    def reset_attach(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttach", []))

    @jsii.member(jsii_name="resetCapabilities")
    def reset_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapabilities", []))

    @jsii.member(jsii_name="resetCgroupnsMode")
    def reset_cgroupns_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCgroupnsMode", []))

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetContainerReadRefreshTimeoutMilliseconds")
    def reset_container_read_refresh_timeout_milliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerReadRefreshTimeoutMilliseconds", []))

    @jsii.member(jsii_name="resetCpuSet")
    def reset_cpu_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuSet", []))

    @jsii.member(jsii_name="resetCpuShares")
    def reset_cpu_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuShares", []))

    @jsii.member(jsii_name="resetDestroyGraceSeconds")
    def reset_destroy_grace_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestroyGraceSeconds", []))

    @jsii.member(jsii_name="resetDevices")
    def reset_devices(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevices", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetDnsOpts")
    def reset_dns_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsOpts", []))

    @jsii.member(jsii_name="resetDnsSearch")
    def reset_dns_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsSearch", []))

    @jsii.member(jsii_name="resetDomainname")
    def reset_domainname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainname", []))

    @jsii.member(jsii_name="resetEntrypoint")
    def reset_entrypoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntrypoint", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetGpus")
    def reset_gpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGpus", []))

    @jsii.member(jsii_name="resetGroupAdd")
    def reset_group_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupAdd", []))

    @jsii.member(jsii_name="resetHealthcheck")
    def reset_healthcheck(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthcheck", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInit")
    def reset_init(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInit", []))

    @jsii.member(jsii_name="resetIpcMode")
    def reset_ipc_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpcMode", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLinks")
    def reset_links(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinks", []))

    @jsii.member(jsii_name="resetLogDriver")
    def reset_log_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDriver", []))

    @jsii.member(jsii_name="resetLogOpts")
    def reset_log_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogOpts", []))

    @jsii.member(jsii_name="resetLogs")
    def reset_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogs", []))

    @jsii.member(jsii_name="resetMaxRetryCount")
    def reset_max_retry_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxRetryCount", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetMemorySwap")
    def reset_memory_swap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemorySwap", []))

    @jsii.member(jsii_name="resetMounts")
    def reset_mounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMounts", []))

    @jsii.member(jsii_name="resetMustRun")
    def reset_must_run(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMustRun", []))

    @jsii.member(jsii_name="resetNetworkAlias")
    def reset_network_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAlias", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetNetworks")
    def reset_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworks", []))

    @jsii.member(jsii_name="resetNetworksAdvanced")
    def reset_networks_advanced(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworksAdvanced", []))

    @jsii.member(jsii_name="resetPidMode")
    def reset_pid_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPidMode", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @jsii.member(jsii_name="resetPrivileged")
    def reset_privileged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileged", []))

    @jsii.member(jsii_name="resetPublishAllPorts")
    def reset_publish_all_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishAllPorts", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetRemoveVolumes")
    def reset_remove_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveVolumes", []))

    @jsii.member(jsii_name="resetRestart")
    def reset_restart(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestart", []))

    @jsii.member(jsii_name="resetRm")
    def reset_rm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRm", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @jsii.member(jsii_name="resetSecurityOpts")
    def reset_security_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityOpts", []))

    @jsii.member(jsii_name="resetShmSize")
    def reset_shm_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShmSize", []))

    @jsii.member(jsii_name="resetStart")
    def reset_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStart", []))

    @jsii.member(jsii_name="resetStdinOpen")
    def reset_stdin_open(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStdinOpen", []))

    @jsii.member(jsii_name="resetStopSignal")
    def reset_stop_signal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopSignal", []))

    @jsii.member(jsii_name="resetStopTimeout")
    def reset_stop_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopTimeout", []))

    @jsii.member(jsii_name="resetStorageOpts")
    def reset_storage_opts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageOpts", []))

    @jsii.member(jsii_name="resetSysctls")
    def reset_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSysctls", []))

    @jsii.member(jsii_name="resetTmpfs")
    def reset_tmpfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTmpfs", []))

    @jsii.member(jsii_name="resetTty")
    def reset_tty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTty", []))

    @jsii.member(jsii_name="resetUlimit")
    def reset_ulimit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUlimit", []))

    @jsii.member(jsii_name="resetUpload")
    def reset_upload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpload", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsernsMode")
    def reset_userns_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernsMode", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @jsii.member(jsii_name="resetWait")
    def reset_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWait", []))

    @jsii.member(jsii_name="resetWaitTimeout")
    def reset_wait_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTimeout", []))

    @jsii.member(jsii_name="resetWorkingDir")
    def reset_working_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkingDir", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bridge")
    def bridge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bridge"))

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> "ContainerCapabilitiesOutputReference":
        return typing.cast("ContainerCapabilitiesOutputReference", jsii.get(self, "capabilities"))

    @builtins.property
    @jsii.member(jsii_name="containerLogs")
    def container_logs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerLogs"))

    @builtins.property
    @jsii.member(jsii_name="devices")
    def devices(self) -> "ContainerDevicesList":
        return typing.cast("ContainerDevicesList", jsii.get(self, "devices"))

    @builtins.property
    @jsii.member(jsii_name="exitCode")
    def exit_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "exitCode"))

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="healthcheck")
    def healthcheck(self) -> "ContainerHealthcheckOutputReference":
        return typing.cast("ContainerHealthcheckOutputReference", jsii.get(self, "healthcheck"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> "ContainerHostList":
        return typing.cast("ContainerHostList", jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipPrefixLength")
    def ip_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipPrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "ContainerLabelsList":
        return typing.cast("ContainerLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="mounts")
    def mounts(self) -> "ContainerMountsList":
        return typing.cast("ContainerMountsList", jsii.get(self, "mounts"))

    @builtins.property
    @jsii.member(jsii_name="networkData")
    def network_data(self) -> "ContainerNetworkDataList":
        return typing.cast("ContainerNetworkDataList", jsii.get(self, "networkData"))

    @builtins.property
    @jsii.member(jsii_name="networksAdvanced")
    def networks_advanced(self) -> "ContainerNetworksAdvancedList":
        return typing.cast("ContainerNetworksAdvancedList", jsii.get(self, "networksAdvanced"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "ContainerPortsList":
        return typing.cast("ContainerPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="ulimit")
    def ulimit(self) -> "ContainerUlimitList":
        return typing.cast("ContainerUlimitList", jsii.get(self, "ulimit"))

    @builtins.property
    @jsii.member(jsii_name="upload")
    def upload(self) -> "ContainerUploadList":
        return typing.cast("ContainerUploadList", jsii.get(self, "upload"))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "ContainerVolumesList":
        return typing.cast("ContainerVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="attachInput")
    def attach_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "attachInput"))

    @builtins.property
    @jsii.member(jsii_name="capabilitiesInput")
    def capabilities_input(self) -> typing.Optional["ContainerCapabilities"]:
        return typing.cast(typing.Optional["ContainerCapabilities"], jsii.get(self, "capabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="cgroupnsModeInput")
    def cgroupns_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cgroupnsModeInput"))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="containerReadRefreshTimeoutMillisecondsInput")
    def container_read_refresh_timeout_milliseconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerReadRefreshTimeoutMillisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSetInput")
    def cpu_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuSetInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSharesInput")
    def cpu_shares_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuSharesInput"))

    @builtins.property
    @jsii.member(jsii_name="destroyGraceSecondsInput")
    def destroy_grace_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "destroyGraceSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="devicesInput")
    def devices_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerDevices"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerDevices"]]], jsii.get(self, "devicesInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsOptsInput")
    def dns_opts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsSearchInput")
    def dns_search_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsSearchInput"))

    @builtins.property
    @jsii.member(jsii_name="domainnameInput")
    def domainname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainnameInput"))

    @builtins.property
    @jsii.member(jsii_name="entrypointInput")
    def entrypoint_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entrypointInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="gpusInput")
    def gpus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gpusInput"))

    @builtins.property
    @jsii.member(jsii_name="groupAddInput")
    def group_add_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupAddInput"))

    @builtins.property
    @jsii.member(jsii_name="healthcheckInput")
    def healthcheck_input(self) -> typing.Optional["ContainerHealthcheck"]:
        return typing.cast(typing.Optional["ContainerHealthcheck"], jsii.get(self, "healthcheckInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerHost"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerHost"]]], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="initInput")
    def init_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "initInput"))

    @builtins.property
    @jsii.member(jsii_name="ipcModeInput")
    def ipc_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipcModeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="linksInput")
    def links_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linksInput"))

    @builtins.property
    @jsii.member(jsii_name="logDriverInput")
    def log_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="logOptsInput")
    def log_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "logOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInput")
    def logs_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "logsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetryCountInput")
    def max_retry_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetryCountInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySwapInput")
    def memory_swap_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySwapInput"))

    @builtins.property
    @jsii.member(jsii_name="mountsInput")
    def mounts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMounts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMounts"]]], jsii.get(self, "mountsInput"))

    @builtins.property
    @jsii.member(jsii_name="mustRunInput")
    def must_run_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mustRunInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkAliasInput")
    def network_alias_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="networksAdvancedInput")
    def networks_advanced_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerNetworksAdvanced"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerNetworksAdvanced"]]], jsii.get(self, "networksAdvancedInput"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="pidModeInput")
    def pid_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pidModeInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedInput")
    def privileged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "privilegedInput"))

    @builtins.property
    @jsii.member(jsii_name="publishAllPortsInput")
    def publish_all_ports_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publishAllPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="removeVolumesInput")
    def remove_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "removeVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="restartInput")
    def restart_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restartInput"))

    @builtins.property
    @jsii.member(jsii_name="rmInput")
    def rm_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rmInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityOptsInput")
    def security_opts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="shmSizeInput")
    def shm_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="stdinOpenInput")
    def stdin_open_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "stdinOpenInput"))

    @builtins.property
    @jsii.member(jsii_name="stopSignalInput")
    def stop_signal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stopSignalInput"))

    @builtins.property
    @jsii.member(jsii_name="stopTimeoutInput")
    def stop_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stopTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="storageOptsInput")
    def storage_opts_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "storageOptsInput"))

    @builtins.property
    @jsii.member(jsii_name="sysctlsInput")
    def sysctls_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsInput")
    def tmpfs_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tmpfsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttyInput")
    def tty_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ttyInput"))

    @builtins.property
    @jsii.member(jsii_name="ulimitInput")
    def ulimit_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUlimit"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUlimit"]]], jsii.get(self, "ulimitInput"))

    @builtins.property
    @jsii.member(jsii_name="uploadInput")
    def upload_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUpload"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUpload"]]], jsii.get(self, "uploadInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="usernsModeInput")
    def userns_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernsModeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerVolumes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerVolumes"]]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="waitInput")
    def wait_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimeoutInput")
    def wait_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="workingDirInput")
    def working_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirInput"))

    @builtins.property
    @jsii.member(jsii_name="attach")
    def attach(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "attach"))

    @attach.setter
    def attach(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40aeeb83dfa58aaa3c10cf15a697a6574e3be99bab712605a6e505bb33a404a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attach", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cgroupnsMode")
    def cgroupns_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cgroupnsMode"))

    @cgroupns_mode.setter
    def cgroupns_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a1dc42e8edbad579ce1c93321ef2fabc4f9b3aebf032e484c1358af6256187c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cgroupnsMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "command"))

    @command.setter
    def command(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9227fa264db70597595ddaf2127e884b1e4a756c0cf351638de59dfc0fdbeeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerReadRefreshTimeoutMilliseconds")
    def container_read_refresh_timeout_milliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerReadRefreshTimeoutMilliseconds"))

    @container_read_refresh_timeout_milliseconds.setter
    def container_read_refresh_timeout_milliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c0fff4d4e62d1b793d297d382a0b4ea214522a2ea0934a8b24d03b5f54c12b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerReadRefreshTimeoutMilliseconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuSet")
    def cpu_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuSet"))

    @cpu_set.setter
    def cpu_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12138d8cb6077180dbb9e2d45c37d6d198d68b44a07b753995d4c9bbee90031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuShares")
    def cpu_shares(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuShares"))

    @cpu_shares.setter
    def cpu_shares(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703dca3f3c2ba3cef7e64dc94e6609595066ff7b8b3f0cba812ed1955a70c929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuShares", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destroyGraceSeconds")
    def destroy_grace_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "destroyGraceSeconds"))

    @destroy_grace_seconds.setter
    def destroy_grace_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e51c5cd1cd057a7a9817e5d193deb4e32e0609797d50b26324b55c103aa2d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destroyGraceSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dns"))

    @dns.setter
    def dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575877cdfc616405c9d74c89f39e82ac461dc11aa66a387f9927e7d81c2be942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnsOpts")
    def dns_opts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsOpts"))

    @dns_opts.setter
    def dns_opts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c302c434d434e1db4361625aa0c232bf297d35873eb4d86b4f9e8525cdc044a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsOpts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dnsSearch")
    def dns_search(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsSearch"))

    @dns_search.setter
    def dns_search(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__246b397e6b05f7319c2b7c31b69d5aaabfd5aafa5fea81a6a6f5aacbb56f8104)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsSearch", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainname")
    def domainname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainname"))

    @domainname.setter
    def domainname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c88594f6c6b71226cb30703cc497893290677336999acd757f4be4ad7398380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entrypoint")
    def entrypoint(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entrypoint"))

    @entrypoint.setter
    def entrypoint(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee8a4e38081fbb030b8d694f52a3e30d71b91ddc179e7d9452c548f94895f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entrypoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c5f7a6dd26ef1d9e2fac7c08c0796147835a037050014a48e531ca227ddf7e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gpus")
    def gpus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gpus"))

    @gpus.setter
    def gpus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e8e2592a74bf60517c26c553468aadfce288fdb5886dbef4bb9378654405b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupAdd")
    def group_add(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupAdd"))

    @group_add.setter
    def group_add(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8571dd0c5e17e6382b854c58be48e378d8e563b3e18f6045b5d58dbfd248ceab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupAdd", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__252237edae22e21091807f78088266d7c2cde6816dd6f9a46b8c592c82758666)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5851caa562a002a0fa13e3ffd210102650b3155416adcd1653315f86c2c8d624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b4b2a40c8441c1c78e7ce96a2e994d22b444111b9bf247c6e5c6eaef9e32cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="init")
    def init(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "init"))

    @init.setter
    def init(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a87e0268f38fbcf3460e0a004fa9fdf56fad7a1dbf25ce223fe608052da4d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "init", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipcMode")
    def ipc_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipcMode"))

    @ipc_mode.setter
    def ipc_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e68cf56cb7eac5d1d14c7adeaf12ec4d1764b40ebe1ea846b26bbed8162d53f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipcMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "links"))

    @links.setter
    def links(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7daa55a5fc38c816d182956fff7c08066ccfbc9e951e261cd14af7cb7ea163de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "links", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDriver"))

    @log_driver.setter
    def log_driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f77942110c0754662015d95c3934b0a829ab14573254e2991f0defd2d93b981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDriver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logOpts")
    def log_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "logOpts"))

    @log_opts.setter
    def log_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e185d1c9463d08cda6d225a264b329cc5ec0488291884f0e37325c46bb2c998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logOpts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "logs"))

    @logs.setter
    def logs(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa37b17dda97ff8623d5e283dc3576e76ab2fe28f08bb7e79932d0ba82acb5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxRetryCount")
    def max_retry_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetryCount"))

    @max_retry_count.setter
    def max_retry_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8316518950db8d0ab140758522c6638d5f2866bbdd84f393640b3250d549db36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetryCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be746b4cfcf79b97e132598fc2a97307118c9aab1fae4d8f964b44369a43f33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memorySwap")
    def memory_swap(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySwap"))

    @memory_swap.setter
    def memory_swap(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0307074c31c7f4401fbd56fdf151e7866b40e52f6d5359d27e16e818da62617c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySwap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mustRun")
    def must_run(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mustRun"))

    @must_run.setter
    def must_run(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f07ebc0010247354841e815e7430cb5b6f7573520e15090a4651e962039bf92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mustRun", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6683a1b4167b283cbaab61766482b7bc5e9e99801c847c6e71b31b863587fbb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkAlias")
    def network_alias(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkAlias"))

    @network_alias.setter
    def network_alias(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f47004de13cfe577f98bb510d113269282197a122b1f5a869cabfa9c6264ab63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b34c0046dd7e05bcde3f267338db98452cde3f354d7bcc10ea2ede8a2e54fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networks"))

    @networks.setter
    def networks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c00a44a66c8b38a625435129c9d756898dcffd56ca4825073ff175e3c3c612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pidMode")
    def pid_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pidMode"))

    @pid_mode.setter
    def pid_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44788be8dc91421b94a1cbdb9f4b86da185db295a0a14b61bacd79551cd5b13e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pidMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "privileged"))

    @privileged.setter
    def privileged(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a34d1b713e0314a494fc8e1bf5abe563360892a2b6877c42b4eee4a331b38d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileged", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publishAllPorts")
    def publish_all_ports(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "publishAllPorts"))

    @publish_all_ports.setter
    def publish_all_ports(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3543b7aebccea66143e4c21278e1cf6445ca2eabd224c561d25beb8cc26bf97a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishAllPorts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7208591003fca68bb202fc8eeac58c432669e1a069d844daac4a6e3d1736a510)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="removeVolumes")
    def remove_volumes(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "removeVolumes"))

    @remove_volumes.setter
    def remove_volumes(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958c3bc61312a8d948cec93124e1385db9e0e0ca665109f15f1d4108c0cad224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeVolumes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="restart")
    def restart(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restart"))

    @restart.setter
    def restart(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__616a0619d12446a85114060a084a66798e886f786e54b0bd782eb904af1e6702)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restart", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rm")
    def rm(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rm"))

    @rm.setter
    def rm(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ebe2e684b69678f2d645738d6f173c43b3576c8216e6faff746c9e16e1a3ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rm", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__357e5d075f9f77e877d9d8f3f5c35e6626e297e3623ed54789c10082bc45a8fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityOpts")
    def security_opts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityOpts"))

    @security_opts.setter
    def security_opts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__493989f7a23bc4e86e4c6da93685e78f2fc60263103bcf8b5b2104bfb24e9066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityOpts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shmSize")
    def shm_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shmSize"))

    @shm_size.setter
    def shm_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9684341ddb755ac8090e9a33cb3cce2d6d56cda24f990532adb12b23506e89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shmSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "start"))

    @start.setter
    def start(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67b30ba649c9149bcb99a9079d207ca6835f124ac6b5ff84c2b290b305be9362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stdinOpen")
    def stdin_open(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "stdinOpen"))

    @stdin_open.setter
    def stdin_open(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dc3c9eaa1491ba0da5d2f01c2c41b8ea5b35b1d1daf60196582ffe52fa39c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stdinOpen", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stopSignal")
    def stop_signal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stopSignal"))

    @stop_signal.setter
    def stop_signal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adda57a975f17bd6938ec29586d18e72f2eae87997495a607971b521f423df72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopSignal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stopTimeout")
    def stop_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stopTimeout"))

    @stop_timeout.setter
    def stop_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed26159fd70aa06114aac6771be8f563ab6f78a14fd22d4c7cf7188267bb274)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopTimeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageOpts")
    def storage_opts(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "storageOpts"))

    @storage_opts.setter
    def storage_opts(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f42f8b07484c0a35952279d91de52431b98cfc1263b5d4f469dab3edb0f5039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageOpts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sysctls")
    def sysctls(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sysctls"))

    @sysctls.setter
    def sysctls(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ffd5f6dacbfae0b42996eb7ddacac897fbd3736bf14d918221570b6f42b6c78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sysctls", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tmpfs")
    def tmpfs(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tmpfs"))

    @tmpfs.setter
    def tmpfs(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__357af71a22db2f70679c4bae0f429f7dc86a4b7dbc27b7bcbeae48da476d0191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tmpfs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tty")
    def tty(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tty"))

    @tty.setter
    def tty(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405db67569515d9dec43c6b49430e728ff303df4a139aeb15158dfde9d2238da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tty", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd9328921849994a6b22b689c869a4f856ef29046fc5c150ac3c7978e1cb5ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="usernsMode")
    def userns_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usernsMode"))

    @userns_mode.setter
    def userns_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4ee8ee9a1b1da42fb5530a402b43974ebe000fe106f46d996e0d0e31bef558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernsMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wait")
    def wait(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "wait"))

    @wait.setter
    def wait(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e88cd1bdb6bdc8303f982ec1d6541f4e52777d99f78aa2748591d1db8458285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wait", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="waitTimeout")
    def wait_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitTimeout"))

    @wait_timeout.setter
    def wait_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede1bbf5b73a1a834276dc52d8bb5fa956450f7b0db6a59edb7341ddaa73b707)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTimeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workingDir")
    def working_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workingDir"))

    @working_dir.setter
    def working_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5242d455ae8d44d68faed4cfc4531fb375a35b6de64a6d85392e764c2029bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDir", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerCapabilities",
    jsii_struct_bases=[],
    name_mapping={"add": "add", "drop": "drop"},
)
class ContainerCapabilities:
    def __init__(
        self,
        *,
        add: typing.Optional[typing.Sequence[builtins.str]] = None,
        drop: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param add: List of linux capabilities to add. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#add Container#add}
        :param drop: List of linux capabilities to drop. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#drop Container#drop}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2790931e1802e970db0fbbece0e90e9b25fc4f6534b2827c8049c94b6f4d1711)
            check_type(argname="argument add", value=add, expected_type=type_hints["add"])
            check_type(argname="argument drop", value=drop, expected_type=type_hints["drop"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add is not None:
            self._values["add"] = add
        if drop is not None:
            self._values["drop"] = drop

    @builtins.property
    def add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of linux capabilities to add.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#add Container#add}
        '''
        result = self._values.get("add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def drop(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of linux capabilities to drop.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#drop Container#drop}
        '''
        result = self._values.get("drop")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerCapabilitiesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerCapabilitiesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0951a6bdc6c10ad4fad15936ef16d38a933374ff088568b681fa560a6bbc4db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdd")
    def reset_add(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdd", []))

    @jsii.member(jsii_name="resetDrop")
    def reset_drop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDrop", []))

    @builtins.property
    @jsii.member(jsii_name="addInput")
    def add_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addInput"))

    @builtins.property
    @jsii.member(jsii_name="dropInput")
    def drop_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dropInput"))

    @builtins.property
    @jsii.member(jsii_name="add")
    def add(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "add"))

    @add.setter
    def add(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec57e0a595c28334f2ec5ed2aa9165ebe79b91365a5ef46491a74425885b9fac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "add", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="drop")
    def drop(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "drop"))

    @drop.setter
    def drop(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e006e321698fcef0e61d7f12b5a43479681c045ac3e6b7c21ffae74b03f1b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "drop", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerCapabilities]:
        return typing.cast(typing.Optional[ContainerCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerCapabilities]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81ce3103e4a6eef3579ba9972833d51a5179e78caf5f13dd047903ca814d0c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "image": "image",
        "name": "name",
        "attach": "attach",
        "capabilities": "capabilities",
        "cgroupns_mode": "cgroupnsMode",
        "command": "command",
        "container_read_refresh_timeout_milliseconds": "containerReadRefreshTimeoutMilliseconds",
        "cpu_set": "cpuSet",
        "cpu_shares": "cpuShares",
        "destroy_grace_seconds": "destroyGraceSeconds",
        "devices": "devices",
        "dns": "dns",
        "dns_opts": "dnsOpts",
        "dns_search": "dnsSearch",
        "domainname": "domainname",
        "entrypoint": "entrypoint",
        "env": "env",
        "gpus": "gpus",
        "group_add": "groupAdd",
        "healthcheck": "healthcheck",
        "host": "host",
        "hostname": "hostname",
        "id": "id",
        "init": "init",
        "ipc_mode": "ipcMode",
        "labels": "labels",
        "links": "links",
        "log_driver": "logDriver",
        "log_opts": "logOpts",
        "logs": "logs",
        "max_retry_count": "maxRetryCount",
        "memory": "memory",
        "memory_swap": "memorySwap",
        "mounts": "mounts",
        "must_run": "mustRun",
        "network_alias": "networkAlias",
        "network_mode": "networkMode",
        "networks": "networks",
        "networks_advanced": "networksAdvanced",
        "pid_mode": "pidMode",
        "ports": "ports",
        "privileged": "privileged",
        "publish_all_ports": "publishAllPorts",
        "read_only": "readOnly",
        "remove_volumes": "removeVolumes",
        "restart": "restart",
        "rm": "rm",
        "runtime": "runtime",
        "security_opts": "securityOpts",
        "shm_size": "shmSize",
        "start": "start",
        "stdin_open": "stdinOpen",
        "stop_signal": "stopSignal",
        "stop_timeout": "stopTimeout",
        "storage_opts": "storageOpts",
        "sysctls": "sysctls",
        "tmpfs": "tmpfs",
        "tty": "tty",
        "ulimit": "ulimit",
        "upload": "upload",
        "user": "user",
        "userns_mode": "usernsMode",
        "volumes": "volumes",
        "wait": "wait",
        "wait_timeout": "waitTimeout",
        "working_dir": "workingDir",
    },
)
class ContainerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        image: builtins.str,
        name: builtins.str,
        attach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        capabilities: typing.Optional[typing.Union[ContainerCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
        cgroupns_mode: typing.Optional[builtins.str] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
        cpu_set: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        destroy_grace_seconds: typing.Optional[jsii.Number] = None,
        devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerDevices", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
        domainname: typing.Optional[builtins.str] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        gpus: typing.Optional[builtins.str] = None,
        group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union["ContainerHealthcheck", typing.Dict[builtins.str, typing.Any]]] = None,
        host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerHost", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        init: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ipc_mode: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        links: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_driver: typing.Optional[builtins.str] = None,
        log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_retry_count: typing.Optional[jsii.Number] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerMounts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        must_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
        network_mode: typing.Optional[builtins.str] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        networks_advanced: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerNetworksAdvanced", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pid_mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        publish_all_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remove_volumes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        restart: typing.Optional[builtins.str] = None,
        rm: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        runtime: typing.Optional[builtins.str] = None,
        security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        start: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stdin_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        stop_timeout: typing.Optional[jsii.Number] = None,
        storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUlimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        upload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerUpload", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[builtins.str] = None,
        userns_mode: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerVolumes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_timeout: typing.Optional[jsii.Number] = None,
        working_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param image: The ID of the image to back this container. The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#image Container#image}
        :param name: The name of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        :param attach: If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#attach Container#attach}
        :param capabilities: capabilities block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#capabilities Container#capabilities}
        :param cgroupns_mode: Cgroup namespace mode to use for the container. Possible values are: ``private``, ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cgroupns_mode Container#cgroupns_mode}
        :param command: The command to use to start the container. For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-f","baz.con"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#command Container#command}
        :param container_read_refresh_timeout_milliseconds: The total number of milliseconds to wait for the container to reach status 'running'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        :param cpu_set: A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_set Container#cpu_set}
        :param cpu_shares: CPU shares (relative weight) for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_shares Container#cpu_shares}
        :param destroy_grace_seconds: If defined will attempt to stop the container before destroying. Container will be destroyed after ``n`` seconds or on successful stop. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#destroy_grace_seconds Container#destroy_grace_seconds}
        :param devices: devices block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#devices Container#devices}
        :param dns: DNS servers to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns Container#dns}
        :param dns_opts: DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_opts Container#dns_opts}
        :param dns_search: DNS search domains that are used when bare unqualified hostnames are used inside of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_search Container#dns_search}
        :param domainname: Domain name of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#domainname Container#domainname}
        :param entrypoint: The command to use as the Entrypoint for the container. The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#entrypoint Container#entrypoint}
        :param env: Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#env Container#env}
        :param gpus: GPU devices to add to the container. Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#gpus Container#gpus}
        :param group_add: Additional groups for the container user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#group_add Container#group_add}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#healthcheck Container#healthcheck}
        :param host: host block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host Container#host}
        :param hostname: Hostname of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#hostname Container#hostname}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#id Container#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param init: Configured whether an init process should be injected for this container. If unset this will default to the ``dockerd`` defaults. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#init Container#init}
        :param ipc_mode: IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipc_mode Container#ipc_mode}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        :param links: Set of links for link based connectivity between containers that are running on the same host. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#links Container#links}
        :param log_driver: The logging driver to use for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_driver Container#log_driver}
        :param log_opts: Key/value pairs to use as options for the logging driver. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_opts Container#log_opts}
        :param logs: Save the container logs (``attach`` must be enabled). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#logs Container#logs}
        :param max_retry_count: The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#max_retry_count Container#max_retry_count}
        :param memory: The memory limit for the container in MBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory Container#memory}
        :param memory_swap: The total memory limit (memory + swap) for the container in MBs. This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory_swap Container#memory_swap}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mounts Container#mounts}
        :param must_run: If ``true``, then the Docker container will be kept running. If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#must_run Container#must_run}
        :param network_alias: Set an alias for the container in all specified networks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_alias Container#network_alias}
        :param network_mode: Network mode of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_mode Container#network_mode}
        :param networks: ID of the networks in which the container is. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks Container#networks}
        :param networks_advanced: networks_advanced block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks_advanced Container#networks_advanced}
        :param pid_mode: he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#pid_mode Container#pid_mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ports Container#ports}
        :param privileged: If ``true``, the container runs in privileged mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#privileged Container#privileged}
        :param publish_all_ports: Publish all ports of the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#publish_all_ports Container#publish_all_ports}
        :param read_only: If ``true``, the container will be started as readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        :param remove_volumes: If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#remove_volumes Container#remove_volumes}
        :param restart: The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#restart Container#restart}
        :param rm: If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#rm Container#rm}
        :param runtime: Runtime to use for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#runtime Container#runtime}
        :param security_opts: List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#security_opts Container#security_opts}
        :param shm_size: Size of ``/dev/shm`` in MBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#shm_size Container#shm_size}
        :param start: If ``true``, then the Docker container will be started after creation. If ``false``, then the container is only created. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start Container#start}
        :param stdin_open: If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stdin_open Container#stdin_open}
        :param stop_signal: Signal to stop a container (default ``SIGTERM``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_signal Container#stop_signal}
        :param stop_timeout: Timeout (in seconds) to stop a container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_timeout Container#stop_timeout}
        :param storage_opts: Key/value pairs for the storage driver options, e.g. ``size``: ``120G``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#storage_opts Container#storage_opts}
        :param sysctls: A map of kernel parameters (sysctls) to set in the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#sysctls Container#sysctls}
        :param tmpfs: A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tmpfs Container#tmpfs}
        :param tty: If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tty Container#tty}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ulimit Container#ulimit}
        :param upload: upload block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#upload Container#upload}
        :param user: User used for run the first process. Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#user Container#user}
        :param userns_mode: Sets the usernamespace mode for the container when usernamespace remapping option is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#userns_mode Container#userns_mode}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volumes Container#volumes}
        :param wait: If ``true``, then the Docker container is waited for being healthy state after creation. If ``false``, then the container health state is not checked. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait Container#wait}
        :param wait_timeout: The timeout in seconds to wait the container to be healthy after creation. Defaults to ``60``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait_timeout Container#wait_timeout}
        :param working_dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#working_dir Container#working_dir}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(capabilities, dict):
            capabilities = ContainerCapabilities(**capabilities)
        if isinstance(healthcheck, dict):
            healthcheck = ContainerHealthcheck(**healthcheck)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0668b751bef53a116e94d361f638de42cb59414e5aa0c897531cf78eb674d88b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attach", value=attach, expected_type=type_hints["attach"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument cgroupns_mode", value=cgroupns_mode, expected_type=type_hints["cgroupns_mode"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument container_read_refresh_timeout_milliseconds", value=container_read_refresh_timeout_milliseconds, expected_type=type_hints["container_read_refresh_timeout_milliseconds"])
            check_type(argname="argument cpu_set", value=cpu_set, expected_type=type_hints["cpu_set"])
            check_type(argname="argument cpu_shares", value=cpu_shares, expected_type=type_hints["cpu_shares"])
            check_type(argname="argument destroy_grace_seconds", value=destroy_grace_seconds, expected_type=type_hints["destroy_grace_seconds"])
            check_type(argname="argument devices", value=devices, expected_type=type_hints["devices"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument dns_opts", value=dns_opts, expected_type=type_hints["dns_opts"])
            check_type(argname="argument dns_search", value=dns_search, expected_type=type_hints["dns_search"])
            check_type(argname="argument domainname", value=domainname, expected_type=type_hints["domainname"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument gpus", value=gpus, expected_type=type_hints["gpus"])
            check_type(argname="argument group_add", value=group_add, expected_type=type_hints["group_add"])
            check_type(argname="argument healthcheck", value=healthcheck, expected_type=type_hints["healthcheck"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument init", value=init, expected_type=type_hints["init"])
            check_type(argname="argument ipc_mode", value=ipc_mode, expected_type=type_hints["ipc_mode"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument links", value=links, expected_type=type_hints["links"])
            check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
            check_type(argname="argument log_opts", value=log_opts, expected_type=type_hints["log_opts"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument max_retry_count", value=max_retry_count, expected_type=type_hints["max_retry_count"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument memory_swap", value=memory_swap, expected_type=type_hints["memory_swap"])
            check_type(argname="argument mounts", value=mounts, expected_type=type_hints["mounts"])
            check_type(argname="argument must_run", value=must_run, expected_type=type_hints["must_run"])
            check_type(argname="argument network_alias", value=network_alias, expected_type=type_hints["network_alias"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
            check_type(argname="argument networks_advanced", value=networks_advanced, expected_type=type_hints["networks_advanced"])
            check_type(argname="argument pid_mode", value=pid_mode, expected_type=type_hints["pid_mode"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument publish_all_ports", value=publish_all_ports, expected_type=type_hints["publish_all_ports"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument remove_volumes", value=remove_volumes, expected_type=type_hints["remove_volumes"])
            check_type(argname="argument restart", value=restart, expected_type=type_hints["restart"])
            check_type(argname="argument rm", value=rm, expected_type=type_hints["rm"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument security_opts", value=security_opts, expected_type=type_hints["security_opts"])
            check_type(argname="argument shm_size", value=shm_size, expected_type=type_hints["shm_size"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument stdin_open", value=stdin_open, expected_type=type_hints["stdin_open"])
            check_type(argname="argument stop_signal", value=stop_signal, expected_type=type_hints["stop_signal"])
            check_type(argname="argument stop_timeout", value=stop_timeout, expected_type=type_hints["stop_timeout"])
            check_type(argname="argument storage_opts", value=storage_opts, expected_type=type_hints["storage_opts"])
            check_type(argname="argument sysctls", value=sysctls, expected_type=type_hints["sysctls"])
            check_type(argname="argument tmpfs", value=tmpfs, expected_type=type_hints["tmpfs"])
            check_type(argname="argument tty", value=tty, expected_type=type_hints["tty"])
            check_type(argname="argument ulimit", value=ulimit, expected_type=type_hints["ulimit"])
            check_type(argname="argument upload", value=upload, expected_type=type_hints["upload"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument userns_mode", value=userns_mode, expected_type=type_hints["userns_mode"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument wait", value=wait, expected_type=type_hints["wait"])
            check_type(argname="argument wait_timeout", value=wait_timeout, expected_type=type_hints["wait_timeout"])
            check_type(argname="argument working_dir", value=working_dir, expected_type=type_hints["working_dir"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image": image,
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if attach is not None:
            self._values["attach"] = attach
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if cgroupns_mode is not None:
            self._values["cgroupns_mode"] = cgroupns_mode
        if command is not None:
            self._values["command"] = command
        if container_read_refresh_timeout_milliseconds is not None:
            self._values["container_read_refresh_timeout_milliseconds"] = container_read_refresh_timeout_milliseconds
        if cpu_set is not None:
            self._values["cpu_set"] = cpu_set
        if cpu_shares is not None:
            self._values["cpu_shares"] = cpu_shares
        if destroy_grace_seconds is not None:
            self._values["destroy_grace_seconds"] = destroy_grace_seconds
        if devices is not None:
            self._values["devices"] = devices
        if dns is not None:
            self._values["dns"] = dns
        if dns_opts is not None:
            self._values["dns_opts"] = dns_opts
        if dns_search is not None:
            self._values["dns_search"] = dns_search
        if domainname is not None:
            self._values["domainname"] = domainname
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if env is not None:
            self._values["env"] = env
        if gpus is not None:
            self._values["gpus"] = gpus
        if group_add is not None:
            self._values["group_add"] = group_add
        if healthcheck is not None:
            self._values["healthcheck"] = healthcheck
        if host is not None:
            self._values["host"] = host
        if hostname is not None:
            self._values["hostname"] = hostname
        if id is not None:
            self._values["id"] = id
        if init is not None:
            self._values["init"] = init
        if ipc_mode is not None:
            self._values["ipc_mode"] = ipc_mode
        if labels is not None:
            self._values["labels"] = labels
        if links is not None:
            self._values["links"] = links
        if log_driver is not None:
            self._values["log_driver"] = log_driver
        if log_opts is not None:
            self._values["log_opts"] = log_opts
        if logs is not None:
            self._values["logs"] = logs
        if max_retry_count is not None:
            self._values["max_retry_count"] = max_retry_count
        if memory is not None:
            self._values["memory"] = memory
        if memory_swap is not None:
            self._values["memory_swap"] = memory_swap
        if mounts is not None:
            self._values["mounts"] = mounts
        if must_run is not None:
            self._values["must_run"] = must_run
        if network_alias is not None:
            self._values["network_alias"] = network_alias
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if networks is not None:
            self._values["networks"] = networks
        if networks_advanced is not None:
            self._values["networks_advanced"] = networks_advanced
        if pid_mode is not None:
            self._values["pid_mode"] = pid_mode
        if ports is not None:
            self._values["ports"] = ports
        if privileged is not None:
            self._values["privileged"] = privileged
        if publish_all_ports is not None:
            self._values["publish_all_ports"] = publish_all_ports
        if read_only is not None:
            self._values["read_only"] = read_only
        if remove_volumes is not None:
            self._values["remove_volumes"] = remove_volumes
        if restart is not None:
            self._values["restart"] = restart
        if rm is not None:
            self._values["rm"] = rm
        if runtime is not None:
            self._values["runtime"] = runtime
        if security_opts is not None:
            self._values["security_opts"] = security_opts
        if shm_size is not None:
            self._values["shm_size"] = shm_size
        if start is not None:
            self._values["start"] = start
        if stdin_open is not None:
            self._values["stdin_open"] = stdin_open
        if stop_signal is not None:
            self._values["stop_signal"] = stop_signal
        if stop_timeout is not None:
            self._values["stop_timeout"] = stop_timeout
        if storage_opts is not None:
            self._values["storage_opts"] = storage_opts
        if sysctls is not None:
            self._values["sysctls"] = sysctls
        if tmpfs is not None:
            self._values["tmpfs"] = tmpfs
        if tty is not None:
            self._values["tty"] = tty
        if ulimit is not None:
            self._values["ulimit"] = ulimit
        if upload is not None:
            self._values["upload"] = upload
        if user is not None:
            self._values["user"] = user
        if userns_mode is not None:
            self._values["userns_mode"] = userns_mode
        if volumes is not None:
            self._values["volumes"] = volumes
        if wait is not None:
            self._values["wait"] = wait
        if wait_timeout is not None:
            self._values["wait_timeout"] = wait_timeout
        if working_dir is not None:
            self._values["working_dir"] = working_dir

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def image(self) -> builtins.str:
        '''The ID of the image to back this container.

        The easiest way to get this value is to use the ``docker_image`` resource as is shown in the example.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#image Container#image}
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attach(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true`` attach to the container after its creation and waits the end of its execution. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#attach Container#attach}
        '''
        result = self._values.get("attach")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[ContainerCapabilities]:
        '''capabilities block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#capabilities Container#capabilities}
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[ContainerCapabilities], result)

    @builtins.property
    def cgroupns_mode(self) -> typing.Optional[builtins.str]:
        '''Cgroup namespace mode to use for the container. Possible values are: ``private``, ``host``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cgroupns_mode Container#cgroupns_mode}
        '''
        result = self._values.get("cgroupns_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to use to start the container.

        For example, to run ``/usr/bin/myprogram -f baz.conf`` set the command to be ``["/usr/bin/myprogram","-f","baz.con"]``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#command Container#command}
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def container_read_refresh_timeout_milliseconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''The total number of milliseconds to wait for the container to reach status 'running'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_read_refresh_timeout_milliseconds Container#container_read_refresh_timeout_milliseconds}
        '''
        result = self._values.get("container_read_refresh_timeout_milliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_set(self) -> typing.Optional[builtins.str]:
        '''A comma-separated list or hyphen-separated range of CPUs a container can use, e.g. ``0-1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_set Container#cpu_set}
        '''
        result = self._values.get("cpu_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_shares(self) -> typing.Optional[jsii.Number]:
        '''CPU shares (relative weight) for the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#cpu_shares Container#cpu_shares}
        '''
        result = self._values.get("cpu_shares")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def destroy_grace_seconds(self) -> typing.Optional[jsii.Number]:
        '''If defined will attempt to stop the container before destroying.

        Container will be destroyed after ``n`` seconds or on successful stop.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#destroy_grace_seconds Container#destroy_grace_seconds}
        '''
        result = self._values.get("destroy_grace_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def devices(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerDevices"]]]:
        '''devices block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#devices Container#devices}
        '''
        result = self._values.get("devices")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerDevices"]]], result)

    @builtins.property
    def dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS servers to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns Container#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_opts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS options used by the DNS provider(s), see ``resolv.conf`` documentation for valid list of options.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_opts Container#dns_opts}
        '''
        result = self._values.get("dns_opts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dns_search(self) -> typing.Optional[typing.List[builtins.str]]:
        '''DNS search domains that are used when bare unqualified hostnames are used inside of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#dns_search Container#dns_search}
        '''
        result = self._values.get("dns_search")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def domainname(self) -> typing.Optional[builtins.str]:
        '''Domain name of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#domainname Container#domainname}
        '''
        result = self._values.get("domainname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to use as the Entrypoint for the container.

        The Entrypoint allows you to configure a container to run as an executable. For example, to run ``/usr/bin/myprogram`` when starting a container, set the entrypoint to be ``"/usr/bin/myprogra"]``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#entrypoint Container#entrypoint}
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Environment variables to set in the form of ``KEY=VALUE``, e.g. ``DEBUG=0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#env Container#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gpus(self) -> typing.Optional[builtins.str]:
        '''GPU devices to add to the container.

        Currently, only the value ``all`` is supported. Passing any other value will result in unexpected behavior.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#gpus Container#gpus}
        '''
        result = self._values.get("gpus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_add(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional groups for the container user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#group_add Container#group_add}
        '''
        result = self._values.get("group_add")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def healthcheck(self) -> typing.Optional["ContainerHealthcheck"]:
        '''healthcheck block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#healthcheck Container#healthcheck}
        '''
        result = self._values.get("healthcheck")
        return typing.cast(typing.Optional["ContainerHealthcheck"], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerHost"]]]:
        '''host block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host Container#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerHost"]]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Hostname of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#hostname Container#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#id Container#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Configured whether an init process should be injected for this container.

        If unset this will default to the ``dockerd`` defaults.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#init Container#init}
        '''
        result = self._values.get("init")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ipc_mode(self) -> typing.Optional[builtins.str]:
        '''IPC sharing mode for the container. Possible values are: ``none``, ``private``, ``shareable``, ``container:<name|id>`` or ``host``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipc_mode Container#ipc_mode}
        '''
        result = self._values.get("ipc_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerLabels"]]], result)

    @builtins.property
    def links(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of links for link based connectivity between containers that are running on the same host.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#links Container#links}
        '''
        result = self._values.get("links")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_driver(self) -> typing.Optional[builtins.str]:
        '''The logging driver to use for the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_driver Container#log_driver}
        '''
        result = self._values.get("log_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_opts(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key/value pairs to use as options for the logging driver.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#log_opts Container#log_opts}
        '''
        result = self._values.get("log_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Save the container logs (``attach`` must be enabled). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#logs Container#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_retry_count(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of times to an attempt a restart when ``restart`` is set to 'on-failure'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#max_retry_count Container#max_retry_count}
        '''
        result = self._values.get("max_retry_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory(self) -> typing.Optional[jsii.Number]:
        '''The memory limit for the container in MBs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory Container#memory}
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_swap(self) -> typing.Optional[jsii.Number]:
        '''The total memory limit (memory + swap) for the container in MBs.

        This setting may compute to ``-1`` after ``terraform apply`` if the target host doesn't support memory swap, when that is the case docker will use a soft limitation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#memory_swap Container#memory_swap}
        '''
        result = self._values.get("memory_swap")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def mounts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMounts"]]]:
        '''mounts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mounts Container#mounts}
        '''
        result = self._values.get("mounts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMounts"]]], result)

    @builtins.property
    def must_run(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, then the Docker container will be kept running.

        If ``false``, then as long as the container exists, Terraform assumes it is successful. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#must_run Container#must_run}
        '''
        result = self._values.get("must_run")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def network_alias(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set an alias for the container in all specified networks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_alias Container#network_alias}
        '''
        result = self._values.get("network_alias")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Network mode of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#network_mode Container#network_mode}
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''ID of the networks in which the container is.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks Container#networks}
        '''
        result = self._values.get("networks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def networks_advanced(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerNetworksAdvanced"]]]:
        '''networks_advanced block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#networks_advanced Container#networks_advanced}
        '''
        result = self._values.get("networks_advanced")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerNetworksAdvanced"]]], result)

    @builtins.property
    def pid_mode(self) -> typing.Optional[builtins.str]:
        '''he PID (Process) Namespace mode for the container. Either ``container:<name|id>`` or ``host``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#pid_mode Container#pid_mode}
        '''
        result = self._values.get("pid_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ports Container#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerPorts"]]], result)

    @builtins.property
    def privileged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, the container runs in privileged mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#privileged Container#privileged}
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def publish_all_ports(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Publish all ports of the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#publish_all_ports Container#publish_all_ports}
        '''
        result = self._values.get("publish_all_ports")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, the container will be started as readonly. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def remove_volumes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, it will remove anonymous volumes associated with the container. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#remove_volumes Container#remove_volumes}
        '''
        result = self._values.get("remove_volumes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def restart(self) -> typing.Optional[builtins.str]:
        '''The restart policy for the container. Must be one of 'no', 'on-failure', 'always', 'unless-stopped'. Defaults to ``no``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#restart Container#restart}
        '''
        result = self._values.get("restart")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rm(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, then the container will be automatically removed when it exits. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#rm Container#rm}
        '''
        result = self._values.get("rm")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''Runtime to use for the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#runtime Container#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_opts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of string values to customize labels for MLS systems, such as SELinux. See https://docs.docker.com/engine/reference/run/#security-configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#security_opts Container#security_opts}
        '''
        result = self._values.get("security_opts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shm_size(self) -> typing.Optional[jsii.Number]:
        '''Size of ``/dev/shm`` in MBs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#shm_size Container#shm_size}
        '''
        result = self._values.get("shm_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, then the Docker container will be started after creation.

        If ``false``, then the container is only created. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start Container#start}
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def stdin_open(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, keep STDIN open even if not attached (``docker run -i``). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stdin_open Container#stdin_open}
        '''
        result = self._values.get("stdin_open")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def stop_signal(self) -> typing.Optional[builtins.str]:
        '''Signal to stop a container (default ``SIGTERM``).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_signal Container#stop_signal}
        '''
        result = self._values.get("stop_signal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stop_timeout(self) -> typing.Optional[jsii.Number]:
        '''Timeout (in seconds) to stop a container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#stop_timeout Container#stop_timeout}
        '''
        result = self._values.get("stop_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_opts(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key/value pairs for the storage driver options, e.g. ``size``: ``120G``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#storage_opts Container#storage_opts}
        '''
        result = self._values.get("storage_opts")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sysctls(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of kernel parameters (sysctls) to set in the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#sysctls Container#sysctls}
        '''
        result = self._values.get("sysctls")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tmpfs(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of container directories which should be replaced by ``tmpfs mounts``, and their corresponding mount options.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tmpfs Container#tmpfs}
        '''
        result = self._values.get("tmpfs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tty(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, allocate a pseudo-tty (``docker run -t``). Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tty Container#tty}
        '''
        result = self._values.get("tty")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ulimit(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUlimit"]]]:
        '''ulimit block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ulimit Container#ulimit}
        '''
        result = self._values.get("ulimit")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUlimit"]]], result)

    @builtins.property
    def upload(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUpload"]]]:
        '''upload block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#upload Container#upload}
        '''
        result = self._values.get("upload")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerUpload"]]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User used for run the first process.

        Format is ``user`` or ``user:group`` which user and group can be passed literraly or by name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#user Container#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def userns_mode(self) -> typing.Optional[builtins.str]:
        '''Sets the usernamespace mode for the container when usernamespace remapping option is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#userns_mode Container#userns_mode}
        '''
        result = self._values.get("userns_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerVolumes"]]]:
        '''volumes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volumes Container#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerVolumes"]]], result)

    @builtins.property
    def wait(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, then the Docker container is waited for being healthy state after creation.

        If ``false``, then the container health state is not checked. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait Container#wait}
        '''
        result = self._values.get("wait")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait_timeout(self) -> typing.Optional[jsii.Number]:
        '''The timeout in seconds to wait the container to be healthy after creation. Defaults to ``60``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#wait_timeout Container#wait_timeout}
        '''
        result = self._values.get("wait_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def working_dir(self) -> typing.Optional[builtins.str]:
        '''The working directory for commands to run in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#working_dir Container#working_dir}
        '''
        result = self._values.get("working_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.container.ContainerDevices",
    jsii_struct_bases=[],
    name_mapping={
        "host_path": "hostPath",
        "container_path": "containerPath",
        "permissions": "permissions",
    },
)
class ContainerDevices:
    def __init__(
        self,
        *,
        host_path: builtins.str,
        container_path: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_path: The path on the host where the device is located. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host_path Container#host_path}
        :param container_path: The path in the container where the device will be bound. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_path Container#container_path}
        :param permissions: The cgroup permissions given to the container to access the device. Defaults to ``rwm``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#permissions Container#permissions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c27b10d1d413a7fe8ac75f976de674eb77580099e7aff550a1a861f83af3b923)
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_path": host_path,
        }
        if container_path is not None:
            self._values["container_path"] = container_path
        if permissions is not None:
            self._values["permissions"] = permissions

    @builtins.property
    def host_path(self) -> builtins.str:
        '''The path on the host where the device is located.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host_path Container#host_path}
        '''
        result = self._values.get("host_path")
        assert result is not None, "Required property 'host_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_path(self) -> typing.Optional[builtins.str]:
        '''The path in the container where the device will be bound.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_path Container#container_path}
        '''
        result = self._values.get("container_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''The cgroup permissions given to the container to access the device. Defaults to ``rwm``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#permissions Container#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerDevices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerDevicesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerDevicesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2ad623880358d6f8b51b6f09921f48cd9c2b012a7e6d0650327593b0cb480c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerDevicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7245998cd864477728c2dbbc585856b0e90bde14f2882fd7d3b22b5204dabe7e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerDevicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c56c91318330cbc189d6a608c878f2f2554ea57eab88784fc36f24d611b60eec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a300c35ea40f39ac0260b69b63863cc9e4bb18933c313708785ae9155f58a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a04fe844a49975f3aa9b0714ec94303650030ec7fff86407cc3c6510212a3aa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerDevices]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerDevices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerDevices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ece0ce431994b3362c75b411fae64890af7bbe52317517d4711302917724c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerDevicesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerDevicesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4672282f1bd753a1a2ccfd2cf0860b7973d53d47dea4438f974cc95843129c3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPath")
    def reset_container_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPath", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @builtins.property
    @jsii.member(jsii_name="containerPathInput")
    def container_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerPathInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPath")
    def container_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerPath"))

    @container_path.setter
    def container_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6780dc29e2f1db9f482a76dfcb3a2fc1edc1956f4cba935dc94b2d02ada8cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a21872f92b1700e33cfd7118c5cc67cc9aaccd33c5e55907f0c96e982bf8d8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c634703177f701ceda71cbd26e3f49f72177f601e243e3e7a2c07c86c00ba389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerDevices]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerDevices]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerDevices]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__522aafed3823e297fac1b4d60753820ac7dcdad0f336c5d2ee348a058199b679)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerHealthcheck",
    jsii_struct_bases=[],
    name_mapping={
        "test": "test",
        "interval": "interval",
        "retries": "retries",
        "start_period": "startPeriod",
        "timeout": "timeout",
    },
)
class ContainerHealthcheck:
    def __init__(
        self,
        *,
        test: typing.Sequence[builtins.str],
        interval: typing.Optional[builtins.str] = None,
        retries: typing.Optional[jsii.Number] = None,
        start_period: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param test: Command to run to check health. For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#test Container#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#interval Container#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#retries Container#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start_period Container#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#timeout Container#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053a42d396ebd35ba5d683f5a2b2fcad62df06394965668ea0f4a55bd282dd5e)
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument start_period", value=start_period, expected_type=type_hints["start_period"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "test": test,
        }
        if interval is not None:
            self._values["interval"] = interval
        if retries is not None:
            self._values["retries"] = retries
        if start_period is not None:
            self._values["start_period"] = start_period
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def test(self) -> typing.List[builtins.str]:
        '''Command to run to check health.

        For example, to run ``curl -f localhost/health`` set the command to be ``["CMD", "curl", "-f", "localhost/health"]``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#test Container#test}
        '''
        result = self._values.get("test")
        assert result is not None, "Required property 'test' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time between running the check (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#interval Container#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Consecutive failures needed to report unhealthy. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#retries Container#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_period(self) -> typing.Optional[builtins.str]:
        '''Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#start_period Container#start_period}
        '''
        result = self._values.get("start_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#timeout Container#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerHealthcheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerHealthcheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerHealthcheckOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdbcf3c7a8bc312dd458c1df2a4be09c173a3c212c9c8155ebee2ef979aef3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetStartPeriod")
    def reset_start_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartPeriod", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="startPeriodInput")
    def start_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="testInput")
    def test_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "testInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0267f0a9e64cb2ceff4bb9ceccf9fae59f1283125a53f7c759b077cbc5f60685)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a8e07acca3be7c2de81beecdb4e903315cb33dc91b40427abfa7f3fbecc3bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startPeriod")
    def start_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startPeriod"))

    @start_period.setter
    def start_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__827b1a40aef5096198baf2c6e957fd271436acfb8348ac0a49949526307c5c5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="test")
    def test(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "test"))

    @test.setter
    def test(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50be8e120ee3bd5d90dcaed844a57db962e17af513581dac40e0ee74b04ee14b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "test", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0f51ff7f54bd43a6bae0efe584a7232c9cbc610a5351bb73d5a63048a3f6bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerHealthcheck]:
        return typing.cast(typing.Optional[ContainerHealthcheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerHealthcheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c60db0267b0147796c31fa34635769005f028789054ab95c9bea3b7c0133c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerHost",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "ip": "ip"},
)
class ContainerHost:
    def __init__(self, *, host: builtins.str, ip: builtins.str) -> None:
        '''
        :param host: Hostname to add. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host Container#host}
        :param ip: IP address this hostname should resolve to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ip Container#ip}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ccfc781c993cb976562a0005114f5ef03db3b05fe3ceb117254e424df4c643)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host": host,
            "ip": ip,
        }

    @builtins.property
    def host(self) -> builtins.str:
        '''Hostname to add.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host Container#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip(self) -> builtins.str:
        '''IP address this hostname should resolve to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ip Container#ip}
        '''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerHostList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerHostList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e233a2282a78df2897fd4e14b40e4b49b89b42997cf453a098235f77ff735389)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerHostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2557b8d85d08a8e8ea38196507b49eda856cc019ae6ee0b5292dca4fd2c271)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerHostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ea9e379ffbac7d9865199fe85aab308055f1dda882a70fa2395aac5493cbe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6692fb08b8bd612b1948f3eb9de937b99bd5998a06535baa5a090389665c3be8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ec61c9d60273c6d07409cb2bb80dc880974ba8dba085652ddef16bfcc3be861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerHost]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerHost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerHost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__135ef0893adfa7cbf39eefc285e9197614c811a1a26cb81e76d5d51cb6ab3fb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerHostOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerHostOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa507edcc04d68bb75d08909e7a43e29b4d676e948915e4b2a02c36000dae002)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c0c49417551a5730e74504e42af5fce08a6ad337902bf33a7ffadaf3a260c12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e2b5be54f54b155280688bf8a625cf991a786d1e8d243ced1bd7b76824319a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerHost]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerHost]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerHost]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f699457876a9267c16c782639ba4775057d205ccd34df119ebace8313c7796a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ContainerLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#label Container#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#value Container#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd383bb73875bf4ecb919742da4f5a4fd95235ac3b5438ab72cfc12d05ad53c8)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#label Container#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#value Container#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerLabelsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffd71205f8e478c1dc1191d4ad072bf6e89c2569c8cdefda6a035cd45c871811)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cf30a7e5bdc3041bdb585ca0ba7a1e99ab942aed617abed14f9b57751b844e6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5518c877d95f9ec0e0778685470248e3e147dc43f381a006e6fdc2d75ad542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c56a3196c735d245f4b7dd33e08f096bf164da595a70544c30a42cfd9458990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034eed4c8f77f83e85e19a48c90de9d9599f54b271dc8b7b94b6127b6ad332ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577691acd73ca45e8ba603f95052ae47c74d7b4e166ee90e38cf3b4eb9554c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerLabelsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8fd6fbed556797d18e6013f177dab26ed7f8c4a224b5124b10adc3a9cf22bff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8802b1a7f84cd29cc63db05d7e6769dcc8f06f912055f71d5f671a7436f5a2be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd03aa5f58821edda14b50794d09b47d9d832860c159394354171579c9d5fd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4763b1dcabdf4ba37eb501a652b9cc225801f00c14f507c8cb5788fb9387642a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerMounts",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "type": "type",
        "bind_options": "bindOptions",
        "read_only": "readOnly",
        "source": "source",
        "tmpfs_options": "tmpfsOptions",
        "volume_options": "volumeOptions",
    },
)
class ContainerMounts:
    def __init__(
        self,
        *,
        target: builtins.str,
        type: builtins.str,
        bind_options: typing.Optional[typing.Union["ContainerMountsBindOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
        tmpfs_options: typing.Optional[typing.Union["ContainerMountsTmpfsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        volume_options: typing.Optional[typing.Union["ContainerMountsVolumeOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: Container path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#target Container#target}
        :param type: The mount type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#type Container#type}
        :param bind_options: bind_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#bind_options Container#bind_options}
        :param read_only: Whether the mount should be read-only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        :param source: Mount source (e.g. a volume name, a host path). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source Container#source}
        :param tmpfs_options: tmpfs_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tmpfs_options Container#tmpfs_options}
        :param volume_options: volume_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volume_options Container#volume_options}
        '''
        if isinstance(bind_options, dict):
            bind_options = ContainerMountsBindOptions(**bind_options)
        if isinstance(tmpfs_options, dict):
            tmpfs_options = ContainerMountsTmpfsOptions(**tmpfs_options)
        if isinstance(volume_options, dict):
            volume_options = ContainerMountsVolumeOptions(**volume_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36bf76b7a97bb8b3fb8bfdcb228391e6b92076731343f85f22a134758fa72a0c)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bind_options", value=bind_options, expected_type=type_hints["bind_options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tmpfs_options", value=tmpfs_options, expected_type=type_hints["tmpfs_options"])
            check_type(argname="argument volume_options", value=volume_options, expected_type=type_hints["volume_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target": target,
            "type": type,
        }
        if bind_options is not None:
            self._values["bind_options"] = bind_options
        if read_only is not None:
            self._values["read_only"] = read_only
        if source is not None:
            self._values["source"] = source
        if tmpfs_options is not None:
            self._values["tmpfs_options"] = tmpfs_options
        if volume_options is not None:
            self._values["volume_options"] = volume_options

    @builtins.property
    def target(self) -> builtins.str:
        '''Container path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#target Container#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The mount type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#type Container#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_options(self) -> typing.Optional["ContainerMountsBindOptions"]:
        '''bind_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#bind_options Container#bind_options}
        '''
        result = self._values.get("bind_options")
        return typing.cast(typing.Optional["ContainerMountsBindOptions"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the mount should be read-only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Mount source (e.g. a volume name, a host path).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source Container#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tmpfs_options(self) -> typing.Optional["ContainerMountsTmpfsOptions"]:
        '''tmpfs_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#tmpfs_options Container#tmpfs_options}
        '''
        result = self._values.get("tmpfs_options")
        return typing.cast(typing.Optional["ContainerMountsTmpfsOptions"], result)

    @builtins.property
    def volume_options(self) -> typing.Optional["ContainerMountsVolumeOptions"]:
        '''volume_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volume_options Container#volume_options}
        '''
        result = self._values.get("volume_options")
        return typing.cast(typing.Optional["ContainerMountsVolumeOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.container.ContainerMountsBindOptions",
    jsii_struct_bases=[],
    name_mapping={"propagation": "propagation"},
)
class ContainerMountsBindOptions:
    def __init__(self, *, propagation: typing.Optional[builtins.str] = None) -> None:
        '''
        :param propagation: A propagation mode with the value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#propagation Container#propagation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cdb3d0daab203b387293a55927990d7486c6dbdd4b923a32b51cb96b464578e)
            check_type(argname="argument propagation", value=propagation, expected_type=type_hints["propagation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if propagation is not None:
            self._values["propagation"] = propagation

    @builtins.property
    def propagation(self) -> typing.Optional[builtins.str]:
        '''A propagation mode with the value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#propagation Container#propagation}
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsBindOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsBindOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7605298cb90767f7f590fc4820b31222d13da158e769780ad10c9ea6eaff8648)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPropagation")
    def reset_propagation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagation", []))

    @builtins.property
    @jsii.member(jsii_name="propagationInput")
    def propagation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagationInput"))

    @builtins.property
    @jsii.member(jsii_name="propagation")
    def propagation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagation"))

    @propagation.setter
    def propagation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea89a58c04ba32814ec9d1234a85516270c38792639754c12b198c707e9ae26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsBindOptions]:
        return typing.cast(typing.Optional[ContainerMountsBindOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsBindOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28db3a274f91fb4689163c5152694df40f5755ebe1deda83d0b438c83c848f29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerMountsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bafbcdfb694ae304630bea35d6d5a744f4a304a5b8ca52adc4947c27c29a479)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerMountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f319073e5044e79561bb2471d821d039df08bbb0ea65538857722dc60cd44c14)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerMountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98507bfe7987cc9e461432c5b5fb5ae551b0a1b48afb51eb5c809c6800e7a6f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d442b27f27090f89f05f329a7183362260d48c70de4d0a20e4256fcd24644961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__055d2b718e2a3d533a3921bc5d382d4335794ddff86a9c6d321beecf4c05310b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMounts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMounts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMounts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b610e28ac4fb8cf637f8d20966c5bb0a92f3afd66f1c005e3fe82d2c3452ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerMountsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda857c098aeeaaf9c82ba7a3d6dac275ff6ebd443997c2638b3f81d97f46663)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBindOptions")
    def put_bind_options(
        self,
        *,
        propagation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param propagation: A propagation mode with the value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#propagation Container#propagation}
        '''
        value = ContainerMountsBindOptions(propagation=propagation)

        return typing.cast(None, jsii.invoke(self, "putBindOptions", [value]))

    @jsii.member(jsii_name="putTmpfsOptions")
    def put_tmpfs_options(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mode Container#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#size_bytes Container#size_bytes}
        '''
        value = ContainerMountsTmpfsOptions(mode=mode, size_bytes=size_bytes)

        return typing.cast(None, jsii.invoke(self, "putTmpfsOptions", [value]))

    @jsii.member(jsii_name="putVolumeOptions")
    def put_volume_options(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerMountsVolumeOptionsLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_name Container#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_options Container#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#no_copy Container#no_copy}
        '''
        value = ContainerMountsVolumeOptions(
            driver_name=driver_name,
            driver_options=driver_options,
            labels=labels,
            no_copy=no_copy,
        )

        return typing.cast(None, jsii.invoke(self, "putVolumeOptions", [value]))

    @jsii.member(jsii_name="resetBindOptions")
    def reset_bind_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBindOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetTmpfsOptions")
    def reset_tmpfs_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTmpfsOptions", []))

    @jsii.member(jsii_name="resetVolumeOptions")
    def reset_volume_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeOptions", []))

    @builtins.property
    @jsii.member(jsii_name="bindOptions")
    def bind_options(self) -> ContainerMountsBindOptionsOutputReference:
        return typing.cast(ContainerMountsBindOptionsOutputReference, jsii.get(self, "bindOptions"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsOptions")
    def tmpfs_options(self) -> "ContainerMountsTmpfsOptionsOutputReference":
        return typing.cast("ContainerMountsTmpfsOptionsOutputReference", jsii.get(self, "tmpfsOptions"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptions")
    def volume_options(self) -> "ContainerMountsVolumeOptionsOutputReference":
        return typing.cast("ContainerMountsVolumeOptionsOutputReference", jsii.get(self, "volumeOptions"))

    @builtins.property
    @jsii.member(jsii_name="bindOptionsInput")
    def bind_options_input(self) -> typing.Optional[ContainerMountsBindOptions]:
        return typing.cast(typing.Optional[ContainerMountsBindOptions], jsii.get(self, "bindOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsOptionsInput")
    def tmpfs_options_input(self) -> typing.Optional["ContainerMountsTmpfsOptions"]:
        return typing.cast(typing.Optional["ContainerMountsTmpfsOptions"], jsii.get(self, "tmpfsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptionsInput")
    def volume_options_input(self) -> typing.Optional["ContainerMountsVolumeOptions"]:
        return typing.cast(typing.Optional["ContainerMountsVolumeOptions"], jsii.get(self, "volumeOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a099c296ee9f2a66ed6d3c74234df0d65d2d3a2edc732c204aa235b8dbb5d553)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e1c059cc87b295a1a2c548b4124ab6743fc97a8b3634952abfeee58e450d984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7309a305f8651211f60e63b011dc7eded2aae99bcb79cc70f021bff2e10b28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c1fc621835ad500ae2b02efff94a38ae3689d8e4082997649d64ca0f0f372b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMounts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMounts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMounts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__673e9810c52e86117ab65eea69bd3c82571db7a8c7d20febf5385063908a414f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerMountsTmpfsOptions",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "size_bytes": "sizeBytes"},
)
class ContainerMountsTmpfsOptions:
    def __init__(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mode Container#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#size_bytes Container#size_bytes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de69cad63efe13dd5d72ba0a4da41ccf1eb5cd5e8c9ded37bd75d8262e4c96cc)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument size_bytes", value=size_bytes, expected_type=type_hints["size_bytes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if size_bytes is not None:
            self._values["size_bytes"] = size_bytes

    @builtins.property
    def mode(self) -> typing.Optional[jsii.Number]:
        '''The permission mode for the tmpfs mount in an integer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#mode Container#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def size_bytes(self) -> typing.Optional[jsii.Number]:
        '''The size for the tmpfs mount in bytes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#size_bytes Container#size_bytes}
        '''
        result = self._values.get("size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsTmpfsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsTmpfsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsTmpfsOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43290204fe3c45632b81c48b99e47f37e5dc4931ab5914ee7c55c7620d2abf34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetSizeBytes")
    def reset_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeBytes", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeBytesInput")
    def size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b770d67c3cb680f3d6fef28753b4f84f018889959a1d672a241fa92cc31dbb61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sizeBytes")
    def size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeBytes"))

    @size_bytes.setter
    def size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ecc6e5a50cd32d66a9f89a871f06d3f89bda7fc08ec6e02f4a941d4ebb53194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsTmpfsOptions]:
        return typing.cast(typing.Optional[ContainerMountsTmpfsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsTmpfsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba1fe4c7fecd0a494a3d48bf375637a7a2527b51b35d01f490a5c5b97aecaf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerMountsVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "driver_name": "driverName",
        "driver_options": "driverOptions",
        "labels": "labels",
        "no_copy": "noCopy",
    },
)
class ContainerMountsVolumeOptions:
    def __init__(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContainerMountsVolumeOptionsLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_name Container#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_options Container#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#no_copy Container#no_copy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3765d463f76a72daf038d1bae8f1a45145d40489c3ad218958841eb6cc607d34)
            check_type(argname="argument driver_name", value=driver_name, expected_type=type_hints["driver_name"])
            check_type(argname="argument driver_options", value=driver_options, expected_type=type_hints["driver_options"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument no_copy", value=no_copy, expected_type=type_hints["no_copy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if driver_name is not None:
            self._values["driver_name"] = driver_name
        if driver_options is not None:
            self._values["driver_options"] = driver_options
        if labels is not None:
            self._values["labels"] = labels
        if no_copy is not None:
            self._values["no_copy"] = no_copy

    @builtins.property
    def driver_name(self) -> typing.Optional[builtins.str]:
        '''Name of the driver to use to create the volume.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_name Container#driver_name}
        '''
        result = self._values.get("driver_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''key/value map of driver specific options.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#driver_options Container#driver_options}
        '''
        result = self._values.get("driver_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMountsVolumeOptionsLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#labels Container#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContainerMountsVolumeOptionsLabels"]]], result)

    @builtins.property
    def no_copy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Populate volume with data from the target.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#no_copy Container#no_copy}
        '''
        result = self._values.get("no_copy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.container.ContainerMountsVolumeOptionsLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ContainerMountsVolumeOptionsLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#label Container#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#value Container#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0388e189676a997973aab6edb56659dd2a84d267b8200e026dd95d36dc8dbde5)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#label Container#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#value Container#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerMountsVolumeOptionsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerMountsVolumeOptionsLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsVolumeOptionsLabelsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4587c399ddade6d6e2b9f35f8c20d7dc63dd575b5274487bd9c299666d00c28c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ContainerMountsVolumeOptionsLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af1e036397083b49e279b1539a6d90ea91679bed11412adb99dff66a9593c9d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerMountsVolumeOptionsLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb5db753cd1b72a1b55d7e3442354598e37fa40a929eb6be9ed32fe092f821ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204f5c4d632c6910f61ae7021cdd5dbca487b7f70744748b1c5dc7be8d89f156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80651f386c6c30b0ba25e0905064cb54c6d98a0b98d2ed7e64068650ab5406c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6443454069c5b002aa90ade2aa7879dfb9ff14780dba08cf2a00c028a0a1c541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerMountsVolumeOptionsLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsVolumeOptionsLabelsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__647684fcbb181143f5233f91bb05e33ccd1088e7eaf054ebafcd54048fa24015)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2e94630bfaa9b8d5209492c8ab27000fe406922ccab8f1af38b0c303e32d9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb7141f34dc1f933b56de2e258dc5d8aca870db6752e8e559a3ab3640c7b32e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMountsVolumeOptionsLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMountsVolumeOptionsLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMountsVolumeOptionsLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cf81649d8a91d0cd49db971db9a8371c95d6aeea05bcd4a615420bf1d53cb40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerMountsVolumeOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerMountsVolumeOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef489ecb5129884df334b98eadcb421a7c604c1ed65ffc039215e12434bf35c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dad236356d66c25054eb04fae0fc655aa8e046fe8a0b76793d304c17ce9f3a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="resetDriverName")
    def reset_driver_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverName", []))

    @jsii.member(jsii_name="resetDriverOptions")
    def reset_driver_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverOptions", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetNoCopy")
    def reset_no_copy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoCopy", []))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> ContainerMountsVolumeOptionsLabelsList:
        return typing.cast(ContainerMountsVolumeOptionsLabelsList, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="driverNameInput")
    def driver_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="driverOptionsInput")
    def driver_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="noCopyInput")
    def no_copy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noCopyInput"))

    @builtins.property
    @jsii.member(jsii_name="driverName")
    def driver_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverName"))

    @driver_name.setter
    def driver_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09de412e129fb8f069cd2e0e3230b0e2dd939219e85faf1099d23aeddc25efe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="driverOptions")
    def driver_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverOptions"))

    @driver_options.setter
    def driver_options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce58489f23cb2178b6f5c13ec2a63e68102413278974a0dd629dd83275c84687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="noCopy")
    def no_copy(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noCopy"))

    @no_copy.setter
    def no_copy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29375523a60e720d8808a255b466af7f2d79c4146a6281fdf21b170ffd484ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noCopy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerMountsVolumeOptions]:
        return typing.cast(typing.Optional[ContainerMountsVolumeOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContainerMountsVolumeOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5090b13fb124d76b0e2943faaa0d0635613ba9875a73ed9f05402c1ad0e2fcb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerNetworkData",
    jsii_struct_bases=[],
    name_mapping={},
)
class ContainerNetworkData:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerNetworkData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerNetworkDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerNetworkDataList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae1a8ed756c894d404212e001bd6b4d28ae7f176a7b1716a617845bf99326cf8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerNetworkDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f85ed47d1dc0352058277683399bd2ddb306a3769f7d5d9bc41d62017f582c35)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerNetworkDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adeb93f7c7cc1233b1eee6d23189a28e6e280e3699bdd3b78c5a3e0ad42e62c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c0550ea9132ee8453acaa6a488173d83813dd31adf5f36774bcb74e9bf87aae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed682d44e172ee8f6ce81e1bd2b7292b269613c627f2a80eadfe1723ab4ed804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]


class ContainerNetworkDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerNetworkDataOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98d94f6ff808815102f790da8bce18d2ac105bdb9d174d973acb64eebd22011)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @builtins.property
    @jsii.member(jsii_name="globalIpv6Address")
    def global_ipv6_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "globalIpv6Address"))

    @builtins.property
    @jsii.member(jsii_name="globalIpv6PrefixLength")
    def global_ipv6_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "globalIpv6PrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipPrefixLength")
    def ip_prefix_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ipPrefixLength"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Gateway")
    def ipv6_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6Gateway"))

    @builtins.property
    @jsii.member(jsii_name="networkName")
    def network_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkName"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContainerNetworkData]:
        return typing.cast(typing.Optional[ContainerNetworkData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContainerNetworkData]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca9833779b8ee112e7b13aad231fbe7f66fc822c1251722f11f33cb93e3be41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerNetworksAdvanced",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "aliases": "aliases",
        "ipv4_address": "ipv4Address",
        "ipv6_address": "ipv6Address",
    },
)
class ContainerNetworksAdvanced:
    def __init__(
        self,
        *,
        name: builtins.str,
        aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipv4_address: typing.Optional[builtins.str] = None,
        ipv6_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name or id of the network to use. You can use ``name`` or ``id`` attribute from a ``docker_network`` resource. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        :param aliases: The network aliases of the container in the specific network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#aliases Container#aliases}
        :param ipv4_address: The IPV4 address of the container in the specific network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipv4_address Container#ipv4_address}
        :param ipv6_address: The IPV6 address of the container in the specific network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipv6_address Container#ipv6_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e35fafaaf1ff52819f16f42e34931124d0bb38caf7f23d40da768e8f20f05d)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aliases", value=aliases, expected_type=type_hints["aliases"])
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument ipv6_address", value=ipv6_address, expected_type=type_hints["ipv6_address"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if aliases is not None:
            self._values["aliases"] = aliases
        if ipv4_address is not None:
            self._values["ipv4_address"] = ipv4_address
        if ipv6_address is not None:
            self._values["ipv6_address"] = ipv6_address

    @builtins.property
    def name(self) -> builtins.str:
        '''The name or id of the network to use.

        You can use ``name`` or ``id`` attribute from a ``docker_network`` resource.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aliases(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The network aliases of the container in the specific network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#aliases Container#aliases}
        '''
        result = self._values.get("aliases")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipv4_address(self) -> typing.Optional[builtins.str]:
        '''The IPV4 address of the container in the specific network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipv4_address Container#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipv6_address(self) -> typing.Optional[builtins.str]:
        '''The IPV6 address of the container in the specific network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ipv6_address Container#ipv6_address}
        '''
        result = self._values.get("ipv6_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerNetworksAdvanced(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerNetworksAdvancedList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerNetworksAdvancedList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8978d2756dc4ca13164bdbae071647b109fe317f68d6a8f2a017822c857ca8ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerNetworksAdvancedOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d9f7d70086d590abd339dc96ba87ace4b36b6727f33b505906d6a129f54150)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerNetworksAdvancedOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa528a0551ee0e2457513dc6812f9b5ae80afcfe7d6bce32c3855af79b111ca3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f1436d5dc460a8dbfd2110ba96359d29012ff9a42b89865b34f1114f436609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19cb9baf359bc8960db27530d3b4ac4beb9441c7a603e091c821ceef067af58b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerNetworksAdvanced]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerNetworksAdvanced]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerNetworksAdvanced]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a365e72161c273af1e371d52e9a95c116382d9a1b35c5e9ad317c3ce0ee3d4c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerNetworksAdvancedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerNetworksAdvancedOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__915b70032d561edf68f9087e737a75fc80ae373b5c80c409a3d4cffbb4d0c48b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAliases")
    def reset_aliases(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliases", []))

    @jsii.member(jsii_name="resetIpv4Address")
    def reset_ipv4_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv4Address", []))

    @jsii.member(jsii_name="resetIpv6Address")
    def reset_ipv6_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6Address", []))

    @builtins.property
    @jsii.member(jsii_name="aliasesInput")
    def aliases_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aliasesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6AddressInput")
    def ipv6_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="aliases")
    def aliases(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliases"))

    @aliases.setter
    def aliases(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1068eff5698b4b4e4660ad4a965b16d43759eb0950629681b547d85b2dc6407b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliases", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2df1a417a03778292b09e0d835f0052ca60a2786332281d175037a96f017d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6Address")
    def ipv6_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6Address"))

    @ipv6_address.setter
    def ipv6_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__141ee8c94de5fd0e0045c71576102609845703ccb168517f431aaa130182ab9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6Address", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3018b820ecfb1834d363862087b9b3ec35f92718b0afa7083580e3019f5318e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerNetworksAdvanced]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerNetworksAdvanced]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerNetworksAdvanced]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9c78398c56f1fe4e9641e8b60b2a67597b1dafea7a84578a00e2fb169359fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerPorts",
    jsii_struct_bases=[],
    name_mapping={
        "internal": "internal",
        "external": "external",
        "ip": "ip",
        "protocol": "protocol",
    },
)
class ContainerPorts:
    def __init__(
        self,
        *,
        internal: jsii.Number,
        external: typing.Optional[jsii.Number] = None,
        ip: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param internal: Port within the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#internal Container#internal}
        :param external: Port exposed out of the container. If not given a free random port ``>= 32768`` will be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#external Container#external}
        :param ip: IP address/mask that can access this port. Defaults to ``0.0.0.0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ip Container#ip}
        :param protocol: Protocol that can be used over this port. Defaults to ``tcp``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#protocol Container#protocol}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded768306be7168a91afabb62ad1c3aeb5519930d434b8890587dd8c2c06b949)
            check_type(argname="argument internal", value=internal, expected_type=type_hints["internal"])
            check_type(argname="argument external", value=external, expected_type=type_hints["external"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "internal": internal,
        }
        if external is not None:
            self._values["external"] = external
        if ip is not None:
            self._values["ip"] = ip
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def internal(self) -> jsii.Number:
        '''Port within the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#internal Container#internal}
        '''
        result = self._values.get("internal")
        assert result is not None, "Required property 'internal' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def external(self) -> typing.Optional[jsii.Number]:
        '''Port exposed out of the container. If not given a free random port ``>= 32768`` will be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#external Container#external}
        '''
        result = self._values.get("external")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''IP address/mask that can access this port. Defaults to ``0.0.0.0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#ip Container#ip}
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Protocol that can be used over this port. Defaults to ``tcp``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#protocol Container#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerPortsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58148ad3fc9843cb7ad7f76e6aa4e6d6755d7b4a1ddfe93cfdc525580595eb38)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18af6e1fe1c023486b265e6cf94cfac7adcc194c0b37e8d84dcc03177d9165bb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f16dc414f572560a3f7037c7baa4fe22de97559bb36b604ed031b763320370d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865081fb892706550991d054d11fc978d60f585364db3d3a1eca791924a1b91a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be673cd3c01cb159d6e346bfcdab38261d933d1a786b20973fbb7b7f8151839)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff8fe51606347c80080c99d7201009c507765ed8cf094fec896cfea810a825a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerPortsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc18f7a1549740b5f2d76e3a8770009c84e84d2cdbd29ce2a1103564b1bd1ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExternal")
    def reset_external(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternal", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="externalInput")
    def external_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "externalInput"))

    @builtins.property
    @jsii.member(jsii_name="internalInput")
    def internal_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "internalInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="external")
    def external(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "external"))

    @external.setter
    def external(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb0ca9b0eb425d0e58ff21be50f367bd640cb7ba255ea58629c679cdeecd4be3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "external", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internal")
    def internal(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "internal"))

    @internal.setter
    def internal(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47c0d8eb04f12640628f26e593c11feb6419fe8e7a4a547098465e5c5c3c133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fe175bac8fde7bdd7003231c8fa1a0c48bb2c92b488f523318ee78156b9bb6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b06f97a6487f6c89d14fa6760ece968343c47e2e83e326e2587bce531c28ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerPorts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerPorts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerPorts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d865e2c1813ee2d7030febd1ccdcf2786975cbc01cc096a616be32cc56289d55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerUlimit",
    jsii_struct_bases=[],
    name_mapping={"hard": "hard", "name": "name", "soft": "soft"},
)
class ContainerUlimit:
    def __init__(
        self,
        *,
        hard: jsii.Number,
        name: builtins.str,
        soft: jsii.Number,
    ) -> None:
        '''
        :param hard: The hard limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#hard Container#hard}
        :param name: The name of the ulimit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        :param soft: The soft limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#soft Container#soft}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5975b23dd190e1400495a55f1c2bc4e15c71c4a9f8ba7b6befae753615cb38f)
            check_type(argname="argument hard", value=hard, expected_type=type_hints["hard"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument soft", value=soft, expected_type=type_hints["soft"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hard": hard,
            "name": name,
            "soft": soft,
        }

    @builtins.property
    def hard(self) -> jsii.Number:
        '''The hard limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#hard Container#hard}
        '''
        result = self._values.get("hard")
        assert result is not None, "Required property 'hard' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the ulimit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#name Container#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def soft(self) -> jsii.Number:
        '''The soft limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#soft Container#soft}
        '''
        result = self._values.get("soft")
        assert result is not None, "Required property 'soft' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerUlimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerUlimitList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerUlimitList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05899289fb172d24ba2277f94cfd3aa1bb4139219d26b3a214d1ed79ff59b373)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerUlimitOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3687af5d70269f79266fdeb2ae4f4f9bfae78e71f23c59bdfde6f1ce1d33eacf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerUlimitOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c00c253173c111ebbc4e5a3e602e8e793bb52600a5df4e3567da22c7899d76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d067d998d702687ed20effba471e0ed956450fb19155e89856d06959262bd84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b7fe5c73e7f32dab1e08af8571c8d4f53107daf8ae10fb2f5f0488d28b6832b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUlimit]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUlimit]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUlimit]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e524370666ce4722dfaaa5beb63f50eded12a52dc59fa25f7d7eb67c83eafd3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerUlimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerUlimitOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb802f9d770a3f72d7ce2f082184f769c6e674330bba4cabd21bff5317914ffb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="hardInput")
    def hard_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hardInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="softInput")
    def soft_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "softInput"))

    @builtins.property
    @jsii.member(jsii_name="hard")
    def hard(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hard"))

    @hard.setter
    def hard(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678e62e230844d1f874d43a6cf39b9c69a9890cdd00d42aca537d482951b1b57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hard", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ca8e9f409ac23296eff62440fb2392104ee0284bbdc5834ab187750386dd3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="soft")
    def soft(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "soft"))

    @soft.setter
    def soft(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc34a4794b56b764ccb7d7283285a9df696cff2a42ca1ec6b2a21cd92d143d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "soft", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUlimit]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUlimit]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUlimit]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146952e2b91c64997b5c4cb8206b6ff5c7d29832a9053d91cbbe5f34c36ca6b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerUpload",
    jsii_struct_bases=[],
    name_mapping={
        "file": "file",
        "content": "content",
        "content_base64": "contentBase64",
        "executable": "executable",
        "source": "source",
        "source_hash": "sourceHash",
    },
)
class ContainerUpload:
    def __init__(
        self,
        *,
        file: builtins.str,
        content: typing.Optional[builtins.str] = None,
        content_base64: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
        source_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: Path to the file in the container where is upload goes to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#file Container#file}
        :param content: Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text. Conflicts with ``content_base64`` & ``source`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#content Container#content}
        :param content_base64: Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for larger binary content such as the result of the ``base64encode`` interpolation function. See `here <https://github.com/terraform-providers/terraform-provider-docker/issues/48#issuecomment-374174588>`_ for the reason. Conflicts with ``content`` & ``source`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#content_base64 Container#content_base64}
        :param executable: If ``true``, the file will be uploaded with user executable permission. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#executable Container#executable}
        :param source: A filename that references a file which will be uploaded as the object content. This allows for large file uploads that do not get stored in state. Conflicts with ``content`` & ``content_base64`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source Container#source}
        :param source_hash: If using ``source``, this will force an update if the file content has updated but the filename has not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source_hash Container#source_hash}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20064f74a453be8648ae36955133f517f04292aad71a0ac8e8f77fa91ba30dbd)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_base64", value=content_base64, expected_type=type_hints["content_base64"])
            check_type(argname="argument executable", value=executable, expected_type=type_hints["executable"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_hash", value=source_hash, expected_type=type_hints["source_hash"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file": file,
        }
        if content is not None:
            self._values["content"] = content
        if content_base64 is not None:
            self._values["content_base64"] = content_base64
        if executable is not None:
            self._values["executable"] = executable
        if source is not None:
            self._values["source"] = source
        if source_hash is not None:
            self._values["source_hash"] = source_hash

    @builtins.property
    def file(self) -> builtins.str:
        '''Path to the file in the container where is upload goes to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#file Container#file}
        '''
        result = self._values.get("file")
        assert result is not None, "Required property 'file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text.

        Conflicts with ``content_base64`` & ``source``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#content Container#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_base64(self) -> typing.Optional[builtins.str]:
        '''Base64-encoded data that will be decoded and uploaded as raw bytes for the object content.

        This allows safely uploading non-UTF8 binary data, but is recommended only for larger binary content such as the result of the ``base64encode`` interpolation function. See `here <https://github.com/terraform-providers/terraform-provider-docker/issues/48#issuecomment-374174588>`_ for the reason. Conflicts with ``content`` & ``source``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#content_base64 Container#content_base64}
        '''
        result = self._values.get("content_base64")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def executable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, the file will be uploaded with user executable permission. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#executable Container#executable}
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''A filename that references a file which will be uploaded as the object content.

        This allows for large file uploads that do not get stored in state. Conflicts with ``content`` & ``content_base64``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source Container#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_hash(self) -> typing.Optional[builtins.str]:
        '''If using ``source``, this will force an update if the file content has updated but the filename has not.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#source_hash Container#source_hash}
        '''
        result = self._values.get("source_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerUpload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerUploadList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerUploadList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8837df982e4fe38f1c4336c890118df586c086101710ade74b2f607f6852c58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerUploadOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8114b081fff4dbbd4cadc2f8fd1aff5711785a1930ba90537ada06be4032a1ce)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerUploadOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeacd97bf652c729d5b35bcdcd8cdd7db632e2bce7417187bd96b3ae0571d5f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc13259de6dc3b595679fdcf213374561c3f112187f8b897fcac3619a14bc621)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c15a4be4550257033437360c4fd1e912e17d07011249b18d72cb7c43daaccdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUpload]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUpload]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUpload]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99b04a3e9b64a846cdadbdce7905f1c5d97c825343844b897c7ae0b9a96d500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerUploadOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerUploadOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa3f492d0fff3fd8bb0a5c6e8a8a45be0f83a4c8ab385703baffc76b86a03e7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetContentBase64")
    def reset_content_base64(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentBase64", []))

    @jsii.member(jsii_name="resetExecutable")
    def reset_executable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutable", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourceHash")
    def reset_source_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHash", []))

    @builtins.property
    @jsii.member(jsii_name="contentBase64Input")
    def content_base64_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="executableInput")
    def executable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "executableInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceHashInput")
    def source_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceHashInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cbeacc78303594845378e19cf9ec6bda68bf8cd432b60d3267db91f6df732e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentBase64")
    def content_base64(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentBase64"))

    @content_base64.setter
    def content_base64(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__513a3ac74e413042c2bf91ed26d84b7f572276bd3f709d44fa69f8db79bdc358)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBase64", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executable")
    def executable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "executable"))

    @executable.setter
    def executable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da4174f4a9b4b4c85bb087c73ca8bb2349903a3b4f1bf9137a5eeb51d0e71895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bcc74287f09a137d1a01519d2cc67cf2ab85ac6d19185707dfa8457b0074486)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50b28ef59178d6b9b3bc8826e11da45f795fd4974d41cdac5b8d52eb786f9aa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceHash")
    def source_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceHash"))

    @source_hash.setter
    def source_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a28bc454cd742a653d74f99deac89c8ec4c1ef93cb6daff66d4bc84c31b142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceHash", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUpload]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUpload]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUpload]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77ac93f83eca1e663a1073960941108e2d3b6a030970051f28566fe9bbdb95f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.container.ContainerVolumes",
    jsii_struct_bases=[],
    name_mapping={
        "container_path": "containerPath",
        "from_container": "fromContainer",
        "host_path": "hostPath",
        "read_only": "readOnly",
        "volume_name": "volumeName",
    },
)
class ContainerVolumes:
    def __init__(
        self,
        *,
        container_path: typing.Optional[builtins.str] = None,
        from_container: typing.Optional[builtins.str] = None,
        host_path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        volume_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_path: The path in the container where the volume will be mounted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_path Container#container_path}
        :param from_container: The container where the volume is coming from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#from_container Container#from_container}
        :param host_path: The path on the host where the volume is coming from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host_path Container#host_path}
        :param read_only: If ``true``, this volume will be readonly. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        :param volume_name: The name of the docker volume which should be mounted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volume_name Container#volume_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0ab96dadeaaa122f736c0f0a6617e3b64eae8f4038c5681bc1fcc3344ddaf0)
            check_type(argname="argument container_path", value=container_path, expected_type=type_hints["container_path"])
            check_type(argname="argument from_container", value=from_container, expected_type=type_hints["from_container"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_name", value=volume_name, expected_type=type_hints["volume_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if container_path is not None:
            self._values["container_path"] = container_path
        if from_container is not None:
            self._values["from_container"] = from_container
        if host_path is not None:
            self._values["host_path"] = host_path
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_name is not None:
            self._values["volume_name"] = volume_name

    @builtins.property
    def container_path(self) -> typing.Optional[builtins.str]:
        '''The path in the container where the volume will be mounted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#container_path Container#container_path}
        '''
        result = self._values.get("container_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_container(self) -> typing.Optional[builtins.str]:
        '''The container where the volume is coming from.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#from_container Container#from_container}
        '''
        result = self._values.get("from_container")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def host_path(self) -> typing.Optional[builtins.str]:
        '''The path on the host where the volume is coming from.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#host_path Container#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, this volume will be readonly. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#read_only Container#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def volume_name(self) -> typing.Optional[builtins.str]:
        '''The name of the docker volume which should be mounted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/container#volume_name Container#volume_name}
        '''
        result = self._values.get("volume_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContainerVolumesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerVolumesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__374f52a023b09df555ac953ebc00f40d46e5ccdf5b20898399fbc5c798236a9e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContainerVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590b2e89e21d76fac2c525ea6b3717c8924ed19e26398631857b94e15bfd4260)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContainerVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7577cea79db4d3f9c7ea47241c5eae5810f78a1f1c64df5c7a4d0514bc9be3b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3eb633f605e9e4aa61570898bfabc9dfc2dafea07f3ae9da50a1cb6947d7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c78f9504de619d8503825b7c1c1596221f2d8aa0e280d632d9618a13e30c595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a2fb0bfd93fb5c16338a6a6ce0cf5e1c9a28fddd6c464417c1a070a27c1a01c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ContainerVolumesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.container.ContainerVolumesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53e2518c8bafb6c3b48191345a5fea8f9db1b6481f6a952f7f68454d7b7730a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContainerPath")
    def reset_container_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPath", []))

    @jsii.member(jsii_name="resetFromContainer")
    def reset_from_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromContainer", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeName")
    def reset_volume_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeName", []))

    @builtins.property
    @jsii.member(jsii_name="containerPathInput")
    def container_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerPathInput"))

    @builtins.property
    @jsii.member(jsii_name="fromContainerInput")
    def from_container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromContainerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeNameInput")
    def volume_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPath")
    def container_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerPath"))

    @container_path.setter
    def container_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d99af286022aa08bd18a53fb394a47934253d7ea6e8c3a02d4dfeb0d1af6ad6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fromContainer")
    def from_container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromContainer"))

    @from_container.setter
    def from_container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ec893b6ca3de50201b621901ac816147d775295b38819c216192705b638878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromContainer", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostPath"))

    @host_path.setter
    def host_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6647081558f3ac3f4015586f4dbfb8758974b171a0717d730640399f9c00eb0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb750e84e1e0bdc4236af83d4e5f18fe93c6439c89f3fd8c3cba95fcea80daf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeName")
    def volume_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeName"))

    @volume_name.setter
    def volume_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bef7c8e9420e2fd8ec44c728611b04cc7aea7e2229398bc476b70dffe278d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerVolumes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerVolumes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerVolumes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9330c7226c7ad44e4efd963b62bea31ff5221f9bd3e543a125ccff2ad8c8d690)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Container",
    "ContainerCapabilities",
    "ContainerCapabilitiesOutputReference",
    "ContainerConfig",
    "ContainerDevices",
    "ContainerDevicesList",
    "ContainerDevicesOutputReference",
    "ContainerHealthcheck",
    "ContainerHealthcheckOutputReference",
    "ContainerHost",
    "ContainerHostList",
    "ContainerHostOutputReference",
    "ContainerLabels",
    "ContainerLabelsList",
    "ContainerLabelsOutputReference",
    "ContainerMounts",
    "ContainerMountsBindOptions",
    "ContainerMountsBindOptionsOutputReference",
    "ContainerMountsList",
    "ContainerMountsOutputReference",
    "ContainerMountsTmpfsOptions",
    "ContainerMountsTmpfsOptionsOutputReference",
    "ContainerMountsVolumeOptions",
    "ContainerMountsVolumeOptionsLabels",
    "ContainerMountsVolumeOptionsLabelsList",
    "ContainerMountsVolumeOptionsLabelsOutputReference",
    "ContainerMountsVolumeOptionsOutputReference",
    "ContainerNetworkData",
    "ContainerNetworkDataList",
    "ContainerNetworkDataOutputReference",
    "ContainerNetworksAdvanced",
    "ContainerNetworksAdvancedList",
    "ContainerNetworksAdvancedOutputReference",
    "ContainerPorts",
    "ContainerPortsList",
    "ContainerPortsOutputReference",
    "ContainerUlimit",
    "ContainerUlimitList",
    "ContainerUlimitOutputReference",
    "ContainerUpload",
    "ContainerUploadList",
    "ContainerUploadOutputReference",
    "ContainerVolumes",
    "ContainerVolumesList",
    "ContainerVolumesOutputReference",
]

publication.publish()

def _typecheckingstub__8420f4ec8afb941e149518b118f3a35ee97ce4675e62b891354bfb9a0048c7dc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    image: builtins.str,
    name: builtins.str,
    attach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    capabilities: typing.Optional[typing.Union[ContainerCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    cgroupns_mode: typing.Optional[builtins.str] = None,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
    cpu_set: typing.Optional[builtins.str] = None,
    cpu_shares: typing.Optional[jsii.Number] = None,
    destroy_grace_seconds: typing.Optional[jsii.Number] = None,
    devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerDevices, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dns: typing.Optional[typing.Sequence[builtins.str]] = None,
    dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
    dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
    domainname: typing.Optional[builtins.str] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Sequence[builtins.str]] = None,
    gpus: typing.Optional[builtins.str] = None,
    group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    healthcheck: typing.Optional[typing.Union[ContainerHealthcheck, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerHost, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hostname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    init: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ipc_mode: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_driver: typing.Optional[builtins.str] = None,
    log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_retry_count: typing.Optional[jsii.Number] = None,
    memory: typing.Optional[jsii.Number] = None,
    memory_swap: typing.Optional[jsii.Number] = None,
    mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMounts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    must_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
    network_mode: typing.Optional[builtins.str] = None,
    networks: typing.Optional[typing.Sequence[builtins.str]] = None,
    networks_advanced: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerNetworksAdvanced, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pid_mode: typing.Optional[builtins.str] = None,
    ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    publish_all_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    remove_volumes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    restart: typing.Optional[builtins.str] = None,
    rm: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    runtime: typing.Optional[builtins.str] = None,
    security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
    shm_size: typing.Optional[jsii.Number] = None,
    start: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stdin_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stop_signal: typing.Optional[builtins.str] = None,
    stop_timeout: typing.Optional[jsii.Number] = None,
    storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUlimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    upload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUpload, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[builtins.str] = None,
    userns_mode: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerVolumes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_timeout: typing.Optional[jsii.Number] = None,
    working_dir: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bff20b73f4c2823f238498715191cbc5bf3c5d91dc13bd09dd0a2603bfe1dd4(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8fa5cf0cf94c147e100eef20d33f2fcdfca770dfb20e57cd4209a35184a1f1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerDevices, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa3e43a2c0d98ad294ed60f8954e449ea89afb7dce4a39392d1102723b6b48b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerHost, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f1cf00f1f2f04c6c6c119c90dd9cb5fa90b120204f498923b2d0d275dee13e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bead9498abea885f6ee8c0ce07bcaa2e41c9e045e6e6b377a05dc8d1c95fa45(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMounts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c023832501ced51e1c1dae71003e9c891751a451cba47d3a2f10e56d1a2ded4c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerNetworksAdvanced, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a2e770611d581eec5f2ef261891a38186749a307b528a0af90889e947f0e28(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed5ad0ad26c56f4143aa4e1a9aa2d3afda343a32849363c488b9d69d867bd99(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUlimit, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a07c651ea4569f2fdc9faaa78f877c74dfaa6119debd5302558eadf58a07fbe(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUpload, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d025bdf12a5d1e7872240f5983d8fcbde3fdd44a68734ea4f1e9900ff4057904(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerVolumes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40aeeb83dfa58aaa3c10cf15a697a6574e3be99bab712605a6e505bb33a404a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a1dc42e8edbad579ce1c93321ef2fabc4f9b3aebf032e484c1358af6256187c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9227fa264db70597595ddaf2127e884b1e4a756c0cf351638de59dfc0fdbeeb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c0fff4d4e62d1b793d297d382a0b4ea214522a2ea0934a8b24d03b5f54c12b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12138d8cb6077180dbb9e2d45c37d6d198d68b44a07b753995d4c9bbee90031(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703dca3f3c2ba3cef7e64dc94e6609595066ff7b8b3f0cba812ed1955a70c929(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e51c5cd1cd057a7a9817e5d193deb4e32e0609797d50b26324b55c103aa2d4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575877cdfc616405c9d74c89f39e82ac461dc11aa66a387f9927e7d81c2be942(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c302c434d434e1db4361625aa0c232bf297d35873eb4d86b4f9e8525cdc044a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246b397e6b05f7319c2b7c31b69d5aaabfd5aafa5fea81a6a6f5aacbb56f8104(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c88594f6c6b71226cb30703cc497893290677336999acd757f4be4ad7398380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee8a4e38081fbb030b8d694f52a3e30d71b91ddc179e7d9452c548f94895f7d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c5f7a6dd26ef1d9e2fac7c08c0796147835a037050014a48e531ca227ddf7e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e8e2592a74bf60517c26c553468aadfce288fdb5886dbef4bb9378654405b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8571dd0c5e17e6382b854c58be48e378d8e563b3e18f6045b5d58dbfd248ceab(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__252237edae22e21091807f78088266d7c2cde6816dd6f9a46b8c592c82758666(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5851caa562a002a0fa13e3ffd210102650b3155416adcd1653315f86c2c8d624(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4b2a40c8441c1c78e7ce96a2e994d22b444111b9bf247c6e5c6eaef9e32cd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a87e0268f38fbcf3460e0a004fa9fdf56fad7a1dbf25ce223fe608052da4d8d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e68cf56cb7eac5d1d14c7adeaf12ec4d1764b40ebe1ea846b26bbed8162d53f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7daa55a5fc38c816d182956fff7c08066ccfbc9e951e261cd14af7cb7ea163de(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f77942110c0754662015d95c3934b0a829ab14573254e2991f0defd2d93b981(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e185d1c9463d08cda6d225a264b329cc5ec0488291884f0e37325c46bb2c998(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa37b17dda97ff8623d5e283dc3576e76ab2fe28f08bb7e79932d0ba82acb5d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8316518950db8d0ab140758522c6638d5f2866bbdd84f393640b3250d549db36(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be746b4cfcf79b97e132598fc2a97307118c9aab1fae4d8f964b44369a43f33(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0307074c31c7f4401fbd56fdf151e7866b40e52f6d5359d27e16e818da62617c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f07ebc0010247354841e815e7430cb5b6f7573520e15090a4651e962039bf92(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6683a1b4167b283cbaab61766482b7bc5e9e99801c847c6e71b31b863587fbb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47004de13cfe577f98bb510d113269282197a122b1f5a869cabfa9c6264ab63(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b34c0046dd7e05bcde3f267338db98452cde3f354d7bcc10ea2ede8a2e54fde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c00a44a66c8b38a625435129c9d756898dcffd56ca4825073ff175e3c3c612(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44788be8dc91421b94a1cbdb9f4b86da185db295a0a14b61bacd79551cd5b13e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a34d1b713e0314a494fc8e1bf5abe563360892a2b6877c42b4eee4a331b38d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3543b7aebccea66143e4c21278e1cf6445ca2eabd224c561d25beb8cc26bf97a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7208591003fca68bb202fc8eeac58c432669e1a069d844daac4a6e3d1736a510(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958c3bc61312a8d948cec93124e1385db9e0e0ca665109f15f1d4108c0cad224(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__616a0619d12446a85114060a084a66798e886f786e54b0bd782eb904af1e6702(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ebe2e684b69678f2d645738d6f173c43b3576c8216e6faff746c9e16e1a3ed(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__357e5d075f9f77e877d9d8f3f5c35e6626e297e3623ed54789c10082bc45a8fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493989f7a23bc4e86e4c6da93685e78f2fc60263103bcf8b5b2104bfb24e9066(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9684341ddb755ac8090e9a33cb3cce2d6d56cda24f990532adb12b23506e89c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b30ba649c9149bcb99a9079d207ca6835f124ac6b5ff84c2b290b305be9362(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dc3c9eaa1491ba0da5d2f01c2c41b8ea5b35b1d1daf60196582ffe52fa39c0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adda57a975f17bd6938ec29586d18e72f2eae87997495a607971b521f423df72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed26159fd70aa06114aac6771be8f563ab6f78a14fd22d4c7cf7188267bb274(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f42f8b07484c0a35952279d91de52431b98cfc1263b5d4f469dab3edb0f5039(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ffd5f6dacbfae0b42996eb7ddacac897fbd3736bf14d918221570b6f42b6c78(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__357af71a22db2f70679c4bae0f429f7dc86a4b7dbc27b7bcbeae48da476d0191(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405db67569515d9dec43c6b49430e728ff303df4a139aeb15158dfde9d2238da(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd9328921849994a6b22b689c869a4f856ef29046fc5c150ac3c7978e1cb5ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4ee8ee9a1b1da42fb5530a402b43974ebe000fe106f46d996e0d0e31bef558(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e88cd1bdb6bdc8303f982ec1d6541f4e52777d99f78aa2748591d1db8458285(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede1bbf5b73a1a834276dc52d8bb5fa956450f7b0db6a59edb7341ddaa73b707(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5242d455ae8d44d68faed4cfc4531fb375a35b6de64a6d85392e764c2029bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2790931e1802e970db0fbbece0e90e9b25fc4f6534b2827c8049c94b6f4d1711(
    *,
    add: typing.Optional[typing.Sequence[builtins.str]] = None,
    drop: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0951a6bdc6c10ad4fad15936ef16d38a933374ff088568b681fa560a6bbc4db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec57e0a595c28334f2ec5ed2aa9165ebe79b91365a5ef46491a74425885b9fac(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e006e321698fcef0e61d7f12b5a43479681c045ac3e6b7c21ffae74b03f1b6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ce3103e4a6eef3579ba9972833d51a5179e78caf5f13dd047903ca814d0c27(
    value: typing.Optional[ContainerCapabilities],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0668b751bef53a116e94d361f638de42cb59414e5aa0c897531cf78eb674d88b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    image: builtins.str,
    name: builtins.str,
    attach: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    capabilities: typing.Optional[typing.Union[ContainerCapabilities, typing.Dict[builtins.str, typing.Any]]] = None,
    cgroupns_mode: typing.Optional[builtins.str] = None,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    container_read_refresh_timeout_milliseconds: typing.Optional[jsii.Number] = None,
    cpu_set: typing.Optional[builtins.str] = None,
    cpu_shares: typing.Optional[jsii.Number] = None,
    destroy_grace_seconds: typing.Optional[jsii.Number] = None,
    devices: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerDevices, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dns: typing.Optional[typing.Sequence[builtins.str]] = None,
    dns_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
    dns_search: typing.Optional[typing.Sequence[builtins.str]] = None,
    domainname: typing.Optional[builtins.str] = None,
    entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
    env: typing.Optional[typing.Sequence[builtins.str]] = None,
    gpus: typing.Optional[builtins.str] = None,
    group_add: typing.Optional[typing.Sequence[builtins.str]] = None,
    healthcheck: typing.Optional[typing.Union[ContainerHealthcheck, typing.Dict[builtins.str, typing.Any]]] = None,
    host: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerHost, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hostname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    init: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ipc_mode: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    links: typing.Optional[typing.Sequence[builtins.str]] = None,
    log_driver: typing.Optional[builtins.str] = None,
    log_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    logs: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_retry_count: typing.Optional[jsii.Number] = None,
    memory: typing.Optional[jsii.Number] = None,
    memory_swap: typing.Optional[jsii.Number] = None,
    mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMounts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    must_run: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    network_alias: typing.Optional[typing.Sequence[builtins.str]] = None,
    network_mode: typing.Optional[builtins.str] = None,
    networks: typing.Optional[typing.Sequence[builtins.str]] = None,
    networks_advanced: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerNetworksAdvanced, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pid_mode: typing.Optional[builtins.str] = None,
    ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    privileged: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    publish_all_ports: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    remove_volumes: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    restart: typing.Optional[builtins.str] = None,
    rm: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    runtime: typing.Optional[builtins.str] = None,
    security_opts: typing.Optional[typing.Sequence[builtins.str]] = None,
    shm_size: typing.Optional[jsii.Number] = None,
    start: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stdin_open: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    stop_signal: typing.Optional[builtins.str] = None,
    stop_timeout: typing.Optional[jsii.Number] = None,
    storage_opts: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    sysctls: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tmpfs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tty: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUlimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    upload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerUpload, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[builtins.str] = None,
    userns_mode: typing.Optional[builtins.str] = None,
    volumes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerVolumes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wait: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_timeout: typing.Optional[jsii.Number] = None,
    working_dir: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27b10d1d413a7fe8ac75f976de674eb77580099e7aff550a1a861f83af3b923(
    *,
    host_path: builtins.str,
    container_path: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2ad623880358d6f8b51b6f09921f48cd9c2b012a7e6d0650327593b0cb480c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7245998cd864477728c2dbbc585856b0e90bde14f2882fd7d3b22b5204dabe7e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56c91318330cbc189d6a608c878f2f2554ea57eab88784fc36f24d611b60eec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a300c35ea40f39ac0260b69b63863cc9e4bb18933c313708785ae9155f58a1a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04fe844a49975f3aa9b0714ec94303650030ec7fff86407cc3c6510212a3aa0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ece0ce431994b3362c75b411fae64890af7bbe52317517d4711302917724c5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerDevices]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4672282f1bd753a1a2ccfd2cf0860b7973d53d47dea4438f974cc95843129c3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6780dc29e2f1db9f482a76dfcb3a2fc1edc1956f4cba935dc94b2d02ada8cda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a21872f92b1700e33cfd7118c5cc67cc9aaccd33c5e55907f0c96e982bf8d8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c634703177f701ceda71cbd26e3f49f72177f601e243e3e7a2c07c86c00ba389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522aafed3823e297fac1b4d60753820ac7dcdad0f336c5d2ee348a058199b679(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerDevices]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053a42d396ebd35ba5d683f5a2b2fcad62df06394965668ea0f4a55bd282dd5e(
    *,
    test: typing.Sequence[builtins.str],
    interval: typing.Optional[builtins.str] = None,
    retries: typing.Optional[jsii.Number] = None,
    start_period: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdbcf3c7a8bc312dd458c1df2a4be09c173a3c212c9c8155ebee2ef979aef3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0267f0a9e64cb2ceff4bb9ceccf9fae59f1283125a53f7c759b077cbc5f60685(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a8e07acca3be7c2de81beecdb4e903315cb33dc91b40427abfa7f3fbecc3bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__827b1a40aef5096198baf2c6e957fd271436acfb8348ac0a49949526307c5c5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50be8e120ee3bd5d90dcaed844a57db962e17af513581dac40e0ee74b04ee14b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0f51ff7f54bd43a6bae0efe584a7232c9cbc610a5351bb73d5a63048a3f6bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c60db0267b0147796c31fa34635769005f028789054ab95c9bea3b7c0133c5(
    value: typing.Optional[ContainerHealthcheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ccfc781c993cb976562a0005114f5ef03db3b05fe3ceb117254e424df4c643(
    *,
    host: builtins.str,
    ip: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e233a2282a78df2897fd4e14b40e4b49b89b42997cf453a098235f77ff735389(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2557b8d85d08a8e8ea38196507b49eda856cc019ae6ee0b5292dca4fd2c271(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ea9e379ffbac7d9865199fe85aab308055f1dda882a70fa2395aac5493cbe9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6692fb08b8bd612b1948f3eb9de937b99bd5998a06535baa5a090389665c3be8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec61c9d60273c6d07409cb2bb80dc880974ba8dba085652ddef16bfcc3be861(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__135ef0893adfa7cbf39eefc285e9197614c811a1a26cb81e76d5d51cb6ab3fb5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerHost]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa507edcc04d68bb75d08909e7a43e29b4d676e948915e4b2a02c36000dae002(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c0c49417551a5730e74504e42af5fce08a6ad337902bf33a7ffadaf3a260c12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e2b5be54f54b155280688bf8a625cf991a786d1e8d243ced1bd7b76824319a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f699457876a9267c16c782639ba4775057d205ccd34df119ebace8313c7796a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerHost]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd383bb73875bf4ecb919742da4f5a4fd95235ac3b5438ab72cfc12d05ad53c8(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffd71205f8e478c1dc1191d4ad072bf6e89c2569c8cdefda6a035cd45c871811(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf30a7e5bdc3041bdb585ca0ba7a1e99ab942aed617abed14f9b57751b844e6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5518c877d95f9ec0e0778685470248e3e147dc43f381a006e6fdc2d75ad542(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c56a3196c735d245f4b7dd33e08f096bf164da595a70544c30a42cfd9458990(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034eed4c8f77f83e85e19a48c90de9d9599f54b271dc8b7b94b6127b6ad332ba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577691acd73ca45e8ba603f95052ae47c74d7b4e166ee90e38cf3b4eb9554c50(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fd6fbed556797d18e6013f177dab26ed7f8c4a224b5124b10adc3a9cf22bff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8802b1a7f84cd29cc63db05d7e6769dcc8f06f912055f71d5f671a7436f5a2be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd03aa5f58821edda14b50794d09b47d9d832860c159394354171579c9d5fd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4763b1dcabdf4ba37eb501a652b9cc225801f00c14f507c8cb5788fb9387642a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerLabels]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36bf76b7a97bb8b3fb8bfdcb228391e6b92076731343f85f22a134758fa72a0c(
    *,
    target: builtins.str,
    type: builtins.str,
    bind_options: typing.Optional[typing.Union[ContainerMountsBindOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source: typing.Optional[builtins.str] = None,
    tmpfs_options: typing.Optional[typing.Union[ContainerMountsTmpfsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_options: typing.Optional[typing.Union[ContainerMountsVolumeOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cdb3d0daab203b387293a55927990d7486c6dbdd4b923a32b51cb96b464578e(
    *,
    propagation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7605298cb90767f7f590fc4820b31222d13da158e769780ad10c9ea6eaff8648(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea89a58c04ba32814ec9d1234a85516270c38792639754c12b198c707e9ae26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28db3a274f91fb4689163c5152694df40f5755ebe1deda83d0b438c83c848f29(
    value: typing.Optional[ContainerMountsBindOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bafbcdfb694ae304630bea35d6d5a744f4a304a5b8ca52adc4947c27c29a479(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f319073e5044e79561bb2471d821d039df08bbb0ea65538857722dc60cd44c14(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98507bfe7987cc9e461432c5b5fb5ae551b0a1b48afb51eb5c809c6800e7a6f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d442b27f27090f89f05f329a7183362260d48c70de4d0a20e4256fcd24644961(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__055d2b718e2a3d533a3921bc5d382d4335794ddff86a9c6d321beecf4c05310b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b610e28ac4fb8cf637f8d20966c5bb0a92f3afd66f1c005e3fe82d2c3452ef(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMounts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda857c098aeeaaf9c82ba7a3d6dac275ff6ebd443997c2638b3f81d97f46663(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a099c296ee9f2a66ed6d3c74234df0d65d2d3a2edc732c204aa235b8dbb5d553(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1c059cc87b295a1a2c548b4124ab6743fc97a8b3634952abfeee58e450d984(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7309a305f8651211f60e63b011dc7eded2aae99bcb79cc70f021bff2e10b28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c1fc621835ad500ae2b02efff94a38ae3689d8e4082997649d64ca0f0f372b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__673e9810c52e86117ab65eea69bd3c82571db7a8c7d20febf5385063908a414f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMounts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de69cad63efe13dd5d72ba0a4da41ccf1eb5cd5e8c9ded37bd75d8262e4c96cc(
    *,
    mode: typing.Optional[jsii.Number] = None,
    size_bytes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43290204fe3c45632b81c48b99e47f37e5dc4931ab5914ee7c55c7620d2abf34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b770d67c3cb680f3d6fef28753b4f84f018889959a1d672a241fa92cc31dbb61(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ecc6e5a50cd32d66a9f89a871f06d3f89bda7fc08ec6e02f4a941d4ebb53194(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba1fe4c7fecd0a494a3d48bf375637a7a2527b51b35d01f490a5c5b97aecaf8(
    value: typing.Optional[ContainerMountsTmpfsOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3765d463f76a72daf038d1bae8f1a45145d40489c3ad218958841eb6cc607d34(
    *,
    driver_name: typing.Optional[builtins.str] = None,
    driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0388e189676a997973aab6edb56659dd2a84d267b8200e026dd95d36dc8dbde5(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4587c399ddade6d6e2b9f35f8c20d7dc63dd575b5274487bd9c299666d00c28c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af1e036397083b49e279b1539a6d90ea91679bed11412adb99dff66a9593c9d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb5db753cd1b72a1b55d7e3442354598e37fa40a929eb6be9ed32fe092f821ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204f5c4d632c6910f61ae7021cdd5dbca487b7f70744748b1c5dc7be8d89f156(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80651f386c6c30b0ba25e0905064cb54c6d98a0b98d2ed7e64068650ab5406c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6443454069c5b002aa90ade2aa7879dfb9ff14780dba08cf2a00c028a0a1c541(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerMountsVolumeOptionsLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__647684fcbb181143f5233f91bb05e33ccd1088e7eaf054ebafcd54048fa24015(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2e94630bfaa9b8d5209492c8ab27000fe406922ccab8f1af38b0c303e32d9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb7141f34dc1f933b56de2e258dc5d8aca870db6752e8e559a3ab3640c7b32e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cf81649d8a91d0cd49db971db9a8371c95d6aeea05bcd4a615420bf1d53cb40(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerMountsVolumeOptionsLabels]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef489ecb5129884df334b98eadcb421a7c604c1ed65ffc039215e12434bf35c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dad236356d66c25054eb04fae0fc655aa8e046fe8a0b76793d304c17ce9f3a78(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContainerMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09de412e129fb8f069cd2e0e3230b0e2dd939219e85faf1099d23aeddc25efe3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce58489f23cb2178b6f5c13ec2a63e68102413278974a0dd629dd83275c84687(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29375523a60e720d8808a255b466af7f2d79c4146a6281fdf21b170ffd484ce2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5090b13fb124d76b0e2943faaa0d0635613ba9875a73ed9f05402c1ad0e2fcb4(
    value: typing.Optional[ContainerMountsVolumeOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1a8ed756c894d404212e001bd6b4d28ae7f176a7b1716a617845bf99326cf8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85ed47d1dc0352058277683399bd2ddb306a3769f7d5d9bc41d62017f582c35(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adeb93f7c7cc1233b1eee6d23189a28e6e280e3699bdd3b78c5a3e0ad42e62c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0550ea9132ee8453acaa6a488173d83813dd31adf5f36774bcb74e9bf87aae(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed682d44e172ee8f6ce81e1bd2b7292b269613c627f2a80eadfe1723ab4ed804(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98d94f6ff808815102f790da8bce18d2ac105bdb9d174d973acb64eebd22011(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca9833779b8ee112e7b13aad231fbe7f66fc822c1251722f11f33cb93e3be41(
    value: typing.Optional[ContainerNetworkData],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e35fafaaf1ff52819f16f42e34931124d0bb38caf7f23d40da768e8f20f05d(
    *,
    name: builtins.str,
    aliases: typing.Optional[typing.Sequence[builtins.str]] = None,
    ipv4_address: typing.Optional[builtins.str] = None,
    ipv6_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8978d2756dc4ca13164bdbae071647b109fe317f68d6a8f2a017822c857ca8ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d9f7d70086d590abd339dc96ba87ace4b36b6727f33b505906d6a129f54150(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa528a0551ee0e2457513dc6812f9b5ae80afcfe7d6bce32c3855af79b111ca3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f1436d5dc460a8dbfd2110ba96359d29012ff9a42b89865b34f1114f436609(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19cb9baf359bc8960db27530d3b4ac4beb9441c7a603e091c821ceef067af58b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a365e72161c273af1e371d52e9a95c116382d9a1b35c5e9ad317c3ce0ee3d4c4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerNetworksAdvanced]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__915b70032d561edf68f9087e737a75fc80ae373b5c80c409a3d4cffbb4d0c48b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1068eff5698b4b4e4660ad4a965b16d43759eb0950629681b547d85b2dc6407b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2df1a417a03778292b09e0d835f0052ca60a2786332281d175037a96f017d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__141ee8c94de5fd0e0045c71576102609845703ccb168517f431aaa130182ab9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3018b820ecfb1834d363862087b9b3ec35f92718b0afa7083580e3019f5318e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9c78398c56f1fe4e9641e8b60b2a67597b1dafea7a84578a00e2fb169359fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerNetworksAdvanced]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded768306be7168a91afabb62ad1c3aeb5519930d434b8890587dd8c2c06b949(
    *,
    internal: jsii.Number,
    external: typing.Optional[jsii.Number] = None,
    ip: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58148ad3fc9843cb7ad7f76e6aa4e6d6755d7b4a1ddfe93cfdc525580595eb38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18af6e1fe1c023486b265e6cf94cfac7adcc194c0b37e8d84dcc03177d9165bb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f16dc414f572560a3f7037c7baa4fe22de97559bb36b604ed031b763320370d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865081fb892706550991d054d11fc978d60f585364db3d3a1eca791924a1b91a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be673cd3c01cb159d6e346bfcdab38261d933d1a786b20973fbb7b7f8151839(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8fe51606347c80080c99d7201009c507765ed8cf094fec896cfea810a825a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc18f7a1549740b5f2d76e3a8770009c84e84d2cdbd29ce2a1103564b1bd1ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0ca9b0eb425d0e58ff21be50f367bd640cb7ba255ea58629c679cdeecd4be3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47c0d8eb04f12640628f26e593c11feb6419fe8e7a4a547098465e5c5c3c133(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe175bac8fde7bdd7003231c8fa1a0c48bb2c92b488f523318ee78156b9bb6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b06f97a6487f6c89d14fa6760ece968343c47e2e83e326e2587bce531c28ca0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d865e2c1813ee2d7030febd1ccdcf2786975cbc01cc096a616be32cc56289d55(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerPorts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5975b23dd190e1400495a55f1c2bc4e15c71c4a9f8ba7b6befae753615cb38f(
    *,
    hard: jsii.Number,
    name: builtins.str,
    soft: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05899289fb172d24ba2277f94cfd3aa1bb4139219d26b3a214d1ed79ff59b373(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3687af5d70269f79266fdeb2ae4f4f9bfae78e71f23c59bdfde6f1ce1d33eacf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c00c253173c111ebbc4e5a3e602e8e793bb52600a5df4e3567da22c7899d76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d067d998d702687ed20effba471e0ed956450fb19155e89856d06959262bd84(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b7fe5c73e7f32dab1e08af8571c8d4f53107daf8ae10fb2f5f0488d28b6832b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e524370666ce4722dfaaa5beb63f50eded12a52dc59fa25f7d7eb67c83eafd3c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUlimit]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb802f9d770a3f72d7ce2f082184f769c6e674330bba4cabd21bff5317914ffb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678e62e230844d1f874d43a6cf39b9c69a9890cdd00d42aca537d482951b1b57(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ca8e9f409ac23296eff62440fb2392104ee0284bbdc5834ab187750386dd3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc34a4794b56b764ccb7d7283285a9df696cff2a42ca1ec6b2a21cd92d143d7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__146952e2b91c64997b5c4cb8206b6ff5c7d29832a9053d91cbbe5f34c36ca6b1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUlimit]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20064f74a453be8648ae36955133f517f04292aad71a0ac8e8f77fa91ba30dbd(
    *,
    file: builtins.str,
    content: typing.Optional[builtins.str] = None,
    content_base64: typing.Optional[builtins.str] = None,
    executable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source: typing.Optional[builtins.str] = None,
    source_hash: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8837df982e4fe38f1c4336c890118df586c086101710ade74b2f607f6852c58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8114b081fff4dbbd4cadc2f8fd1aff5711785a1930ba90537ada06be4032a1ce(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeacd97bf652c729d5b35bcdcd8cdd7db632e2bce7417187bd96b3ae0571d5f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc13259de6dc3b595679fdcf213374561c3f112187f8b897fcac3619a14bc621(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c15a4be4550257033437360c4fd1e912e17d07011249b18d72cb7c43daaccdf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99b04a3e9b64a846cdadbdce7905f1c5d97c825343844b897c7ae0b9a96d500(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerUpload]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa3f492d0fff3fd8bb0a5c6e8a8a45be0f83a4c8ab385703baffc76b86a03e7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbeacc78303594845378e19cf9ec6bda68bf8cd432b60d3267db91f6df732e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__513a3ac74e413042c2bf91ed26d84b7f572276bd3f709d44fa69f8db79bdc358(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da4174f4a9b4b4c85bb087c73ca8bb2349903a3b4f1bf9137a5eeb51d0e71895(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcc74287f09a137d1a01519d2cc67cf2ab85ac6d19185707dfa8457b0074486(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b28ef59178d6b9b3bc8826e11da45f795fd4974d41cdac5b8d52eb786f9aa4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a28bc454cd742a653d74f99deac89c8ec4c1ef93cb6daff66d4bc84c31b142(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ac93f83eca1e663a1073960941108e2d3b6a030970051f28566fe9bbdb95f2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerUpload]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0ab96dadeaaa122f736c0f0a6617e3b64eae8f4038c5681bc1fcc3344ddaf0(
    *,
    container_path: typing.Optional[builtins.str] = None,
    from_container: typing.Optional[builtins.str] = None,
    host_path: typing.Optional[builtins.str] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    volume_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__374f52a023b09df555ac953ebc00f40d46e5ccdf5b20898399fbc5c798236a9e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590b2e89e21d76fac2c525ea6b3717c8924ed19e26398631857b94e15bfd4260(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7577cea79db4d3f9c7ea47241c5eae5810f78a1f1c64df5c7a4d0514bc9be3b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3eb633f605e9e4aa61570898bfabc9dfc2dafea07f3ae9da50a1cb6947d7a7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c78f9504de619d8503825b7c1c1596221f2d8aa0e280d632d9618a13e30c595(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2fb0bfd93fb5c16338a6a6ce0cf5e1c9a28fddd6c464417c1a070a27c1a01c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContainerVolumes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53e2518c8bafb6c3b48191345a5fea8f9db1b6481f6a952f7f68454d7b7730a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d99af286022aa08bd18a53fb394a47934253d7ea6e8c3a02d4dfeb0d1af6ad6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ec893b6ca3de50201b621901ac816147d775295b38819c216192705b638878(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6647081558f3ac3f4015586f4dbfb8758974b171a0717d730640399f9c00eb0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb750e84e1e0bdc4236af83d4e5f18fe93c6439c89f3fd8c3cba95fcea80daf2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bef7c8e9420e2fd8ec44c728611b04cc7aea7e2229398bc476b70dffe278d3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9330c7226c7ad44e4efd963b62bea31ff5221f9bd3e543a125ccff2ad8c8d690(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ContainerVolumes]],
) -> None:
    """Type checking stubs"""
    pass
