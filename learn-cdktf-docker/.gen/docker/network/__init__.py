r'''
# `docker_network`

Refer to the Terraform Registry for docs: [`docker_network`](https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network).
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


class Network(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.network.Network",
):
    '''Represents a {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network docker_network}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        attachable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_duplicate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ipam_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ipam_driver: typing.Optional[builtins.str] = None,
        ipam_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network docker_network} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the Docker network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#name Network#name}
        :param attachable: Enable manual container attachment to the network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#attachable Network#attachable}
        :param check_duplicate: Requests daemon to check for networks with same name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#check_duplicate Network#check_duplicate}
        :param driver: The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#driver Network#driver}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: Create swarm routing-mesh network. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ingress Network#ingress}
        :param internal: Whether the network is internal. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#internal Network#internal}
        :param ipam_config: ipam_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_config Network#ipam_config}
        :param ipam_driver: Driver used by the custom IP scheme of the network. Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_driver Network#ipam_driver}
        :param ipam_options: Provide explicit options to the IPAM driver. Valid options vary with ``ipam_driver`` and refer to that driver's documentation for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_options Network#ipam_options}
        :param ipv6: Enable IPv6 networking. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipv6 Network#ipv6}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#labels Network#labels}
        :param options: Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#options Network#options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__218985ac8fc00a3223969045ccb0eb63761b5ea03d541fb9f4b707052a90ccdf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConfig(
            name=name,
            attachable=attachable,
            check_duplicate=check_duplicate,
            driver=driver,
            id=id,
            ingress=ingress,
            internal=internal,
            ipam_config=ipam_config,
            ipam_driver=ipam_driver,
            ipam_options=ipam_options,
            ipv6=ipv6,
            labels=labels,
            options=options,
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
        '''Generates CDKTF code for importing a Network resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Network to import.
        :param import_from_id: The id of the existing Network that should be imported. Refer to the {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Network to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b12b44e21f03ca40228f6b9cc51136bda0e663dfdf51112035762c32cf13eaec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putIpamConfig")
    def put_ipam_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ead55450684b75eb9e23b5d3558b9f468e1c3124e2e26d061c18512d2f149b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpamConfig", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7ec1f3ce02fe104e53ae82a83c732f7d79b4e9fe5ef10d63b66a83737c1f59f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="resetAttachable")
    def reset_attachable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttachable", []))

    @jsii.member(jsii_name="resetCheckDuplicate")
    def reset_check_duplicate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckDuplicate", []))

    @jsii.member(jsii_name="resetDriver")
    def reset_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriver", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @jsii.member(jsii_name="resetInternal")
    def reset_internal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternal", []))

    @jsii.member(jsii_name="resetIpamConfig")
    def reset_ipam_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpamConfig", []))

    @jsii.member(jsii_name="resetIpamDriver")
    def reset_ipam_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpamDriver", []))

    @jsii.member(jsii_name="resetIpamOptions")
    def reset_ipam_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpamOptions", []))

    @jsii.member(jsii_name="resetIpv6")
    def reset_ipv6(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

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
    @jsii.member(jsii_name="ipamConfig")
    def ipam_config(self) -> "NetworkIpamConfigList":
        return typing.cast("NetworkIpamConfigList", jsii.get(self, "ipamConfig"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "NetworkLabelsList":
        return typing.cast("NetworkLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @builtins.property
    @jsii.member(jsii_name="attachableInput")
    def attachable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "attachableInput"))

    @builtins.property
    @jsii.member(jsii_name="checkDuplicateInput")
    def check_duplicate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "checkDuplicateInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="internalInput")
    def internal_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamConfigInput")
    def ipam_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkIpamConfig"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkIpamConfig"]]], jsii.get(self, "ipamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamDriverInput")
    def ipam_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipamDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="ipamOptionsInput")
    def ipam_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "ipamOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6Input")
    def ipv6_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ipv6Input"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="attachable")
    def attachable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "attachable"))

    @attachable.setter
    def attachable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a291a759ab4d5010dac97cc4bca489634c3258bb8da94e2d611807fdf62f483)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="checkDuplicate")
    def check_duplicate(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "checkDuplicate"))

    @check_duplicate.setter
    def check_duplicate(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89b8ea2a5238674aaa3b83b76951ead4045fe0954780f3a5505c651448e3b31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkDuplicate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a228670bbc8f68646d2222f6737a47649267a1b932f987f9f4b631f9ba381d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52052a2c0858cd004a33128e50c2ddb3d1b12e752f73e557374bae744823e14a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ingress"))

    @ingress.setter
    def ingress(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cde5a06ba7647b23b0afcbb63d2b9fc1524c886ee7c36dd11b4d95706a74b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internal")
    def internal(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "internal"))

    @internal.setter
    def internal(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24ace73edb9b86328ded7ff61fee3de2ab081ee54bb88f405f46f3423f36d02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipamDriver")
    def ipam_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipamDriver"))

    @ipam_driver.setter
    def ipam_driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d7923fe07366174d5facc3f1dcd924c086b89c7312694a6891f009b5e10c9d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipamDriver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipamOptions")
    def ipam_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "ipamOptions"))

    @ipam_options.setter
    def ipam_options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__864a05adce9583ca9fe91ee565291bf6e184c566a7a333a3565533c12bbd206b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipamOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ipv6"))

    @ipv6.setter
    def ipv6(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5522b70a0a0e8f4b9d88c92861b6181183da3475ce31d8eca19180759a0e9220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31242c5cfb673c1fac7d10fe18f1ec1717e92f065f27a9e8f5ecb28f6c2bc1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e138ada15241e75505611e6a6ae4e63284a5ecc0edab566574a70f172a5a8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.network.NetworkConfig",
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
        "attachable": "attachable",
        "check_duplicate": "checkDuplicate",
        "driver": "driver",
        "id": "id",
        "ingress": "ingress",
        "internal": "internal",
        "ipam_config": "ipamConfig",
        "ipam_driver": "ipamDriver",
        "ipam_options": "ipamOptions",
        "ipv6": "ipv6",
        "labels": "labels",
        "options": "options",
    },
)
class NetworkConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        attachable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        check_duplicate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        driver: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        internal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ipam_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkIpamConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        ipam_driver: typing.Optional[builtins.str] = None,
        ipam_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NetworkLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the Docker network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#name Network#name}
        :param attachable: Enable manual container attachment to the network. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#attachable Network#attachable}
        :param check_duplicate: Requests daemon to check for networks with same name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#check_duplicate Network#check_duplicate}
        :param driver: The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#driver Network#driver}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: Create swarm routing-mesh network. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ingress Network#ingress}
        :param internal: Whether the network is internal. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#internal Network#internal}
        :param ipam_config: ipam_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_config Network#ipam_config}
        :param ipam_driver: Driver used by the custom IP scheme of the network. Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_driver Network#ipam_driver}
        :param ipam_options: Provide explicit options to the IPAM driver. Valid options vary with ``ipam_driver`` and refer to that driver's documentation for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_options Network#ipam_options}
        :param ipv6: Enable IPv6 networking. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipv6 Network#ipv6}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#labels Network#labels}
        :param options: Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#options Network#options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a15458757b6822868c2d774eb993770ce2fea1779bf6a9ea52035e09761a45d0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument attachable", value=attachable, expected_type=type_hints["attachable"])
            check_type(argname="argument check_duplicate", value=check_duplicate, expected_type=type_hints["check_duplicate"])
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument internal", value=internal, expected_type=type_hints["internal"])
            check_type(argname="argument ipam_config", value=ipam_config, expected_type=type_hints["ipam_config"])
            check_type(argname="argument ipam_driver", value=ipam_driver, expected_type=type_hints["ipam_driver"])
            check_type(argname="argument ipam_options", value=ipam_options, expected_type=type_hints["ipam_options"])
            check_type(argname="argument ipv6", value=ipv6, expected_type=type_hints["ipv6"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
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
        if attachable is not None:
            self._values["attachable"] = attachable
        if check_duplicate is not None:
            self._values["check_duplicate"] = check_duplicate
        if driver is not None:
            self._values["driver"] = driver
        if id is not None:
            self._values["id"] = id
        if ingress is not None:
            self._values["ingress"] = ingress
        if internal is not None:
            self._values["internal"] = internal
        if ipam_config is not None:
            self._values["ipam_config"] = ipam_config
        if ipam_driver is not None:
            self._values["ipam_driver"] = ipam_driver
        if ipam_options is not None:
            self._values["ipam_options"] = ipam_options
        if ipv6 is not None:
            self._values["ipv6"] = ipv6
        if labels is not None:
            self._values["labels"] = labels
        if options is not None:
            self._values["options"] = options

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
        '''The name of the Docker network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#name Network#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable manual container attachment to the network.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#attachable Network#attachable}
        '''
        result = self._values.get("attachable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def check_duplicate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Requests daemon to check for networks with same name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#check_duplicate Network#check_duplicate}
        '''
        result = self._values.get("check_duplicate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def driver(self) -> typing.Optional[builtins.str]:
        '''The driver of the Docker network. Possible values are ``bridge``, ``host``, ``overlay``, ``macvlan``. See `network docs <https://docs.docker.com/network/#network-drivers>`_ for more details.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#driver Network#driver}
        '''
        result = self._values.get("driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#id Network#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Create swarm routing-mesh network. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ingress Network#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def internal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the network is internal.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#internal Network#internal}
        '''
        result = self._values.get("internal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ipam_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkIpamConfig"]]]:
        '''ipam_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_config Network#ipam_config}
        '''
        result = self._values.get("ipam_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkIpamConfig"]]], result)

    @builtins.property
    def ipam_driver(self) -> typing.Optional[builtins.str]:
        '''Driver used by the custom IP scheme of the network. Defaults to ``default``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_driver Network#ipam_driver}
        '''
        result = self._values.get("ipam_driver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipam_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Provide explicit options to the IPAM driver.

        Valid options vary with ``ipam_driver`` and refer to that driver's documentation for more details.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipam_options Network#ipam_options}
        '''
        result = self._values.get("ipam_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def ipv6(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable IPv6 networking. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ipv6 Network#ipv6}
        '''
        result = self._values.get("ipv6")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#labels Network#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NetworkLabels"]]], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Only available with bridge networks. See `bridge options docs <https://docs.docker.com/engine/reference/commandline/network_create/#bridge-driver-options>`_ for more details.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#options Network#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.network.NetworkIpamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "aux_address": "auxAddress",
        "gateway": "gateway",
        "ip_range": "ipRange",
        "subnet": "subnet",
    },
)
class NetworkIpamConfig:
    def __init__(
        self,
        *,
        aux_address: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gateway: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        subnet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aux_address: Auxiliary IPv4 or IPv6 addresses used by Network driver. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#aux_address Network#aux_address}
        :param gateway: The IP address of the gateway. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#gateway Network#gateway}
        :param ip_range: The ip range in CIDR form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ip_range Network#ip_range}
        :param subnet: The subnet in CIDR form. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#subnet Network#subnet}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada63cfca148f922ac9d0c670260884470422079ed0076e36750bda662566b7b)
            check_type(argname="argument aux_address", value=aux_address, expected_type=type_hints["aux_address"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
            check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aux_address is not None:
            self._values["aux_address"] = aux_address
        if gateway is not None:
            self._values["gateway"] = gateway
        if ip_range is not None:
            self._values["ip_range"] = ip_range
        if subnet is not None:
            self._values["subnet"] = subnet

    @builtins.property
    def aux_address(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Auxiliary IPv4 or IPv6 addresses used by Network driver.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#aux_address Network#aux_address}
        '''
        result = self._values.get("aux_address")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def gateway(self) -> typing.Optional[builtins.str]:
        '''The IP address of the gateway.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#gateway Network#gateway}
        '''
        result = self._values.get("gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_range(self) -> typing.Optional[builtins.str]:
        '''The ip range in CIDR form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#ip_range Network#ip_range}
        '''
        result = self._values.get("ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet(self) -> typing.Optional[builtins.str]:
        '''The subnet in CIDR form.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#subnet Network#subnet}
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkIpamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkIpamConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.network.NetworkIpamConfigList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c579bab855c68996136d8ea1fa4814fdf80b76d4dc11fe14331a3ae5f142d9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkIpamConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a855205dd90564f01936b348f4ae9d511bdbb3d908543308716aa36c4ed47f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkIpamConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0982dfc3dc516fc7a359a356dfee7ad7b12c1969b0f804b326b1da2055edf47)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9937e0f2d6d72ccb08283e30ead2ce8e327ebefe7523b0dd70efc8c6e718cfb1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5be3233b89e1328ce23d014c70756bbfed0d25ec5010ec51af2280d948c0aa5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkIpamConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkIpamConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkIpamConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e08c6d388a0441abe018b94e224f12b1651dc02527856ed088118e09de72da06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class NetworkIpamConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.network.NetworkIpamConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe336ad54e95499fcc6b9b205ccb76d82b6bd88ec6ed0a7dfc3359675c64c90c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAuxAddress")
    def reset_aux_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuxAddress", []))

    @jsii.member(jsii_name="resetGateway")
    def reset_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGateway", []))

    @jsii.member(jsii_name="resetIpRange")
    def reset_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRange", []))

    @jsii.member(jsii_name="resetSubnet")
    def reset_subnet(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnet", []))

    @builtins.property
    @jsii.member(jsii_name="auxAddressInput")
    def aux_address_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "auxAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeInput")
    def ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetInput")
    def subnet_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetInput"))

    @builtins.property
    @jsii.member(jsii_name="auxAddress")
    def aux_address(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "auxAddress"))

    @aux_address.setter
    def aux_address(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b4ec522b31ae6163225b68e0e6184cd482c700d5a847bacc8acfa27e4952c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auxAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @gateway.setter
    def gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ca3a50e9ff68bcbba2ef1e551e02205e5fe530f80dc60fb7ba4605d7a83c5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gateway", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ipRange")
    def ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRange"))

    @ip_range.setter
    def ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6e0f94e7a91da17f1193b4762127f29b11a1585b9a0a2e51d5a6a87f099647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRange", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnet")
    def subnet(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnet"))

    @subnet.setter
    def subnet(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e72143d9bbf4b6c224363519cd414df0f4e6bbb0cdb6b7f8046d43ecb029183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkIpamConfig]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkIpamConfig]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkIpamConfig]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564cf3c3982c27711812a1c76bb8526b8e4e66904d8b416166898ac26c87e5f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.network.NetworkLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class NetworkLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#label Network#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#value Network#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913661dce3191eb13b579942f1150e128fd516402e24961a595cfca4826b4b29)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#label Network#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/network#value Network#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.network.NetworkLabelsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c5c9b4346f35d83534878420c6fee41b163577efaa16bfa8488c77f22443660)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NetworkLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071fab2f4f17922fb8724468504e13bf0ab8ed6b062175d7815faf34fa02085e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd9e940205a100f54600617722e4996741c175b9baae0a9286479d919a1f294)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e36b370a148e9f0f2671acb705e38566090317748c22fe9ba9ca01522701ed3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa4892f3cc01f3ae8cbdb830b5c09489dc2a4bcd2eff86df8c8a0e4e55397f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789c43e449b3e4f345f36cd84510c4f5a2437744328db96285249c42edb3e832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class NetworkLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.network.NetworkLabelsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__277e3a15b2882bfe4ac406393c5da47449f6e1c6fd076ab028afb30ba318d04e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5a67570907dc0574bdfd9659536b2582db762c377c4f2c635b54a0ed11eceae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c844e7aec8c5008b968fe92d93649e6f8f7295710e6d7f8e12f999c43220493a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9275833b0163651f35b89ac178775585ceb70089a6d13f43ac24f238d3cd053f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Network",
    "NetworkConfig",
    "NetworkIpamConfig",
    "NetworkIpamConfigList",
    "NetworkIpamConfigOutputReference",
    "NetworkLabels",
    "NetworkLabelsList",
    "NetworkLabelsOutputReference",
]

publication.publish()

def _typecheckingstub__218985ac8fc00a3223969045ccb0eb63761b5ea03d541fb9f4b707052a90ccdf(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    attachable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_duplicate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    driver: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ingress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    internal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ipam_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkIpamConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ipam_driver: typing.Optional[builtins.str] = None,
    ipam_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__b12b44e21f03ca40228f6b9cc51136bda0e663dfdf51112035762c32cf13eaec(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead55450684b75eb9e23b5d3558b9f468e1c3124e2e26d061c18512d2f149b98(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkIpamConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7ec1f3ce02fe104e53ae82a83c732f7d79b4e9fe5ef10d63b66a83737c1f59f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a291a759ab4d5010dac97cc4bca489634c3258bb8da94e2d611807fdf62f483(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89b8ea2a5238674aaa3b83b76951ead4045fe0954780f3a5505c651448e3b31(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a228670bbc8f68646d2222f6737a47649267a1b932f987f9f4b631f9ba381d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52052a2c0858cd004a33128e50c2ddb3d1b12e752f73e557374bae744823e14a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cde5a06ba7647b23b0afcbb63d2b9fc1524c886ee7c36dd11b4d95706a74b58(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24ace73edb9b86328ded7ff61fee3de2ab081ee54bb88f405f46f3423f36d02(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d7923fe07366174d5facc3f1dcd924c086b89c7312694a6891f009b5e10c9d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__864a05adce9583ca9fe91ee565291bf6e184c566a7a333a3565533c12bbd206b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5522b70a0a0e8f4b9d88c92861b6181183da3475ce31d8eca19180759a0e9220(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31242c5cfb673c1fac7d10fe18f1ec1717e92f065f27a9e8f5ecb28f6c2bc1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e138ada15241e75505611e6a6ae4e63284a5ecc0edab566574a70f172a5a8f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15458757b6822868c2d774eb993770ce2fea1779bf6a9ea52035e09761a45d0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    attachable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    check_duplicate: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    driver: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ingress: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    internal: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ipam_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkIpamConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ipam_driver: typing.Optional[builtins.str] = None,
    ipam_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ipv6: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NetworkLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada63cfca148f922ac9d0c670260884470422079ed0076e36750bda662566b7b(
    *,
    aux_address: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    gateway: typing.Optional[builtins.str] = None,
    ip_range: typing.Optional[builtins.str] = None,
    subnet: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c579bab855c68996136d8ea1fa4814fdf80b76d4dc11fe14331a3ae5f142d9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a855205dd90564f01936b348f4ae9d511bdbb3d908543308716aa36c4ed47f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0982dfc3dc516fc7a359a356dfee7ad7b12c1969b0f804b326b1da2055edf47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9937e0f2d6d72ccb08283e30ead2ce8e327ebefe7523b0dd70efc8c6e718cfb1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5be3233b89e1328ce23d014c70756bbfed0d25ec5010ec51af2280d948c0aa5e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08c6d388a0441abe018b94e224f12b1651dc02527856ed088118e09de72da06(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkIpamConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe336ad54e95499fcc6b9b205ccb76d82b6bd88ec6ed0a7dfc3359675c64c90c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b4ec522b31ae6163225b68e0e6184cd482c700d5a847bacc8acfa27e4952c9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ca3a50e9ff68bcbba2ef1e551e02205e5fe530f80dc60fb7ba4605d7a83c5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6e0f94e7a91da17f1193b4762127f29b11a1585b9a0a2e51d5a6a87f099647(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e72143d9bbf4b6c224363519cd414df0f4e6bbb0cdb6b7f8046d43ecb029183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564cf3c3982c27711812a1c76bb8526b8e4e66904d8b416166898ac26c87e5f7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkIpamConfig]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913661dce3191eb13b579942f1150e128fd516402e24961a595cfca4826b4b29(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5c9b4346f35d83534878420c6fee41b163577efaa16bfa8488c77f22443660(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071fab2f4f17922fb8724468504e13bf0ab8ed6b062175d7815faf34fa02085e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd9e940205a100f54600617722e4996741c175b9baae0a9286479d919a1f294(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e36b370a148e9f0f2671acb705e38566090317748c22fe9ba9ca01522701ed3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4892f3cc01f3ae8cbdb830b5c09489dc2a4bcd2eff86df8c8a0e4e55397f2d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789c43e449b3e4f345f36cd84510c4f5a2437744328db96285249c42edb3e832(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NetworkLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277e3a15b2882bfe4ac406393c5da47449f6e1c6fd076ab028afb30ba318d04e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a67570907dc0574bdfd9659536b2582db762c377c4f2c635b54a0ed11eceae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c844e7aec8c5008b968fe92d93649e6f8f7295710e6d7f8e12f999c43220493a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9275833b0163651f35b89ac178775585ceb70089a6d13f43ac24f238d3cd053f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, NetworkLabels]],
) -> None:
    """Type checking stubs"""
    pass
