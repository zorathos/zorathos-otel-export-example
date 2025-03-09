"""
运行如下命令以安装环境
python version 3.8.20
conda create -n zorathos-log-python-example
conda activate zorathos-log-python-example
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install


运行以下命令来测试这个example
Linux:
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_EXPORTER_OTLP_INSECURE=true
opentelemetry-instrument \
  --traces_exporter console,otlp \
  --metrics_exporter console,otlp \
  --logs_exporter console,otlp \
  --service_name python-logs-example \
  --exporter_otlp_endpoint 10.68.115.112:50051 \
  python log-example.py

Windows:
set OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
set OTEL_EXPORTER_OTLP_INSECURE=true
opentelemetry-instrument ^
  --traces_exporter console,otlp ^
  --metrics_exporter console,otlp ^
  --logs_exporter console,otlp ^
  --service_name python-logs-example ^
  --exporter_otlp_endpoint 10.68.115.112:50051 ^
  python log-example.py
"""

# logging 用于记录日志消息，trace 来自 opentelemetry 包，用于追踪功能。
import logging

from opentelemetry import trace

# 接下来，从追踪器提供者获取一个追踪器对象。通过调用 get_tracer 方法并传入模块的 __name__，创建一个特定于此模块的追踪器。
# 该name表示的是serviceName 上传到arktouros后默认在default的namespace下
tracer = trace.get_tracer_provider().get_tracer(__name__)

# 一条带span的日志信息 理论上也可以直接log，因为有serviceName传进来了
# Trace context correlation
with tracer.start_as_current_span("foo"):
    # Do something
    current_span = trace.get_current_span()
    current_span.add_event("This is a span event")
    logging.getLogger().error("This is a log message")
