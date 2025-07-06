r'''
# `docker_service`

Refer to the Terraform Registry for docs: [`docker_service`](https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service).
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


class Service(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.Service",
):
    '''Represents a {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service docker_service}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        task_spec: typing.Union["ServiceTaskSpec", typing.Dict[builtins.str, typing.Any]],
        auth: typing.Optional[typing.Union["ServiceAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        converge_config: typing.Optional[typing.Union["ServiceConvergeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        endpoint_spec: typing.Optional[typing.Union["ServiceEndpointSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mode: typing.Optional[typing.Union["ServiceMode", typing.Dict[builtins.str, typing.Any]]] = None,
        rollback_config: typing.Optional[typing.Union["ServiceRollbackConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        update_config: typing.Optional[typing.Union["ServiceUpdateConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service docker_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        :param task_spec: task_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#task_spec Service#task_spec}
        :param auth: auth block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#auth Service#auth}
        :param converge_config: converge_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#converge_config Service#converge_config}
        :param endpoint_spec: endpoint_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#endpoint_spec Service#endpoint_spec}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#id Service#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param mode: mode block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param rollback_config: rollback_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#rollback_config Service#rollback_config}
        :param update_config: update_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#update_config Service#update_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c6848e96b699a6cc01123087da0a7f73c40f029660d845330d762845f15058f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceConfig(
            name=name,
            task_spec=task_spec,
            auth=auth,
            converge_config=converge_config,
            endpoint_spec=endpoint_spec,
            id=id,
            labels=labels,
            mode=mode,
            rollback_config=rollback_config,
            update_config=update_config,
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
        '''Generates CDKTF code for importing a Service resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Service to import.
        :param import_from_id: The id of the existing Service that should be imported. Refer to the {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Service to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c841ce0d32a20dcd698ed9f78fc3a30ad1091aec6726fab796716c3502f446)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        *,
        server_address: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_address: The address of the server for the authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#server_address Service#server_address}
        :param password: The password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#password Service#password}
        :param username: The username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#username Service#username}
        '''
        value = ServiceAuth(
            server_address=server_address, password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="putConvergeConfig")
    def put_converge_config(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delay: The interval to check if the desired state is reached ``(ms|s)``. Defaults to ``7s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param timeout: The timeout of the service to reach the desired state ``(s|m)``. Defaults to ``3m``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        value = ServiceConvergeConfig(delay=delay, timeout=timeout)

        return typing.cast(None, jsii.invoke(self, "putConvergeConfig", [value]))

    @jsii.member(jsii_name="putEndpointSpec")
    def put_endpoint_spec(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceEndpointSpecPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param mode: The mode of resolution to use for internal load balancing between tasks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#ports Service#ports}
        '''
        value = ServiceEndpointSpec(mode=mode, ports=ports)

        return typing.cast(None, jsii.invoke(self, "putEndpointSpec", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceLabels", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9101889c65e8900e7754ba448261b2a93c073a52fab240ee8feb049f349bb4b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="putMode")
    def put_mode(
        self,
        *,
        global_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replicated: typing.Optional[typing.Union["ServiceModeReplicated", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param global_: The global service mode. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#global Service#global}
        :param replicated: replicated block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicated Service#replicated}
        '''
        value = ServiceMode(global_=global_, replicated=replicated)

        return typing.cast(None, jsii.invoke(self, "putMode", [value]))

    @jsii.member(jsii_name="putRollbackConfig")
    def put_rollback_config(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        failure_action: typing.Optional[builtins.str] = None,
        max_failure_ratio: typing.Optional[builtins.str] = None,
        monitor: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
        parallelism: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delay: Delay between task rollbacks (ns|us|ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param failure_action: Action on rollback failure: pause | continue. Defaults to ``pause``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        :param max_failure_ratio: Failure rate to tolerate during a rollback. Defaults to ``0.0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        :param monitor: Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        :param order: Rollback order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        :param parallelism: Maximum number of tasks to be rollbacked in one iteration. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        value = ServiceRollbackConfig(
            delay=delay,
            failure_action=failure_action,
            max_failure_ratio=max_failure_ratio,
            monitor=monitor,
            order=order,
            parallelism=parallelism,
        )

        return typing.cast(None, jsii.invoke(self, "putRollbackConfig", [value]))

    @jsii.member(jsii_name="putTaskSpec")
    def put_task_spec(
        self,
        *,
        container_spec: typing.Union["ServiceTaskSpecContainerSpec", typing.Dict[builtins.str, typing.Any]],
        force_update: typing.Optional[jsii.Number] = None,
        log_driver: typing.Optional[typing.Union["ServiceTaskSpecLogDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        placement: typing.Optional[typing.Union["ServiceTaskSpecPlacement", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["ServiceTaskSpecResources", typing.Dict[builtins.str, typing.Any]]] = None,
        restart_policy: typing.Optional[typing.Union["ServiceTaskSpecRestartPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_spec: container_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#container_spec Service#container_spec}
        :param force_update: A counter that triggers an update even if no relevant parameters have been changed. See the `spec <https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#force_update Service#force_update}
        :param log_driver: log_driver block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#log_driver Service#log_driver}
        :param networks: Ids of the networks in which the container will be put in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#networks Service#networks}
        :param placement: placement block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#placement Service#placement}
        :param resources: resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#resources Service#resources}
        :param restart_policy: restart_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#restart_policy Service#restart_policy}
        :param runtime: Runtime is the type of runtime specified for the task executor. See the `types <https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#runtime Service#runtime}
        '''
        value = ServiceTaskSpec(
            container_spec=container_spec,
            force_update=force_update,
            log_driver=log_driver,
            networks=networks,
            placement=placement,
            resources=resources,
            restart_policy=restart_policy,
            runtime=runtime,
        )

        return typing.cast(None, jsii.invoke(self, "putTaskSpec", [value]))

    @jsii.member(jsii_name="putUpdateConfig")
    def put_update_config(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        failure_action: typing.Optional[builtins.str] = None,
        max_failure_ratio: typing.Optional[builtins.str] = None,
        monitor: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
        parallelism: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delay: Delay between task updates ``(ns|us|ms|s|m|h)``. Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param failure_action: Action on update failure: ``pause``, ``continue`` or ``rollback``. Defaults to ``pause``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        :param max_failure_ratio: Failure rate to tolerate during an update. Defaults to ``0.0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        :param monitor: Duration after each task update to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        :param order: Update order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        :param parallelism: Maximum number of tasks to be updated in one iteration. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        value = ServiceUpdateConfig(
            delay=delay,
            failure_action=failure_action,
            max_failure_ratio=max_failure_ratio,
            monitor=monitor,
            order=order,
            parallelism=parallelism,
        )

        return typing.cast(None, jsii.invoke(self, "putUpdateConfig", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetConvergeConfig")
    def reset_converge_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConvergeConfig", []))

    @jsii.member(jsii_name="resetEndpointSpec")
    def reset_endpoint_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointSpec", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetRollbackConfig")
    def reset_rollback_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollbackConfig", []))

    @jsii.member(jsii_name="resetUpdateConfig")
    def reset_update_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdateConfig", []))

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
    @jsii.member(jsii_name="auth")
    def auth(self) -> "ServiceAuthOutputReference":
        return typing.cast("ServiceAuthOutputReference", jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="convergeConfig")
    def converge_config(self) -> "ServiceConvergeConfigOutputReference":
        return typing.cast("ServiceConvergeConfigOutputReference", jsii.get(self, "convergeConfig"))

    @builtins.property
    @jsii.member(jsii_name="endpointSpec")
    def endpoint_spec(self) -> "ServiceEndpointSpecOutputReference":
        return typing.cast("ServiceEndpointSpecOutputReference", jsii.get(self, "endpointSpec"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> "ServiceLabelsList":
        return typing.cast("ServiceLabelsList", jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> "ServiceModeOutputReference":
        return typing.cast("ServiceModeOutputReference", jsii.get(self, "mode"))

    @builtins.property
    @jsii.member(jsii_name="rollbackConfig")
    def rollback_config(self) -> "ServiceRollbackConfigOutputReference":
        return typing.cast("ServiceRollbackConfigOutputReference", jsii.get(self, "rollbackConfig"))

    @builtins.property
    @jsii.member(jsii_name="taskSpec")
    def task_spec(self) -> "ServiceTaskSpecOutputReference":
        return typing.cast("ServiceTaskSpecOutputReference", jsii.get(self, "taskSpec"))

    @builtins.property
    @jsii.member(jsii_name="updateConfig")
    def update_config(self) -> "ServiceUpdateConfigOutputReference":
        return typing.cast("ServiceUpdateConfigOutputReference", jsii.get(self, "updateConfig"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional["ServiceAuth"]:
        return typing.cast(typing.Optional["ServiceAuth"], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="convergeConfigInput")
    def converge_config_input(self) -> typing.Optional["ServiceConvergeConfig"]:
        return typing.cast(typing.Optional["ServiceConvergeConfig"], jsii.get(self, "convergeConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointSpecInput")
    def endpoint_spec_input(self) -> typing.Optional["ServiceEndpointSpec"]:
        return typing.cast(typing.Optional["ServiceEndpointSpec"], jsii.get(self, "endpointSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceLabels"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceLabels"]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional["ServiceMode"]:
        return typing.cast(typing.Optional["ServiceMode"], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackConfigInput")
    def rollback_config_input(self) -> typing.Optional["ServiceRollbackConfig"]:
        return typing.cast(typing.Optional["ServiceRollbackConfig"], jsii.get(self, "rollbackConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="taskSpecInput")
    def task_spec_input(self) -> typing.Optional["ServiceTaskSpec"]:
        return typing.cast(typing.Optional["ServiceTaskSpec"], jsii.get(self, "taskSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="updateConfigInput")
    def update_config_input(self) -> typing.Optional["ServiceUpdateConfig"]:
        return typing.cast(typing.Optional["ServiceUpdateConfig"], jsii.get(self, "updateConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__525bcd2ae62ead591721e6dd219a1196b02fd45a6bb4da60e7cfe03279dfab5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab347ff274a6e46ce8c2f2aad29e7c579a777117c9ce4adacbf2b67eee8f9f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceAuth",
    jsii_struct_bases=[],
    name_mapping={
        "server_address": "serverAddress",
        "password": "password",
        "username": "username",
    },
)
class ServiceAuth:
    def __init__(
        self,
        *,
        server_address: builtins.str,
        password: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_address: The address of the server for the authentication. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#server_address Service#server_address}
        :param password: The password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#password Service#password}
        :param username: The username. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#username Service#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2732a09d18600575e862c7e1f903f1234f3db88c5561209ba580772f0d01b7a1)
            check_type(argname="argument server_address", value=server_address, expected_type=type_hints["server_address"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "server_address": server_address,
        }
        if password is not None:
            self._values["password"] = password
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def server_address(self) -> builtins.str:
        '''The address of the server for the authentication.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#server_address Service#server_address}
        '''
        result = self._values.get("server_address")
        assert result is not None, "Required property 'server_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#password Service#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#username Service#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceAuthOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9947af8f1cedb509fd0a41bab6ad14cef842460f57dd079a2adc9cb5c17e389)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="serverAddressInput")
    def server_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d07dd7d2579e8bbd83d25a2c36a7197aa2d72c81b1bc6a5ce567b5f90f257c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverAddress")
    def server_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverAddress"))

    @server_address.setter
    def server_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8ff0da173877f09a3a8c68b1028b4d65bd7bbe779417daf3cb69037437f0ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b287afbd961f1d7c75f000e96d72a7b0e17a5bcb8d77f4ff5e5f68c437768d8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceAuth]:
        return typing.cast(typing.Optional[ServiceAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceAuth]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450cfbd5cf2a1f27f7ffd091db5d919572e393231ed93150148eb06d5abec262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceConfig",
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
        "task_spec": "taskSpec",
        "auth": "auth",
        "converge_config": "convergeConfig",
        "endpoint_spec": "endpointSpec",
        "id": "id",
        "labels": "labels",
        "mode": "mode",
        "rollback_config": "rollbackConfig",
        "update_config": "updateConfig",
    },
)
class ServiceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        task_spec: typing.Union["ServiceTaskSpec", typing.Dict[builtins.str, typing.Any]],
        auth: typing.Optional[typing.Union[ServiceAuth, typing.Dict[builtins.str, typing.Any]]] = None,
        converge_config: typing.Optional[typing.Union["ServiceConvergeConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        endpoint_spec: typing.Optional[typing.Union["ServiceEndpointSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mode: typing.Optional[typing.Union["ServiceMode", typing.Dict[builtins.str, typing.Any]]] = None,
        rollback_config: typing.Optional[typing.Union["ServiceRollbackConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        update_config: typing.Optional[typing.Union["ServiceUpdateConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        :param task_spec: task_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#task_spec Service#task_spec}
        :param auth: auth block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#auth Service#auth}
        :param converge_config: converge_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#converge_config Service#converge_config}
        :param endpoint_spec: endpoint_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#endpoint_spec Service#endpoint_spec}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#id Service#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param mode: mode block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param rollback_config: rollback_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#rollback_config Service#rollback_config}
        :param update_config: update_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#update_config Service#update_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(task_spec, dict):
            task_spec = ServiceTaskSpec(**task_spec)
        if isinstance(auth, dict):
            auth = ServiceAuth(**auth)
        if isinstance(converge_config, dict):
            converge_config = ServiceConvergeConfig(**converge_config)
        if isinstance(endpoint_spec, dict):
            endpoint_spec = ServiceEndpointSpec(**endpoint_spec)
        if isinstance(mode, dict):
            mode = ServiceMode(**mode)
        if isinstance(rollback_config, dict):
            rollback_config = ServiceRollbackConfig(**rollback_config)
        if isinstance(update_config, dict):
            update_config = ServiceUpdateConfig(**update_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592645dea33e425062a305c3d1d79325599cfe63b22b3969f6aa6671a824d114)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument task_spec", value=task_spec, expected_type=type_hints["task_spec"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument converge_config", value=converge_config, expected_type=type_hints["converge_config"])
            check_type(argname="argument endpoint_spec", value=endpoint_spec, expected_type=type_hints["endpoint_spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument rollback_config", value=rollback_config, expected_type=type_hints["rollback_config"])
            check_type(argname="argument update_config", value=update_config, expected_type=type_hints["update_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "task_spec": task_spec,
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
        if auth is not None:
            self._values["auth"] = auth
        if converge_config is not None:
            self._values["converge_config"] = converge_config
        if endpoint_spec is not None:
            self._values["endpoint_spec"] = endpoint_spec
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if mode is not None:
            self._values["mode"] = mode
        if rollback_config is not None:
            self._values["rollback_config"] = rollback_config
        if update_config is not None:
            self._values["update_config"] = update_config

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
        '''Name of the service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_spec(self) -> "ServiceTaskSpec":
        '''task_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#task_spec Service#task_spec}
        '''
        result = self._values.get("task_spec")
        assert result is not None, "Required property 'task_spec' is missing"
        return typing.cast("ServiceTaskSpec", result)

    @builtins.property
    def auth(self) -> typing.Optional[ServiceAuth]:
        '''auth block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#auth Service#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[ServiceAuth], result)

    @builtins.property
    def converge_config(self) -> typing.Optional["ServiceConvergeConfig"]:
        '''converge_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#converge_config Service#converge_config}
        '''
        result = self._values.get("converge_config")
        return typing.cast(typing.Optional["ServiceConvergeConfig"], result)

    @builtins.property
    def endpoint_spec(self) -> typing.Optional["ServiceEndpointSpec"]:
        '''endpoint_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#endpoint_spec Service#endpoint_spec}
        '''
        result = self._values.get("endpoint_spec")
        return typing.cast(typing.Optional["ServiceEndpointSpec"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#id Service#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceLabels"]]], result)

    @builtins.property
    def mode(self) -> typing.Optional["ServiceMode"]:
        '''mode block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional["ServiceMode"], result)

    @builtins.property
    def rollback_config(self) -> typing.Optional["ServiceRollbackConfig"]:
        '''rollback_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#rollback_config Service#rollback_config}
        '''
        result = self._values.get("rollback_config")
        return typing.cast(typing.Optional["ServiceRollbackConfig"], result)

    @builtins.property
    def update_config(self) -> typing.Optional["ServiceUpdateConfig"]:
        '''update_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#update_config Service#update_config}
        '''
        result = self._values.get("update_config")
        return typing.cast(typing.Optional["ServiceUpdateConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceConvergeConfig",
    jsii_struct_bases=[],
    name_mapping={"delay": "delay", "timeout": "timeout"},
)
class ServiceConvergeConfig:
    def __init__(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delay: The interval to check if the desired state is reached ``(ms|s)``. Defaults to ``7s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param timeout: The timeout of the service to reach the desired state ``(s|m)``. Defaults to ``3m``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c0bdc25c51e0363f4174971e3e443ea09f15b95591bd2cf166063400394860)
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delay is not None:
            self._values["delay"] = delay
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def delay(self) -> typing.Optional[builtins.str]:
        '''The interval to check if the desired state is reached ``(ms|s)``. Defaults to ``7s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''The timeout of the service to reach the desired state ``(s|m)``. Defaults to ``3m``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceConvergeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceConvergeConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceConvergeConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4cc6bb981f239c9b5bcdf366b859cef004ff3c9a9accd0fa854f9b3a1f29189)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1431fa879200c8b0cbb8dbc05b78ebb63f33e5a29210f0ce2f2ea1d12cb92bd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07bbda935240a162ab678096d6a390106281be87dbc50cef36add9fac2f97f6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceConvergeConfig]:
        return typing.cast(typing.Optional[ServiceConvergeConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceConvergeConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb46b18d28a763749bb6a116c4c622e0108b8860f6d54600973e98afc6be8f6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceEndpointSpec",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "ports": "ports"},
)
class ServiceEndpointSpec:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceEndpointSpecPorts", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param mode: The mode of resolution to use for internal load balancing between tasks. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param ports: ports block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#ports Service#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01234264d9f7a98704f7877e505807fe35ea6b4ba74a410d0945d5af3cd33220)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''The mode of resolution to use for internal load balancing between tasks.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ports(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceEndpointSpecPorts"]]]:
        '''ports block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#ports Service#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceEndpointSpecPorts"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEndpointSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEndpointSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceEndpointSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ebfd458f24d15529a4cb1480cc779c0f8775ce35ae38cf1a7e5441419763cfb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPorts")
    def put_ports(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceEndpointSpecPorts", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3222ece2ee7c3c065acf8dfc94826e8d8107b7f1983cbf2ab2448b9956f831c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPorts", [value]))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> "ServiceEndpointSpecPortsList":
        return typing.cast("ServiceEndpointSpecPortsList", jsii.get(self, "ports"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceEndpointSpecPorts"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceEndpointSpecPorts"]]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3583440fc6e22cf3b2afa8e6824f5c30d81f9bcf85a67aaab4d2089ab50dab5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceEndpointSpec]:
        return typing.cast(typing.Optional[ServiceEndpointSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceEndpointSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb97cc8bfc4b0d5444759b601b656b34410c1efdc35f9553b87b95094d2b259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceEndpointSpecPorts",
    jsii_struct_bases=[],
    name_mapping={
        "target_port": "targetPort",
        "name": "name",
        "protocol": "protocol",
        "published_port": "publishedPort",
        "publish_mode": "publishMode",
    },
)
class ServiceEndpointSpecPorts:
    def __init__(
        self,
        *,
        target_port: jsii.Number,
        name: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        published_port: typing.Optional[jsii.Number] = None,
        publish_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target_port: The port inside the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#target_port Service#target_port}
        :param name: A random name for the port. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        :param protocol: Rrepresents the protocol of a port: ``tcp``, ``udp`` or ``sctp``. Defaults to ``tcp``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#protocol Service#protocol}
        :param published_port: The port on the swarm hosts. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#published_port Service#published_port}
        :param publish_mode: Represents the mode in which the port is to be published: 'ingress' or 'host'. Defaults to ``ingress``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#publish_mode Service#publish_mode}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081c511e9919d97caf957bc62b7f0db6a9e9f88f925a51baf4a87b223e670471)
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument published_port", value=published_port, expected_type=type_hints["published_port"])
            check_type(argname="argument publish_mode", value=publish_mode, expected_type=type_hints["publish_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_port": target_port,
        }
        if name is not None:
            self._values["name"] = name
        if protocol is not None:
            self._values["protocol"] = protocol
        if published_port is not None:
            self._values["published_port"] = published_port
        if publish_mode is not None:
            self._values["publish_mode"] = publish_mode

    @builtins.property
    def target_port(self) -> jsii.Number:
        '''The port inside the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#target_port Service#target_port}
        '''
        result = self._values.get("target_port")
        assert result is not None, "Required property 'target_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A random name for the port.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Rrepresents the protocol of a port: ``tcp``, ``udp`` or ``sctp``. Defaults to ``tcp``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#protocol Service#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def published_port(self) -> typing.Optional[jsii.Number]:
        '''The port on the swarm hosts.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#published_port Service#published_port}
        '''
        result = self._values.get("published_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def publish_mode(self) -> typing.Optional[builtins.str]:
        '''Represents the mode in which the port is to be published: 'ingress' or 'host'. Defaults to ``ingress``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#publish_mode Service#publish_mode}
        '''
        result = self._values.get("publish_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEndpointSpecPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEndpointSpecPortsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceEndpointSpecPortsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53209f8baeb535250ce84bceb9826bdecd4589fe50e0d4a6ee2ca41908c3d39d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceEndpointSpecPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05dcacdb60c2c6748c027133114df5e89053e729f7584d072be646c9208dbae9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEndpointSpecPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ce50b001829f095e603454c347c3210c24b6c1aa894a0ded37b073421272312)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57bafc9e30637080998304a82fc675b10e5d17351a10412bb8393aa6e2b4b804)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c4bc8e7cfba3d5fa85e001c581ee9c1043d23712e721741d7672470cf06ddcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceEndpointSpecPorts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceEndpointSpecPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceEndpointSpecPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec0ab09844fa7f0cb551f85eb7948767fc082af1c0bb47870988c514eab366cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceEndpointSpecPortsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceEndpointSpecPortsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36cd644d1820367c5b00598d3be854da0a5f67e06346ee7ea234f08915cc1272)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetPublishedPort")
    def reset_published_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishedPort", []))

    @jsii.member(jsii_name="resetPublishMode")
    def reset_publish_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublishMode", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="publishedPortInput")
    def published_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "publishedPortInput"))

    @builtins.property
    @jsii.member(jsii_name="publishModeInput")
    def publish_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publishModeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortInput")
    def target_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetPortInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7475c43347a92c1bd67cc82d83a709a3d402e9ccb04a6b79b2ef8291008703f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__024c24cdb669f3980db549ac09cd88d03eb3660d139d0283294d0d3cdd765c6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publishedPort")
    def published_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "publishedPort"))

    @published_port.setter
    def published_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d69105aafce5dbb5b5416af8d5749ee93ecaef9a709b2f27d283bb9688895d1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishedPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publishMode")
    def publish_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publishMode"))

    @publish_mode.setter
    def publish_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0036e1c0ca77c3ecc5a6a1b9f0a7ceb806cea7e4fe1c184672311b147a37747b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetPort")
    def target_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetPort"))

    @target_port.setter
    def target_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c558cd534fe39a994bc4e51e8440e8145fa0721c351daeb2c56a4b7d5217d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceEndpointSpecPorts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceEndpointSpecPorts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceEndpointSpecPorts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed29e82d8eb700d8a424834c4b4fde52093fbf3984ba3185bfaf04b03c25fa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ServiceLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48f4b893185d26d8c69741ea68ca2dd0ba0276381abed6d0084d8dacc669f09c)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceLabelsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__13d7cb9daf560e92f76b07bf981a18df7b553db5a69836a1376457725d614a3b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47bf76fdb8f398c624224cfd5cfae03e5ad7c7eb63cad3240b268cbcd0627dd2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3950bbae4a1b8df79ff1fc544ceee19c4f7c24da154d0bee9d6bae7835ae94bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27289398beabfc747a7479f87d464f6615c00d7998ad376bbe2525844d133f31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fafe819b446ac5e2bd125f40dd8196e57d10f9c575993d1d96f55f2f609b538a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a88ea585a0793512624c940cf46830b05cce57e12baf808e4d73e3e34c96294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceLabelsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b32406cf1b36cb436cf7bf0b50ea2d38fa5db2a16941ac9f17806c1a89dea78)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8110e60b0e7d94b982739f820ea7eed7cee0d7dc3724445cd3d6c1ec89931b01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e24cf56950c16b61ac0270a61e7beb9124d0b32955267422f94325107c9830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__237b8d00b744900f6ce40d69525b08f819e591c1ffec49770c8a644df07dd9c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceMode",
    jsii_struct_bases=[],
    name_mapping={"global_": "global", "replicated": "replicated"},
)
class ServiceMode:
    def __init__(
        self,
        *,
        global_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        replicated: typing.Optional[typing.Union["ServiceModeReplicated", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param global_: The global service mode. Defaults to ``false``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#global Service#global}
        :param replicated: replicated block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicated Service#replicated}
        '''
        if isinstance(replicated, dict):
            replicated = ServiceModeReplicated(**replicated)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748e3845500af1efd8ef69bfee2e1d983e90177cd4259f37faa35f59fae52e67)
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
            check_type(argname="argument replicated", value=replicated, expected_type=type_hints["replicated"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if global_ is not None:
            self._values["global_"] = global_
        if replicated is not None:
            self._values["replicated"] = replicated

    @builtins.property
    def global_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''The global service mode. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#global Service#global}
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def replicated(self) -> typing.Optional["ServiceModeReplicated"]:
        '''replicated block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicated Service#replicated}
        '''
        result = self._values.get("replicated")
        return typing.cast(typing.Optional["ServiceModeReplicated"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceModeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceModeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1eff7c39aea572ba1e691f22ec4fb7ea7bcb0ad911a0d4ee42ccc9625ec96a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putReplicated")
    def put_replicated(self, *, replicas: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param replicas: The amount of replicas of the service. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicas Service#replicas}
        '''
        value = ServiceModeReplicated(replicas=replicas)

        return typing.cast(None, jsii.invoke(self, "putReplicated", [value]))

    @jsii.member(jsii_name="resetGlobal")
    def reset_global(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobal", []))

    @jsii.member(jsii_name="resetReplicated")
    def reset_replicated(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicated", []))

    @builtins.property
    @jsii.member(jsii_name="replicated")
    def replicated(self) -> "ServiceModeReplicatedOutputReference":
        return typing.cast("ServiceModeReplicatedOutputReference", jsii.get(self, "replicated"))

    @builtins.property
    @jsii.member(jsii_name="globalInput")
    def global_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "globalInput"))

    @builtins.property
    @jsii.member(jsii_name="replicatedInput")
    def replicated_input(self) -> typing.Optional["ServiceModeReplicated"]:
        return typing.cast(typing.Optional["ServiceModeReplicated"], jsii.get(self, "replicatedInput"))

    @builtins.property
    @jsii.member(jsii_name="global")
    def global_(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "global"))

    @global_.setter
    def global_(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eca08ec9f6935803f67bbc1ef758c7aec6c8337b96a0ead9c44d049cffd20d0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "global", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceMode]:
        return typing.cast(typing.Optional[ServiceMode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceMode]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f874417786b7a52043aa3290e6509469f2e797ba02da9b24f2c43b55a6b5cde9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceModeReplicated",
    jsii_struct_bases=[],
    name_mapping={"replicas": "replicas"},
)
class ServiceModeReplicated:
    def __init__(self, *, replicas: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param replicas: The amount of replicas of the service. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicas Service#replicas}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f9f27ec2ee1556dfb50f2aab479ab29f4715ecfb644ac7e295865cc160eed9e)
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if replicas is not None:
            self._values["replicas"] = replicas

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''The amount of replicas of the service. Defaults to ``1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#replicas Service#replicas}
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceModeReplicated(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceModeReplicatedOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceModeReplicatedOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__806df2a7c238dd4c14b2c8f884e0e148f7655c476b9056429ecfde174a495b48)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReplicas")
    def reset_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplicas", []))

    @builtins.property
    @jsii.member(jsii_name="replicasInput")
    def replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicasInput"))

    @builtins.property
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "replicas"))

    @replicas.setter
    def replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92fc63a4d742a6a5df7224c89eb1ea611005510defa3e7c883ba1cd7eeb45365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicas", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceModeReplicated]:
        return typing.cast(typing.Optional[ServiceModeReplicated], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceModeReplicated]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac69e5b988b2573acbbb326d0d0869867d65940c603046953b4294da77a9ff8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceRollbackConfig",
    jsii_struct_bases=[],
    name_mapping={
        "delay": "delay",
        "failure_action": "failureAction",
        "max_failure_ratio": "maxFailureRatio",
        "monitor": "monitor",
        "order": "order",
        "parallelism": "parallelism",
    },
)
class ServiceRollbackConfig:
    def __init__(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        failure_action: typing.Optional[builtins.str] = None,
        max_failure_ratio: typing.Optional[builtins.str] = None,
        monitor: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
        parallelism: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delay: Delay between task rollbacks (ns|us|ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param failure_action: Action on rollback failure: pause | continue. Defaults to ``pause``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        :param max_failure_ratio: Failure rate to tolerate during a rollback. Defaults to ``0.0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        :param monitor: Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        :param order: Rollback order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        :param parallelism: Maximum number of tasks to be rollbacked in one iteration. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__676afc586bb77216f990fca7e04e2ca84318c80e8ff2797d0fc703ea6b3e8250)
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument failure_action", value=failure_action, expected_type=type_hints["failure_action"])
            check_type(argname="argument max_failure_ratio", value=max_failure_ratio, expected_type=type_hints["max_failure_ratio"])
            check_type(argname="argument monitor", value=monitor, expected_type=type_hints["monitor"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delay is not None:
            self._values["delay"] = delay
        if failure_action is not None:
            self._values["failure_action"] = failure_action
        if max_failure_ratio is not None:
            self._values["max_failure_ratio"] = max_failure_ratio
        if monitor is not None:
            self._values["monitor"] = monitor
        if order is not None:
            self._values["order"] = order
        if parallelism is not None:
            self._values["parallelism"] = parallelism

    @builtins.property
    def delay(self) -> typing.Optional[builtins.str]:
        '''Delay between task rollbacks (ns|us|ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_action(self) -> typing.Optional[builtins.str]:
        '''Action on rollback failure: pause | continue. Defaults to ``pause``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        '''
        result = self._values.get("failure_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_failure_ratio(self) -> typing.Optional[builtins.str]:
        '''Failure rate to tolerate during a rollback. Defaults to ``0.0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        '''
        result = self._values.get("max_failure_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor(self) -> typing.Optional[builtins.str]:
        '''Duration after each task rollback to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        '''
        result = self._values.get("monitor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order(self) -> typing.Optional[builtins.str]:
        '''Rollback order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        '''
        result = self._values.get("order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parallelism(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of tasks to be rollbacked in one iteration. Defaults to ``1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceRollbackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceRollbackConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceRollbackConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90a62323f0d9b6ef643175cda6e63d9fc0bbb8230937fce33dc00464e325d80b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @jsii.member(jsii_name="resetFailureAction")
    def reset_failure_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureAction", []))

    @jsii.member(jsii_name="resetMaxFailureRatio")
    def reset_max_failure_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailureRatio", []))

    @jsii.member(jsii_name="resetMonitor")
    def reset_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitor", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="failureActionInput")
    def failure_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failureActionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailureRatioInput")
    def max_failure_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxFailureRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorInput")
    def monitor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5169397934e464cd0a646294da597cd73ac39b8da466e677208d0c398be380cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="failureAction")
    def failure_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureAction"))

    @failure_action.setter
    def failure_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2964f364544c84952bd71839d93c5c0b9f92345f0263d48d6ec67a2131b41f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureAction", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxFailureRatio")
    def max_failure_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxFailureRatio"))

    @max_failure_ratio.setter
    def max_failure_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee3c8e4144670f8a10fe2c7bc7a9e81d97bd109e2b57a6562b0f382e684f076d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailureRatio", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="monitor")
    def monitor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitor"))

    @monitor.setter
    def monitor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82debe4bc964022e20e907bf5f08f9f10da748794d343f6f38592eed082dbc55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitor", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "order"))

    @order.setter
    def order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb7728d93d8c31c297b00bcebc9ae5f95440c2b43e6d36d90e10650359a0c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelism"))

    @parallelism.setter
    def parallelism(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9c7c3713230e93d95214862561a7380360a6b16b312aa6f006b6231e59f72a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelism", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceRollbackConfig]:
        return typing.cast(typing.Optional[ServiceRollbackConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceRollbackConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe30eac6031c81863d19cfa62f7a60cc49121d8f12b87df620340601247e2e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpec",
    jsii_struct_bases=[],
    name_mapping={
        "container_spec": "containerSpec",
        "force_update": "forceUpdate",
        "log_driver": "logDriver",
        "networks": "networks",
        "placement": "placement",
        "resources": "resources",
        "restart_policy": "restartPolicy",
        "runtime": "runtime",
    },
)
class ServiceTaskSpec:
    def __init__(
        self,
        *,
        container_spec: typing.Union["ServiceTaskSpecContainerSpec", typing.Dict[builtins.str, typing.Any]],
        force_update: typing.Optional[jsii.Number] = None,
        log_driver: typing.Optional[typing.Union["ServiceTaskSpecLogDriver", typing.Dict[builtins.str, typing.Any]]] = None,
        networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        placement: typing.Optional[typing.Union["ServiceTaskSpecPlacement", typing.Dict[builtins.str, typing.Any]]] = None,
        resources: typing.Optional[typing.Union["ServiceTaskSpecResources", typing.Dict[builtins.str, typing.Any]]] = None,
        restart_policy: typing.Optional[typing.Union["ServiceTaskSpecRestartPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        runtime: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_spec: container_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#container_spec Service#container_spec}
        :param force_update: A counter that triggers an update even if no relevant parameters have been changed. See the `spec <https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#force_update Service#force_update}
        :param log_driver: log_driver block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#log_driver Service#log_driver}
        :param networks: Ids of the networks in which the container will be put in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#networks Service#networks}
        :param placement: placement block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#placement Service#placement}
        :param resources: resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#resources Service#resources}
        :param restart_policy: restart_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#restart_policy Service#restart_policy}
        :param runtime: Runtime is the type of runtime specified for the task executor. See the `types <https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go>`_. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#runtime Service#runtime}
        '''
        if isinstance(container_spec, dict):
            container_spec = ServiceTaskSpecContainerSpec(**container_spec)
        if isinstance(log_driver, dict):
            log_driver = ServiceTaskSpecLogDriver(**log_driver)
        if isinstance(placement, dict):
            placement = ServiceTaskSpecPlacement(**placement)
        if isinstance(resources, dict):
            resources = ServiceTaskSpecResources(**resources)
        if isinstance(restart_policy, dict):
            restart_policy = ServiceTaskSpecRestartPolicy(**restart_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d336120923c53aef986146bc12940831e5b2368231d134c0dd44a96b9d948b)
            check_type(argname="argument container_spec", value=container_spec, expected_type=type_hints["container_spec"])
            check_type(argname="argument force_update", value=force_update, expected_type=type_hints["force_update"])
            check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
            check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument restart_policy", value=restart_policy, expected_type=type_hints["restart_policy"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_spec": container_spec,
        }
        if force_update is not None:
            self._values["force_update"] = force_update
        if log_driver is not None:
            self._values["log_driver"] = log_driver
        if networks is not None:
            self._values["networks"] = networks
        if placement is not None:
            self._values["placement"] = placement
        if resources is not None:
            self._values["resources"] = resources
        if restart_policy is not None:
            self._values["restart_policy"] = restart_policy
        if runtime is not None:
            self._values["runtime"] = runtime

    @builtins.property
    def container_spec(self) -> "ServiceTaskSpecContainerSpec":
        '''container_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#container_spec Service#container_spec}
        '''
        result = self._values.get("container_spec")
        assert result is not None, "Required property 'container_spec' is missing"
        return typing.cast("ServiceTaskSpecContainerSpec", result)

    @builtins.property
    def force_update(self) -> typing.Optional[jsii.Number]:
        '''A counter that triggers an update even if no relevant parameters have been changed. See the `spec <https://github.com/docker/swarmkit/blob/master/api/specs.proto#L126>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#force_update Service#force_update}
        '''
        result = self._values.get("force_update")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def log_driver(self) -> typing.Optional["ServiceTaskSpecLogDriver"]:
        '''log_driver block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#log_driver Service#log_driver}
        '''
        result = self._values.get("log_driver")
        return typing.cast(typing.Optional["ServiceTaskSpecLogDriver"], result)

    @builtins.property
    def networks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Ids of the networks in which the  container will be put in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#networks Service#networks}
        '''
        result = self._values.get("networks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def placement(self) -> typing.Optional["ServiceTaskSpecPlacement"]:
        '''placement block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#placement Service#placement}
        '''
        result = self._values.get("placement")
        return typing.cast(typing.Optional["ServiceTaskSpecPlacement"], result)

    @builtins.property
    def resources(self) -> typing.Optional["ServiceTaskSpecResources"]:
        '''resources block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#resources Service#resources}
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional["ServiceTaskSpecResources"], result)

    @builtins.property
    def restart_policy(self) -> typing.Optional["ServiceTaskSpecRestartPolicy"]:
        '''restart_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#restart_policy Service#restart_policy}
        '''
        result = self._values.get("restart_policy")
        return typing.cast(typing.Optional["ServiceTaskSpecRestartPolicy"], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''Runtime is the type of runtime specified for the task executor. See the `types <https://github.com/moby/moby/blob/master/api/types/swarm/runtime.go>`_.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#runtime Service#runtime}
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpec",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "args": "args",
        "command": "command",
        "configs": "configs",
        "dir": "dir",
        "dns_config": "dnsConfig",
        "env": "env",
        "groups": "groups",
        "healthcheck": "healthcheck",
        "hostname": "hostname",
        "hosts": "hosts",
        "isolation": "isolation",
        "labels": "labels",
        "mounts": "mounts",
        "privileges": "privileges",
        "read_only": "readOnly",
        "secrets": "secrets",
        "stop_grace_period": "stopGracePeriod",
        "stop_signal": "stopSignal",
        "user": "user",
    },
)
class ServiceTaskSpecContainerSpec:
    def __init__(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecConfigs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dir: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecDnsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecHealthcheck", typing.Dict[builtins.str, typing.Any]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecHosts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        isolation: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecMounts", typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileges: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecPrivileges", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecSecrets", typing.Dict[builtins.str, typing.Any]]]]] = None,
        stop_grace_period: typing.Optional[builtins.str] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The image name to use for the containers of the service, like ``nginx:1.17.6``. Also use the data-source or resource of ``docker_image`` with the ``repo_digest`` or ``docker_registry_image`` with the ``name`` attribute for this, as shown in the examples. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#image Service#image}
        :param args: Arguments to the command. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#args Service#args}
        :param command: The command/entrypoint to be run in the image. According to the `docker cli <https://github.com/docker/cli/blob/v20.10.7/cli/command/service/opts.go#L705>`_ the override of the entrypoint is also passed to the ``command`` property and there is no ``entrypoint`` attribute in the ``ContainerSpec`` of the service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#command Service#command}
        :param configs: configs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#configs Service#configs}
        :param dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dir Service#dir}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dns_config Service#dns_config}
        :param env: A list of environment variables in the form VAR="value". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#env Service#env}
        :param groups: A list of additional groups that the container process will run as. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#groups Service#groups}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#healthcheck Service#healthcheck}
        :param hostname: The hostname to use for the container, as a valid RFC 1123 hostname. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hostname Service#hostname}
        :param hosts: hosts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hosts Service#hosts}
        :param isolation: Isolation technology of the containers running the service. (Windows only). Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#isolation Service#isolation}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mounts Service#mounts}
        :param privileges: privileges block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#privileges Service#privileges}
        :param read_only: Mount the container's root filesystem as read only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#read_only Service#read_only}
        :param secrets: secrets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secrets Service#secrets}
        :param stop_grace_period: Amount of time to wait for the container to terminate before forcefully removing it (ms|s|m|h). If not specified or '0s' the destroy will not check if all tasks/containers of the service terminate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_grace_period Service#stop_grace_period}
        :param stop_signal: Signal to stop the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_signal Service#stop_signal}
        :param user: The user inside the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        if isinstance(dns_config, dict):
            dns_config = ServiceTaskSpecContainerSpecDnsConfig(**dns_config)
        if isinstance(healthcheck, dict):
            healthcheck = ServiceTaskSpecContainerSpecHealthcheck(**healthcheck)
        if isinstance(privileges, dict):
            privileges = ServiceTaskSpecContainerSpecPrivileges(**privileges)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482915048177ac8ed887d05e795dea88e9a382d0f4ee35a4ce1140147dc00503)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument configs", value=configs, expected_type=type_hints["configs"])
            check_type(argname="argument dir", value=dir, expected_type=type_hints["dir"])
            check_type(argname="argument dns_config", value=dns_config, expected_type=type_hints["dns_config"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument healthcheck", value=healthcheck, expected_type=type_hints["healthcheck"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument isolation", value=isolation, expected_type=type_hints["isolation"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument mounts", value=mounts, expected_type=type_hints["mounts"])
            check_type(argname="argument privileges", value=privileges, expected_type=type_hints["privileges"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secrets", value=secrets, expected_type=type_hints["secrets"])
            check_type(argname="argument stop_grace_period", value=stop_grace_period, expected_type=type_hints["stop_grace_period"])
            check_type(argname="argument stop_signal", value=stop_signal, expected_type=type_hints["stop_signal"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image": image,
        }
        if args is not None:
            self._values["args"] = args
        if command is not None:
            self._values["command"] = command
        if configs is not None:
            self._values["configs"] = configs
        if dir is not None:
            self._values["dir"] = dir
        if dns_config is not None:
            self._values["dns_config"] = dns_config
        if env is not None:
            self._values["env"] = env
        if groups is not None:
            self._values["groups"] = groups
        if healthcheck is not None:
            self._values["healthcheck"] = healthcheck
        if hostname is not None:
            self._values["hostname"] = hostname
        if hosts is not None:
            self._values["hosts"] = hosts
        if isolation is not None:
            self._values["isolation"] = isolation
        if labels is not None:
            self._values["labels"] = labels
        if mounts is not None:
            self._values["mounts"] = mounts
        if privileges is not None:
            self._values["privileges"] = privileges
        if read_only is not None:
            self._values["read_only"] = read_only
        if secrets is not None:
            self._values["secrets"] = secrets
        if stop_grace_period is not None:
            self._values["stop_grace_period"] = stop_grace_period
        if stop_signal is not None:
            self._values["stop_signal"] = stop_signal
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def image(self) -> builtins.str:
        '''The image name to use for the containers of the service, like ``nginx:1.17.6``. Also use the data-source or resource of ``docker_image`` with the ``repo_digest`` or ``docker_registry_image`` with the ``name`` attribute for this, as shown in the examples.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#image Service#image}
        '''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Arguments to the command.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#args Service#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command/entrypoint to be run in the image.

        According to the `docker cli <https://github.com/docker/cli/blob/v20.10.7/cli/command/service/opts.go#L705>`_ the override of the entrypoint is also passed to the ``command`` property and there is no ``entrypoint`` attribute in the ``ContainerSpec`` of the service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#command Service#command}
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def configs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecConfigs"]]]:
        '''configs block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#configs Service#configs}
        '''
        result = self._values.get("configs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecConfigs"]]], result)

    @builtins.property
    def dir(self) -> typing.Optional[builtins.str]:
        '''The working directory for commands to run in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dir Service#dir}
        '''
        result = self._values.get("dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_config(self) -> typing.Optional["ServiceTaskSpecContainerSpecDnsConfig"]:
        '''dns_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dns_config Service#dns_config}
        '''
        result = self._values.get("dns_config")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecDnsConfig"], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of environment variables in the form VAR="value".

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#env Service#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of additional groups that the container process will run as.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#groups Service#groups}
        '''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def healthcheck(self) -> typing.Optional["ServiceTaskSpecContainerSpecHealthcheck"]:
        '''healthcheck block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#healthcheck Service#healthcheck}
        '''
        result = self._values.get("healthcheck")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecHealthcheck"], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''The hostname to use for the container, as a valid RFC 1123 hostname.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hostname Service#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecHosts"]]]:
        '''hosts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hosts Service#hosts}
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecHosts"]]], result)

    @builtins.property
    def isolation(self) -> typing.Optional[builtins.str]:
        '''Isolation technology of the containers running the service. (Windows only). Defaults to ``default``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#isolation Service#isolation}
        '''
        result = self._values.get("isolation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecLabels"]]], result)

    @builtins.property
    def mounts(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecMounts"]]]:
        '''mounts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mounts Service#mounts}
        '''
        result = self._values.get("mounts")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecMounts"]]], result)

    @builtins.property
    def privileges(self) -> typing.Optional["ServiceTaskSpecContainerSpecPrivileges"]:
        '''privileges block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#privileges Service#privileges}
        '''
        result = self._values.get("privileges")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecPrivileges"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Mount the container's root filesystem as read only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#read_only Service#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secrets(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecSecrets"]]]:
        '''secrets block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secrets Service#secrets}
        '''
        result = self._values.get("secrets")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecSecrets"]]], result)

    @builtins.property
    def stop_grace_period(self) -> typing.Optional[builtins.str]:
        '''Amount of time to wait for the container to terminate before forcefully removing it (ms|s|m|h).

        If not specified or '0s' the destroy will not check if all tasks/containers of the service terminate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_grace_period Service#stop_grace_period}
        '''
        result = self._values.get("stop_grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stop_signal(self) -> typing.Optional[builtins.str]:
        '''Signal to stop the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_signal Service#stop_signal}
        '''
        result = self._values.get("stop_signal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user inside the container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecConfigs",
    jsii_struct_bases=[],
    name_mapping={
        "config_id": "configId",
        "file_name": "fileName",
        "config_name": "configName",
        "file_gid": "fileGid",
        "file_mode": "fileMode",
        "file_uid": "fileUid",
    },
)
class ServiceTaskSpecContainerSpecConfigs:
    def __init__(
        self,
        *,
        config_id: builtins.str,
        file_name: builtins.str,
        config_name: typing.Optional[builtins.str] = None,
        file_gid: typing.Optional[builtins.str] = None,
        file_mode: typing.Optional[jsii.Number] = None,
        file_uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param config_id: ID of the specific config that we're referencing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#config_id Service#config_id}
        :param file_name: Represents the final filename in the filesystem. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_name Service#file_name}
        :param config_name: Name of the config that this references, but this is just provided for lookup/display purposes. The config in the reference will be identified by its ID Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#config_name Service#config_name}
        :param file_gid: Represents the file GID. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_gid Service#file_gid}
        :param file_mode: Represents represents the FileMode of the file. Defaults to ``0o444``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_mode Service#file_mode}
        :param file_uid: Represents the file UID. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_uid Service#file_uid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77dda369ce826711059257e681cbf1e5a45ed1e47a8bc33276e2a600b09ec13e)
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
            check_type(argname="argument config_name", value=config_name, expected_type=type_hints["config_name"])
            check_type(argname="argument file_gid", value=file_gid, expected_type=type_hints["file_gid"])
            check_type(argname="argument file_mode", value=file_mode, expected_type=type_hints["file_mode"])
            check_type(argname="argument file_uid", value=file_uid, expected_type=type_hints["file_uid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "file_name": file_name,
        }
        if config_name is not None:
            self._values["config_name"] = config_name
        if file_gid is not None:
            self._values["file_gid"] = file_gid
        if file_mode is not None:
            self._values["file_mode"] = file_mode
        if file_uid is not None:
            self._values["file_uid"] = file_uid

    @builtins.property
    def config_id(self) -> builtins.str:
        '''ID of the specific config that we're referencing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#config_id Service#config_id}
        '''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_name(self) -> builtins.str:
        '''Represents the final filename in the filesystem.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_name Service#file_name}
        '''
        result = self._values.get("file_name")
        assert result is not None, "Required property 'file_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_name(self) -> typing.Optional[builtins.str]:
        '''Name of the config that this references, but this is just provided for lookup/display purposes.

        The config in the reference will be identified by its ID

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#config_name Service#config_name}
        '''
        result = self._values.get("config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_gid(self) -> typing.Optional[builtins.str]:
        '''Represents the file GID. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_gid Service#file_gid}
        '''
        result = self._values.get("file_gid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_mode(self) -> typing.Optional[jsii.Number]:
        '''Represents represents the FileMode of the file. Defaults to ``0o444``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_mode Service#file_mode}
        '''
        result = self._values.get("file_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def file_uid(self) -> typing.Optional[builtins.str]:
        '''Represents the file UID. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_uid Service#file_uid}
        '''
        result = self._values.get("file_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecConfigsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecConfigsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8db746da53638f97893aa60ad267ccb8496cc335527b15dc2a0b1c2a7aa8f634)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff62e3e6dfa9801aeb7b563f760a293882325d1e0ba5ec1cae6bd4984f1bd274)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ed15ceb32161e41d7348e32a5ac580dc8a02ec082a090a1d216182a74030c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d03291e4ba89d773b2b04af0c7eceac2eadbb8cc45c9bbdf43748b007f8c426)
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
            type_hints = typing.get_type_hints(_typecheckingstub__37b21be17b0f7d07bb6ba38213e3270c9556c84f6fe6e31e5e59c7c94ac6ac8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c252b897c57bf15efc064cd085b4013b3ddf8c9dc725408f3a693887b2ccc08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecConfigsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecConfigsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1c75fcfccc88aa553fedaf97471170415ce2753e993ea0e55f71ee1c4cb7122)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConfigName")
    def reset_config_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigName", []))

    @jsii.member(jsii_name="resetFileGid")
    def reset_file_gid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileGid", []))

    @jsii.member(jsii_name="resetFileMode")
    def reset_file_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileMode", []))

    @jsii.member(jsii_name="resetFileUid")
    def reset_file_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUid", []))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configNameInput")
    def config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileGidInput")
    def file_gid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileGidInput"))

    @builtins.property
    @jsii.member(jsii_name="fileModeInput")
    def file_mode_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileModeInput"))

    @builtins.property
    @jsii.member(jsii_name="fileNameInput")
    def file_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUidInput")
    def file_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileUidInput"))

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9346b4869790e5c23b56614063a530a7e77f44fb00f74936409a25a483dcf0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configName")
    def config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configName"))

    @config_name.setter
    def config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a8d276c9bc3a08767f04c5dbb1b1f87e3ede887e4256e552c0e543da880f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileGid")
    def file_gid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileGid"))

    @file_gid.setter
    def file_gid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3511ba809aa2c7b4db940279b8dd61f547ce381afb1d91c15ee09f0a5ff5a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileGid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileMode")
    def file_mode(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileMode"))

    @file_mode.setter
    def file_mode(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40fcfe6a6b1abae9a3bf0409c6117714208aad1edf2232f30ca619feec2f99a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileName")
    def file_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileName"))

    @file_name.setter
    def file_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dc331f1653ca664c838ac65a4a2bb28ebda31bc30eca7e7a90da2fe8abcb36a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileUid")
    def file_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileUid"))

    @file_uid.setter
    def file_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b7330acfa53e441f0a9a72400e9b1a340c2de7a995cdf7d3e38491f3975fdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecConfigs]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecConfigs]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecConfigs]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e280d984bbbca23045c62d6708bfe57de8ff44341ac4afaa60f1cf5049c63e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecDnsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "nameservers": "nameservers",
        "options": "options",
        "search": "search",
    },
)
class ServiceTaskSpecContainerSpecDnsConfig:
    def __init__(
        self,
        *,
        nameservers: typing.Sequence[builtins.str],
        options: typing.Optional[typing.Sequence[builtins.str]] = None,
        search: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param nameservers: The IP addresses of the name servers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nameservers Service#nameservers}
        :param options: A list of internal resolver variables to be modified (e.g., ``debug``, ``ndots:3``, etc.). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        :param search: A search list for host-name lookup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#search Service#search}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0b45d604b4f2b522d49c9a49f43cf60db330a80c6b4756693d379e6ccfc5a1f)
            check_type(argname="argument nameservers", value=nameservers, expected_type=type_hints["nameservers"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nameservers": nameservers,
        }
        if options is not None:
            self._values["options"] = options
        if search is not None:
            self._values["search"] = search

    @builtins.property
    def nameservers(self) -> typing.List[builtins.str]:
        '''The IP addresses of the name servers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nameservers Service#nameservers}
        '''
        result = self._values.get("nameservers")
        assert result is not None, "Required property 'nameservers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of internal resolver variables to be modified (e.g., ``debug``, ``ndots:3``, etc.).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A search list for host-name lookup.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#search Service#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecDnsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecDnsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecDnsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76a90b5b3de5f31022e4928a64929f63b7cd5bc6b23c00da65656514163bee15)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @builtins.property
    @jsii.member(jsii_name="nameserversInput")
    def nameservers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameserversInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameservers")
    def nameservers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameservers"))

    @nameservers.setter
    def nameservers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dcb12918cef65dc2a34fb84e36216b772054e3569595c0f635d5536a1cb4944)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameservers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be817d2fe5ffa21def0f7dbfb3bd37132ca08574484ba9774344b8247c56eee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "search"))

    @search.setter
    def search(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ff591abd150d03fba309c06b8bdbeca107a41d71b9614bd9b0012c6bd849f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "search", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecContainerSpecDnsConfig]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecDnsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecDnsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f9d4cb17761e6460f112a19bd1853ac167db02e863c959dad89587722b3df65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecHealthcheck",
    jsii_struct_bases=[],
    name_mapping={
        "test": "test",
        "interval": "interval",
        "retries": "retries",
        "start_period": "startPeriod",
        "timeout": "timeout",
    },
)
class ServiceTaskSpecContainerSpecHealthcheck:
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
        :param test: The test to perform as list. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#test Service#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#interval Service#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#retries Service#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#start_period Service#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18aac2635ee61a87bb02acaeb22569e07387e46189f487ae93b22c3e7543f1cd)
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
        '''The test to perform as list.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#test Service#test}
        '''
        result = self._values.get("test")
        assert result is not None, "Required property 'test' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Time between running the check (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#interval Service#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Consecutive failures needed to report unhealthy. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#retries Service#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_period(self) -> typing.Optional[builtins.str]:
        '''Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#start_period Service#start_period}
        '''
        result = self._values.get("start_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecHealthcheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecHealthcheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecHealthcheckOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9509152655f8ab05c182c508cc0acecea0223bc2b5da612332c510e3b6a688c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6617f7c27bbd7770bb714aafd29b14392b7ddb4acf107492576b5241a22623c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4001c49f0626de13a663e8976a0acd954a4a2019c2db1dedb5831d74c57321)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startPeriod")
    def start_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startPeriod"))

    @start_period.setter
    def start_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c696aa20cf5e9f240f93f7e886d6277bf9e32d4dc83854034f226c12ccbbfa2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="test")
    def test(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "test"))

    @test.setter
    def test(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb4888632d31cd0e75f8321c82f10b352ad1cbcd7860cc6a4941f86001ea5d64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "test", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__675fe7d5674302a834ac0060dbe2f7263e74708722d025e8c4ebd73f20b06f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecHealthcheck]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecHealthcheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecHealthcheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c229fdf41d6ae0e042a2513922c140a3dbf1d557a39f2feb2670de0245347e7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecHosts",
    jsii_struct_bases=[],
    name_mapping={"host": "host", "ip": "ip"},
)
class ServiceTaskSpecContainerSpecHosts:
    def __init__(self, *, host: builtins.str, ip: builtins.str) -> None:
        '''
        :param host: The name of the host. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#host Service#host}
        :param ip: The ip of the host. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#ip Service#ip}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9acf8730c55f9b581990a0bf5d33d9e0e4d39230817836e22a9a71d06f7bde4f)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host": host,
            "ip": ip,
        }

    @builtins.property
    def host(self) -> builtins.str:
        '''The name of the host.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#host Service#host}
        '''
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip(self) -> builtins.str:
        '''The ip of the host.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#ip Service#ip}
        '''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecHosts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecHostsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecHostsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__422771b29253daca0e508f8e41795087bf333df496d5e4a21a56575dce522cb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecHostsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0caed2d42e785844e3b7238154bff271dae75fa26dcc3a5ff218380d02dcef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecHostsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f5d1709c0025f4d7c0bdcd4448cecd92e2d028ec5334ed0781e59fe01543bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__55a71940fbce6fc936f43301e90986b1f0ba47973e2c04f508f54f4071c1f7eb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f31965b284b88bfcd52c835a659c920e963b242a2433149edf36b902c4a6a99c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f312cf312f6283b7753cb156532deb8a8720ff116bbdb84ba462347383d10d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecHostsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecHostsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5d10bc119e2e9ba7c3bd8668b51694fae1715c0675dfc119b2be70fb08651a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ba224749030745f0cfcb42989de78b9b47c75f82d6647abc0fe9dc264baa226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324005385c52387f65bfeda1b3f61dd1dc5223246cf1801964744c7837edb7c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecHosts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecHosts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecHosts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1283365caf4edb1162b96d1e3b8efb0a4ac5c2e7aaa2a8ee69daf52ea2c1603d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ServiceTaskSpecContainerSpecLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e5167fec32e3fdb227611aae63fc6686e4d389abd2d87036529bb8d60b9b36)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecLabelsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__282ec92cb5f067f7f48ba0c8606b4407ccdbd4ed60bf2c73d000ff4624b82f3d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d92616c660bf04a2e3ead7b36aa86235d748bf8c7a986970366458ae220c6d92)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597b34941e53b22d23851dbfdc44f4cffd76ff174a01833a916552eb8626c535)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d75fc527973f257125167403f86afeea7f9b9886e0a8a769a0d142bcc2d952d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccbfd2346da3d9ae59b95821631852d5b14d9f51336ba95163b51bac621f4e31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d454bb9a6790d3a4c547a8c8698d635e04e4ca52a46e7c97451b40f5d799d91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecLabelsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e01f4ce063aacb7179eadb0f05d38e92e8f9b658a34118d98174abe90ac3c04)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8415473a39bbbe7da4ebfef0578f80d7d999ee7c72526a8af2f6a0ea4c444d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c9d236229e1e7127c8ac4bd917f04ae4a56d23eb06dc7c1ee1b16ac99d38bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b26b73c3733591900f41706d77b7ab66439e8faf70ca219c375e2f338cf222c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMounts",
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
class ServiceTaskSpecContainerSpecMounts:
    def __init__(
        self,
        *,
        target: builtins.str,
        type: builtins.str,
        bind_options: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecMountsBindOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        source: typing.Optional[builtins.str] = None,
        tmpfs_options: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecMountsTmpfsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        volume_options: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecMountsVolumeOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: Container path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#target Service#target}
        :param type: The mount type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#type Service#type}
        :param bind_options: bind_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#bind_options Service#bind_options}
        :param read_only: Whether the mount should be read-only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#read_only Service#read_only}
        :param source: Mount source (e.g. a volume name, a host path). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#source Service#source}
        :param tmpfs_options: tmpfs_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#tmpfs_options Service#tmpfs_options}
        :param volume_options: volume_options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#volume_options Service#volume_options}
        '''
        if isinstance(bind_options, dict):
            bind_options = ServiceTaskSpecContainerSpecMountsBindOptions(**bind_options)
        if isinstance(tmpfs_options, dict):
            tmpfs_options = ServiceTaskSpecContainerSpecMountsTmpfsOptions(**tmpfs_options)
        if isinstance(volume_options, dict):
            volume_options = ServiceTaskSpecContainerSpecMountsVolumeOptions(**volume_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b685b9129d5d62e195fb1651091d3e3939bb0b94b787fd4e77f12281df8901ad)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#target Service#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The mount type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#type Service#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bind_options(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecMountsBindOptions"]:
        '''bind_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#bind_options Service#bind_options}
        '''
        result = self._values.get("bind_options")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecMountsBindOptions"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether the mount should be read-only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#read_only Service#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Mount source (e.g. a volume name, a host path).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#source Service#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tmpfs_options(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecMountsTmpfsOptions"]:
        '''tmpfs_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#tmpfs_options Service#tmpfs_options}
        '''
        result = self._values.get("tmpfs_options")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecMountsTmpfsOptions"], result)

    @builtins.property
    def volume_options(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecMountsVolumeOptions"]:
        '''volume_options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#volume_options Service#volume_options}
        '''
        result = self._values.get("volume_options")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecMountsVolumeOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecMounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsBindOptions",
    jsii_struct_bases=[],
    name_mapping={"propagation": "propagation"},
)
class ServiceTaskSpecContainerSpecMountsBindOptions:
    def __init__(self, *, propagation: typing.Optional[builtins.str] = None) -> None:
        '''
        :param propagation: Bind propagation refers to whether or not mounts created within a given bind-mount or named volume can be propagated to replicas of that mount. See the `docs <https://docs.docker.com/storage/bind-mounts/#configure-bind-propagation>`_ for details. Defaults to ``rprivate`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#propagation Service#propagation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e33608fdcc9fcabe4d8869a6c7edf5cedb9e722a63e14094372d3d031c70b58f)
            check_type(argname="argument propagation", value=propagation, expected_type=type_hints["propagation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if propagation is not None:
            self._values["propagation"] = propagation

    @builtins.property
    def propagation(self) -> typing.Optional[builtins.str]:
        '''Bind propagation refers to whether or not mounts created within a given bind-mount or named volume can be propagated to replicas of that mount.

        See the `docs <https://docs.docker.com/storage/bind-mounts/#configure-bind-propagation>`_ for details. Defaults to ``rprivate``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#propagation Service#propagation}
        '''
        result = self._values.get("propagation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecMountsBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecMountsBindOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsBindOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__535737c98703236cdd5d1123db718a9c7020013e1c7fb8556579c2f15ad4e0a6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ebf18b55f80f61fc5404f7f1479e9be3e8b731af32ddc5d275058a41cde1ce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4096ec49b246c6fb0329f917be9a6a0f1bd398051bade317a4e9db80cf3e5396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecMountsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a12658a63a94e38d7b4b69808c1a780d2d0b949629e335602a28f4877b201c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecMountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c70b62ea6327b9f1bf2895772be873ff87e4b82945cf23e455f9ff434b6e89d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecMountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fabee5f9e0b0b1617baaf869341b0f08d5d6051ae7f7bade9b5f49f8d29061)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2634ba50a02799adf4464215f2efe2bdae20a5cfa3aa2672edd8ddc525189443)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11cceff91620c30adc1cfffa8e603947aa04f11827aa9429ec7b0abe77844281)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b21a51d70784fab3ba11a260bcc127d46eea7ece9dc1e4bee9bc1e05a35c053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecMountsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ea95d50baf9c9eed1773bcfe058754f45446810b680a359baf6684f76e1108b)
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
        :param propagation: Bind propagation refers to whether or not mounts created within a given bind-mount or named volume can be propagated to replicas of that mount. See the `docs <https://docs.docker.com/storage/bind-mounts/#configure-bind-propagation>`_ for details. Defaults to ``rprivate`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#propagation Service#propagation}
        '''
        value = ServiceTaskSpecContainerSpecMountsBindOptions(propagation=propagation)

        return typing.cast(None, jsii.invoke(self, "putBindOptions", [value]))

    @jsii.member(jsii_name="putTmpfsOptions")
    def put_tmpfs_options(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#size_bytes Service#size_bytes}
        '''
        value = ServiceTaskSpecContainerSpecMountsTmpfsOptions(
            mode=mode, size_bytes=size_bytes
        )

        return typing.cast(None, jsii.invoke(self, "putTmpfsOptions", [value]))

    @jsii.member(jsii_name="putVolumeOptions")
    def put_volume_options(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_name Service#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_options Service#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#no_copy Service#no_copy}
        '''
        value = ServiceTaskSpecContainerSpecMountsVolumeOptions(
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
    def bind_options(
        self,
    ) -> ServiceTaskSpecContainerSpecMountsBindOptionsOutputReference:
        return typing.cast(ServiceTaskSpecContainerSpecMountsBindOptionsOutputReference, jsii.get(self, "bindOptions"))

    @builtins.property
    @jsii.member(jsii_name="tmpfsOptions")
    def tmpfs_options(
        self,
    ) -> "ServiceTaskSpecContainerSpecMountsTmpfsOptionsOutputReference":
        return typing.cast("ServiceTaskSpecContainerSpecMountsTmpfsOptionsOutputReference", jsii.get(self, "tmpfsOptions"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptions")
    def volume_options(
        self,
    ) -> "ServiceTaskSpecContainerSpecMountsVolumeOptionsOutputReference":
        return typing.cast("ServiceTaskSpecContainerSpecMountsVolumeOptionsOutputReference", jsii.get(self, "volumeOptions"))

    @builtins.property
    @jsii.member(jsii_name="bindOptionsInput")
    def bind_options_input(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions], jsii.get(self, "bindOptionsInput"))

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
    def tmpfs_options_input(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecMountsTmpfsOptions"]:
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecMountsTmpfsOptions"], jsii.get(self, "tmpfsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeOptionsInput")
    def volume_options_input(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecMountsVolumeOptions"]:
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecMountsVolumeOptions"], jsii.get(self, "volumeOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__90b6029cfb3f79bbdabd0a1fb9bf02d21c150d9e4009f33bccd4bc578b8957ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__118aecb58de8a917c235810da9b73e0e8c6b4e9a59bd9b0f0d7d33620415bac8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d053618615e9c14b81bf345bad15a52ff81956ce7d9f729551044bc0332014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f99c330817312f90f299e822cb1278084cf5f92b5fc49c321b392d726e1a385)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMounts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMounts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMounts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653e9e8c714b06d6903027d7640cd94bf89e33dd8599f61decdb362057985660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsTmpfsOptions",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "size_bytes": "sizeBytes"},
)
class ServiceTaskSpecContainerSpecMountsTmpfsOptions:
    def __init__(
        self,
        *,
        mode: typing.Optional[jsii.Number] = None,
        size_bytes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: The permission mode for the tmpfs mount in an integer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        :param size_bytes: The size for the tmpfs mount in bytes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#size_bytes Service#size_bytes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6736605039db227252e4667a4eebdf09d54713aed75df90f6cbde7cd05684a)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mode Service#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def size_bytes(self) -> typing.Optional[jsii.Number]:
        '''The size for the tmpfs mount in bytes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#size_bytes Service#size_bytes}
        '''
        result = self._values.get("size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecMountsTmpfsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecMountsTmpfsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsTmpfsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dea7491106ee9753c3b6f946f717283fa23369a1899390ee2e01d33e5f510ff3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94a76d7955daab4a4ffe920a4a02d9ff6ad8323e593b9e867215b809a9e06655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sizeBytes")
    def size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeBytes"))

    @size_bytes.setter
    def size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85d1fcc82e3f8ac7a026d394cb6baa9d13b57b01a7b275b4de3c4067606139d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecMountsTmpfsOptions]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecMountsTmpfsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecMountsTmpfsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__193f8b3273d2b070c9c48b35ec6fa51bccad07af66c3a4724673610d82e26d10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsVolumeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "driver_name": "driverName",
        "driver_options": "driverOptions",
        "labels": "labels",
        "no_copy": "noCopy",
    },
)
class ServiceTaskSpecContainerSpecMountsVolumeOptions:
    def __init__(
        self,
        *,
        driver_name: typing.Optional[builtins.str] = None,
        driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels", typing.Dict[builtins.str, typing.Any]]]]] = None,
        no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param driver_name: Name of the driver to use to create the volume. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_name Service#driver_name}
        :param driver_options: key/value map of driver specific options. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_options Service#driver_options}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param no_copy: Populate volume with data from the target. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#no_copy Service#no_copy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85a012927e166a1d9777ed70a83eecb259d15c8fb0ff072ac4ab817db44c493d)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_name Service#driver_name}
        '''
        result = self._values.get("driver_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def driver_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''key/value map of driver specific options.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#driver_options Service#driver_options}
        '''
        result = self._values.get("driver_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels"]]]:
        '''labels block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels"]]], result)

    @builtins.property
    def no_copy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Populate volume with data from the target.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#no_copy Service#no_copy}
        '''
        result = self._values.get("no_copy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecMountsVolumeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "value": "value"},
)
class ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels:
    def __init__(self, *, label: builtins.str, value: builtins.str) -> None:
        '''
        :param label: Name of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        :param value: Value of the label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ce28612a27d9f132753f88f503b0d370d0ea7398d7b7c19cf8deab91267ec6)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''Name of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#label Service#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#value Service#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e1e72b9761377fde752f0eb1afa339b463e07ad5242ddc4e9f4388115fcc6dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da2ce8f7ff7c48e46b59548808cde272c55f4049bb4d31696a3be072899b6d3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c064b9c0d115bc9c7e6c1453d2b36d387f92deb762d0b6af68fbd804674bb43)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d3cf4b5b71228f89a6dbd7e0b70a57c555c7b08957c91deee8e01505e640c29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce118fcbb1fdb4fd4a2bb1aedb13efa4154fa6000756e8051d4836813d94795f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fdad1c7b2806b0734328fadbdd392adbea5996a0179c473ad4d25c7eeedf1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__21a694b90cdb194b34f37cf1572719d1551844b3a6b42404f8f319d86c0208e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd8fb747aa45f53532792b8c3e97b3c7cfbf95cfac6225b5db74e6a8ea2c8aa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f444fedbf484f7144fe909565470c9efa017d3aaf844a65cd66a0f5573cee4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e447167ac81f26efe494f927d48c618e1d8ed40ea1fc200999e2b93aab05295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecMountsVolumeOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecMountsVolumeOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b94c71f645e88e28e75d67c492dec5bca9b5e72442822294f7a34dc298218819)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932599b34976868c9cc761720b5e618f7a958cf9187f5849b6b1ee6b933d330c)
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
    def labels(self) -> ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsList:
        return typing.cast(ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsList, jsii.get(self, "labels"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]], jsii.get(self, "labelsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__49832756cfa5b71a4231109e633f6f0f7b9ea2eb5dc65f9604e66e1e31890225)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="driverOptions")
    def driver_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverOptions"))

    @driver_options.setter
    def driver_options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b00f4b097d82cd43aa7b9772eaacd3c4b422ca67e41141d5653a0b3d838bf85)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0093b40c6e5810678d6eb9f4ec3efa27ec55d49878155075b10c871e3de6e2f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noCopy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecMountsVolumeOptions]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecMountsVolumeOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecMountsVolumeOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__142379bd073c8d8bca0db6439612d0d4e67b977aaa3e4e61a173aa23422da47e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89f000178dafb4d3bf383c79e1e46a81b85648a4b54ac8327f95ed66f029a773)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfigs")
    def put_configs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecConfigs, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70783c19d786c1bb0bf3a01aee2e47e733f88c5876dec92ebdf8fe9f33f2148)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfigs", [value]))

    @jsii.member(jsii_name="putDnsConfig")
    def put_dns_config(
        self,
        *,
        nameservers: typing.Sequence[builtins.str],
        options: typing.Optional[typing.Sequence[builtins.str]] = None,
        search: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param nameservers: The IP addresses of the name servers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nameservers Service#nameservers}
        :param options: A list of internal resolver variables to be modified (e.g., ``debug``, ``ndots:3``, etc.). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        :param search: A search list for host-name lookup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#search Service#search}
        '''
        value = ServiceTaskSpecContainerSpecDnsConfig(
            nameservers=nameservers, options=options, search=search
        )

        return typing.cast(None, jsii.invoke(self, "putDnsConfig", [value]))

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
        :param test: The test to perform as list. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#test Service#test}
        :param interval: Time between running the check (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#interval Service#interval}
        :param retries: Consecutive failures needed to report unhealthy. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#retries Service#retries}
        :param start_period: Start period for the container to initialize before counting retries towards unstable (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#start_period Service#start_period}
        :param timeout: Maximum time to allow one check to run (ms|s|m|h). Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#timeout Service#timeout}
        '''
        value = ServiceTaskSpecContainerSpecHealthcheck(
            test=test,
            interval=interval,
            retries=retries,
            start_period=start_period,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthcheck", [value]))

    @jsii.member(jsii_name="putHosts")
    def put_hosts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecHosts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb0a67090a0513b8a119da68d49262af6e2419af8753002d6ca4c540b587336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHosts", [value]))

    @jsii.member(jsii_name="putLabels")
    def put_labels(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecLabels, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881fa8374f255c1d10370df34e16ed340d11a61aa1508eb8e8679cdbd36b4ef5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabels", [value]))

    @jsii.member(jsii_name="putMounts")
    def put_mounts(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMounts, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8511a8f470268d30858d3ae9d60418a2b9f9b45afe4e7ad99a52fdea73dc8622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMounts", [value]))

    @jsii.member(jsii_name="putPrivileges")
    def put_privileges(
        self,
        *,
        credential_spec: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecPrivilegesCredentialSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux_context: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param credential_spec: credential_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#credential_spec Service#credential_spec}
        :param se_linux_context: se_linux_context block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#se_linux_context Service#se_linux_context}
        '''
        value = ServiceTaskSpecContainerSpecPrivileges(
            credential_spec=credential_spec, se_linux_context=se_linux_context
        )

        return typing.cast(None, jsii.invoke(self, "putPrivileges", [value]))

    @jsii.member(jsii_name="putSecrets")
    def put_secrets(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecContainerSpecSecrets", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2cc3fd55b1c41325faae54e0014b22cccccc9d692a7946ec339e217e3f3475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecrets", [value]))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetCommand")
    def reset_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommand", []))

    @jsii.member(jsii_name="resetConfigs")
    def reset_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigs", []))

    @jsii.member(jsii_name="resetDir")
    def reset_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDir", []))

    @jsii.member(jsii_name="resetDnsConfig")
    def reset_dns_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsConfig", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @jsii.member(jsii_name="resetHealthcheck")
    def reset_healthcheck(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthcheck", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetIsolation")
    def reset_isolation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsolation", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMounts")
    def reset_mounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMounts", []))

    @jsii.member(jsii_name="resetPrivileges")
    def reset_privileges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileges", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecrets")
    def reset_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecrets", []))

    @jsii.member(jsii_name="resetStopGracePeriod")
    def reset_stop_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopGracePeriod", []))

    @jsii.member(jsii_name="resetStopSignal")
    def reset_stop_signal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopSignal", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="configs")
    def configs(self) -> ServiceTaskSpecContainerSpecConfigsList:
        return typing.cast(ServiceTaskSpecContainerSpecConfigsList, jsii.get(self, "configs"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfig")
    def dns_config(self) -> ServiceTaskSpecContainerSpecDnsConfigOutputReference:
        return typing.cast(ServiceTaskSpecContainerSpecDnsConfigOutputReference, jsii.get(self, "dnsConfig"))

    @builtins.property
    @jsii.member(jsii_name="healthcheck")
    def healthcheck(self) -> ServiceTaskSpecContainerSpecHealthcheckOutputReference:
        return typing.cast(ServiceTaskSpecContainerSpecHealthcheckOutputReference, jsii.get(self, "healthcheck"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> ServiceTaskSpecContainerSpecHostsList:
        return typing.cast(ServiceTaskSpecContainerSpecHostsList, jsii.get(self, "hosts"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> ServiceTaskSpecContainerSpecLabelsList:
        return typing.cast(ServiceTaskSpecContainerSpecLabelsList, jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="mounts")
    def mounts(self) -> ServiceTaskSpecContainerSpecMountsList:
        return typing.cast(ServiceTaskSpecContainerSpecMountsList, jsii.get(self, "mounts"))

    @builtins.property
    @jsii.member(jsii_name="privileges")
    def privileges(self) -> "ServiceTaskSpecContainerSpecPrivilegesOutputReference":
        return typing.cast("ServiceTaskSpecContainerSpecPrivilegesOutputReference", jsii.get(self, "privileges"))

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> "ServiceTaskSpecContainerSpecSecretsList":
        return typing.cast("ServiceTaskSpecContainerSpecSecretsList", jsii.get(self, "secrets"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="commandInput")
    def command_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "commandInput"))

    @builtins.property
    @jsii.member(jsii_name="configsInput")
    def configs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]], jsii.get(self, "configsInput"))

    @builtins.property
    @jsii.member(jsii_name="dirInput")
    def dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dirInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsConfigInput")
    def dns_config_input(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecDnsConfig]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecDnsConfig], jsii.get(self, "dnsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="healthcheckInput")
    def healthcheck_input(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecHealthcheck]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecHealthcheck], jsii.get(self, "healthcheckInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="isolationInput")
    def isolation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isolationInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="mountsInput")
    def mounts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]], jsii.get(self, "mountsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegesInput")
    def privileges_input(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecPrivileges"]:
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecPrivileges"], jsii.get(self, "privilegesInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretsInput")
    def secrets_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecSecrets"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecContainerSpecSecrets"]]], jsii.get(self, "secretsInput"))

    @builtins.property
    @jsii.member(jsii_name="stopGracePeriodInput")
    def stop_grace_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stopGracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="stopSignalInput")
    def stop_signal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stopSignalInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d65a6afd404e5a7dff8f89aa58317c4bbe2bce704d96e546291932787c7920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="command")
    def command(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "command"))

    @command.setter
    def command(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41a92d99b7bd35dbb9ca18c8bcb289581c05f6b03a3279d60bfaccb2963e8e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "command", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dir")
    def dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dir"))

    @dir.setter
    def dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4005aed1e5df9556c37c69ac8a0cc67fa29b3d214b9b4f58efafbdb088adaad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dir", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504c82fbb5897df26fe5b3714617ba7310842e3a1b311ff13f9487b80abef517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ecd588061eb1f05c17d0bbb7a0225ee35cef716355939702eb69cbcbf8af003)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878aa2cb756f5cdf407087bf277a8e4c01d961e99f11bccf74d5b6fb5cdb4618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78eb59fa029123091747eaf79af1954764e1145dfae653bdb6acdbad31103ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isolation")
    def isolation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isolation"))

    @isolation.setter
    def isolation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf1112000eaa69e834221b8970acfff7663e9d4e49080f78972080afefbb2ac3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isolation", value) # pyright: ignore[reportArgumentType]

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
            type_hints = typing.get_type_hints(_typecheckingstub__f11a4b7d5fae07d47d064400ace846aa92b9536b94d41c7a9e519db304579495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stopGracePeriod")
    def stop_grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stopGracePeriod"))

    @stop_grace_period.setter
    def stop_grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e774403f91221d5dcb5e63986bcdebddba77203d8be24ab65a9ced1dee5d203a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopGracePeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="stopSignal")
    def stop_signal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stopSignal"))

    @stop_signal.setter
    def stop_signal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b50b823f2dce9d5cbf62fcd76d2bf148d5dec1c7e9b944cdb8df2e7a2fac94f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopSignal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393d5f247e3615541f6d85089f8f0feef42fcd97b49289975ee7d8fc5e278856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecContainerSpec]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96626279af5b0cc2b182b21ecb5287e017c6e38117b25de304d985a4ab50e77c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivileges",
    jsii_struct_bases=[],
    name_mapping={
        "credential_spec": "credentialSpec",
        "se_linux_context": "seLinuxContext",
    },
)
class ServiceTaskSpecContainerSpecPrivileges:
    def __init__(
        self,
        *,
        credential_spec: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecPrivilegesCredentialSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        se_linux_context: typing.Optional[typing.Union["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param credential_spec: credential_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#credential_spec Service#credential_spec}
        :param se_linux_context: se_linux_context block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#se_linux_context Service#se_linux_context}
        '''
        if isinstance(credential_spec, dict):
            credential_spec = ServiceTaskSpecContainerSpecPrivilegesCredentialSpec(**credential_spec)
        if isinstance(se_linux_context, dict):
            se_linux_context = ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext(**se_linux_context)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca38051962cf61632a82c270055a8c21333179224999c3d94199e7458e6f1f7)
            check_type(argname="argument credential_spec", value=credential_spec, expected_type=type_hints["credential_spec"])
            check_type(argname="argument se_linux_context", value=se_linux_context, expected_type=type_hints["se_linux_context"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if credential_spec is not None:
            self._values["credential_spec"] = credential_spec
        if se_linux_context is not None:
            self._values["se_linux_context"] = se_linux_context

    @builtins.property
    def credential_spec(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecPrivilegesCredentialSpec"]:
        '''credential_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#credential_spec Service#credential_spec}
        '''
        result = self._values.get("credential_spec")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecPrivilegesCredentialSpec"], result)

    @builtins.property
    def se_linux_context(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext"]:
        '''se_linux_context block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#se_linux_context Service#se_linux_context}
        '''
        result = self._values.get("se_linux_context")
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecPrivileges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivilegesCredentialSpec",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "registry": "registry"},
)
class ServiceTaskSpecContainerSpecPrivilegesCredentialSpec:
    def __init__(
        self,
        *,
        file: typing.Optional[builtins.str] = None,
        registry: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: Load credential spec from this file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file Service#file}
        :param registry: Load credential spec from this value in the Windows registry. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#registry Service#registry}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__583e5ff538ecebccdd77184bc5d48e67d26bc128e714664596b984d39327a541)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if registry is not None:
            self._values["registry"] = registry

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        '''Load credential spec from this file.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file Service#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry(self) -> typing.Optional[builtins.str]:
        '''Load credential spec from this value in the Windows registry.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#registry Service#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecPrivilegesCredentialSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecPrivilegesCredentialSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivilegesCredentialSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdbb27953799d56db00fa2a6a741c7e29a09856601b6e57560d8be9606fc010e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "file"))

    @file.setter
    def file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4106350ba57f4a424c7fd074914a050af0bdfc64232d7563438d2da629299269)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "file", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88208da60711a5028f75887a450d94c238b6441c55ae6a641cb2640fe2663024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5127b77e2bdb3a1b5311d5a940578743e43c4640c63b3376e7f5de19bdf43971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecPrivilegesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivilegesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef19fc3cb39271f29c20d494f44df7612abb8340e26bc46ead9db628b0ccff24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCredentialSpec")
    def put_credential_spec(
        self,
        *,
        file: typing.Optional[builtins.str] = None,
        registry: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file: Load credential spec from this file. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file Service#file}
        :param registry: Load credential spec from this value in the Windows registry. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#registry Service#registry}
        '''
        value = ServiceTaskSpecContainerSpecPrivilegesCredentialSpec(
            file=file, registry=registry
        )

        return typing.cast(None, jsii.invoke(self, "putCredentialSpec", [value]))

    @jsii.member(jsii_name="putSeLinuxContext")
    def put_se_linux_context(
        self,
        *,
        disable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        level: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disable: Disable SELinux. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#disable Service#disable}
        :param level: SELinux level label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#level Service#level}
        :param role: SELinux role label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#role Service#role}
        :param type: SELinux type label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#type Service#type}
        :param user: SELinux user label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        value = ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext(
            disable=disable, level=level, role=role, type=type, user=user
        )

        return typing.cast(None, jsii.invoke(self, "putSeLinuxContext", [value]))

    @jsii.member(jsii_name="resetCredentialSpec")
    def reset_credential_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialSpec", []))

    @jsii.member(jsii_name="resetSeLinuxContext")
    def reset_se_linux_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinuxContext", []))

    @builtins.property
    @jsii.member(jsii_name="credentialSpec")
    def credential_spec(
        self,
    ) -> ServiceTaskSpecContainerSpecPrivilegesCredentialSpecOutputReference:
        return typing.cast(ServiceTaskSpecContainerSpecPrivilegesCredentialSpecOutputReference, jsii.get(self, "credentialSpec"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxContext")
    def se_linux_context(
        self,
    ) -> "ServiceTaskSpecContainerSpecPrivilegesSeLinuxContextOutputReference":
        return typing.cast("ServiceTaskSpecContainerSpecPrivilegesSeLinuxContextOutputReference", jsii.get(self, "seLinuxContext"))

    @builtins.property
    @jsii.member(jsii_name="credentialSpecInput")
    def credential_spec_input(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec], jsii.get(self, "credentialSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxContextInput")
    def se_linux_context_input(
        self,
    ) -> typing.Optional["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext"]:
        return typing.cast(typing.Optional["ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext"], jsii.get(self, "seLinuxContextInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecContainerSpecPrivileges]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecPrivileges], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecPrivileges],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e657a3150fe577a62182bdc386338e7d77f6eaed2f2fe3663862159ae63fd745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext",
    jsii_struct_bases=[],
    name_mapping={
        "disable": "disable",
        "level": "level",
        "role": "role",
        "type": "type",
        "user": "user",
    },
)
class ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext:
    def __init__(
        self,
        *,
        disable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        level: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disable: Disable SELinux. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#disable Service#disable}
        :param level: SELinux level label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#level Service#level}
        :param role: SELinux role label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#role Service#role}
        :param type: SELinux type label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#type Service#type}
        :param user: SELinux user label. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__209751b4bdc209838c8ce85939a18a5e87dd1d78a26097469e460094297831be)
            check_type(argname="argument disable", value=disable, expected_type=type_hints["disable"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disable is not None:
            self._values["disable"] = disable
        if level is not None:
            self._values["level"] = level
        if role is not None:
            self._values["role"] = role
        if type is not None:
            self._values["type"] = type
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def disable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Disable SELinux.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#disable Service#disable}
        '''
        result = self._values.get("disable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''SELinux level label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#level Service#level}
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''SELinux role label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#role Service#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''SELinux type label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#type Service#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''SELinux user label.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecPrivilegesSeLinuxContextOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecPrivilegesSeLinuxContextOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a196b497b7bbc14393b6c342c5253c02aa871657f920c66933560417cbe3ce9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisable")
    def reset_disable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisable", []))

    @jsii.member(jsii_name="resetLevel")
    def reset_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevel", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="disableInput")
    def disable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableInput"))

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="disable")
    def disable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disable"))

    @disable.setter
    def disable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d39a70fd72ff39f83ebdeb5666a804ad0f57d61d98fc1a2684539247b9a8d9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4369687617f5eac861a66d86d13f45cfa69293cc6fc8bce7b2c0efe6d4b15fc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e6d388cbfe440cf2aa0a72e1dd0db6e088ae6c019e35053b436a449baed7e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ea17e908028deaf5220f74a525269342202fe5e7895b4ae49a02e0fcea0770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a64c3501f3bf1fe19b298a0009b737fb1429e8d49638dfc77df1f6deb921a9fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aab776a721ceff498560b15b6797c4184819f0ec14d046cf267bc0a533b7cb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecContainerSpecSecrets",
    jsii_struct_bases=[],
    name_mapping={
        "file_name": "fileName",
        "secret_id": "secretId",
        "file_gid": "fileGid",
        "file_mode": "fileMode",
        "file_uid": "fileUid",
        "secret_name": "secretName",
    },
)
class ServiceTaskSpecContainerSpecSecrets:
    def __init__(
        self,
        *,
        file_name: builtins.str,
        secret_id: builtins.str,
        file_gid: typing.Optional[builtins.str] = None,
        file_mode: typing.Optional[jsii.Number] = None,
        file_uid: typing.Optional[builtins.str] = None,
        secret_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param file_name: Represents the final filename in the filesystem. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_name Service#file_name}
        :param secret_id: ID of the specific secret that we're referencing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secret_id Service#secret_id}
        :param file_gid: Represents the file GID. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_gid Service#file_gid}
        :param file_mode: Represents represents the FileMode of the file. Defaults to ``0o444``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_mode Service#file_mode}
        :param file_uid: Represents the file UID. Defaults to ``0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_uid Service#file_uid}
        :param secret_name: Name of the secret that this references, but this is just provided for lookup/display purposes. The config in the reference will be identified by its ID Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secret_name Service#secret_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad99f66779cd9ce798811945331f60e9fff6dd106de12db64b9349fd21394ff0)
            check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
            check_type(argname="argument file_gid", value=file_gid, expected_type=type_hints["file_gid"])
            check_type(argname="argument file_mode", value=file_mode, expected_type=type_hints["file_mode"])
            check_type(argname="argument file_uid", value=file_uid, expected_type=type_hints["file_uid"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_name": file_name,
            "secret_id": secret_id,
        }
        if file_gid is not None:
            self._values["file_gid"] = file_gid
        if file_mode is not None:
            self._values["file_mode"] = file_mode
        if file_uid is not None:
            self._values["file_uid"] = file_uid
        if secret_name is not None:
            self._values["secret_name"] = secret_name

    @builtins.property
    def file_name(self) -> builtins.str:
        '''Represents the final filename in the filesystem.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_name Service#file_name}
        '''
        result = self._values.get("file_name")
        assert result is not None, "Required property 'file_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''ID of the specific secret that we're referencing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secret_id Service#secret_id}
        '''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_gid(self) -> typing.Optional[builtins.str]:
        '''Represents the file GID. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_gid Service#file_gid}
        '''
        result = self._values.get("file_gid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_mode(self) -> typing.Optional[jsii.Number]:
        '''Represents represents the FileMode of the file. Defaults to ``0o444``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_mode Service#file_mode}
        '''
        result = self._values.get("file_mode")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def file_uid(self) -> typing.Optional[builtins.str]:
        '''Represents the file UID. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#file_uid Service#file_uid}
        '''
        result = self._values.get("file_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_name(self) -> typing.Optional[builtins.str]:
        '''Name of the secret that this references, but this is just provided for lookup/display purposes.

        The config in the reference will be identified by its ID

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secret_name Service#secret_name}
        '''
        result = self._values.get("secret_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecContainerSpecSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecContainerSpecSecretsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecSecretsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3eb9337958335abb003bd219e7d924b15956d474599a894e4eaaa99caa53659a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecContainerSpecSecretsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5a9dc81889a4ef5a7c840bd12b62609b988a0af8bfd4cd187319d753d51ed0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecContainerSpecSecretsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07d2b716959a179eb310c03933acb44b2d08eea6d8d02c83bb28e0447be3ec93)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b3f08c79ff7e95e4ef15f255190339575beef10885d48305225d0417f52a35c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8efef47f2463ecf5f56e5fb0c32b3e580d0c0fe8c303ae063821f722166a9894)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecSecrets]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecSecrets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecSecrets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93e25d8b4c413e201b4bf6f6b853a094479ff6afcf58d5a950ddf624d198df6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecContainerSpecSecretsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecContainerSpecSecretsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__488ff8a1e98c6d7a975d88610f3a87e466dfe757266f948f52a617507828f482)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFileGid")
    def reset_file_gid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileGid", []))

    @jsii.member(jsii_name="resetFileMode")
    def reset_file_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileMode", []))

    @jsii.member(jsii_name="resetFileUid")
    def reset_file_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUid", []))

    @jsii.member(jsii_name="resetSecretName")
    def reset_secret_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretName", []))

    @builtins.property
    @jsii.member(jsii_name="fileGidInput")
    def file_gid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileGidInput"))

    @builtins.property
    @jsii.member(jsii_name="fileModeInput")
    def file_mode_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fileModeInput"))

    @builtins.property
    @jsii.member(jsii_name="fileNameInput")
    def file_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUidInput")
    def file_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileUidInput"))

    @builtins.property
    @jsii.member(jsii_name="secretIdInput")
    def secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fileGid")
    def file_gid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileGid"))

    @file_gid.setter
    def file_gid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b159f849de1274b59fb1d6abb1427ff1214aa41f93ce30e3a6fac242081a0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileGid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileMode")
    def file_mode(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fileMode"))

    @file_mode.setter
    def file_mode(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1217be6aeb979f4b9a5e83a637c33228e14356b750cec3d3fc270e94f82c9d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileName")
    def file_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileName"))

    @file_name.setter
    def file_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2200af58ea72fe762bcb77a9d0e30d2e8916c6fee6bb9cb2bf7003c9b0d26200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileUid")
    def file_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileUid"))

    @file_uid.setter
    def file_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2a3aabaabbe1db407ea24aaa618ca8525120ea123e16b267a57fbeef9550dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secretId")
    def secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretId"))

    @secret_id.setter
    def secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50030d1d91d3172fbd5e70766f271d5d46991e1bba845b5a0ea9db1812c5023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d61012d82b22473e66fa0b4d1c77d0459495fa4488604ee1975ac1ba99fceb97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecSecrets]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecSecrets]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecSecrets]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d13520f63daa78c02ac60cc78f78bcfa58739161e797492a56dac99057ccc1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecLogDriver",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "options": "options"},
)
class ServiceTaskSpecLogDriver:
    def __init__(
        self,
        *,
        name: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: The logging driver to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        :param options: The options for the logging driver. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3022c257263e46ab6959fed7d002af4014d88de9cb8401b713bb40f2fa4d065)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if options is not None:
            self._values["options"] = options

    @builtins.property
    def name(self) -> builtins.str:
        '''The logging driver to use.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The options for the logging driver.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecLogDriver(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecLogDriverOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecLogDriverOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__885e32a7da035fa81f5c46448d3e1ac5d29c88e37391d352c11a1b7192739f20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a66aff319f7fe4637525825b52e5c6e83ca23330952c856fcf77ee1f1fd6feb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1badb2e1bf9baef8469c848f462c91b3c2263af3b90a36fc208f693919ead256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecLogDriver]:
        return typing.cast(typing.Optional[ServiceTaskSpecLogDriver], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceTaskSpecLogDriver]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f93b4a5018c2a59a696f1bf5c76e5be337258bda11689603fe36c075f62174f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba3cde21110c3c577d2d1126be878f449913ce381e999a8ecb08dd3ae5226ee8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContainerSpec")
    def put_container_spec(
        self,
        *,
        image: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
        dir: typing.Optional[builtins.str] = None,
        dns_config: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecDnsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        healthcheck: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecHealthcheck, typing.Dict[builtins.str, typing.Any]]] = None,
        hostname: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecHosts, typing.Dict[builtins.str, typing.Any]]]]] = None,
        isolation: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
        mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMounts, typing.Dict[builtins.str, typing.Any]]]]] = None,
        privileges: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecPrivileges, typing.Dict[builtins.str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecSecrets, typing.Dict[builtins.str, typing.Any]]]]] = None,
        stop_grace_period: typing.Optional[builtins.str] = None,
        stop_signal: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The image name to use for the containers of the service, like ``nginx:1.17.6``. Also use the data-source or resource of ``docker_image`` with the ``repo_digest`` or ``docker_registry_image`` with the ``name`` attribute for this, as shown in the examples. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#image Service#image}
        :param args: Arguments to the command. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#args Service#args}
        :param command: The command/entrypoint to be run in the image. According to the `docker cli <https://github.com/docker/cli/blob/v20.10.7/cli/command/service/opts.go#L705>`_ the override of the entrypoint is also passed to the ``command`` property and there is no ``entrypoint`` attribute in the ``ContainerSpec`` of the service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#command Service#command}
        :param configs: configs block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#configs Service#configs}
        :param dir: The working directory for commands to run in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dir Service#dir}
        :param dns_config: dns_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#dns_config Service#dns_config}
        :param env: A list of environment variables in the form VAR="value". Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#env Service#env}
        :param groups: A list of additional groups that the container process will run as. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#groups Service#groups}
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#healthcheck Service#healthcheck}
        :param hostname: The hostname to use for the container, as a valid RFC 1123 hostname. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hostname Service#hostname}
        :param hosts: hosts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#hosts Service#hosts}
        :param isolation: Isolation technology of the containers running the service. (Windows only). Defaults to ``default``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#isolation Service#isolation}
        :param labels: labels block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#labels Service#labels}
        :param mounts: mounts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#mounts Service#mounts}
        :param privileges: privileges block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#privileges Service#privileges}
        :param read_only: Mount the container's root filesystem as read only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#read_only Service#read_only}
        :param secrets: secrets block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#secrets Service#secrets}
        :param stop_grace_period: Amount of time to wait for the container to terminate before forcefully removing it (ms|s|m|h). If not specified or '0s' the destroy will not check if all tasks/containers of the service terminate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_grace_period Service#stop_grace_period}
        :param stop_signal: Signal to stop the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#stop_signal Service#stop_signal}
        :param user: The user inside the container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#user Service#user}
        '''
        value = ServiceTaskSpecContainerSpec(
            image=image,
            args=args,
            command=command,
            configs=configs,
            dir=dir,
            dns_config=dns_config,
            env=env,
            groups=groups,
            healthcheck=healthcheck,
            hostname=hostname,
            hosts=hosts,
            isolation=isolation,
            labels=labels,
            mounts=mounts,
            privileges=privileges,
            read_only=read_only,
            secrets=secrets,
            stop_grace_period=stop_grace_period,
            stop_signal=stop_signal,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putContainerSpec", [value]))

    @jsii.member(jsii_name="putLogDriver")
    def put_log_driver(
        self,
        *,
        name: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param name: The logging driver to use. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#name Service#name}
        :param options: The options for the logging driver. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#options Service#options}
        '''
        value = ServiceTaskSpecLogDriver(name=name, options=options)

        return typing.cast(None, jsii.invoke(self, "putLogDriver", [value]))

    @jsii.member(jsii_name="putPlacement")
    def put_placement(
        self,
        *,
        constraints: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_replicas: typing.Optional[jsii.Number] = None,
        platforms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecPlacementPlatforms", typing.Dict[builtins.str, typing.Any]]]]] = None,
        prefs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param constraints: An array of constraints. e.g.: ``node.role==manager``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#constraints Service#constraints}
        :param max_replicas: Maximum number of replicas for per node (default value is ``0``, which is unlimited). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_replicas Service#max_replicas}
        :param platforms: platforms block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#platforms Service#platforms}
        :param prefs: Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: ``spread=node.role.manager`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#prefs Service#prefs}
        '''
        value = ServiceTaskSpecPlacement(
            constraints=constraints,
            max_replicas=max_replicas,
            platforms=platforms,
            prefs=prefs,
        )

        return typing.cast(None, jsii.invoke(self, "putPlacement", [value]))

    @jsii.member(jsii_name="putResources")
    def put_resources(
        self,
        *,
        limits: typing.Optional[typing.Union["ServiceTaskSpecResourcesLimits", typing.Dict[builtins.str, typing.Any]]] = None,
        reservation: typing.Optional[typing.Union["ServiceTaskSpecResourcesReservation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param limits: limits block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#limits Service#limits}
        :param reservation: reservation block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#reservation Service#reservation}
        '''
        value = ServiceTaskSpecResources(limits=limits, reservation=reservation)

        return typing.cast(None, jsii.invoke(self, "putResources", [value]))

    @jsii.member(jsii_name="putRestartPolicy")
    def put_restart_policy(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        delay: typing.Optional[builtins.str] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param condition: Condition for restart. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#condition Service#condition}
        :param delay: Delay between restart attempts (ms|s|m|h). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param max_attempts: Maximum attempts to restart a given container before giving up (default value is ``0``, which is ignored). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_attempts Service#max_attempts}
        :param window: The time window used to evaluate the restart policy (default value is ``0``, which is unbounded) (ms|s|m|h). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#window Service#window}
        '''
        value = ServiceTaskSpecRestartPolicy(
            condition=condition, delay=delay, max_attempts=max_attempts, window=window
        )

        return typing.cast(None, jsii.invoke(self, "putRestartPolicy", [value]))

    @jsii.member(jsii_name="resetForceUpdate")
    def reset_force_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceUpdate", []))

    @jsii.member(jsii_name="resetLogDriver")
    def reset_log_driver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDriver", []))

    @jsii.member(jsii_name="resetNetworks")
    def reset_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworks", []))

    @jsii.member(jsii_name="resetPlacement")
    def reset_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacement", []))

    @jsii.member(jsii_name="resetResources")
    def reset_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResources", []))

    @jsii.member(jsii_name="resetRestartPolicy")
    def reset_restart_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestartPolicy", []))

    @jsii.member(jsii_name="resetRuntime")
    def reset_runtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRuntime", []))

    @builtins.property
    @jsii.member(jsii_name="containerSpec")
    def container_spec(self) -> ServiceTaskSpecContainerSpecOutputReference:
        return typing.cast(ServiceTaskSpecContainerSpecOutputReference, jsii.get(self, "containerSpec"))

    @builtins.property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> ServiceTaskSpecLogDriverOutputReference:
        return typing.cast(ServiceTaskSpecLogDriverOutputReference, jsii.get(self, "logDriver"))

    @builtins.property
    @jsii.member(jsii_name="placement")
    def placement(self) -> "ServiceTaskSpecPlacementOutputReference":
        return typing.cast("ServiceTaskSpecPlacementOutputReference", jsii.get(self, "placement"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "ServiceTaskSpecResourcesOutputReference":
        return typing.cast("ServiceTaskSpecResourcesOutputReference", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="restartPolicy")
    def restart_policy(self) -> "ServiceTaskSpecRestartPolicyOutputReference":
        return typing.cast("ServiceTaskSpecRestartPolicyOutputReference", jsii.get(self, "restartPolicy"))

    @builtins.property
    @jsii.member(jsii_name="containerSpecInput")
    def container_spec_input(self) -> typing.Optional[ServiceTaskSpecContainerSpec]:
        return typing.cast(typing.Optional[ServiceTaskSpecContainerSpec], jsii.get(self, "containerSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="forceUpdateInput")
    def force_update_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "forceUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="logDriverInput")
    def log_driver_input(self) -> typing.Optional[ServiceTaskSpecLogDriver]:
        return typing.cast(typing.Optional[ServiceTaskSpecLogDriver], jsii.get(self, "logDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="placementInput")
    def placement_input(self) -> typing.Optional["ServiceTaskSpecPlacement"]:
        return typing.cast(typing.Optional["ServiceTaskSpecPlacement"], jsii.get(self, "placementInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(self) -> typing.Optional["ServiceTaskSpecResources"]:
        return typing.cast(typing.Optional["ServiceTaskSpecResources"], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="restartPolicyInput")
    def restart_policy_input(self) -> typing.Optional["ServiceTaskSpecRestartPolicy"]:
        return typing.cast(typing.Optional["ServiceTaskSpecRestartPolicy"], jsii.get(self, "restartPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="runtimeInput")
    def runtime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="forceUpdate")
    def force_update(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "forceUpdate"))

    @force_update.setter
    def force_update(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cbe6160723186b98cf9f7adb99b0ef2d5be8ab0acba30a00b550e73ee02ac6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networks"))

    @networks.setter
    def networks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5744bbce9bbd500870a89258b0b30988eddc1ab0f58377abaa8a9bafaf84d5af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd2a0f5517896babeb5bff2d7759f8df6eefd7776826f384a3f95c48a4da67b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpec]:
        return typing.cast(typing.Optional[ServiceTaskSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceTaskSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f646d3d0a3210fe0eb19055876c1886b54dff3d3d9aa6d68e1c1e411082a6c0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecPlacement",
    jsii_struct_bases=[],
    name_mapping={
        "constraints": "constraints",
        "max_replicas": "maxReplicas",
        "platforms": "platforms",
        "prefs": "prefs",
    },
)
class ServiceTaskSpecPlacement:
    def __init__(
        self,
        *,
        constraints: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_replicas: typing.Optional[jsii.Number] = None,
        platforms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecPlacementPlatforms", typing.Dict[builtins.str, typing.Any]]]]] = None,
        prefs: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param constraints: An array of constraints. e.g.: ``node.role==manager``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#constraints Service#constraints}
        :param max_replicas: Maximum number of replicas for per node (default value is ``0``, which is unlimited). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_replicas Service#max_replicas}
        :param platforms: platforms block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#platforms Service#platforms}
        :param prefs: Preferences provide a way to make the scheduler aware of factors such as topology. They are provided in order from highest to lowest precedence, e.g.: ``spread=node.role.manager`` Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#prefs Service#prefs}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fff629f2991668ecf74fb12935c5a6de8f475f9838362db350be2f221d91d3)
            check_type(argname="argument constraints", value=constraints, expected_type=type_hints["constraints"])
            check_type(argname="argument max_replicas", value=max_replicas, expected_type=type_hints["max_replicas"])
            check_type(argname="argument platforms", value=platforms, expected_type=type_hints["platforms"])
            check_type(argname="argument prefs", value=prefs, expected_type=type_hints["prefs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if constraints is not None:
            self._values["constraints"] = constraints
        if max_replicas is not None:
            self._values["max_replicas"] = max_replicas
        if platforms is not None:
            self._values["platforms"] = platforms
        if prefs is not None:
            self._values["prefs"] = prefs

    @builtins.property
    def constraints(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of constraints. e.g.: ``node.role==manager``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#constraints Service#constraints}
        '''
        result = self._values.get("constraints")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_replicas(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of replicas for per node (default value is ``0``, which is unlimited).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_replicas Service#max_replicas}
        '''
        result = self._values.get("max_replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def platforms(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecPlacementPlatforms"]]]:
        '''platforms block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#platforms Service#platforms}
        '''
        result = self._values.get("platforms")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecPlacementPlatforms"]]], result)

    @builtins.property
    def prefs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Preferences provide a way to make the scheduler aware of factors such as topology.

        They are provided in order from highest to lowest precedence, e.g.: ``spread=node.role.manager``

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#prefs Service#prefs}
        '''
        result = self._values.get("prefs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecPlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecPlacementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecPlacementOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a7995c63fb15e188fe9d9f8800ebdf1cd6270fa0111d7f62c874eceef5f77ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPlatforms")
    def put_platforms(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ServiceTaskSpecPlacementPlatforms", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__015f7603489f85331a2077a0e7d7a1f501d11e8fb304a0e3c48895b80adb2b41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlatforms", [value]))

    @jsii.member(jsii_name="resetConstraints")
    def reset_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConstraints", []))

    @jsii.member(jsii_name="resetMaxReplicas")
    def reset_max_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxReplicas", []))

    @jsii.member(jsii_name="resetPlatforms")
    def reset_platforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatforms", []))

    @jsii.member(jsii_name="resetPrefs")
    def reset_prefs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefs", []))

    @builtins.property
    @jsii.member(jsii_name="platforms")
    def platforms(self) -> "ServiceTaskSpecPlacementPlatformsList":
        return typing.cast("ServiceTaskSpecPlacementPlatformsList", jsii.get(self, "platforms"))

    @builtins.property
    @jsii.member(jsii_name="constraintsInput")
    def constraints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "constraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicasInput")
    def max_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="platformsInput")
    def platforms_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecPlacementPlatforms"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ServiceTaskSpecPlacementPlatforms"]]], jsii.get(self, "platformsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefsInput")
    def prefs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "prefsInput"))

    @builtins.property
    @jsii.member(jsii_name="constraints")
    def constraints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "constraints"))

    @constraints.setter
    def constraints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdc5e82d798ed63e77e9917b0863f7fc86e8f84c679b752b7293d8a6cf724059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constraints", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxReplicas")
    def max_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxReplicas"))

    @max_replicas.setter
    def max_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15fe6547d12fb1caabad0323207d85de8b06188f86c09970c3202225b2ecd382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxReplicas", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="prefs")
    def prefs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "prefs"))

    @prefs.setter
    def prefs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aaaaf7f266d9097cff1bc4bee4ded4a892aade54a043aaa88fe6e4b04af6031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecPlacement]:
        return typing.cast(typing.Optional[ServiceTaskSpecPlacement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceTaskSpecPlacement]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de775fa17024aada62d2f45297c1d79feb976d295af82426ec56a18ebfafcae7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecPlacementPlatforms",
    jsii_struct_bases=[],
    name_mapping={"architecture": "architecture", "os": "os"},
)
class ServiceTaskSpecPlacementPlatforms:
    def __init__(self, *, architecture: builtins.str, os: builtins.str) -> None:
        '''
        :param architecture: The architecture, e.g. ``amd64``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#architecture Service#architecture}
        :param os: The operation system, e.g. ``linux``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#os Service#os}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367c31c9175b8f3b2d8d8dee33a9190c952e7dd0a07e114118a4777c3e6ed4c9)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "architecture": architecture,
            "os": os,
        }

    @builtins.property
    def architecture(self) -> builtins.str:
        '''The architecture, e.g. ``amd64``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#architecture Service#architecture}
        '''
        result = self._values.get("architecture")
        assert result is not None, "Required property 'architecture' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def os(self) -> builtins.str:
        '''The operation system, e.g. ``linux``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#os Service#os}
        '''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecPlacementPlatforms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecPlacementPlatformsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecPlacementPlatformsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e70bf80d5d4417a7bdbe34812f10d29a741cc533e5d367289468d1dd3fc5ed1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceTaskSpecPlacementPlatformsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82b560f9329e847da6bf93f2a0327a1ded568b48aefdebfb848e66c50c944950)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceTaskSpecPlacementPlatformsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ccde0210369664ac9660fcd8c02ee854e478e76934596464cbdd43e680ac06)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5cecb1e81647d3763307d274101ebeb01d2b0d66c610695a0fa2d53a5c0340b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b46694df1ff45257b34ec511746bc998cc45e0a5fc644930a33dbee0cf336a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecPlacementPlatforms]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecPlacementPlatforms]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecPlacementPlatforms]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98f214a99b38dbb502e56568235e84b4df3fa8e6455c9cb4c6bcd5be8a17ee48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecPlacementPlatformsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecPlacementPlatformsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__223fe2ff6bcec9ef2c3c75ed46f0b975dba38be8ab07a03a65eb4d85c7a067be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="architectureInput")
    def architecture_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architectureInput"))

    @builtins.property
    @jsii.member(jsii_name="osInput")
    def os_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osInput"))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d49a4bcde6d1549ca97a835c34fa303ef8b0bbda20c94ccccf6d2c996f56497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="os")
    def os(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "os"))

    @os.setter
    def os(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aaf265ab7a1b1909ef78fd518099cc423115cfd933f497415dd3a2325662011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "os", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecPlacementPlatforms]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecPlacementPlatforms]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecPlacementPlatforms]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3198bfd39908323dda47daa7663856233b01e4eae54d3113356649ae376552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecResources",
    jsii_struct_bases=[],
    name_mapping={"limits": "limits", "reservation": "reservation"},
)
class ServiceTaskSpecResources:
    def __init__(
        self,
        *,
        limits: typing.Optional[typing.Union["ServiceTaskSpecResourcesLimits", typing.Dict[builtins.str, typing.Any]]] = None,
        reservation: typing.Optional[typing.Union["ServiceTaskSpecResourcesReservation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param limits: limits block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#limits Service#limits}
        :param reservation: reservation block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#reservation Service#reservation}
        '''
        if isinstance(limits, dict):
            limits = ServiceTaskSpecResourcesLimits(**limits)
        if isinstance(reservation, dict):
            reservation = ServiceTaskSpecResourcesReservation(**reservation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9b45d5c787b7d5215af7796de52c8ed1b384453da5148fb37431b5e2092662)
            check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            check_type(argname="argument reservation", value=reservation, expected_type=type_hints["reservation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if limits is not None:
            self._values["limits"] = limits
        if reservation is not None:
            self._values["reservation"] = reservation

    @builtins.property
    def limits(self) -> typing.Optional["ServiceTaskSpecResourcesLimits"]:
        '''limits block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#limits Service#limits}
        '''
        result = self._values.get("limits")
        return typing.cast(typing.Optional["ServiceTaskSpecResourcesLimits"], result)

    @builtins.property
    def reservation(self) -> typing.Optional["ServiceTaskSpecResourcesReservation"]:
        '''reservation block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#reservation Service#reservation}
        '''
        result = self._values.get("reservation")
        return typing.cast(typing.Optional["ServiceTaskSpecResourcesReservation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecResourcesLimits",
    jsii_struct_bases=[],
    name_mapping={"memory_bytes": "memoryBytes", "nano_cpus": "nanoCpus"},
)
class ServiceTaskSpecResourcesLimits:
    def __init__(
        self,
        *,
        memory_bytes: typing.Optional[jsii.Number] = None,
        nano_cpus: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param memory_bytes: The amounf of memory in bytes the container allocates. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        :param nano_cpus: CPU shares in units of ``1/1e9`` (or ``10^-9``) of the CPU. Should be at least ``1000000``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae7cec76250c146e291f3c3268d473e0224565755d16744c5906bed71548fc3)
            check_type(argname="argument memory_bytes", value=memory_bytes, expected_type=type_hints["memory_bytes"])
            check_type(argname="argument nano_cpus", value=nano_cpus, expected_type=type_hints["nano_cpus"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if memory_bytes is not None:
            self._values["memory_bytes"] = memory_bytes
        if nano_cpus is not None:
            self._values["nano_cpus"] = nano_cpus

    @builtins.property
    def memory_bytes(self) -> typing.Optional[jsii.Number]:
        '''The amounf of memory in bytes the container allocates.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        '''
        result = self._values.get("memory_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nano_cpus(self) -> typing.Optional[jsii.Number]:
        '''CPU shares in units of ``1/1e9`` (or ``10^-9``) of the CPU. Should be at least ``1000000``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        result = self._values.get("nano_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecResourcesLimits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecResourcesLimitsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecResourcesLimitsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9bb5a06653f767cf723ac24991169bf3b428f3e4b1a4274be0a82d1d185b86e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMemoryBytes")
    def reset_memory_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryBytes", []))

    @jsii.member(jsii_name="resetNanoCpus")
    def reset_nano_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanoCpus", []))

    @builtins.property
    @jsii.member(jsii_name="memoryBytesInput")
    def memory_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="nanoCpusInput")
    def nano_cpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanoCpusInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryBytes")
    def memory_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryBytes"))

    @memory_bytes.setter
    def memory_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab521f058cf60d27fdb987e23988b5b2ec5355fad2380122e1cd90061b2d2aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="nanoCpus")
    def nano_cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanoCpus"))

    @nano_cpus.setter
    def nano_cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c932bae813f326d49389e4011bb4fd1cf11a7d1c161cddaadc5afa2f787a60fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanoCpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecResourcesLimits]:
        return typing.cast(typing.Optional[ServiceTaskSpecResourcesLimits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecResourcesLimits],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e45647de2b4d627ed733ae32d34fa61b8420c7320286fcab2e39bbae38651e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__011f2cd779878c4d398c9432f09975891bbfb455ec9bae42bd57a805c46d8be5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLimits")
    def put_limits(
        self,
        *,
        memory_bytes: typing.Optional[jsii.Number] = None,
        nano_cpus: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param memory_bytes: The amounf of memory in bytes the container allocates. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        :param nano_cpus: CPU shares in units of ``1/1e9`` (or ``10^-9``) of the CPU. Should be at least ``1000000``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        value = ServiceTaskSpecResourcesLimits(
            memory_bytes=memory_bytes, nano_cpus=nano_cpus
        )

        return typing.cast(None, jsii.invoke(self, "putLimits", [value]))

    @jsii.member(jsii_name="putReservation")
    def put_reservation(
        self,
        *,
        generic_resources: typing.Optional[typing.Union["ServiceTaskSpecResourcesReservationGenericResources", typing.Dict[builtins.str, typing.Any]]] = None,
        memory_bytes: typing.Optional[jsii.Number] = None,
        nano_cpus: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param generic_resources: generic_resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#generic_resources Service#generic_resources}
        :param memory_bytes: The amounf of memory in bytes the container allocates. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        :param nano_cpus: CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least ``1000000``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        value = ServiceTaskSpecResourcesReservation(
            generic_resources=generic_resources,
            memory_bytes=memory_bytes,
            nano_cpus=nano_cpus,
        )

        return typing.cast(None, jsii.invoke(self, "putReservation", [value]))

    @jsii.member(jsii_name="resetLimits")
    def reset_limits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLimits", []))

    @jsii.member(jsii_name="resetReservation")
    def reset_reservation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservation", []))

    @builtins.property
    @jsii.member(jsii_name="limits")
    def limits(self) -> ServiceTaskSpecResourcesLimitsOutputReference:
        return typing.cast(ServiceTaskSpecResourcesLimitsOutputReference, jsii.get(self, "limits"))

    @builtins.property
    @jsii.member(jsii_name="reservation")
    def reservation(self) -> "ServiceTaskSpecResourcesReservationOutputReference":
        return typing.cast("ServiceTaskSpecResourcesReservationOutputReference", jsii.get(self, "reservation"))

    @builtins.property
    @jsii.member(jsii_name="limitsInput")
    def limits_input(self) -> typing.Optional[ServiceTaskSpecResourcesLimits]:
        return typing.cast(typing.Optional[ServiceTaskSpecResourcesLimits], jsii.get(self, "limitsInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationInput")
    def reservation_input(
        self,
    ) -> typing.Optional["ServiceTaskSpecResourcesReservation"]:
        return typing.cast(typing.Optional["ServiceTaskSpecResourcesReservation"], jsii.get(self, "reservationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecResources]:
        return typing.cast(typing.Optional[ServiceTaskSpecResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceTaskSpecResources]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3358546eb8c0437b841d9d251dc88fe0f37ea2ae873feede82be8ea261fd7c85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecResourcesReservation",
    jsii_struct_bases=[],
    name_mapping={
        "generic_resources": "genericResources",
        "memory_bytes": "memoryBytes",
        "nano_cpus": "nanoCpus",
    },
)
class ServiceTaskSpecResourcesReservation:
    def __init__(
        self,
        *,
        generic_resources: typing.Optional[typing.Union["ServiceTaskSpecResourcesReservationGenericResources", typing.Dict[builtins.str, typing.Any]]] = None,
        memory_bytes: typing.Optional[jsii.Number] = None,
        nano_cpus: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param generic_resources: generic_resources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#generic_resources Service#generic_resources}
        :param memory_bytes: The amounf of memory in bytes the container allocates. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        :param nano_cpus: CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least ``1000000``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        if isinstance(generic_resources, dict):
            generic_resources = ServiceTaskSpecResourcesReservationGenericResources(**generic_resources)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18186dc55c233aa6f8f3d7ea56679bc38bee8f910f05405a112b3740b119826f)
            check_type(argname="argument generic_resources", value=generic_resources, expected_type=type_hints["generic_resources"])
            check_type(argname="argument memory_bytes", value=memory_bytes, expected_type=type_hints["memory_bytes"])
            check_type(argname="argument nano_cpus", value=nano_cpus, expected_type=type_hints["nano_cpus"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if generic_resources is not None:
            self._values["generic_resources"] = generic_resources
        if memory_bytes is not None:
            self._values["memory_bytes"] = memory_bytes
        if nano_cpus is not None:
            self._values["nano_cpus"] = nano_cpus

    @builtins.property
    def generic_resources(
        self,
    ) -> typing.Optional["ServiceTaskSpecResourcesReservationGenericResources"]:
        '''generic_resources block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#generic_resources Service#generic_resources}
        '''
        result = self._values.get("generic_resources")
        return typing.cast(typing.Optional["ServiceTaskSpecResourcesReservationGenericResources"], result)

    @builtins.property
    def memory_bytes(self) -> typing.Optional[jsii.Number]:
        '''The amounf of memory in bytes the container allocates.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#memory_bytes Service#memory_bytes}
        '''
        result = self._values.get("memory_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def nano_cpus(self) -> typing.Optional[jsii.Number]:
        '''CPU shares in units of 1/1e9 (or 10^-9) of the CPU. Should be at least ``1000000``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#nano_cpus Service#nano_cpus}
        '''
        result = self._values.get("nano_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecResourcesReservation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecResourcesReservationGenericResources",
    jsii_struct_bases=[],
    name_mapping={
        "discrete_resources_spec": "discreteResourcesSpec",
        "named_resources_spec": "namedResourcesSpec",
    },
)
class ServiceTaskSpecResourcesReservationGenericResources:
    def __init__(
        self,
        *,
        discrete_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
        named_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param discrete_resources_spec: The Integer resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#discrete_resources_spec Service#discrete_resources_spec}
        :param named_resources_spec: The String resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#named_resources_spec Service#named_resources_spec}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6030acd814dc6d6ee9cdce790053d8b30a66deae59cdb17151c4342eb558357)
            check_type(argname="argument discrete_resources_spec", value=discrete_resources_spec, expected_type=type_hints["discrete_resources_spec"])
            check_type(argname="argument named_resources_spec", value=named_resources_spec, expected_type=type_hints["named_resources_spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if discrete_resources_spec is not None:
            self._values["discrete_resources_spec"] = discrete_resources_spec
        if named_resources_spec is not None:
            self._values["named_resources_spec"] = named_resources_spec

    @builtins.property
    def discrete_resources_spec(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Integer resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#discrete_resources_spec Service#discrete_resources_spec}
        '''
        result = self._values.get("discrete_resources_spec")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def named_resources_spec(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The String resources.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#named_resources_spec Service#named_resources_spec}
        '''
        result = self._values.get("named_resources_spec")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecResourcesReservationGenericResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecResourcesReservationGenericResourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecResourcesReservationGenericResourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e3e1f0ef86939b7a5aa5e7a06ffce7cdb3ba7a61a72826ee05e0a2a339ff02d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDiscreteResourcesSpec")
    def reset_discrete_resources_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscreteResourcesSpec", []))

    @jsii.member(jsii_name="resetNamedResourcesSpec")
    def reset_named_resources_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamedResourcesSpec", []))

    @builtins.property
    @jsii.member(jsii_name="discreteResourcesSpecInput")
    def discrete_resources_spec_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "discreteResourcesSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="namedResourcesSpecInput")
    def named_resources_spec_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "namedResourcesSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="discreteResourcesSpec")
    def discrete_resources_spec(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "discreteResourcesSpec"))

    @discrete_resources_spec.setter
    def discrete_resources_spec(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0eff52c541163d6865abaecb10c7e40d78ef9a0efede8a1b8703633f0134e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discreteResourcesSpec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namedResourcesSpec")
    def named_resources_spec(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "namedResourcesSpec"))

    @named_resources_spec.setter
    def named_resources_spec(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa923d082c5704821df7d599389f7aff3f1b75b0f85d23e64acb303a5bdfb67f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namedResourcesSpec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceTaskSpecResourcesReservationGenericResources]:
        return typing.cast(typing.Optional[ServiceTaskSpecResourcesReservationGenericResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecResourcesReservationGenericResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__941bf0429463aad7755eda69ecd565c0e6743d79606c61d838b22f94d8e656da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class ServiceTaskSpecResourcesReservationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecResourcesReservationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af9794bf26c8e2cde71e32b3ec85edf87a9aa2f28e6289fc6802ecec0bf41222)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGenericResources")
    def put_generic_resources(
        self,
        *,
        discrete_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
        named_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param discrete_resources_spec: The Integer resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#discrete_resources_spec Service#discrete_resources_spec}
        :param named_resources_spec: The String resources. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#named_resources_spec Service#named_resources_spec}
        '''
        value = ServiceTaskSpecResourcesReservationGenericResources(
            discrete_resources_spec=discrete_resources_spec,
            named_resources_spec=named_resources_spec,
        )

        return typing.cast(None, jsii.invoke(self, "putGenericResources", [value]))

    @jsii.member(jsii_name="resetGenericResources")
    def reset_generic_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenericResources", []))

    @jsii.member(jsii_name="resetMemoryBytes")
    def reset_memory_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryBytes", []))

    @jsii.member(jsii_name="resetNanoCpus")
    def reset_nano_cpus(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNanoCpus", []))

    @builtins.property
    @jsii.member(jsii_name="genericResources")
    def generic_resources(
        self,
    ) -> ServiceTaskSpecResourcesReservationGenericResourcesOutputReference:
        return typing.cast(ServiceTaskSpecResourcesReservationGenericResourcesOutputReference, jsii.get(self, "genericResources"))

    @builtins.property
    @jsii.member(jsii_name="genericResourcesInput")
    def generic_resources_input(
        self,
    ) -> typing.Optional[ServiceTaskSpecResourcesReservationGenericResources]:
        return typing.cast(typing.Optional[ServiceTaskSpecResourcesReservationGenericResources], jsii.get(self, "genericResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryBytesInput")
    def memory_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memoryBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="nanoCpusInput")
    def nano_cpus_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nanoCpusInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryBytes")
    def memory_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memoryBytes"))

    @memory_bytes.setter
    def memory_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a47f11d3ab2216dfaeffa6270dc61eb6a8ce44344668ff00131e4a0f0013ba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryBytes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="nanoCpus")
    def nano_cpus(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nanoCpus"))

    @nano_cpus.setter
    def nano_cpus(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86fcba21192f418a9d4a36342c7d4c6d7f8b3d982a90120dfea2d6091b5e826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nanoCpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecResourcesReservation]:
        return typing.cast(typing.Optional[ServiceTaskSpecResourcesReservation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecResourcesReservation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d15bd681dd6b1a1b53571055cccefc26298eb637ef11751aeab943ca1d6f73b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceTaskSpecRestartPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "delay": "delay",
        "max_attempts": "maxAttempts",
        "window": "window",
    },
)
class ServiceTaskSpecRestartPolicy:
    def __init__(
        self,
        *,
        condition: typing.Optional[builtins.str] = None,
        delay: typing.Optional[builtins.str] = None,
        max_attempts: typing.Optional[jsii.Number] = None,
        window: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param condition: Condition for restart. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#condition Service#condition}
        :param delay: Delay between restart attempts (ms|s|m|h). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param max_attempts: Maximum attempts to restart a given container before giving up (default value is ``0``, which is ignored). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_attempts Service#max_attempts}
        :param window: The time window used to evaluate the restart policy (default value is ``0``, which is unbounded) (ms|s|m|h). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#window Service#window}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c10df9a6cf7694abd2379c61013a7e694b9e30f4c75b12148de33254ef963f47)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if condition is not None:
            self._values["condition"] = condition
        if delay is not None:
            self._values["delay"] = delay
        if max_attempts is not None:
            self._values["max_attempts"] = max_attempts
        if window is not None:
            self._values["window"] = window

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''Condition for restart.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#condition Service#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delay(self) -> typing.Optional[builtins.str]:
        '''Delay between restart attempts (ms|s|m|h).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_attempts(self) -> typing.Optional[jsii.Number]:
        '''Maximum attempts to restart a given container before giving up (default value is ``0``, which is ignored).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_attempts Service#max_attempts}
        '''
        result = self._values.get("max_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def window(self) -> typing.Optional[builtins.str]:
        '''The time window used to evaluate the restart policy (default value is ``0``, which is unbounded) (ms|s|m|h).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#window Service#window}
        '''
        result = self._values.get("window")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTaskSpecRestartPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceTaskSpecRestartPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceTaskSpecRestartPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfde21518c4f49b3947f57f6f399de67b81fea38518211937c318627fda4f228)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @jsii.member(jsii_name="resetMaxAttempts")
    def reset_max_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAttempts", []))

    @jsii.member(jsii_name="resetWindow")
    def reset_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindow", []))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a08cdd7eb8092f2c796d56f87041e92c053d4b6a5c2ca2ff18bdc493f2b7584f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2212eadf3deba5f0629ff4e4bcfbcf0a002f67599628a34498cde56e692d5bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c142018e8f9442eddae82b093534d6038d3a3917a264b78a09d240a09293ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6523f674fc781bbe357270492353ecbcdccd953427b1775af5d4713a9ef3a799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceTaskSpecRestartPolicy]:
        return typing.cast(typing.Optional[ServiceTaskSpecRestartPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceTaskSpecRestartPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__274af0a249851744aa6ac822d95fb84ce433057f2c5eb4e36a500d8d588c503e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="docker.service.ServiceUpdateConfig",
    jsii_struct_bases=[],
    name_mapping={
        "delay": "delay",
        "failure_action": "failureAction",
        "max_failure_ratio": "maxFailureRatio",
        "monitor": "monitor",
        "order": "order",
        "parallelism": "parallelism",
    },
)
class ServiceUpdateConfig:
    def __init__(
        self,
        *,
        delay: typing.Optional[builtins.str] = None,
        failure_action: typing.Optional[builtins.str] = None,
        max_failure_ratio: typing.Optional[builtins.str] = None,
        monitor: typing.Optional[builtins.str] = None,
        order: typing.Optional[builtins.str] = None,
        parallelism: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delay: Delay between task updates ``(ns|us|ms|s|m|h)``. Defaults to ``0s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        :param failure_action: Action on update failure: ``pause``, ``continue`` or ``rollback``. Defaults to ``pause``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        :param max_failure_ratio: Failure rate to tolerate during an update. Defaults to ``0.0``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        :param monitor: Duration after each task update to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        :param order: Update order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        :param parallelism: Maximum number of tasks to be updated in one iteration. Defaults to ``1``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__424b459aacec14bde9c78295c2338387270a30ca774d3b1f71d64b13cc1c393f)
            check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
            check_type(argname="argument failure_action", value=failure_action, expected_type=type_hints["failure_action"])
            check_type(argname="argument max_failure_ratio", value=max_failure_ratio, expected_type=type_hints["max_failure_ratio"])
            check_type(argname="argument monitor", value=monitor, expected_type=type_hints["monitor"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument parallelism", value=parallelism, expected_type=type_hints["parallelism"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delay is not None:
            self._values["delay"] = delay
        if failure_action is not None:
            self._values["failure_action"] = failure_action
        if max_failure_ratio is not None:
            self._values["max_failure_ratio"] = max_failure_ratio
        if monitor is not None:
            self._values["monitor"] = monitor
        if order is not None:
            self._values["order"] = order
        if parallelism is not None:
            self._values["parallelism"] = parallelism

    @builtins.property
    def delay(self) -> typing.Optional[builtins.str]:
        '''Delay between task updates ``(ns|us|ms|s|m|h)``. Defaults to ``0s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#delay Service#delay}
        '''
        result = self._values.get("delay")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_action(self) -> typing.Optional[builtins.str]:
        '''Action on update failure: ``pause``, ``continue`` or ``rollback``. Defaults to ``pause``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#failure_action Service#failure_action}
        '''
        result = self._values.get("failure_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_failure_ratio(self) -> typing.Optional[builtins.str]:
        '''Failure rate to tolerate during an update. Defaults to ``0.0``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#max_failure_ratio Service#max_failure_ratio}
        '''
        result = self._values.get("max_failure_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monitor(self) -> typing.Optional[builtins.str]:
        '''Duration after each task update to monitor for failure (ns|us|ms|s|m|h). Defaults to ``5s``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#monitor Service#monitor}
        '''
        result = self._values.get("monitor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order(self) -> typing.Optional[builtins.str]:
        '''Update order: either 'stop-first' or 'start-first'. Defaults to ``stop-first``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#order Service#order}
        '''
        result = self._values.get("order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parallelism(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of tasks to be updated in one iteration. Defaults to ``1``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/kreuzwerker/docker/2.24.0/docs/resources/service#parallelism Service#parallelism}
        '''
        result = self._values.get("parallelism")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceUpdateConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceUpdateConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="docker.service.ServiceUpdateConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__257778cc353e1937f38715e8f3c76b35d00bd87f417ee366a7dc206936ceb678)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelay")
    def reset_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelay", []))

    @jsii.member(jsii_name="resetFailureAction")
    def reset_failure_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureAction", []))

    @jsii.member(jsii_name="resetMaxFailureRatio")
    def reset_max_failure_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailureRatio", []))

    @jsii.member(jsii_name="resetMonitor")
    def reset_monitor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitor", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetParallelism")
    def reset_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParallelism", []))

    @builtins.property
    @jsii.member(jsii_name="delayInput")
    def delay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delayInput"))

    @builtins.property
    @jsii.member(jsii_name="failureActionInput")
    def failure_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failureActionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailureRatioInput")
    def max_failure_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxFailureRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorInput")
    def monitor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitorInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="parallelismInput")
    def parallelism_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "parallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="delay")
    def delay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delay"))

    @delay.setter
    def delay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__864f45d8ccbc047e606511f163479edb0910738a08daad5c445602197144658d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delay", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="failureAction")
    def failure_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureAction"))

    @failure_action.setter
    def failure_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de26b9ba06681aed9b64352155eb7793daf4738ac0a7c5a8f94587cb57b0572b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureAction", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxFailureRatio")
    def max_failure_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxFailureRatio"))

    @max_failure_ratio.setter
    def max_failure_ratio(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddf5f6bf5943e81e04833c2fa764e6907341a57bfe0011c5777086ee32bb1c8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailureRatio", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="monitor")
    def monitor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitor"))

    @monitor.setter
    def monitor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccbeae1f2fa946cc866f8076b439a6646f9c1ed8c577527914ea1f854f7fa0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitor", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "order"))

    @order.setter
    def order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b54afdf5578dec5df98ba5fa5fbfb7af10adfcc47b9807d11be4c6a19a7092f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parallelism")
    def parallelism(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "parallelism"))

    @parallelism.setter
    def parallelism(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33142146bba142ff21e9c9aa6fa092c2091c443d8a4f20dc0808f2768651df7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parallelism", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceUpdateConfig]:
        return typing.cast(typing.Optional[ServiceUpdateConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceUpdateConfig]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a92c3b78c3bff68e1873e596d72e995a93f61a8bc6fdc8eac9b51061f2e9a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Service",
    "ServiceAuth",
    "ServiceAuthOutputReference",
    "ServiceConfig",
    "ServiceConvergeConfig",
    "ServiceConvergeConfigOutputReference",
    "ServiceEndpointSpec",
    "ServiceEndpointSpecOutputReference",
    "ServiceEndpointSpecPorts",
    "ServiceEndpointSpecPortsList",
    "ServiceEndpointSpecPortsOutputReference",
    "ServiceLabels",
    "ServiceLabelsList",
    "ServiceLabelsOutputReference",
    "ServiceMode",
    "ServiceModeOutputReference",
    "ServiceModeReplicated",
    "ServiceModeReplicatedOutputReference",
    "ServiceRollbackConfig",
    "ServiceRollbackConfigOutputReference",
    "ServiceTaskSpec",
    "ServiceTaskSpecContainerSpec",
    "ServiceTaskSpecContainerSpecConfigs",
    "ServiceTaskSpecContainerSpecConfigsList",
    "ServiceTaskSpecContainerSpecConfigsOutputReference",
    "ServiceTaskSpecContainerSpecDnsConfig",
    "ServiceTaskSpecContainerSpecDnsConfigOutputReference",
    "ServiceTaskSpecContainerSpecHealthcheck",
    "ServiceTaskSpecContainerSpecHealthcheckOutputReference",
    "ServiceTaskSpecContainerSpecHosts",
    "ServiceTaskSpecContainerSpecHostsList",
    "ServiceTaskSpecContainerSpecHostsOutputReference",
    "ServiceTaskSpecContainerSpecLabels",
    "ServiceTaskSpecContainerSpecLabelsList",
    "ServiceTaskSpecContainerSpecLabelsOutputReference",
    "ServiceTaskSpecContainerSpecMounts",
    "ServiceTaskSpecContainerSpecMountsBindOptions",
    "ServiceTaskSpecContainerSpecMountsBindOptionsOutputReference",
    "ServiceTaskSpecContainerSpecMountsList",
    "ServiceTaskSpecContainerSpecMountsOutputReference",
    "ServiceTaskSpecContainerSpecMountsTmpfsOptions",
    "ServiceTaskSpecContainerSpecMountsTmpfsOptionsOutputReference",
    "ServiceTaskSpecContainerSpecMountsVolumeOptions",
    "ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels",
    "ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsList",
    "ServiceTaskSpecContainerSpecMountsVolumeOptionsLabelsOutputReference",
    "ServiceTaskSpecContainerSpecMountsVolumeOptionsOutputReference",
    "ServiceTaskSpecContainerSpecOutputReference",
    "ServiceTaskSpecContainerSpecPrivileges",
    "ServiceTaskSpecContainerSpecPrivilegesCredentialSpec",
    "ServiceTaskSpecContainerSpecPrivilegesCredentialSpecOutputReference",
    "ServiceTaskSpecContainerSpecPrivilegesOutputReference",
    "ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext",
    "ServiceTaskSpecContainerSpecPrivilegesSeLinuxContextOutputReference",
    "ServiceTaskSpecContainerSpecSecrets",
    "ServiceTaskSpecContainerSpecSecretsList",
    "ServiceTaskSpecContainerSpecSecretsOutputReference",
    "ServiceTaskSpecLogDriver",
    "ServiceTaskSpecLogDriverOutputReference",
    "ServiceTaskSpecOutputReference",
    "ServiceTaskSpecPlacement",
    "ServiceTaskSpecPlacementOutputReference",
    "ServiceTaskSpecPlacementPlatforms",
    "ServiceTaskSpecPlacementPlatformsList",
    "ServiceTaskSpecPlacementPlatformsOutputReference",
    "ServiceTaskSpecResources",
    "ServiceTaskSpecResourcesLimits",
    "ServiceTaskSpecResourcesLimitsOutputReference",
    "ServiceTaskSpecResourcesOutputReference",
    "ServiceTaskSpecResourcesReservation",
    "ServiceTaskSpecResourcesReservationGenericResources",
    "ServiceTaskSpecResourcesReservationGenericResourcesOutputReference",
    "ServiceTaskSpecResourcesReservationOutputReference",
    "ServiceTaskSpecRestartPolicy",
    "ServiceTaskSpecRestartPolicyOutputReference",
    "ServiceUpdateConfig",
    "ServiceUpdateConfigOutputReference",
]

publication.publish()

def _typecheckingstub__0c6848e96b699a6cc01123087da0a7f73c40f029660d845330d762845f15058f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    task_spec: typing.Union[ServiceTaskSpec, typing.Dict[builtins.str, typing.Any]],
    auth: typing.Optional[typing.Union[ServiceAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    converge_config: typing.Optional[typing.Union[ServiceConvergeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    endpoint_spec: typing.Optional[typing.Union[ServiceEndpointSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mode: typing.Optional[typing.Union[ServiceMode, typing.Dict[builtins.str, typing.Any]]] = None,
    rollback_config: typing.Optional[typing.Union[ServiceRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    update_config: typing.Optional[typing.Union[ServiceUpdateConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__d7c841ce0d32a20dcd698ed9f78fc3a30ad1091aec6726fab796716c3502f446(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9101889c65e8900e7754ba448261b2a93c073a52fab240ee8feb049f349bb4b1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525bcd2ae62ead591721e6dd219a1196b02fd45a6bb4da60e7cfe03279dfab5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab347ff274a6e46ce8c2f2aad29e7c579a777117c9ce4adacbf2b67eee8f9f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2732a09d18600575e862c7e1f903f1234f3db88c5561209ba580772f0d01b7a1(
    *,
    server_address: builtins.str,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9947af8f1cedb509fd0a41bab6ad14cef842460f57dd079a2adc9cb5c17e389(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d07dd7d2579e8bbd83d25a2c36a7197aa2d72c81b1bc6a5ce567b5f90f257c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8ff0da173877f09a3a8c68b1028b4d65bd7bbe779417daf3cb69037437f0ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b287afbd961f1d7c75f000e96d72a7b0e17a5bcb8d77f4ff5e5f68c437768d8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450cfbd5cf2a1f27f7ffd091db5d919572e393231ed93150148eb06d5abec262(
    value: typing.Optional[ServiceAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592645dea33e425062a305c3d1d79325599cfe63b22b3969f6aa6671a824d114(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    task_spec: typing.Union[ServiceTaskSpec, typing.Dict[builtins.str, typing.Any]],
    auth: typing.Optional[typing.Union[ServiceAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    converge_config: typing.Optional[typing.Union[ServiceConvergeConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    endpoint_spec: typing.Optional[typing.Union[ServiceEndpointSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mode: typing.Optional[typing.Union[ServiceMode, typing.Dict[builtins.str, typing.Any]]] = None,
    rollback_config: typing.Optional[typing.Union[ServiceRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    update_config: typing.Optional[typing.Union[ServiceUpdateConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c0bdc25c51e0363f4174971e3e443ea09f15b95591bd2cf166063400394860(
    *,
    delay: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4cc6bb981f239c9b5bcdf366b859cef004ff3c9a9accd0fa854f9b3a1f29189(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1431fa879200c8b0cbb8dbc05b78ebb63f33e5a29210f0ce2f2ea1d12cb92bd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07bbda935240a162ab678096d6a390106281be87dbc50cef36add9fac2f97f6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb46b18d28a763749bb6a116c4c622e0108b8860f6d54600973e98afc6be8f6c(
    value: typing.Optional[ServiceConvergeConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01234264d9f7a98704f7877e505807fe35ea6b4ba74a410d0945d5af3cd33220(
    *,
    mode: typing.Optional[builtins.str] = None,
    ports: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceEndpointSpecPorts, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebfd458f24d15529a4cb1480cc779c0f8775ce35ae38cf1a7e5441419763cfb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3222ece2ee7c3c065acf8dfc94826e8d8107b7f1983cbf2ab2448b9956f831c1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceEndpointSpecPorts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3583440fc6e22cf3b2afa8e6824f5c30d81f9bcf85a67aaab4d2089ab50dab5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb97cc8bfc4b0d5444759b601b656b34410c1efdc35f9553b87b95094d2b259(
    value: typing.Optional[ServiceEndpointSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081c511e9919d97caf957bc62b7f0db6a9e9f88f925a51baf4a87b223e670471(
    *,
    target_port: jsii.Number,
    name: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    published_port: typing.Optional[jsii.Number] = None,
    publish_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53209f8baeb535250ce84bceb9826bdecd4589fe50e0d4a6ee2ca41908c3d39d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05dcacdb60c2c6748c027133114df5e89053e729f7584d072be646c9208dbae9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ce50b001829f095e603454c347c3210c24b6c1aa894a0ded37b073421272312(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bafc9e30637080998304a82fc675b10e5d17351a10412bb8393aa6e2b4b804(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c4bc8e7cfba3d5fa85e001c581ee9c1043d23712e721741d7672470cf06ddcb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec0ab09844fa7f0cb551f85eb7948767fc082af1c0bb47870988c514eab366cf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceEndpointSpecPorts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36cd644d1820367c5b00598d3be854da0a5f67e06346ee7ea234f08915cc1272(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7475c43347a92c1bd67cc82d83a709a3d402e9ccb04a6b79b2ef8291008703f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024c24cdb669f3980db549ac09cd88d03eb3660d139d0283294d0d3cdd765c6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d69105aafce5dbb5b5416af8d5749ee93ecaef9a709b2f27d283bb9688895d1d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0036e1c0ca77c3ecc5a6a1b9f0a7ceb806cea7e4fe1c184672311b147a37747b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c558cd534fe39a994bc4e51e8440e8145fa0721c351daeb2c56a4b7d5217d3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed29e82d8eb700d8a424834c4b4fde52093fbf3984ba3185bfaf04b03c25fa4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceEndpointSpecPorts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f4b893185d26d8c69741ea68ca2dd0ba0276381abed6d0084d8dacc669f09c(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d7cb9daf560e92f76b07bf981a18df7b553db5a69836a1376457725d614a3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47bf76fdb8f398c624224cfd5cfae03e5ad7c7eb63cad3240b268cbcd0627dd2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3950bbae4a1b8df79ff1fc544ceee19c4f7c24da154d0bee9d6bae7835ae94bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27289398beabfc747a7479f87d464f6615c00d7998ad376bbe2525844d133f31(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafe819b446ac5e2bd125f40dd8196e57d10f9c575993d1d96f55f2f609b538a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a88ea585a0793512624c940cf46830b05cce57e12baf808e4d73e3e34c96294(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b32406cf1b36cb436cf7bf0b50ea2d38fa5db2a16941ac9f17806c1a89dea78(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8110e60b0e7d94b982739f820ea7eed7cee0d7dc3724445cd3d6c1ec89931b01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e24cf56950c16b61ac0270a61e7beb9124d0b32955267422f94325107c9830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__237b8d00b744900f6ce40d69525b08f819e591c1ffec49770c8a644df07dd9c6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceLabels]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748e3845500af1efd8ef69bfee2e1d983e90177cd4259f37faa35f59fae52e67(
    *,
    global_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    replicated: typing.Optional[typing.Union[ServiceModeReplicated, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1eff7c39aea572ba1e691f22ec4fb7ea7bcb0ad911a0d4ee42ccc9625ec96a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eca08ec9f6935803f67bbc1ef758c7aec6c8337b96a0ead9c44d049cffd20d0d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f874417786b7a52043aa3290e6509469f2e797ba02da9b24f2c43b55a6b5cde9(
    value: typing.Optional[ServiceMode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f9f27ec2ee1556dfb50f2aab479ab29f4715ecfb644ac7e295865cc160eed9e(
    *,
    replicas: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806df2a7c238dd4c14b2c8f884e0e148f7655c476b9056429ecfde174a495b48(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92fc63a4d742a6a5df7224c89eb1ea611005510defa3e7c883ba1cd7eeb45365(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac69e5b988b2573acbbb326d0d0869867d65940c603046953b4294da77a9ff8a(
    value: typing.Optional[ServiceModeReplicated],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676afc586bb77216f990fca7e04e2ca84318c80e8ff2797d0fc703ea6b3e8250(
    *,
    delay: typing.Optional[builtins.str] = None,
    failure_action: typing.Optional[builtins.str] = None,
    max_failure_ratio: typing.Optional[builtins.str] = None,
    monitor: typing.Optional[builtins.str] = None,
    order: typing.Optional[builtins.str] = None,
    parallelism: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a62323f0d9b6ef643175cda6e63d9fc0bbb8230937fce33dc00464e325d80b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5169397934e464cd0a646294da597cd73ac39b8da466e677208d0c398be380cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2964f364544c84952bd71839d93c5c0b9f92345f0263d48d6ec67a2131b41f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3c8e4144670f8a10fe2c7bc7a9e81d97bd109e2b57a6562b0f382e684f076d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82debe4bc964022e20e907bf5f08f9f10da748794d343f6f38592eed082dbc55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb7728d93d8c31c297b00bcebc9ae5f95440c2b43e6d36d90e10650359a0c88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9c7c3713230e93d95214862561a7380360a6b16b312aa6f006b6231e59f72a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afe30eac6031c81863d19cfa62f7a60cc49121d8f12b87df620340601247e2e5(
    value: typing.Optional[ServiceRollbackConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d336120923c53aef986146bc12940831e5b2368231d134c0dd44a96b9d948b(
    *,
    container_spec: typing.Union[ServiceTaskSpecContainerSpec, typing.Dict[builtins.str, typing.Any]],
    force_update: typing.Optional[jsii.Number] = None,
    log_driver: typing.Optional[typing.Union[ServiceTaskSpecLogDriver, typing.Dict[builtins.str, typing.Any]]] = None,
    networks: typing.Optional[typing.Sequence[builtins.str]] = None,
    placement: typing.Optional[typing.Union[ServiceTaskSpecPlacement, typing.Dict[builtins.str, typing.Any]]] = None,
    resources: typing.Optional[typing.Union[ServiceTaskSpecResources, typing.Dict[builtins.str, typing.Any]]] = None,
    restart_policy: typing.Optional[typing.Union[ServiceTaskSpecRestartPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    runtime: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482915048177ac8ed887d05e795dea88e9a382d0f4ee35a4ce1140147dc00503(
    *,
    image: builtins.str,
    args: typing.Optional[typing.Sequence[builtins.str]] = None,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    configs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecConfigs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dir: typing.Optional[builtins.str] = None,
    dns_config: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecDnsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    healthcheck: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecHealthcheck, typing.Dict[builtins.str, typing.Any]]] = None,
    hostname: typing.Optional[builtins.str] = None,
    hosts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecHosts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    isolation: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mounts: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMounts, typing.Dict[builtins.str, typing.Any]]]]] = None,
    privileges: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecPrivileges, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secrets: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecSecrets, typing.Dict[builtins.str, typing.Any]]]]] = None,
    stop_grace_period: typing.Optional[builtins.str] = None,
    stop_signal: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77dda369ce826711059257e681cbf1e5a45ed1e47a8bc33276e2a600b09ec13e(
    *,
    config_id: builtins.str,
    file_name: builtins.str,
    config_name: typing.Optional[builtins.str] = None,
    file_gid: typing.Optional[builtins.str] = None,
    file_mode: typing.Optional[jsii.Number] = None,
    file_uid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db746da53638f97893aa60ad267ccb8496cc335527b15dc2a0b1c2a7aa8f634(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff62e3e6dfa9801aeb7b563f760a293882325d1e0ba5ec1cae6bd4984f1bd274(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ed15ceb32161e41d7348e32a5ac580dc8a02ec082a090a1d216182a74030c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d03291e4ba89d773b2b04af0c7eceac2eadbb8cc45c9bbdf43748b007f8c426(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b21be17b0f7d07bb6ba38213e3270c9556c84f6fe6e31e5e59c7c94ac6ac8a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c252b897c57bf15efc064cd085b4013b3ddf8c9dc725408f3a693887b2ccc08(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecConfigs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1c75fcfccc88aa553fedaf97471170415ce2753e993ea0e55f71ee1c4cb7122(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9346b4869790e5c23b56614063a530a7e77f44fb00f74936409a25a483dcf0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a8d276c9bc3a08767f04c5dbb1b1f87e3ede887e4256e552c0e543da880f7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3511ba809aa2c7b4db940279b8dd61f547ce381afb1d91c15ee09f0a5ff5a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40fcfe6a6b1abae9a3bf0409c6117714208aad1edf2232f30ca619feec2f99a9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dc331f1653ca664c838ac65a4a2bb28ebda31bc30eca7e7a90da2fe8abcb36a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b7330acfa53e441f0a9a72400e9b1a340c2de7a995cdf7d3e38491f3975fdc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e280d984bbbca23045c62d6708bfe57de8ff44341ac4afaa60f1cf5049c63e8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecConfigs]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b45d604b4f2b522d49c9a49f43cf60db330a80c6b4756693d379e6ccfc5a1f(
    *,
    nameservers: typing.Sequence[builtins.str],
    options: typing.Optional[typing.Sequence[builtins.str]] = None,
    search: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a90b5b3de5f31022e4928a64929f63b7cd5bc6b23c00da65656514163bee15(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dcb12918cef65dc2a34fb84e36216b772054e3569595c0f635d5536a1cb4944(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be817d2fe5ffa21def0f7dbfb3bd37132ca08574484ba9774344b8247c56eee2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ff591abd150d03fba309c06b8bdbeca107a41d71b9614bd9b0012c6bd849f83(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f9d4cb17761e6460f112a19bd1853ac167db02e863c959dad89587722b3df65(
    value: typing.Optional[ServiceTaskSpecContainerSpecDnsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18aac2635ee61a87bb02acaeb22569e07387e46189f487ae93b22c3e7543f1cd(
    *,
    test: typing.Sequence[builtins.str],
    interval: typing.Optional[builtins.str] = None,
    retries: typing.Optional[jsii.Number] = None,
    start_period: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9509152655f8ab05c182c508cc0acecea0223bc2b5da612332c510e3b6a688c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6617f7c27bbd7770bb714aafd29b14392b7ddb4acf107492576b5241a22623c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4001c49f0626de13a663e8976a0acd954a4a2019c2db1dedb5831d74c57321(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c696aa20cf5e9f240f93f7e886d6277bf9e32d4dc83854034f226c12ccbbfa2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4888632d31cd0e75f8321c82f10b352ad1cbcd7860cc6a4941f86001ea5d64(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__675fe7d5674302a834ac0060dbe2f7263e74708722d025e8c4ebd73f20b06f2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c229fdf41d6ae0e042a2513922c140a3dbf1d557a39f2feb2670de0245347e7f(
    value: typing.Optional[ServiceTaskSpecContainerSpecHealthcheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9acf8730c55f9b581990a0bf5d33d9e0e4d39230817836e22a9a71d06f7bde4f(
    *,
    host: builtins.str,
    ip: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422771b29253daca0e508f8e41795087bf333df496d5e4a21a56575dce522cb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0caed2d42e785844e3b7238154bff271dae75fa26dcc3a5ff218380d02dcef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f5d1709c0025f4d7c0bdcd4448cecd92e2d028ec5334ed0781e59fe01543bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a71940fbce6fc936f43301e90986b1f0ba47973e2c04f508f54f4071c1f7eb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f31965b284b88bfcd52c835a659c920e963b242a2433149edf36b902c4a6a99c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f312cf312f6283b7753cb156532deb8a8720ff116bbdb84ba462347383d10d1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecHosts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d10bc119e2e9ba7c3bd8668b51694fae1715c0675dfc119b2be70fb08651a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba224749030745f0cfcb42989de78b9b47c75f82d6647abc0fe9dc264baa226(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324005385c52387f65bfeda1b3f61dd1dc5223246cf1801964744c7837edb7c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1283365caf4edb1162b96d1e3b8efb0a4ac5c2e7aaa2a8ee69daf52ea2c1603d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecHosts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e5167fec32e3fdb227611aae63fc6686e4d389abd2d87036529bb8d60b9b36(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__282ec92cb5f067f7f48ba0c8606b4407ccdbd4ed60bf2c73d000ff4624b82f3d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d92616c660bf04a2e3ead7b36aa86235d748bf8c7a986970366458ae220c6d92(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597b34941e53b22d23851dbfdc44f4cffd76ff174a01833a916552eb8626c535(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75fc527973f257125167403f86afeea7f9b9886e0a8a769a0d142bcc2d952d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccbfd2346da3d9ae59b95821631852d5b14d9f51336ba95163b51bac621f4e31(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d454bb9a6790d3a4c547a8c8698d635e04e4ca52a46e7c97451b40f5d799d91(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e01f4ce063aacb7179eadb0f05d38e92e8f9b658a34118d98174abe90ac3c04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8415473a39bbbe7da4ebfef0578f80d7d999ee7c72526a8af2f6a0ea4c444d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c9d236229e1e7127c8ac4bd917f04ae4a56d23eb06dc7c1ee1b16ac99d38bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b26b73c3733591900f41706d77b7ab66439e8faf70ca219c375e2f338cf222c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecLabels]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b685b9129d5d62e195fb1651091d3e3939bb0b94b787fd4e77f12281df8901ad(
    *,
    target: builtins.str,
    type: builtins.str,
    bind_options: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecMountsBindOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    read_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    source: typing.Optional[builtins.str] = None,
    tmpfs_options: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecMountsTmpfsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    volume_options: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecMountsVolumeOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e33608fdcc9fcabe4d8869a6c7edf5cedb9e722a63e14094372d3d031c70b58f(
    *,
    propagation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__535737c98703236cdd5d1123db718a9c7020013e1c7fb8556579c2f15ad4e0a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebf18b55f80f61fc5404f7f1479e9be3e8b731af32ddc5d275058a41cde1ce1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4096ec49b246c6fb0329f917be9a6a0f1bd398051bade317a4e9db80cf3e5396(
    value: typing.Optional[ServiceTaskSpecContainerSpecMountsBindOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a12658a63a94e38d7b4b69808c1a780d2d0b949629e335602a28f4877b201c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c70b62ea6327b9f1bf2895772be873ff87e4b82945cf23e455f9ff434b6e89d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fabee5f9e0b0b1617baaf869341b0f08d5d6051ae7f7bade9b5f49f8d29061(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2634ba50a02799adf4464215f2efe2bdae20a5cfa3aa2672edd8ddc525189443(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cceff91620c30adc1cfffa8e603947aa04f11827aa9429ec7b0abe77844281(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b21a51d70784fab3ba11a260bcc127d46eea7ece9dc1e4bee9bc1e05a35c053(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMounts]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea95d50baf9c9eed1773bcfe058754f45446810b680a359baf6684f76e1108b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90b6029cfb3f79bbdabd0a1fb9bf02d21c150d9e4009f33bccd4bc578b8957ef(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__118aecb58de8a917c235810da9b73e0e8c6b4e9a59bd9b0f0d7d33620415bac8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d053618615e9c14b81bf345bad15a52ff81956ce7d9f729551044bc0332014(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f99c330817312f90f299e822cb1278084cf5f92b5fc49c321b392d726e1a385(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653e9e8c714b06d6903027d7640cd94bf89e33dd8599f61decdb362057985660(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMounts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a6736605039db227252e4667a4eebdf09d54713aed75df90f6cbde7cd05684a(
    *,
    mode: typing.Optional[jsii.Number] = None,
    size_bytes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea7491106ee9753c3b6f946f717283fa23369a1899390ee2e01d33e5f510ff3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a76d7955daab4a4ffe920a4a02d9ff6ad8323e593b9e867215b809a9e06655(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d1fcc82e3f8ac7a026d394cb6baa9d13b57b01a7b275b4de3c4067606139d3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193f8b3273d2b070c9c48b35ec6fa51bccad07af66c3a4724673610d82e26d10(
    value: typing.Optional[ServiceTaskSpecContainerSpecMountsTmpfsOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85a012927e166a1d9777ed70a83eecb259d15c8fb0ff072ac4ab817db44c493d(
    *,
    driver_name: typing.Optional[builtins.str] = None,
    driver_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    labels: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]]] = None,
    no_copy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ce28612a27d9f132753f88f503b0d370d0ea7398d7b7c19cf8deab91267ec6(
    *,
    label: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e1e72b9761377fde752f0eb1afa339b463e07ad5242ddc4e9f4388115fcc6dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da2ce8f7ff7c48e46b59548808cde272c55f4049bb4d31696a3be072899b6d3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c064b9c0d115bc9c7e6c1453d2b36d387f92deb762d0b6af68fbd804674bb43(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3cf4b5b71228f89a6dbd7e0b70a57c555c7b08957c91deee8e01505e640c29(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce118fcbb1fdb4fd4a2bb1aedb13efa4154fa6000756e8051d4836813d94795f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fdad1c7b2806b0734328fadbdd392adbea5996a0179c473ad4d25c7eeedf1f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a694b90cdb194b34f37cf1572719d1551844b3a6b42404f8f319d86c0208e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8fb747aa45f53532792b8c3e97b3c7cfbf95cfac6225b5db74e6a8ea2c8aa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f444fedbf484f7144fe909565470c9efa017d3aaf844a65cd66a0f5573cee4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e447167ac81f26efe494f927d48c618e1d8ed40ea1fc200999e2b93aab05295(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94c71f645e88e28e75d67c492dec5bca9b5e72442822294f7a34dc298218819(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932599b34976868c9cc761720b5e618f7a958cf9187f5849b6b1ee6b933d330c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMountsVolumeOptionsLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49832756cfa5b71a4231109e633f6f0f7b9ea2eb5dc65f9604e66e1e31890225(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b00f4b097d82cd43aa7b9772eaacd3c4b422ca67e41141d5653a0b3d838bf85(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0093b40c6e5810678d6eb9f4ec3efa27ec55d49878155075b10c871e3de6e2f1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142379bd073c8d8bca0db6439612d0d4e67b977aaa3e4e61a173aa23422da47e(
    value: typing.Optional[ServiceTaskSpecContainerSpecMountsVolumeOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f000178dafb4d3bf383c79e1e46a81b85648a4b54ac8327f95ed66f029a773(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70783c19d786c1bb0bf3a01aee2e47e733f88c5876dec92ebdf8fe9f33f2148(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecConfigs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb0a67090a0513b8a119da68d49262af6e2419af8753002d6ca4c540b587336(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecHosts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881fa8374f255c1d10370df34e16ed340d11a61aa1508eb8e8679cdbd36b4ef5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecLabels, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8511a8f470268d30858d3ae9d60418a2b9f9b45afe4e7ad99a52fdea73dc8622(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecMounts, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2cc3fd55b1c41325faae54e0014b22cccccc9d692a7946ec339e217e3f3475(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecContainerSpecSecrets, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d65a6afd404e5a7dff8f89aa58317c4bbe2bce704d96e546291932787c7920(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41a92d99b7bd35dbb9ca18c8bcb289581c05f6b03a3279d60bfaccb2963e8e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4005aed1e5df9556c37c69ac8a0cc67fa29b3d214b9b4f58efafbdb088adaad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504c82fbb5897df26fe5b3714617ba7310842e3a1b311ff13f9487b80abef517(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ecd588061eb1f05c17d0bbb7a0225ee35cef716355939702eb69cbcbf8af003(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878aa2cb756f5cdf407087bf277a8e4c01d961e99f11bccf74d5b6fb5cdb4618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78eb59fa029123091747eaf79af1954764e1145dfae653bdb6acdbad31103ea1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf1112000eaa69e834221b8970acfff7663e9d4e49080f78972080afefbb2ac3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11a4b7d5fae07d47d064400ace846aa92b9536b94d41c7a9e519db304579495(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e774403f91221d5dcb5e63986bcdebddba77203d8be24ab65a9ced1dee5d203a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b50b823f2dce9d5cbf62fcd76d2bf148d5dec1c7e9b944cdb8df2e7a2fac94f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393d5f247e3615541f6d85089f8f0feef42fcd97b49289975ee7d8fc5e278856(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96626279af5b0cc2b182b21ecb5287e017c6e38117b25de304d985a4ab50e77c(
    value: typing.Optional[ServiceTaskSpecContainerSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca38051962cf61632a82c270055a8c21333179224999c3d94199e7458e6f1f7(
    *,
    credential_spec: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    se_linux_context: typing.Optional[typing.Union[ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__583e5ff538ecebccdd77184bc5d48e67d26bc128e714664596b984d39327a541(
    *,
    file: typing.Optional[builtins.str] = None,
    registry: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdbb27953799d56db00fa2a6a741c7e29a09856601b6e57560d8be9606fc010e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4106350ba57f4a424c7fd074914a050af0bdfc64232d7563438d2da629299269(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88208da60711a5028f75887a450d94c238b6441c55ae6a641cb2640fe2663024(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5127b77e2bdb3a1b5311d5a940578743e43c4640c63b3376e7f5de19bdf43971(
    value: typing.Optional[ServiceTaskSpecContainerSpecPrivilegesCredentialSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef19fc3cb39271f29c20d494f44df7612abb8340e26bc46ead9db628b0ccff24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e657a3150fe577a62182bdc386338e7d77f6eaed2f2fe3663862159ae63fd745(
    value: typing.Optional[ServiceTaskSpecContainerSpecPrivileges],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209751b4bdc209838c8ce85939a18a5e87dd1d78a26097469e460094297831be(
    *,
    disable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    level: typing.Optional[builtins.str] = None,
    role: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a196b497b7bbc14393b6c342c5253c02aa871657f920c66933560417cbe3ce9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d39a70fd72ff39f83ebdeb5666a804ad0f57d61d98fc1a2684539247b9a8d9e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4369687617f5eac861a66d86d13f45cfa69293cc6fc8bce7b2c0efe6d4b15fc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e6d388cbfe440cf2aa0a72e1dd0db6e088ae6c019e35053b436a449baed7e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ea17e908028deaf5220f74a525269342202fe5e7895b4ae49a02e0fcea0770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64c3501f3bf1fe19b298a0009b737fb1429e8d49638dfc77df1f6deb921a9fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aab776a721ceff498560b15b6797c4184819f0ec14d046cf267bc0a533b7cb7(
    value: typing.Optional[ServiceTaskSpecContainerSpecPrivilegesSeLinuxContext],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad99f66779cd9ce798811945331f60e9fff6dd106de12db64b9349fd21394ff0(
    *,
    file_name: builtins.str,
    secret_id: builtins.str,
    file_gid: typing.Optional[builtins.str] = None,
    file_mode: typing.Optional[jsii.Number] = None,
    file_uid: typing.Optional[builtins.str] = None,
    secret_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb9337958335abb003bd219e7d924b15956d474599a894e4eaaa99caa53659a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5a9dc81889a4ef5a7c840bd12b62609b988a0af8bfd4cd187319d753d51ed0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07d2b716959a179eb310c03933acb44b2d08eea6d8d02c83bb28e0447be3ec93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3f08c79ff7e95e4ef15f255190339575beef10885d48305225d0417f52a35c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8efef47f2463ecf5f56e5fb0c32b3e580d0c0fe8c303ae063821f722166a9894(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93e25d8b4c413e201b4bf6f6b853a094479ff6afcf58d5a950ddf624d198df6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecContainerSpecSecrets]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488ff8a1e98c6d7a975d88610f3a87e466dfe757266f948f52a617507828f482(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b159f849de1274b59fb1d6abb1427ff1214aa41f93ce30e3a6fac242081a0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1217be6aeb979f4b9a5e83a637c33228e14356b750cec3d3fc270e94f82c9d3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2200af58ea72fe762bcb77a9d0e30d2e8916c6fee6bb9cb2bf7003c9b0d26200(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df2a3aabaabbe1db407ea24aaa618ca8525120ea123e16b267a57fbeef9550dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50030d1d91d3172fbd5e70766f271d5d46991e1bba845b5a0ea9db1812c5023(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61012d82b22473e66fa0b4d1c77d0459495fa4488604ee1975ac1ba99fceb97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d13520f63daa78c02ac60cc78f78bcfa58739161e797492a56dac99057ccc1c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecContainerSpecSecrets]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3022c257263e46ab6959fed7d002af4014d88de9cb8401b713bb40f2fa4d065(
    *,
    name: builtins.str,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__885e32a7da035fa81f5c46448d3e1ac5d29c88e37391d352c11a1b7192739f20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66aff319f7fe4637525825b52e5c6e83ca23330952c856fcf77ee1f1fd6feb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1badb2e1bf9baef8469c848f462c91b3c2263af3b90a36fc208f693919ead256(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f93b4a5018c2a59a696f1bf5c76e5be337258bda11689603fe36c075f62174f(
    value: typing.Optional[ServiceTaskSpecLogDriver],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3cde21110c3c577d2d1126be878f449913ce381e999a8ecb08dd3ae5226ee8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cbe6160723186b98cf9f7adb99b0ef2d5be8ab0acba30a00b550e73ee02ac6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5744bbce9bbd500870a89258b0b30988eddc1ab0f58377abaa8a9bafaf84d5af(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd2a0f5517896babeb5bff2d7759f8df6eefd7776826f384a3f95c48a4da67b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f646d3d0a3210fe0eb19055876c1886b54dff3d3d9aa6d68e1c1e411082a6c0a(
    value: typing.Optional[ServiceTaskSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fff629f2991668ecf74fb12935c5a6de8f475f9838362db350be2f221d91d3(
    *,
    constraints: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_replicas: typing.Optional[jsii.Number] = None,
    platforms: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecPlacementPlatforms, typing.Dict[builtins.str, typing.Any]]]]] = None,
    prefs: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a7995c63fb15e188fe9d9f8800ebdf1cd6270fa0111d7f62c874eceef5f77ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015f7603489f85331a2077a0e7d7a1f501d11e8fb304a0e3c48895b80adb2b41(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ServiceTaskSpecPlacementPlatforms, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdc5e82d798ed63e77e9917b0863f7fc86e8f84c679b752b7293d8a6cf724059(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15fe6547d12fb1caabad0323207d85de8b06188f86c09970c3202225b2ecd382(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aaaaf7f266d9097cff1bc4bee4ded4a892aade54a043aaa88fe6e4b04af6031(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de775fa17024aada62d2f45297c1d79feb976d295af82426ec56a18ebfafcae7(
    value: typing.Optional[ServiceTaskSpecPlacement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367c31c9175b8f3b2d8d8dee33a9190c952e7dd0a07e114118a4777c3e6ed4c9(
    *,
    architecture: builtins.str,
    os: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70bf80d5d4417a7bdbe34812f10d29a741cc533e5d367289468d1dd3fc5ed1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b560f9329e847da6bf93f2a0327a1ded568b48aefdebfb848e66c50c944950(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ccde0210369664ac9660fcd8c02ee854e478e76934596464cbdd43e680ac06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5cecb1e81647d3763307d274101ebeb01d2b0d66c610695a0fa2d53a5c0340b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b46694df1ff45257b34ec511746bc998cc45e0a5fc644930a33dbee0cf336a5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f214a99b38dbb502e56568235e84b4df3fa8e6455c9cb4c6bcd5be8a17ee48(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ServiceTaskSpecPlacementPlatforms]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__223fe2ff6bcec9ef2c3c75ed46f0b975dba38be8ab07a03a65eb4d85c7a067be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d49a4bcde6d1549ca97a835c34fa303ef8b0bbda20c94ccccf6d2c996f56497(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aaf265ab7a1b1909ef78fd518099cc423115cfd933f497415dd3a2325662011(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3198bfd39908323dda47daa7663856233b01e4eae54d3113356649ae376552(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, ServiceTaskSpecPlacementPlatforms]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9b45d5c787b7d5215af7796de52c8ed1b384453da5148fb37431b5e2092662(
    *,
    limits: typing.Optional[typing.Union[ServiceTaskSpecResourcesLimits, typing.Dict[builtins.str, typing.Any]]] = None,
    reservation: typing.Optional[typing.Union[ServiceTaskSpecResourcesReservation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae7cec76250c146e291f3c3268d473e0224565755d16744c5906bed71548fc3(
    *,
    memory_bytes: typing.Optional[jsii.Number] = None,
    nano_cpus: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb5a06653f767cf723ac24991169bf3b428f3e4b1a4274be0a82d1d185b86e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab521f058cf60d27fdb987e23988b5b2ec5355fad2380122e1cd90061b2d2aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c932bae813f326d49389e4011bb4fd1cf11a7d1c161cddaadc5afa2f787a60fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e45647de2b4d627ed733ae32d34fa61b8420c7320286fcab2e39bbae38651e(
    value: typing.Optional[ServiceTaskSpecResourcesLimits],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011f2cd779878c4d398c9432f09975891bbfb455ec9bae42bd57a805c46d8be5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3358546eb8c0437b841d9d251dc88fe0f37ea2ae873feede82be8ea261fd7c85(
    value: typing.Optional[ServiceTaskSpecResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18186dc55c233aa6f8f3d7ea56679bc38bee8f910f05405a112b3740b119826f(
    *,
    generic_resources: typing.Optional[typing.Union[ServiceTaskSpecResourcesReservationGenericResources, typing.Dict[builtins.str, typing.Any]]] = None,
    memory_bytes: typing.Optional[jsii.Number] = None,
    nano_cpus: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6030acd814dc6d6ee9cdce790053d8b30a66deae59cdb17151c4342eb558357(
    *,
    discrete_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
    named_resources_spec: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3e1f0ef86939b7a5aa5e7a06ffce7cdb3ba7a61a72826ee05e0a2a339ff02d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0eff52c541163d6865abaecb10c7e40d78ef9a0efede8a1b8703633f0134e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa923d082c5704821df7d599389f7aff3f1b75b0f85d23e64acb303a5bdfb67f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941bf0429463aad7755eda69ecd565c0e6743d79606c61d838b22f94d8e656da(
    value: typing.Optional[ServiceTaskSpecResourcesReservationGenericResources],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9794bf26c8e2cde71e32b3ec85edf87a9aa2f28e6289fc6802ecec0bf41222(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a47f11d3ab2216dfaeffa6270dc61eb6a8ce44344668ff00131e4a0f0013ba3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86fcba21192f418a9d4a36342c7d4c6d7f8b3d982a90120dfea2d6091b5e826(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d15bd681dd6b1a1b53571055cccefc26298eb637ef11751aeab943ca1d6f73b(
    value: typing.Optional[ServiceTaskSpecResourcesReservation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c10df9a6cf7694abd2379c61013a7e694b9e30f4c75b12148de33254ef963f47(
    *,
    condition: typing.Optional[builtins.str] = None,
    delay: typing.Optional[builtins.str] = None,
    max_attempts: typing.Optional[jsii.Number] = None,
    window: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfde21518c4f49b3947f57f6f399de67b81fea38518211937c318627fda4f228(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a08cdd7eb8092f2c796d56f87041e92c053d4b6a5c2ca2ff18bdc493f2b7584f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2212eadf3deba5f0629ff4e4bcfbcf0a002f67599628a34498cde56e692d5bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c142018e8f9442eddae82b093534d6038d3a3917a264b78a09d240a09293ace(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6523f674fc781bbe357270492353ecbcdccd953427b1775af5d4713a9ef3a799(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__274af0a249851744aa6ac822d95fb84ce433057f2c5eb4e36a500d8d588c503e(
    value: typing.Optional[ServiceTaskSpecRestartPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__424b459aacec14bde9c78295c2338387270a30ca774d3b1f71d64b13cc1c393f(
    *,
    delay: typing.Optional[builtins.str] = None,
    failure_action: typing.Optional[builtins.str] = None,
    max_failure_ratio: typing.Optional[builtins.str] = None,
    monitor: typing.Optional[builtins.str] = None,
    order: typing.Optional[builtins.str] = None,
    parallelism: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257778cc353e1937f38715e8f3c76b35d00bd87f417ee366a7dc206936ceb678(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__864f45d8ccbc047e606511f163479edb0910738a08daad5c445602197144658d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de26b9ba06681aed9b64352155eb7793daf4738ac0a7c5a8f94587cb57b0572b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddf5f6bf5943e81e04833c2fa764e6907341a57bfe0011c5777086ee32bb1c8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccbeae1f2fa946cc866f8076b439a6646f9c1ed8c577527914ea1f854f7fa0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b54afdf5578dec5df98ba5fa5fbfb7af10adfcc47b9807d11be4c6a19a7092f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33142146bba142ff21e9c9aa6fa092c2091c443d8a4f20dc0808f2768651df7a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a92c3b78c3bff68e1873e596d72e995a93f61a8bc6fdc8eac9b51061f2e9a70(
    value: typing.Optional[ServiceUpdateConfig],
) -> None:
    """Type checking stubs"""
    pass
