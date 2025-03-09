## MAPS项目日志上报指导

### 技术说明

#### arktouros项目

MAPS项目日志管理使用arktouros项目基底进行。arktouros项目是实验室为631编写的服务治理能力增强软件的宿主机端，强独立，不依赖与外部api，允许数据使用自有格式、OpenTelemetry协议格式、沈阳遥测格式，通过文件、GRPC、TCP上报接入，并为用户提供可视化操作界面与运维脚本。

arktouros项目的代码托管在 https://github.com/wangminan/arktouros 上，在本地服务器GitLab上有镜像仓库。

arktouros的本地实例运行在服务器上，接收器配置使用otelGrpc，grpc接收器端口为50051，因此您可以在上报时使用**10.68.115.112:50051**作为上报host。arktouros的用户界面端口为50052，您可以访问 http://10.68.115.112:50052 来查看arktouros的看板。

#### OpenTelemetry协议

OpenTelemetry协议是现在业界使用的主流服务遥测协议，规范了用户上报日志、链路追踪与数值数据的格式，并为各语言用户提供了开箱即用的标准SDK。日志管理将使用该协议作为日志上报的基底格式，并允许用户在需要时同时上报链路遥测和数值遥测数据。

需要注意的是，arktouros使用的OpenTelemetry协议为2024年上半年版本，目前的OpenTelemetry协议大版本没有发生变化，但是某些新增字段，如日志的`event_name`可选字段不可用。



### 文档引导

+ OpenTelemetry协议protobuf定义 [opentelemetry-proto/opentelemetry/proto at main · open-telemetry/opentelemetry-proto](https://github.com/open-telemetry/opentelemetry-proto/tree/main/opentelemetry/proto)
+ OpenTelemetry数据流 [Collector Data Flow Dashboard | OpenTelemetry](https://opentelemetry.io/docs/demo/collector-data-flow-dashboard/)
+ OpenTelemetry标准client的exporter配置 [Configuration | OpenTelemetry](https://opentelemetry.io/docs/collector/configuration/#exporters)
+ OpenTelemetry的零代码注入Python用例说明 [Python zero-code instrumentation | OpenTelemetry](https://opentelemetry.io/docs/zero-code/python/)
+ OpenTelemetry的Java场景用例说明，注意，该场景分为纯Java项目的Agent插桩与SpringBoot条件下的starter插桩 [Java zero-code instrumentation | OpenTelemetry](https://opentelemetry.io/docs/zero-code/java/)



### 代码示例

所有基础引导可以在源码和配置中找到，没有多余的文件，所有内容都是必须的。如果有其他问题请参考上文中指出的文档。

Python版本用例基于Python 3.8.20编写，Java版本基于GraalVM Jdk 21.0.6编写。

+ Python用例  [zorathos-otel-export-example/zorathos-log-python-example at main · zorathos/zorathos-otel-export-example](https://github.com/zorathos/zorathos-otel-export-example/tree/main/zorathos-log-python-example)

+ Java用例

  在引入合适依赖的前提下，Java场景支持Graal Native Image编译

  + SpringBoot [zorathos-otel-export-example/zorathos-log-springboot-example at main · zorathos/zorathos-otel-export-example](https://github.com/zorathos/zorathos-otel-export-example/tree/main/zorathos-log-springboot-example)

    使用SpringBoot标准支持的Logback框架编写

  + Java Agent [zorathos-otel-export-example/zorathos-log-java-agent-example at main · zorathos/zorathos-otel-export-example](https://github.com/zorathos/zorathos-otel-export-example/tree/main/zorathos-log-java-agent-example)

    使用Log4j2框架编写并支持迁移到Logback

所有示例将被Mirror到实验室服务器Gitee，您也可以在 [zorathos / zorathos-otel-export-example · GitLab](http://10.68.115.112:8929/zorathos/zorathos-otel-export-example) 上浏览本项目

实际效果

![image-20250309132419357](https://raw.githubusercontent.com/WangMinan/Pics/main/image-20250309132419357.png)

![image-20250309132441283](https://raw.githubusercontent.com/WangMinan/Pics/main/image-20250309132441283.png)