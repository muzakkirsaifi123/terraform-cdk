r'''
# `docker_image`

Refer to the Terraform Registry for docs: [`docker_image`](https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image).
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


class Image(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.image.Image",
):
    '''Represents a {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image docker_image}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        build_attribute: typing.Optional[typing.Union["ImageBuild", typing.Dict[builtins.str, typing.Any]]] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keep_locally: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pull_trigger: typing.Optional[builtins.str] = None,
        pull_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image docker_image} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the Docker image, including any tags or SHA256 repo digests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#name Image#name}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build Image#build}
        :param force_remove: If true, then the image is removed forcibly when the resource is destroyed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        :param keep_locally: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker local storage on destroy operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#keep_locally Image#keep_locally}
        :param pull_trigger: A value which cause an image pull when changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_trigger Image#pull_trigger}
        :param pull_triggers: List of values which cause an image pull when changed. This is used to store the image digest from the registry when using the `docker_registry_image <../data-sources/registry_image.md>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_triggers Image#pull_triggers}
        :param triggers: A map of arbitrary strings that, when changed, will force the ``docker_image`` resource to be replaced. This can be used to rebuild an image when contents of source code folders change Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#triggers Image#triggers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee4c5b81d4f8b2e597fd1eb70503445c493b67c8ca8c24816e0908d3bd26d29)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ImageConfig(
            name=name,
            build_attribute=build_attribute,
            force_remove=force_remove,
            keep_locally=keep_locally,
            pull_trigger=pull_trigger,
            pull_triggers=pull_triggers,
            triggers=triggers,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a Image resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Image to import.
        :param import_from_id: The id of the existing Image that should be imported. Refer to the {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Image to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96730940723e4378cbad6ef291f3ccc3db496b1d472a365a076f3ab999c4a8e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putBuildAttribute")
    def put_build_attribute(
        self,
        *,
        path: builtins.str,
        build_arg: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        label: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Context path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#path Image#path}
        :param build_arg: Set build-time variables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build_arg Image#build_arg}
        :param dockerfile: Name of the Dockerfile. Defaults to ``Dockerfile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#dockerfile Image#dockerfile}
        :param force_remove: Always remove intermediate containers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        :param label: Set metadata for an image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#label Image#label}
        :param no_cache: Do not use cache when building the image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#no_cache Image#no_cache}
        :param remove: Remove intermediate containers after a successful build. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#remove Image#remove}
        :param tag: Name and optionally a tag in the 'name:tag' format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#tag Image#tag}
        :param target: Set the target build stage to build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#target Image#target}
        '''
        value = ImageBuild(
            path=path,
            build_arg=build_arg,
            dockerfile=dockerfile,
            force_remove=force_remove,
            label=label,
            no_cache=no_cache,
            remove=remove,
            tag=tag,
            target=target,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildAttribute", [value]))

    @jsii.member(jsii_name="resetBuildAttribute")
    def reset_build_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildAttribute", []))

    @jsii.member(jsii_name="resetForceRemove")
    def reset_force_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRemove", []))

    @jsii.member(jsii_name="resetKeepLocally")
    def reset_keep_locally(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepLocally", []))

    @jsii.member(jsii_name="resetPullTrigger")
    def reset_pull_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullTrigger", []))

    @jsii.member(jsii_name="resetPullTriggers")
    def reset_pull_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullTriggers", []))

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
    def build_attribute(self) -> "ImageBuildOutputReference":
        return typing.cast("ImageBuildOutputReference", jsii.get(self, "buildAttribute"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageId"))

    @builtins.property
    @jsii.member(jsii_name="latest")
    def latest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latest"))

    @builtins.property
    @jsii.member(jsii_name="output")
    def output(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "output"))

    @builtins.property
    @jsii.member(jsii_name="repoDigest")
    def repo_digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoDigest"))

    @builtins.property
    @jsii.member(jsii_name="buildAttributeInput")
    def build_attribute_input(self) -> typing.Optional["ImageBuild"]:
        return typing.cast(typing.Optional["ImageBuild"], jsii.get(self, "buildAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRemoveInput")
    def force_remove_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="keepLocallyInput")
    def keep_locally_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "keepLocallyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pullTriggerInput")
    def pull_trigger_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pullTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="pullTriggersInput")
    def pull_triggers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pullTriggersInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d133e0e50957ac9028501dc5eb1f9c2b4ba054bcc33de4818f21bd20957690a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRemove", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="keepLocally")
    def keep_locally(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "keepLocally"))

    @keep_locally.setter
    def keep_locally(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__171789a0eb7e9a6d9eb8d87339fc389e94075d842339f92518e9863238c76631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepLocally", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13a087b0a9bf3c4fb2f55692dfd498fd24e9cff3a71a0e66df369801cc2ccb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pullTrigger")
    def pull_trigger(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pullTrigger"))

    @pull_trigger.setter
    def pull_trigger(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38923360e50f19d7f267addc041302a5d5e02c246877bbeaa48afa8363d401f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullTrigger", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pullTriggers")
    def pull_triggers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pullTriggers"))

    @pull_triggers.setter
    def pull_triggers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a49a2b1bc8a971261b1931fa27aa21180c43bc4163f113da1efbe87eedf60dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullTriggers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c6982908cf05288d1f8567076a2c9494cedf9061071b61fd7e93ee2c864453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.image.ImageBuild",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "build_arg": "buildArg",
        "dockerfile": "dockerfile",
        "force_remove": "forceRemove",
        "label": "label",
        "no_cache": "noCache",
        "remove": "remove",
        "tag": "tag",
        "target": "target",
    },
)
class ImageBuild:
    def __init__(
        self,
        *,
        path: builtins.str,
        build_arg: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        label: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tag: typing.Optional[typing.Sequence[builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Context path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#path Image#path}
        :param build_arg: Set build-time variables. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build_arg Image#build_arg}
        :param dockerfile: Name of the Dockerfile. Defaults to ``Dockerfile``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#dockerfile Image#dockerfile}
        :param force_remove: Always remove intermediate containers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        :param label: Set metadata for an image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#label Image#label}
        :param no_cache: Do not use cache when building the image. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#no_cache Image#no_cache}
        :param remove: Remove intermediate containers after a successful build. Defaults to ``true``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#remove Image#remove}
        :param tag: Name and optionally a tag in the 'name:tag' format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#tag Image#tag}
        :param target: Set the target build stage to build. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#target Image#target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__513cd8bbbdd0d1d5e03cdbfeed95b8fa6c48f2c4e9d0c5b7b07f31b626d6a55e)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument build_arg", value=build_arg, expected_type=type_hints["build_arg"])
            check_type(argname="argument dockerfile", value=dockerfile, expected_type=type_hints["dockerfile"])
            check_type(argname="argument force_remove", value=force_remove, expected_type=type_hints["force_remove"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument no_cache", value=no_cache, expected_type=type_hints["no_cache"])
            check_type(argname="argument remove", value=remove, expected_type=type_hints["remove"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }
        if build_arg is not None:
            self._values["build_arg"] = build_arg
        if dockerfile is not None:
            self._values["dockerfile"] = dockerfile
        if force_remove is not None:
            self._values["force_remove"] = force_remove
        if label is not None:
            self._values["label"] = label
        if no_cache is not None:
            self._values["no_cache"] = no_cache
        if remove is not None:
            self._values["remove"] = remove
        if tag is not None:
            self._values["tag"] = tag
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def path(self) -> builtins.str:
        '''Context path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#path Image#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_arg(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Set build-time variables.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build_arg Image#build_arg}
        '''
        result = self._values.get("build_arg")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def dockerfile(self) -> typing.Optional[builtins.str]:
        '''Name of the Dockerfile. Defaults to ``Dockerfile``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#dockerfile Image#dockerfile}
        '''
        result = self._values.get("dockerfile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_remove(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Always remove intermediate containers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        '''
        result = self._values.get("force_remove")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def label(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Set metadata for an image.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#label Image#label}
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def no_cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Do not use cache when building the image.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#no_cache Image#no_cache}
        '''
        result = self._values.get("no_cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def remove(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Remove intermediate containers after a successful build. Defaults to  ``true``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#remove Image#remove}
        '''
        result = self._values.get("remove")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Name and optionally a tag in the 'name:tag' format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#tag Image#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Set the target build stage to build.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#target Image#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageBuildOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.image.ImageBuildOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12758a96736c9de8ec905bfba980c60722baae6dba1b1e723159f11868df0273)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuildArg")
    def reset_build_arg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildArg", []))

    @jsii.member(jsii_name="resetDockerfile")
    def reset_dockerfile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfile", []))

    @jsii.member(jsii_name="resetForceRemove")
    def reset_force_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRemove", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetNoCache")
    def reset_no_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoCache", []))

    @jsii.member(jsii_name="resetRemove")
    def reset_remove(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemove", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="buildArgInput")
    def build_arg_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "buildArgInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfileInput")
    def dockerfile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRemoveInput")
    def force_remove_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceRemoveInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="noCacheInput")
    def no_cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="removeInput")
    def remove_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "removeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="buildArg")
    def build_arg(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "buildArg"))

    @build_arg.setter
    def build_arg(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4398fc3a290cca70ecd9fcc0dc2778c22595b8b8297532ba6dfe60cafb42869d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildArg", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dockerfile")
    def dockerfile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfile"))

    @dockerfile.setter
    def dockerfile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a329881e7b5e90c5a4fd638ca7f6ae6bc1f57048f51c2f02285eb1bff89c0fb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfile", value) # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__597e201629d9283317c54d193ca2c1c08b7f6acf9b902c385f52782c05eb4596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRemove", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "label"))

    @label.setter
    def label(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbaeea8f1e67077f722c61929ee85ad7baf4b5efd0c5af97b9ce5b390ebedcab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__219566f27fa38b086ba39335fef2e4c9ee40c5665f0291111725e7c6ba6c7656)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noCache", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a1d1c6b4283dbeebfd8fb6dfb99a89df99e2455a6d7a00486f3f4eab69f1240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value) # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__34cdb0968f56c2f76c06b59c69f442466412150a48dcc62b454cc1aef7043974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remove", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341f100aaab81d00641fb6d32a2e53854790818cbaa00dd1cb3f49e356972817)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ffc04a701798fe9139985c792c02eea29a025f479305afd239c1f39ee8d8c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ImageBuild]:
        return typing.cast(typing.Optional[ImageBuild], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ImageBuild]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d66a6281340c2d2261771197dbc3cdfeb0cf42b8863aca0a3a419413e340e49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.image.ImageConfig",
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
        "force_remove": "forceRemove",
        "keep_locally": "keepLocally",
        "pull_trigger": "pullTrigger",
        "pull_triggers": "pullTriggers",
        "triggers": "triggers",
    },
)
class ImageConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        build_attribute: typing.Optional[typing.Union[ImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
        force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        keep_locally: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        pull_trigger: typing.Optional[builtins.str] = None,
        pull_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param name: The name of the Docker image, including any tags or SHA256 repo digests. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#name Image#name}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build Image#build}
        :param force_remove: If true, then the image is removed forcibly when the resource is destroyed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        :param keep_locally: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker local storage on destroy operation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#keep_locally Image#keep_locally}
        :param pull_trigger: A value which cause an image pull when changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_trigger Image#pull_trigger}
        :param pull_triggers: List of values which cause an image pull when changed. This is used to store the image digest from the registry when using the `docker_registry_image <../data-sources/registry_image.md>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_triggers Image#pull_triggers}
        :param triggers: A map of arbitrary strings that, when changed, will force the ``docker_image`` resource to be replaced. This can be used to rebuild an image when contents of source code folders change Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#triggers Image#triggers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(build_attribute, dict):
            build_attribute = ImageBuild(**build_attribute)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5b0051fa9d0362e01ba9aad84d4dd93c9cc37f8ea599e35c77782ff74e6023)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument build_attribute", value=build_attribute, expected_type=type_hints["build_attribute"])
            check_type(argname="argument force_remove", value=force_remove, expected_type=type_hints["force_remove"])
            check_type(argname="argument keep_locally", value=keep_locally, expected_type=type_hints["keep_locally"])
            check_type(argname="argument pull_trigger", value=pull_trigger, expected_type=type_hints["pull_trigger"])
            check_type(argname="argument pull_triggers", value=pull_triggers, expected_type=type_hints["pull_triggers"])
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
        if force_remove is not None:
            self._values["force_remove"] = force_remove
        if keep_locally is not None:
            self._values["keep_locally"] = keep_locally
        if pull_trigger is not None:
            self._values["pull_trigger"] = pull_trigger
        if pull_triggers is not None:
            self._values["pull_triggers"] = pull_triggers
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
        '''The name of the Docker image, including any tags or SHA256 repo digests.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#name Image#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_attribute(self) -> typing.Optional[ImageBuild]:
        '''build block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#build Image#build}
        '''
        result = self._values.get("build_attribute")
        return typing.cast(typing.Optional[ImageBuild], result)

    @builtins.property
    def force_remove(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, then the image is removed forcibly when the resource is destroyed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#force_remove Image#force_remove}
        '''
        result = self._values.get("force_remove")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def keep_locally(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''If true, then the Docker image won't be deleted on destroy operation.

        If this is false, it will delete the image from the docker local storage on destroy operation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#keep_locally Image#keep_locally}
        '''
        result = self._values.get("keep_locally")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def pull_trigger(self) -> typing.Optional[builtins.str]:
        '''A value which cause an image pull when changed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_trigger Image#pull_trigger}
        '''
        result = self._values.get("pull_trigger")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of values which cause an image pull when changed.

        This is used to store the image digest from the registry when using the `docker_registry_image <../data-sources/registry_image.md>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#pull_triggers Image#pull_triggers}
        '''
        result = self._values.get("pull_triggers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of arbitrary strings that, when changed, will force the ``docker_image`` resource to be replaced.

        This can be used to rebuild an image when contents of source code folders change

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/image#triggers Image#triggers}
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Image",
    "ImageBuild",
    "ImageBuildOutputReference",
    "ImageConfig",
]

publication.publish()

def _typecheckingstub__9ee4c5b81d4f8b2e597fd1eb70503445c493b67c8ca8c24816e0908d3bd26d29(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    build_attribute: typing.Optional[typing.Union[ImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
    force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    keep_locally: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pull_trigger: typing.Optional[builtins.str] = None,
    pull_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__e96730940723e4378cbad6ef291f3ccc3db496b1d472a365a076f3ab999c4a8e(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d133e0e50957ac9028501dc5eb1f9c2b4ba054bcc33de4818f21bd20957690a5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171789a0eb7e9a6d9eb8d87339fc389e94075d842339f92518e9863238c76631(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13a087b0a9bf3c4fb2f55692dfd498fd24e9cff3a71a0e66df369801cc2ccb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38923360e50f19d7f267addc041302a5d5e02c246877bbeaa48afa8363d401f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a49a2b1bc8a971261b1931fa27aa21180c43bc4163f113da1efbe87eedf60dd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c6982908cf05288d1f8567076a2c9494cedf9061071b61fd7e93ee2c864453(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__513cd8bbbdd0d1d5e03cdbfeed95b8fa6c48f2c4e9d0c5b7b07f31b626d6a55e(
    *,
    path: builtins.str,
    build_arg: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    dockerfile: typing.Optional[builtins.str] = None,
    force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    label: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    no_cache: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tag: typing.Optional[typing.Sequence[builtins.str]] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12758a96736c9de8ec905bfba980c60722baae6dba1b1e723159f11868df0273(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4398fc3a290cca70ecd9fcc0dc2778c22595b8b8297532ba6dfe60cafb42869d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a329881e7b5e90c5a4fd638ca7f6ae6bc1f57048f51c2f02285eb1bff89c0fb4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597e201629d9283317c54d193ca2c1c08b7f6acf9b902c385f52782c05eb4596(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbaeea8f1e67077f722c61929ee85ad7baf4b5efd0c5af97b9ce5b390ebedcab(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__219566f27fa38b086ba39335fef2e4c9ee40c5665f0291111725e7c6ba6c7656(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1d1c6b4283dbeebfd8fb6dfb99a89df99e2455a6d7a00486f3f4eab69f1240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34cdb0968f56c2f76c06b59c69f442466412150a48dcc62b454cc1aef7043974(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341f100aaab81d00641fb6d32a2e53854790818cbaa00dd1cb3f49e356972817(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ffc04a701798fe9139985c792c02eea29a025f479305afd239c1f39ee8d8c88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d66a6281340c2d2261771197dbc3cdfeb0cf42b8863aca0a3a419413e340e49(
    value: typing.Optional[ImageBuild],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5b0051fa9d0362e01ba9aad84d4dd93c9cc37f8ea599e35c77782ff74e6023(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    build_attribute: typing.Optional[typing.Union[ImageBuild, typing.Dict[builtins.str, typing.Any]]] = None,
    force_remove: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    keep_locally: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    pull_trigger: typing.Optional[builtins.str] = None,
    pull_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
