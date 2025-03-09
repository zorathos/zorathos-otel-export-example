@echo off
REM opentelemetry-javaagent.jar needs to be downloaded from https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases, version 2.13.3
java -javaagent:.\opentelemetry-javaagent.jar ^
     -Dotel.service.name=log-java-agent-example ^
     -Dotel.exporter.otlp.protocol=grpc ^
     -Dotel.exporter.otlp.endpoint=http://10.68.115.112:50051 ^
     -Dotel.logs.exporter=otlp ^
     -Dotel.metrics.exporter=otlp ^
     -Dotel.traces.exporter=otlp ^
     -jar ..\target\zorathos-log-java-agent-example-0.0.1.jar
