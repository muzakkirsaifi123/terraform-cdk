r'''
# `docker_registry_image`

Refer to the Terraform Registry for docs: [`docker_registry_image`](https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image).
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


class RegistryImage(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImage",
):
    '''Represents a {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image docker_registry_image}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        build_attribute: typing.Optional[typing.Union["RegistryImageBuild", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keep_remotely: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image docker_registry_image} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the Docker image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#name RegistryImage#name}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build RegistryImage#build}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#id RegistryImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_skip_verify: If ``true``, the verification of TLS certificates of the server/registry is disabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#insecure_skip_verify RegistryImage#insecure_skip_verify}
        :param keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker registry on destroy operation. Defaults to ``false`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#keep_remotely RegistryImage#keep_remotely}
        :param triggers: A map of arbitrary strings that, when changed, will force the ``docker_registry_image`` resource to be replaced. This can be used to rebuild an image when contents of source code folders change or to repush a local image Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#triggers RegistryImage#triggers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2671116897cf8aed30f5abdf331c7e525a63a2285e99551c6ec5aa6d7bb873d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RegistryImageConfig(
            name=name,
            build_attribute=build_attribute,
            id=id,
            insecure_skip_verify=insecure_skip_verify,
            keep_remotely=keep_remotely,
            triggers=triggers,
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
        '''Generates CDKTF code for importing a RegistryImage resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the RegistryImage to import.
        :param import_from_id: The id of the existing RegistryImage that should be imported. Refer to the {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the RegistryImage to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb2669073186121bed9d1b5d91f2ba3348aeede720d0b99573c6513acf02a68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putBuildAttribute")
    def put_build_attribute(
        self,
        *,
        context: builtins.str,
        auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RegistryImageBuildAuthConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_id: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        cgroup_parent: typing.Optional[builtins.str] = None,
        cpu_period: typing.Optional[jsii.Number] = None,
        cpu_quota: typing.Optional[jsii.Number] = None,
        cpu_set_cpus: typing.Optional[builtins.str] = None,
        cpu_set_mems: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        extra_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        isolation: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        network_mode: typing.Optional[builtins.str] = None,
        no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        platform: typing.Optional[builtins.str] = None,
        pull_parent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remote_context: typing.Optional[builtins.str] = None,
        remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_opt: typing.Optional[typing.Sequence[builtins.str]] = None,
        session_id: typing.Optional[builtins.str] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        squash: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        suppress_output: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        target: typing.Optional[builtins.str] = None,
        ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RegistryImageBuildUlimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: The absolute path to the context folder. You can use the helper function '${path.cwd}/context-dir'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#context RegistryImage#context}
        :param auth_config: auth_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#auth_config RegistryImage#auth_config}
        :param build_args: Pairs for build-time variables in the form TODO. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_args RegistryImage#build_args}
        :param build_id: BuildID is an optional identifier that can be passed together with the build request. The same identifier can be used to gracefully cancel the build with the cancel request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_id RegistryImage#build_id}
        :param cache_from: Images to consider as cache sources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cache_from RegistryImage#cache_from}
        :param cgroup_parent: Optional parent cgroup for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cgroup_parent RegistryImage#cgroup_parent}
        :param cpu_period: The length of a CPU period in microseconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_period RegistryImage#cpu_period}
        :param cpu_quota: Microseconds of CPU time that the container can get in a CPU period. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_quota RegistryImage#cpu_quota}
        :param cpu_set_cpus: CPUs in which to allow execution (e.g., ``0-3``, ``0``, ``1``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_cpus RegistryImage#cpu_set_cpus}
        :param cpu_set_mems: MEMs in which to allow execution (``0-3``, ``0``, ``1``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_mems RegistryImage#cpu_set_mems}
        :param cpu_shares: CPU shares (relative weight). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_shares RegistryImage#cpu_shares}
        :param dockerfile: Dockerfile file. Defaults to ``Dockerfile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#dockerfile RegistryImage#dockerfile}
        :param extra_hosts: A list of hostnames/IP mappings to add to the container’s /etc/hosts file. Specified in the form ["hostname:IP"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#extra_hosts RegistryImage#extra_hosts}
        :param force_remove: Always remove intermediate containers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#force_remove RegistryImage#force_remove}
        :param isolation: Isolation represents the isolation technology of a container. The supported values are. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#isolation RegistryImage#isolation}
        :param labels: User-defined key/value metadata. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#labels RegistryImage#labels}
        :param memory: Set memory limit for build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory RegistryImage#memory}
        :param memory_swap: Total memory (memory + swap), -1 to enable unlimited swap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory_swap RegistryImage#memory_swap}
        :param network_mode: Set the networking mode for the RUN instructions during build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#network_mode RegistryImage#network_mode}
        :param no_cache: Do not use the cache when building the image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#no_cache RegistryImage#no_cache}
        :param platform: Set platform if server is multi-platform capable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#platform RegistryImage#platform}
        :param pull_parent: Attempt to pull the image even if an older image exists locally. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#pull_parent RegistryImage#pull_parent}
        :param remote_context: A Git repository URI or HTTP/HTTPS context URI. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remote_context RegistryImage#remote_context}
        :param remove: Remove intermediate containers after a successful build (default behavior). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remove RegistryImage#remove}
        :param security_opt: The security options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#security_opt RegistryImage#security_opt}
        :param session_id: Set an ID for the build session. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#session_id RegistryImage#session_id}
        :param shm_size: Size of /dev/shm in bytes. The size must be greater than 0. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#shm_size RegistryImage#shm_size}
        :param squash: If true the new layers are squashed into a new image with a single new layer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#squash RegistryImage#squash}
        :param suppress_output: Suppress the build output and print image ID on success. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#suppress_output RegistryImage#suppress_output}
        :param target: Set the target build stage to build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#target RegistryImage#target}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#ulimit RegistryImage#ulimit}
        :param version: Version of the underlying builder to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#version RegistryImage#version}
        '''
        value = RegistryImageBuild(
            context=context,
            auth_config=auth_config,
            build_args=build_args,
            build_id=build_id,
            cache_from=cache_from,
            cgroup_parent=cgroup_parent,
            cpu_period=cpu_period,
            cpu_quota=cpu_quota,
            cpu_set_cpus=cpu_set_cpus,
            cpu_set_mems=cpu_set_mems,
            cpu_shares=cpu_shares,
            dockerfile=dockerfile,
            extra_hosts=extra_hosts,
            force_remove=force_remove,
            isolation=isolation,
            labels=labels,
            memory=memory,
            memory_swap=memory_swap,
            network_mode=network_mode,
            no_cache=no_cache,
            platform=platform,
            pull_parent=pull_parent,
            remote_context=remote_context,
            remove=remove,
            security_opt=security_opt,
            session_id=session_id,
            shm_size=shm_size,
            squash=squash,
            suppress_output=suppress_output,
            target=target,
            ulimit=ulimit,
            version=version,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildAttribute", [value]))

    @jsii.member(jsii_name="resetBuildAttribute")
    def reset_build_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildAttribute", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInsecureSkipVerify")
    def reset_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetKeepRemotely")
    def reset_keep_remotely(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepRemotely", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

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
    @jsii.member(jsii_name="buildAttribute")
    def build_attribute(self) -> "RegistryImageBuildOutputReference":
        return typing.cast("RegistryImageBuildOutputReference", jsii.get(self, "buildAttribute"))

    @builtins.property
    @jsii.member(jsii_name="sha256Digest")
    def sha256_digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256Digest"))

    @builtins.property
    @jsii.member(jsii_name="buildAttributeInput")
    def build_attribute_input(self) -> typing.Optional["RegistryImageBuild"]:
        return typing.cast(typing.Optional["RegistryImageBuild"], jsii.get(self, "buildAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerifyInput")
    def insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="keepRemotelyInput")
    def keep_remotely_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepRemotelyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d67fba200759df5b458b1caa4be7cef5ac0e035a87d3b2923ce3b4e6e9a4e24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerify")
    def insecure_skip_verify(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSkipVerify"))

    @insecure_skip_verify.setter
    def insecure_skip_verify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a6c5c397b208d418773503f20a6a2901d008b8a4d40b51a3235747511fed36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerify", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="keepRemotely")
    def keep_remotely(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "keepRemotely"))

    @keep_remotely.setter
    def keep_remotely(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef684fffe984f287ac48c1eea564fec8a0c5b04f67c0eb6283dc83739f20951a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepRemotely", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff06ba0e9a1bf8e7c95013c273005eac4612259fe0e8ddd243489ed76fd3fd92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e74b1d9cf78af37e12e9ad0e45955111442e30701942e0f8510064d1faaca50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.registryImage.RegistryImageBuild",
    jsii_struct_bases=[],
    name_mapping={
        "context": "context",
        "auth_config": "authConfig",
        "build_args": "buildArgs",
        "build_id": "buildId",
        "cache_from": "cacheFrom",
        "cgroup_parent": "cgroupParent",
        "cpu_period": "cpuPeriod",
        "cpu_quota": "cpuQuota",
        "cpu_set_cpus": "cpuSetCpus",
        "cpu_set_mems": "cpuSetMems",
        "cpu_shares": "cpuShares",
        "dockerfile": "dockerfile",
        "extra_hosts": "extraHosts",
        "force_remove": "forceRemove",
        "isolation": "isolation",
        "labels": "labels",
        "memory": "memory",
        "memory_swap": "memorySwap",
        "network_mode": "networkMode",
        "no_cache": "noCache",
        "platform": "platform",
        "pull_parent": "pullParent",
        "remote_context": "remoteContext",
        "remove": "remove",
        "security_opt": "securityOpt",
        "session_id": "sessionId",
        "shm_size": "shmSize",
        "squash": "squash",
        "suppress_output": "suppressOutput",
        "target": "target",
        "ulimit": "ulimit",
        "version": "version",
    },
)
class RegistryImageBuild:
    def __init__(
        self,
        *,
        context: builtins.str,
        auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RegistryImageBuildAuthConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        build_id: typing.Optional[builtins.str] = None,
        cache_from: typing.Optional[typing.Sequence[builtins.str]] = None,
        cgroup_parent: typing.Optional[builtins.str] = None,
        cpu_period: typing.Optional[jsii.Number] = None,
        cpu_quota: typing.Optional[jsii.Number] = None,
        cpu_set_cpus: typing.Optional[builtins.str] = None,
        cpu_set_mems: typing.Optional[builtins.str] = None,
        cpu_shares: typing.Optional[jsii.Number] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        extra_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        isolation: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory: typing.Optional[jsii.Number] = None,
        memory_swap: typing.Optional[jsii.Number] = None,
        network_mode: typing.Optional[builtins.str] = None,
        no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        platform: typing.Optional[builtins.str] = None,
        pull_parent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remote_context: typing.Optional[builtins.str] = None,
        remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_opt: typing.Optional[typing.Sequence[builtins.str]] = None,
        session_id: typing.Optional[builtins.str] = None,
        shm_size: typing.Optional[jsii.Number] = None,
        squash: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        suppress_output: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        target: typing.Optional[builtins.str] = None,
        ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RegistryImageBuildUlimit", typing.Dict[builtins.str, typing.Any]]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param context: The absolute path to the context folder. You can use the helper function '${path.cwd}/context-dir'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#context RegistryImage#context}
        :param auth_config: auth_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#auth_config RegistryImage#auth_config}
        :param build_args: Pairs for build-time variables in the form TODO. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_args RegistryImage#build_args}
        :param build_id: BuildID is an optional identifier that can be passed together with the build request. The same identifier can be used to gracefully cancel the build with the cancel request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_id RegistryImage#build_id}
        :param cache_from: Images to consider as cache sources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cache_from RegistryImage#cache_from}
        :param cgroup_parent: Optional parent cgroup for the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cgroup_parent RegistryImage#cgroup_parent}
        :param cpu_period: The length of a CPU period in microseconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_period RegistryImage#cpu_period}
        :param cpu_quota: Microseconds of CPU time that the container can get in a CPU period. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_quota RegistryImage#cpu_quota}
        :param cpu_set_cpus: CPUs in which to allow execution (e.g., ``0-3``, ``0``, ``1``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_cpus RegistryImage#cpu_set_cpus}
        :param cpu_set_mems: MEMs in which to allow execution (``0-3``, ``0``, ``1``). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_mems RegistryImage#cpu_set_mems}
        :param cpu_shares: CPU shares (relative weight). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_shares RegistryImage#cpu_shares}
        :param dockerfile: Dockerfile file. Defaults to ``Dockerfile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#dockerfile RegistryImage#dockerfile}
        :param extra_hosts: A list of hostnames/IP mappings to add to the container’s /etc/hosts file. Specified in the form ["hostname:IP"]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#extra_hosts RegistryImage#extra_hosts}
        :param force_remove: Always remove intermediate containers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#force_remove RegistryImage#force_remove}
        :param isolation: Isolation represents the isolation technology of a container. The supported values are. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#isolation RegistryImage#isolation}
        :param labels: User-defined key/value metadata. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#labels RegistryImage#labels}
        :param memory: Set memory limit for build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory RegistryImage#memory}
        :param memory_swap: Total memory (memory + swap), -1 to enable unlimited swap. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory_swap RegistryImage#memory_swap}
        :param network_mode: Set the networking mode for the RUN instructions during build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#network_mode RegistryImage#network_mode}
        :param no_cache: Do not use the cache when building the image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#no_cache RegistryImage#no_cache}
        :param platform: Set platform if server is multi-platform capable. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#platform RegistryImage#platform}
        :param pull_parent: Attempt to pull the image even if an older image exists locally. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#pull_parent RegistryImage#pull_parent}
        :param remote_context: A Git repository URI or HTTP/HTTPS context URI. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remote_context RegistryImage#remote_context}
        :param remove: Remove intermediate containers after a successful build (default behavior). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remove RegistryImage#remove}
        :param security_opt: The security options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#security_opt RegistryImage#security_opt}
        :param session_id: Set an ID for the build session. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#session_id RegistryImage#session_id}
        :param shm_size: Size of /dev/shm in bytes. The size must be greater than 0. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#shm_size RegistryImage#shm_size}
        :param squash: If true the new layers are squashed into a new image with a single new layer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#squash RegistryImage#squash}
        :param suppress_output: Suppress the build output and print image ID on success. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#suppress_output RegistryImage#suppress_output}
        :param target: Set the target build stage to build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#target RegistryImage#target}
        :param ulimit: ulimit block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#ulimit RegistryImage#ulimit}
        :param version: Version of the underlying builder to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#version RegistryImage#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42dfe44dc3fae7d1f27f768d21cc84f587e81ebddf696c172df512008c8f3f5b)
            check_type(argname="argument context", value=context, expected_type=type_hints["context"])
            check_type(argname="argument auth_config", value=auth_config, expected_type=type_hints["auth_config"])
            check_type(argname="argument build_args", value=build_args, expected_type=type_hints["build_args"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument cache_from", value=cache_from, expected_type=type_hints["cache_from"])
            check_type(argname="argument cgroup_parent", value=cgroup_parent, expected_type=type_hints["cgroup_parent"])
            check_type(argname="argument cpu_period", value=cpu_period, expected_type=type_hints["cpu_period"])
            check_type(argname="argument cpu_quota", value=cpu_quota, expected_type=type_hints["cpu_quota"])
            check_type(argname="argument cpu_set_cpus", value=cpu_set_cpus, expected_type=type_hints["cpu_set_cpus"])
            check_type(argname="argument cpu_set_mems", value=cpu_set_mems, expected_type=type_hints["cpu_set_mems"])
            check_type(argname="argument cpu_shares", value=cpu_shares, expected_type=type_hints["cpu_shares"])
            check_type(argname="argument dockerfile", value=dockerfile, expected_type=type_hints["dockerfile"])
            check_type(argname="argument extra_hosts", value=extra_hosts, expected_type=type_hints["extra_hosts"])
            check_type(argname="argument force_remove", value=force_remove, expected_type=type_hints["force_remove"])
            check_type(argname="argument isolation", value=isolation, expected_type=type_hints["isolation"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            check_type(argname="argument memory_swap", value=memory_swap, expected_type=type_hints["memory_swap"])
            check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
            check_type(argname="argument no_cache", value=no_cache, expected_type=type_hints["no_cache"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument pull_parent", value=pull_parent, expected_type=type_hints["pull_parent"])
            check_type(argname="argument remote_context", value=remote_context, expected_type=type_hints["remote_context"])
            check_type(argname="argument remove", value=remove, expected_type=type_hints["remove"])
            check_type(argname="argument security_opt", value=security_opt, expected_type=type_hints["security_opt"])
            check_type(argname="argument session_id", value=session_id, expected_type=type_hints["session_id"])
            check_type(argname="argument shm_size", value=shm_size, expected_type=type_hints["shm_size"])
            check_type(argname="argument squash", value=squash, expected_type=type_hints["squash"])
            check_type(argname="argument suppress_output", value=suppress_output, expected_type=type_hints["suppress_output"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument ulimit", value=ulimit, expected_type=type_hints["ulimit"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "context": context,
        }
        if auth_config is not None:
            self._values["auth_config"] = auth_config
        if build_args is not None:
            self._values["build_args"] = build_args
        if build_id is not None:
            self._values["build_id"] = build_id
        if cache_from is not None:
            self._values["cache_from"] = cache_from
        if cgroup_parent is not None:
            self._values["cgroup_parent"] = cgroup_parent
        if cpu_period is not None:
            self._values["cpu_period"] = cpu_period
        if cpu_quota is not None:
            self._values["cpu_quota"] = cpu_quota
        if cpu_set_cpus is not None:
            self._values["cpu_set_cpus"] = cpu_set_cpus
        if cpu_set_mems is not None:
            self._values["cpu_set_mems"] = cpu_set_mems
        if cpu_shares is not None:
            self._values["cpu_shares"] = cpu_shares
        if dockerfile is not None:
            self._values["dockerfile"] = dockerfile
        if extra_hosts is not None:
            self._values["extra_hosts"] = extra_hosts
        if force_remove is not None:
            self._values["force_remove"] = force_remove
        if isolation is not None:
            self._values["isolation"] = isolation
        if labels is not None:
            self._values["labels"] = labels
        if memory is not None:
            self._values["memory"] = memory
        if memory_swap is not None:
            self._values["memory_swap"] = memory_swap
        if network_mode is not None:
            self._values["network_mode"] = network_mode
        if no_cache is not None:
            self._values["no_cache"] = no_cache
        if platform is not None:
            self._values["platform"] = platform
        if pull_parent is not None:
            self._values["pull_parent"] = pull_parent
        if remote_context is not None:
            self._values["remote_context"] = remote_context
        if remove is not None:
            self._values["remove"] = remove
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if session_id is not None:
            self._values["session_id"] = session_id
        if shm_size is not None:
            self._values["shm_size"] = shm_size
        if squash is not None:
            self._values["squash"] = squash
        if suppress_output is not None:
            self._values["suppress_output"] = suppress_output
        if target is not None:
            self._values["target"] = target
        if ulimit is not None:
            self._values["ulimit"] = ulimit
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def context(self) -> builtins.str:
        '''The absolute path to the context folder. You can use the helper function '${path.cwd}/context-dir'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#context RegistryImage#context}
        '''
        result = self._values.get("context")
        assert result is not None, "Required property 'context' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildAuthConfig"]]]:
        '''auth_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#auth_config RegistryImage#auth_config}
        '''
        result = self._values.get("auth_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildAuthConfig"]]], result)

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Pairs for build-time variables in the form TODO.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_args RegistryImage#build_args}
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def build_id(self) -> typing.Optional[builtins.str]:
        '''BuildID is an optional identifier that can be passed together with the build request.

        The same identifier can be used to gracefully cancel the build with the cancel request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build_id RegistryImage#build_id}
        '''
        result = self._values.get("build_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_from(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Images to consider as cache sources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cache_from RegistryImage#cache_from}
        '''
        result = self._values.get("cache_from")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cgroup_parent(self) -> typing.Optional[builtins.str]:
        '''Optional parent cgroup for the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cgroup_parent RegistryImage#cgroup_parent}
        '''
        result = self._values.get("cgroup_parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_period(self) -> typing.Optional[jsii.Number]:
        '''The length of a CPU period in microseconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_period RegistryImage#cpu_period}
        '''
        result = self._values.get("cpu_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_quota(self) -> typing.Optional[jsii.Number]:
        '''Microseconds of CPU time that the container can get in a CPU period.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_quota RegistryImage#cpu_quota}
        '''
        result = self._values.get("cpu_quota")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cpu_set_cpus(self) -> typing.Optional[builtins.str]:
        '''CPUs in which to allow execution (e.g., ``0-3``, ``0``, ``1``).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_cpus RegistryImage#cpu_set_cpus}
        '''
        result = self._values.get("cpu_set_cpus")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_set_mems(self) -> typing.Optional[builtins.str]:
        '''MEMs in which to allow execution (``0-3``, ``0``, ``1``).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_set_mems RegistryImage#cpu_set_mems}
        '''
        result = self._values.get("cpu_set_mems")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpu_shares(self) -> typing.Optional[jsii.Number]:
        '''CPU shares (relative weight).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#cpu_shares RegistryImage#cpu_shares}
        '''
        result = self._values.get("cpu_shares")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dockerfile(self) -> typing.Optional[builtins.str]:
        '''Dockerfile file. Defaults to ``Dockerfile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#dockerfile RegistryImage#dockerfile}
        '''
        result = self._values.get("dockerfile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of hostnames/IP mappings to add to the container’s /etc/hosts file. Specified in the form ["hostname:IP"].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#extra_hosts RegistryImage#extra_hosts}
        '''
        result = self._values.get("extra_hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def force_remove(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Always remove intermediate containers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#force_remove RegistryImage#force_remove}
        '''
        result = self._values.get("force_remove")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def isolation(self) -> typing.Optional[builtins.str]:
        '''Isolation represents the isolation technology of a container. The supported values are.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#isolation RegistryImage#isolation}
        '''
        result = self._values.get("isolation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-defined key/value metadata.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#labels RegistryImage#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory(self) -> typing.Optional[jsii.Number]:
        '''Set memory limit for build.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory RegistryImage#memory}
        '''
        result = self._values.get("memory")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_swap(self) -> typing.Optional[jsii.Number]:
        '''Total memory (memory + swap), -1 to enable unlimited swap.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#memory_swap RegistryImage#memory_swap}
        '''
        result = self._values.get("memory_swap")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_mode(self) -> typing.Optional[builtins.str]:
        '''Set the networking mode for the RUN instructions during build.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#network_mode RegistryImage#network_mode}
        '''
        result = self._values.get("network_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Do not use the cache when building the image.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#no_cache RegistryImage#no_cache}
        '''
        result = self._values.get("no_cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Set platform if server is multi-platform capable.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#platform RegistryImage#platform}
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_parent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Attempt to pull the image even if an older image exists locally.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#pull_parent RegistryImage#pull_parent}
        '''
        result = self._values.get("pull_parent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def remote_context(self) -> typing.Optional[builtins.str]:
        '''A Git repository URI or HTTP/HTTPS context URI.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remote_context RegistryImage#remote_context}
        '''
        result = self._values.get("remote_context")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Remove intermediate containers after a successful build (default behavior).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#remove RegistryImage#remove}
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The security options.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#security_opt RegistryImage#security_opt}
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def session_id(self) -> typing.Optional[builtins.str]:
        '''Set an ID for the build session.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#session_id RegistryImage#session_id}
        '''
        result = self._values.get("session_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shm_size(self) -> typing.Optional[jsii.Number]:
        '''Size of /dev/shm in bytes. The size must be greater than 0.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#shm_size RegistryImage#shm_size}
        '''
        result = self._values.get("shm_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def squash(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true the new layers are squashed into a new image with a single new layer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#squash RegistryImage#squash}
        '''
        result = self._values.get("squash")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def suppress_output(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Suppress the build output and print image ID on success.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#suppress_output RegistryImage#suppress_output}
        '''
        result = self._values.get("suppress_output")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Set the target build stage to build.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#target RegistryImage#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ulimit(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildUlimit"]]]:
        '''ulimit block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#ulimit RegistryImage#ulimit}
        '''
        result = self._values.get("ulimit")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildUlimit"]]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version of the underlying builder to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#version RegistryImage#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryImageBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.registryImage.RegistryImageBuildAuthConfig",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "auth": "auth",
        "email": "email",
        "identity_token": "identityToken",
        "password": "password",
        "registry_token": "registryToken",
        "server_address": "serverAddress",
        "user_name": "userName",
    },
)
class RegistryImageBuildAuthConfig:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        auth: typing.Optional[builtins.str] = None,
        email: typing.Optional[builtins.str] = None,
        identity_token: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        registry_token: typing.Optional[builtins.str] = None,
        server_address: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: hostname of the registry. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#host_name RegistryImage#host_name}
        :param auth: the auth token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#auth RegistryImage#auth}
        :param email: the user emal. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#email RegistryImage#email}
        :param identity_token: the identity token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#identity_token RegistryImage#identity_token}
        :param password: the registry password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#password RegistryImage#password}
        :param registry_token: the registry token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#registry_token RegistryImage#registry_token}
        :param server_address: the server address. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#server_address RegistryImage#server_address}
        :param user_name: the registry user name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#user_name RegistryImage#user_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a832b76df879954fc5249755df19532788b96ea74ce141c7aeeb04634196162)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument identity_token", value=identity_token, expected_type=type_hints["identity_token"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument registry_token", value=registry_token, expected_type=type_hints["registry_token"])
            check_type(argname="argument server_address", value=server_address, expected_type=type_hints["server_address"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_name": host_name,
        }
        if auth is not None:
            self._values["auth"] = auth
        if email is not None:
            self._values["email"] = email
        if identity_token is not None:
            self._values["identity_token"] = identity_token
        if password is not None:
            self._values["password"] = password
        if registry_token is not None:
            self._values["registry_token"] = registry_token
        if server_address is not None:
            self._values["server_address"] = server_address
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def host_name(self) -> builtins.str:
        '''hostname of the registry.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#host_name RegistryImage#host_name}
        '''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional[builtins.str]:
        '''the auth token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#auth RegistryImage#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''the user emal.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#email RegistryImage#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_token(self) -> typing.Optional[builtins.str]:
        '''the identity token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#identity_token RegistryImage#identity_token}
        '''
        result = self._values.get("identity_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''the registry password.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#password RegistryImage#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_token(self) -> typing.Optional[builtins.str]:
        '''the registry token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#registry_token RegistryImage#registry_token}
        '''
        result = self._values.get("registry_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_address(self) -> typing.Optional[builtins.str]:
        '''the server address.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#server_address RegistryImage#server_address}
        '''
        result = self._values.get("server_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''the registry user name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#user_name RegistryImage#user_name}
        '''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryImageBuildAuthConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RegistryImageBuildAuthConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImageBuildAuthConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a34cf497bd09cfad54b36a1f686566382c5d49121894fce2c2f2ae503d6a79a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RegistryImageBuildAuthConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0c5ee9dabc6d1f489aee1d1bdab6b3147fea095f7ed32463ceb06ccab4fc7c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RegistryImageBuildAuthConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfbf4bc5cf7b70c224e649b1a629f1673bbf90c86cc6fc242420e93816de659)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15555f184e0a6a4cbe087b55ccfed2b5f0dfad71fe8409fc117d817c1727578c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f3c61f6085452af35e17eaae953574914d46c59c2c27a853eb6e924e84c7cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ede1eb91d84efbd140ccb4bcae2f8b1d62a0c8220aa5c24edb04749c9a98332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RegistryImageBuildAuthConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImageBuildAuthConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__042a537bd626c2ebfd94c38c705126a0f5f8810ae6049314d45fe1ab43f74fa2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetIdentityToken")
    def reset_identity_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityToken", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRegistryToken")
    def reset_registry_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryToken", []))

    @jsii.member(jsii_name="resetServerAddress")
    def reset_server_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerAddress", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityTokenInput")
    def identity_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="registryTokenInput")
    def registry_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAddressInput")
    def server_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "auth"))

    @auth.setter
    def auth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72b32ec97ebea251983394c30d8a0acb63cd20de3fc0bceeae81d998b44fa351)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87a35c5e0af0e65e80593d9869604d59d5899c1c6e4fd1e111a29f1f3e7673e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9dec81feabe7797f2ea18d127306c27716e5d36301d10a71002ac84772cc153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityToken")
    def identity_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityToken"))

    @identity_token.setter
    def identity_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba49a619b7094dd7a3b108d1b056d66f6798d6d0cf6b7130b372a9a7ac3cfbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fc5f2661ca2ae6ebc3f57c824484b9529cff85f65219c23dabc3471eca3744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="registryToken")
    def registry_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryToken"))

    @registry_token.setter
    def registry_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d18bbca6be3b7410c36cbcd785989a0c316d9ada8909441140b80b0413c50e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryToken", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverAddress")
    def server_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverAddress"))

    @server_address.setter
    def server_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97ca412fa6e6c8ff7e4598ff12b5d46a287a799e8a1c8c1ab8c28cf472a79bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11aa2eab3999640d94783487efe9b9d12d45c05c63a44ce9ae287ec5978a3544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildAuthConfig]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildAuthConfig]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildAuthConfig]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a108fde6e572bb93b16337a3c0c8a804cc72ca1c2219e61d9c499a687a73d7c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RegistryImageBuildOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImageBuildOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38a0cd14c1293a4c24e2b41259e906e46b7b4f3b26814c7598588d603f3f5214)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAuthConfig")
    def put_auth_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RegistryImageBuildAuthConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22614ac12badb102ae36d4f7dcd3af6908df7f3ec15cf522b701d2e37678f978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAuthConfig", [value]))

    @jsii.member(jsii_name="putUlimit")
    def put_ulimit(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RegistryImageBuildUlimit", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83dbbc63aa37d405a56b857fa39c1a5254cc6fe93b8d3cea9c26e6f087477a3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUlimit", [value]))

    @jsii.member(jsii_name="resetAuthConfig")
    def reset_auth_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthConfig", []))

    @jsii.member(jsii_name="resetBuildArgs")
    def reset_build_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildArgs", []))

    @jsii.member(jsii_name="resetBuildId")
    def reset_build_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildId", []))

    @jsii.member(jsii_name="resetCacheFrom")
    def reset_cache_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheFrom", []))

    @jsii.member(jsii_name="resetCgroupParent")
    def reset_cgroup_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCgroupParent", []))

    @jsii.member(jsii_name="resetCpuPeriod")
    def reset_cpu_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuPeriod", []))

    @jsii.member(jsii_name="resetCpuQuota")
    def reset_cpu_quota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuQuota", []))

    @jsii.member(jsii_name="resetCpuSetCpus")
    def reset_cpu_set_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuSetCpus", []))

    @jsii.member(jsii_name="resetCpuSetMems")
    def reset_cpu_set_mems(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuSetMems", []))

    @jsii.member(jsii_name="resetCpuShares")
    def reset_cpu_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpuShares", []))

    @jsii.member(jsii_name="resetDockerfile")
    def reset_dockerfile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfile", []))

    @jsii.member(jsii_name="resetExtraHosts")
    def reset_extra_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraHosts", []))

    @jsii.member(jsii_name="resetForceRemove")
    def reset_force_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRemove", []))

    @jsii.member(jsii_name="resetIsolation")
    def reset_isolation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsolation", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMemory")
    def reset_memory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemory", []))

    @jsii.member(jsii_name="resetMemorySwap")
    def reset_memory_swap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemorySwap", []))

    @jsii.member(jsii_name="resetNetworkMode")
    def reset_network_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkMode", []))

    @jsii.member(jsii_name="resetNoCache")
    def reset_no_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoCache", []))

    @jsii.member(jsii_name="resetPlatform")
    def reset_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatform", []))

    @jsii.member(jsii_name="resetPullParent")
    def reset_pull_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullParent", []))

    @jsii.member(jsii_name="resetRemoteContext")
    def reset_remote_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteContext", []))

    @jsii.member(jsii_name="resetRemove")
    def reset_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemove", []))

    @jsii.member(jsii_name="resetSecurityOpt")
    def reset_security_opt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityOpt", []))

    @jsii.member(jsii_name="resetSessionId")
    def reset_session_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionId", []))

    @jsii.member(jsii_name="resetShmSize")
    def reset_shm_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShmSize", []))

    @jsii.member(jsii_name="resetSquash")
    def reset_squash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquash", []))

    @jsii.member(jsii_name="resetSuppressOutput")
    def reset_suppress_output(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppressOutput", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetUlimit")
    def reset_ulimit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUlimit", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="authConfig")
    def auth_config(self) -> RegistryImageBuildAuthConfigList:
        return typing.cast(RegistryImageBuildAuthConfigList, jsii.get(self, "authConfig"))

    @builtins.property
    @jsii.member(jsii_name="ulimit")
    def ulimit(self) -> "RegistryImageBuildUlimitList":
        return typing.cast("RegistryImageBuildUlimitList", jsii.get(self, "ulimit"))

    @builtins.property
    @jsii.member(jsii_name="authConfigInput")
    def auth_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]], jsii.get(self, "authConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="buildArgsInput")
    def build_args_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "buildArgsInput"))

    @builtins.property
    @jsii.member(jsii_name="buildIdInput")
    def build_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheFromInput")
    def cache_from_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheFromInput"))

    @builtins.property
    @jsii.member(jsii_name="cgroupParentInput")
    def cgroup_parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cgroupParentInput"))

    @builtins.property
    @jsii.member(jsii_name="contextInput")
    def context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contextInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuPeriodInput")
    def cpu_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuQuotaInput")
    def cpu_quota_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuQuotaInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSetCpusInput")
    def cpu_set_cpus_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuSetCpusInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSetMemsInput")
    def cpu_set_mems_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpuSetMemsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpuSharesInput")
    def cpu_shares_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cpuSharesInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfileInput")
    def dockerfile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileInput"))

    @builtins.property
    @jsii.member(jsii_name="extraHostsInput")
    def extra_hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "extraHostsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRemoveInput")
    def force_remove_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="isolationInput")
    def isolation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isolationInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryInput")
    def memory_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySwapInput")
    def memory_swap_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySwapInput"))

    @builtins.property
    @jsii.member(jsii_name="networkModeInput")
    def network_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkModeInput"))

    @builtins.property
    @jsii.member(jsii_name="noCacheInput")
    def no_cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="pullParentInput")
    def pull_parent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "pullParentInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteContextInput")
    def remote_context_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteContextInput"))

    @builtins.property
    @jsii.member(jsii_name="removeInput")
    def remove_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "removeInput"))

    @builtins.property
    @jsii.member(jsii_name="securityOptInput")
    def security_opt_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityOptInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionIdInput")
    def session_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="shmSizeInput")
    def shm_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "shmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="squashInput")
    def squash_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "squashInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressOutputInput")
    def suppress_output_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "suppressOutputInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="ulimitInput")
    def ulimit_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildUlimit"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RegistryImageBuildUlimit"]]], jsii.get(self, "ulimitInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="buildArgs")
    def build_args(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "buildArgs"))

    @build_args.setter
    def build_args(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb41e120dd4f93983e8f66750df4d5bba6917ef583d45913e32ec3183c2321df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildArgs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildId"))

    @build_id.setter
    def build_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589c608123ebc51869572c3cb17758a6b7e6f4df728c8f98ffe2bed7791e8fd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cacheFrom")
    def cache_from(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cacheFrom"))

    @cache_from.setter
    def cache_from(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f6574c65b061e10323ac7861332cbcf70e6a68b8b3f8c1e2f779bd3eb76e922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheFrom", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cgroupParent")
    def cgroup_parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cgroupParent"))

    @cgroup_parent.setter
    def cgroup_parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5691866897861e56cd1d95c9c0424710e65f5ee19913590196160b52a1f59a6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cgroupParent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="context")
    def context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "context"))

    @context.setter
    def context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3360aba56fa83cdbd18333c72c98a5fe86a6d0bf2b1c9be0049bcab0bc9d22c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "context", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuPeriod")
    def cpu_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuPeriod"))

    @cpu_period.setter
    def cpu_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d459a7b5b4b24b09cf5efb6a713547c9eb6db503cfe8eb55ecca34a6819d093c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuQuota")
    def cpu_quota(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuQuota"))

    @cpu_quota.setter
    def cpu_quota(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6b9e96994bb3647875f006ba91eb875cc37e11ac8508046beb06e2e2843bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuQuota", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuSetCpus")
    def cpu_set_cpus(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuSetCpus"))

    @cpu_set_cpus.setter
    def cpu_set_cpus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19750d20866df99a77862581ad8e433c7dd08febd984de6e6c7ead6a7b6b8a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuSetCpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuSetMems")
    def cpu_set_mems(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpuSetMems"))

    @cpu_set_mems.setter
    def cpu_set_mems(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e7e69a8ad6b6dd092d2078afe321fc765790325de5a0e2cb12a628ee4cfa35d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuSetMems", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cpuShares")
    def cpu_shares(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cpuShares"))

    @cpu_shares.setter
    def cpu_shares(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f5000c5a4bf2a9c9b0497acd982970fa93cadc06d9fc310ec1ec78463a6719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpuShares", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dockerfile")
    def dockerfile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfile"))

    @dockerfile.setter
    def dockerfile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8933f0f089d852831b4e77805a9540ab729cea9eddb125ff8acc5ab4b171a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfile", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="extraHosts")
    def extra_hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "extraHosts"))

    @extra_hosts.setter
    def extra_hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79bdb65fc45ef7bdd1479333f26a842d933f08c8010168ef4b46215350884663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraHosts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="forceRemove")
    def force_remove(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceRemove"))

    @force_remove.setter
    def force_remove(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d490447db0d21b3b341966d542b1233ccaf968b12cdec7de91f55380ee3d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRemove", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isolation")
    def isolation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isolation"))

    @isolation.setter
    def isolation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf15dc948d014732c98b02a75628aaf35278526417d260ffd4bbc016e1e7e076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isolation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd1a709f683ecd20d8f171a076d39bbabf5aa4d5366fc20bbfc0244aa1f70bd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memory")
    def memory(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memory"))

    @memory.setter
    def memory(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9283c3e3011614c89310080274e60362a9db17dd9b778820fde6c2cf64e9f57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memory", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memorySwap")
    def memory_swap(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySwap"))

    @memory_swap.setter
    def memory_swap(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ed754e692721dc8e02738b6466d8bb2f5931db6df5b71b7bb233a331aba876)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySwap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkMode")
    def network_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkMode"))

    @network_mode.setter
    def network_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa27fa89a975e1471c7e20ec0dbbcd1d58ca82785cd57c679519d736027ee5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="noCache")
    def no_cache(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noCache"))

    @no_cache.setter
    def no_cache(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9dcca6af72df3663b383c3df97c5975549587b565257012b23a052180a3be7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noCache", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7fa1f144f7ae42803957096386de0708a7835667830911bbb057ab74a203088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pullParent")
    def pull_parent(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "pullParent"))

    @pull_parent.setter
    def pull_parent(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76c2bd9156235f37fa480ca008c5f7b4a9a1a4213f304f7f1213f484765a45f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullParent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteContext")
    def remote_context(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteContext"))

    @remote_context.setter
    def remote_context(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ca58913233a8619825b74947fcc90668dc71aace9bbdcefa57ba179202fae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteContext", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remove")
    def remove(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "remove"))

    @remove.setter
    def remove(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4174d87c20cc617e4fe2dcd143066969a17c7473f73de9dab962ec83d5fe3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remove", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityOpt")
    def security_opt(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityOpt"))

    @security_opt.setter
    def security_opt(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e70aa915fe4a9905613ebe39dea3682713f4d513a9e56c6f3c0ab9d438b7dae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityOpt", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sessionId")
    def session_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionId"))

    @session_id.setter
    def session_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebcfe6b2029964a039235e60841705d8ff07675b034191408576fd186a5692f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shmSize")
    def shm_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "shmSize"))

    @shm_size.setter
    def shm_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a06a295c5c8bce418c604fe1d8e803b3665fc704f2f9d45bbdf348eb82e0d84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shmSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="squash")
    def squash(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "squash"))

    @squash.setter
    def squash(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262d1b00748577088b71c56fb675e66a84abdf246ce6f319a25f1f965d6823d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squash", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="suppressOutput")
    def suppress_output(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "suppressOutput"))

    @suppress_output.setter
    def suppress_output(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd248eb639e5cc0a6adcdc47d6e05d98fe2d43ea014acf40d2b261c8f4eda002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressOutput", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c788e73287bb190c7e4c6f2efb0749143a15bdd9c97b7845621ff73e79f78723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d00b0b821dbf4690240cc50a1872e37916a6ef34f6fab2553a3450574c71d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RegistryImageBuild]:
        return typing.cast(typing.Optional[RegistryImageBuild], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RegistryImageBuild]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358216c9e785e05af5f2f0f6afd9559655a3b5a7616faeb913b5e8b139cdd345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.registryImage.RegistryImageBuildUlimit",
    jsii_struct_bases=[],
    name_mapping={"hard": "hard", "name": "name", "soft": "soft"},
)
class RegistryImageBuildUlimit:
    def __init__(
        self,
        *,
        hard: jsii.Number,
        name: builtins.str,
        soft: jsii.Number,
    ) -> None:
        '''
        :param hard: soft limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#hard RegistryImage#hard}
        :param name: type of ulimit, e.g. ``nofile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#name RegistryImage#name}
        :param soft: hard limit. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#soft RegistryImage#soft}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a459fe4315de4306acf3d13225824b2f8a78a6017eef291aa8ce1cc13f2ef2)
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
        '''soft limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#hard RegistryImage#hard}
        '''
        result = self._values.get("hard")
        assert result is not None, "Required property 'hard' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''type of ulimit, e.g. ``nofile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#name RegistryImage#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def soft(self) -> jsii.Number:
        '''hard limit.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#soft RegistryImage#soft}
        '''
        result = self._values.get("soft")
        assert result is not None, "Required property 'soft' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryImageBuildUlimit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RegistryImageBuildUlimitList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImageBuildUlimitList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6540141051ddd81e87bfd30d793a4bf2bb504bfa016a5fda62c7225b090a6e6e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RegistryImageBuildUlimitOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d875c100d2941de11908fe214335b6e7d2c88ec0e2e9eb32e8c4e08203b74791)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RegistryImageBuildUlimitOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd281c257355cbc277de0e6129f0578ea2e1101daf987f242d7ad1eaf0b1fa0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c92ad14bec797359d32b87a538f8a06df0d8abb6777d5b6ae10abb6eeca66705)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e86a33375516ac1ee39d7da43afcaf5e3bba6bb5b0e4cf42c861fcf202782809)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildUlimit]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildUlimit]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildUlimit]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcceaa012d660e1b726a79204626204fe9020cb26b108e0290fc88fdcaffb025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class RegistryImageBuildUlimitOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.registryImage.RegistryImageBuildUlimitOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba5f7fe3b813cf556da137dd98b2ea3e462fe80a2c162bd331a8a91d6da5668e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ad4b097f2c8d07ad3b8b4894bc3dcf87fccf5154b0fc347f374e64768f0ff77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hard", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c6990fd3437127f3adf51b3fa6a208a86397d84748840f92031584e0a5165e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="soft")
    def soft(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "soft"))

    @soft.setter
    def soft(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac13143374a43d6a1de1cb44d44af9dcde161fd4f508d822b29a1f49f8be84a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "soft", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildUlimit]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildUlimit]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildUlimit]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caa1b782ef9a15c870b2eb7863acc02029e6515823fa4dcab69478b117ef2777)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.registryImage.RegistryImageConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "build_attribute": "buildAttribute",
        "id": "id",
        "insecure_skip_verify": "insecureSkipVerify",
        "keep_remotely": "keepRemotely",
        "triggers": "triggers",
    },
)
class RegistryImageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        build_attribute: typing.Optional[typing.Union[RegistryImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keep_remotely: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the Docker image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#name RegistryImage#name}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build RegistryImage#build}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#id RegistryImage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insecure_skip_verify: If ``true``, the verification of TLS certificates of the server/registry is disabled. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#insecure_skip_verify RegistryImage#insecure_skip_verify}
        :param keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker registry on destroy operation. Defaults to ``false`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#keep_remotely RegistryImage#keep_remotely}
        :param triggers: A map of arbitrary strings that, when changed, will force the ``docker_registry_image`` resource to be replaced. This can be used to rebuild an image when contents of source code folders change or to repush a local image Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#triggers RegistryImage#triggers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(build_attribute, dict):
            build_attribute = RegistryImageBuild(**build_attribute)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b0b0ab4ae49eda201b45853c6b7bb6fac24c8efbe79c76ccc071be057bfc4a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument build_attribute", value=build_attribute, expected_type=type_hints["build_attribute"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument keep_remotely", value=keep_remotely, expected_type=type_hints["keep_remotely"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if build_attribute is not None:
            self._values["build_attribute"] = build_attribute
        if id is not None:
            self._values["id"] = id
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if keep_remotely is not None:
            self._values["keep_remotely"] = keep_remotely
        if triggers is not None:
            self._values["triggers"] = triggers

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
    def name(self) -> builtins.str:
        '''The name of the Docker image.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#name RegistryImage#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_attribute(self) -> typing.Optional[RegistryImageBuild]:
        '''build block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#build RegistryImage#build}
        '''
        result = self._values.get("build_attribute")
        return typing.cast(typing.Optional[RegistryImageBuild], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#id RegistryImage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If ``true``, the verification of TLS certificates of the server/registry is disabled. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#insecure_skip_verify RegistryImage#insecure_skip_verify}
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def keep_remotely(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, then the Docker image won't be deleted on destroy operation.

        If this is false, it will delete the image from the docker registry on destroy operation. Defaults to ``false``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#keep_remotely RegistryImage#keep_remotely}
        '''
        result = self._values.get("keep_remotely")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of arbitrary strings that, when changed, will force the ``docker_registry_image`` resource to be replaced.

        This can be used to rebuild an image when contents of source code folders change or to repush a local image

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/registry_image#triggers RegistryImage#triggers}
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RegistryImage",
    "RegistryImageBuild",
    "RegistryImageBuildAuthConfig",
    "RegistryImageBuildAuthConfigList",
    "RegistryImageBuildAuthConfigOutputReference",
    "RegistryImageBuildOutputReference",
    "RegistryImageBuildUlimit",
    "RegistryImageBuildUlimitList",
    "RegistryImageBuildUlimitOutputReference",
    "RegistryImageConfig",
]

publication.publish()

def _typecheckingstub__2671116897cf8aed30f5abdf331c7e525a63a2285e99551c6ec5aa6d7bb873d4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    build_attribute: typing.Optional[typing.Union[RegistryImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    keep_remotely: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__beb2669073186121bed9d1b5d91f2ba3348aeede720d0b99573c6513acf02a68(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d67fba200759df5b458b1caa4be7cef5ac0e035a87d3b2923ce3b4e6e9a4e24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a6c5c397b208d418773503f20a6a2901d008b8a4d40b51a3235747511fed36(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef684fffe984f287ac48c1eea564fec8a0c5b04f67c0eb6283dc83739f20951a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff06ba0e9a1bf8e7c95013c273005eac4612259fe0e8ddd243489ed76fd3fd92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e74b1d9cf78af37e12e9ad0e45955111442e30701942e0f8510064d1faaca50(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42dfe44dc3fae7d1f27f768d21cc84f587e81ebddf696c172df512008c8f3f5b(
    *,
    context: builtins.str,
    auth_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RegistryImageBuildAuthConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    build_id: typing.Optional[builtins.str] = None,
    cache_from: typing.Optional[typing.Sequence[builtins.str]] = None,
    cgroup_parent: typing.Optional[builtins.str] = None,
    cpu_period: typing.Optional[jsii.Number] = None,
    cpu_quota: typing.Optional[jsii.Number] = None,
    cpu_set_cpus: typing.Optional[builtins.str] = None,
    cpu_set_mems: typing.Optional[builtins.str] = None,
    cpu_shares: typing.Optional[jsii.Number] = None,
    dockerfile: typing.Optional[builtins.str] = None,
    extra_hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    isolation: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    memory: typing.Optional[jsii.Number] = None,
    memory_swap: typing.Optional[jsii.Number] = None,
    network_mode: typing.Optional[builtins.str] = None,
    no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    platform: typing.Optional[builtins.str] = None,
    pull_parent: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    remote_context: typing.Optional[builtins.str] = None,
    remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_opt: typing.Optional[typing.Sequence[builtins.str]] = None,
    session_id: typing.Optional[builtins.str] = None,
    shm_size: typing.Optional[jsii.Number] = None,
    squash: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    suppress_output: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    target: typing.Optional[builtins.str] = None,
    ulimit: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RegistryImageBuildUlimit, typing.Dict[builtins.str, typing.Any]]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a832b76df879954fc5249755df19532788b96ea74ce141c7aeeb04634196162(
    *,
    host_name: builtins.str,
    auth: typing.Optional[builtins.str] = None,
    email: typing.Optional[builtins.str] = None,
    identity_token: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    registry_token: typing.Optional[builtins.str] = None,
    server_address: typing.Optional[builtins.str] = None,
    user_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34cf497bd09cfad54b36a1f686566382c5d49121894fce2c2f2ae503d6a79a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0c5ee9dabc6d1f489aee1d1bdab6b3147fea095f7ed32463ceb06ccab4fc7c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfbf4bc5cf7b70c224e649b1a629f1673bbf90c86cc6fc242420e93816de659(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15555f184e0a6a4cbe087b55ccfed2b5f0dfad71fe8409fc117d817c1727578c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3c61f6085452af35e17eaae953574914d46c59c2c27a853eb6e924e84c7cd2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ede1eb91d84efbd140ccb4bcae2f8b1d62a0c8220aa5c24edb04749c9a98332(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildAuthConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__042a537bd626c2ebfd94c38c705126a0f5f8810ae6049314d45fe1ab43f74fa2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b32ec97ebea251983394c30d8a0acb63cd20de3fc0bceeae81d998b44fa351(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a35c5e0af0e65e80593d9869604d59d5899c1c6e4fd1e111a29f1f3e7673e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9dec81feabe7797f2ea18d127306c27716e5d36301d10a71002ac84772cc153(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba49a619b7094dd7a3b108d1b056d66f6798d6d0cf6b7130b372a9a7ac3cfbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fc5f2661ca2ae6ebc3f57c824484b9529cff85f65219c23dabc3471eca3744(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d18bbca6be3b7410c36cbcd785989a0c316d9ada8909441140b80b0413c50e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97ca412fa6e6c8ff7e4598ff12b5d46a287a799e8a1c8c1ab8c28cf472a79bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11aa2eab3999640d94783487efe9b9d12d45c05c63a44ce9ae287ec5978a3544(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a108fde6e572bb93b16337a3c0c8a804cc72ca1c2219e61d9c499a687a73d7c7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildAuthConfig]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a0cd14c1293a4c24e2b41259e906e46b7b4f3b26814c7598588d603f3f5214(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22614ac12badb102ae36d4f7dcd3af6908df7f3ec15cf522b701d2e37678f978(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RegistryImageBuildAuthConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83dbbc63aa37d405a56b857fa39c1a5254cc6fe93b8d3cea9c26e6f087477a3a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RegistryImageBuildUlimit, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb41e120dd4f93983e8f66750df4d5bba6917ef583d45913e32ec3183c2321df(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589c608123ebc51869572c3cb17758a6b7e6f4df728c8f98ffe2bed7791e8fd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6574c65b061e10323ac7861332cbcf70e6a68b8b3f8c1e2f779bd3eb76e922(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5691866897861e56cd1d95c9c0424710e65f5ee19913590196160b52a1f59a6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3360aba56fa83cdbd18333c72c98a5fe86a6d0bf2b1c9be0049bcab0bc9d22c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d459a7b5b4b24b09cf5efb6a713547c9eb6db503cfe8eb55ecca34a6819d093c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6b9e96994bb3647875f006ba91eb875cc37e11ac8508046beb06e2e2843bc3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19750d20866df99a77862581ad8e433c7dd08febd984de6e6c7ead6a7b6b8a13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e7e69a8ad6b6dd092d2078afe321fc765790325de5a0e2cb12a628ee4cfa35d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f5000c5a4bf2a9c9b0497acd982970fa93cadc06d9fc310ec1ec78463a6719(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8933f0f089d852831b4e77805a9540ab729cea9eddb125ff8acc5ab4b171a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bdb65fc45ef7bdd1479333f26a842d933f08c8010168ef4b46215350884663(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d490447db0d21b3b341966d542b1233ccaf968b12cdec7de91f55380ee3d54(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf15dc948d014732c98b02a75628aaf35278526417d260ffd4bbc016e1e7e076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1a709f683ecd20d8f171a076d39bbabf5aa4d5366fc20bbfc0244aa1f70bd9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9283c3e3011614c89310080274e60362a9db17dd9b778820fde6c2cf64e9f57(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ed754e692721dc8e02738b6466d8bb2f5931db6df5b71b7bb233a331aba876(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa27fa89a975e1471c7e20ec0dbbcd1d58ca82785cd57c679519d736027ee5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9dcca6af72df3663b383c3df97c5975549587b565257012b23a052180a3be7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7fa1f144f7ae42803957096386de0708a7835667830911bbb057ab74a203088(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c2bd9156235f37fa480ca008c5f7b4a9a1a4213f304f7f1213f484765a45f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ca58913233a8619825b74947fcc90668dc71aace9bbdcefa57ba179202fae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4174d87c20cc617e4fe2dcd143066969a17c7473f73de9dab962ec83d5fe3c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e70aa915fe4a9905613ebe39dea3682713f4d513a9e56c6f3c0ab9d438b7dae(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebcfe6b2029964a039235e60841705d8ff07675b034191408576fd186a5692f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a06a295c5c8bce418c604fe1d8e803b3665fc704f2f9d45bbdf348eb82e0d84(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262d1b00748577088b71c56fb675e66a84abdf246ce6f319a25f1f965d6823d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd248eb639e5cc0a6adcdc47d6e05d98fe2d43ea014acf40d2b261c8f4eda002(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c788e73287bb190c7e4c6f2efb0749143a15bdd9c97b7845621ff73e79f78723(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d00b0b821dbf4690240cc50a1872e37916a6ef34f6fab2553a3450574c71d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358216c9e785e05af5f2f0f6afd9559655a3b5a7616faeb913b5e8b139cdd345(
    value: typing.Optional[RegistryImageBuild],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a459fe4315de4306acf3d13225824b2f8a78a6017eef291aa8ce1cc13f2ef2(
    *,
    hard: jsii.Number,
    name: builtins.str,
    soft: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6540141051ddd81e87bfd30d793a4bf2bb504bfa016a5fda62c7225b090a6e6e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d875c100d2941de11908fe214335b6e7d2c88ec0e2e9eb32e8c4e08203b74791(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd281c257355cbc277de0e6129f0578ea2e1101daf987f242d7ad1eaf0b1fa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92ad14bec797359d32b87a538f8a06df0d8abb6777d5b6ae10abb6eeca66705(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86a33375516ac1ee39d7da43afcaf5e3bba6bb5b0e4cf42c861fcf202782809(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcceaa012d660e1b726a79204626204fe9020cb26b108e0290fc88fdcaffb025(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RegistryImageBuildUlimit]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5f7fe3b813cf556da137dd98b2ea3e462fe80a2c162bd331a8a91d6da5668e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad4b097f2c8d07ad3b8b4894bc3dcf87fccf5154b0fc347f374e64768f0ff77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c6990fd3437127f3adf51b3fa6a208a86397d84748840f92031584e0a5165e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac13143374a43d6a1de1cb44d44af9dcde161fd4f508d822b29a1f49f8be84a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa1b782ef9a15c870b2eb7863acc02029e6515823fa4dcab69478b117ef2777(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, RegistryImageBuildUlimit]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b0b0ab4ae49eda201b45853c6b7bb6fac24c8efbe79c76ccc071be057bfc4a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    build_attribute: typing.Optional[typing.Union[RegistryImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    keep_remotely: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
