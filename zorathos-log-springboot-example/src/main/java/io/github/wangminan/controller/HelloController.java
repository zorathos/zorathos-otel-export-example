package io.github.wangminan.controller;

import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.metrics.Meter;
import io.opentelemetry.api.trace.Tracer;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author : [wangminan]
 * @description : 测试用controller
 */
@RestController
@Slf4j
public class HelloController {
    // 可以在下文中调用
    private final Tracer tracer;
    private final Meter meter;

    /**
     * 自动装配的opentelemetry对象
     * @param openTelemetry opentelemetry对象
     */
    public HelloController(OpenTelemetry openTelemetry) {
        this.tracer = openTelemetry.getTracer("log-test-springboot");
        this.meter = openTelemetry.getMeter("log-test-springboot");
    }

    @GetMapping("/hello")
    public String hello() {
        log.info("hello otel with springboot!");
        return "hello";
    }
}
