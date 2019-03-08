# alertmanager-opsgenie-proxy

Provides the ability to customize alert messages to be more OpsGenie friendly, such as enabling alias customization

# install & dependencies

You will need:
- Python >3.5,
- sanic module https://github.com/huge-success/sanic
- requests module

## install instructions

1. `git clone github.com/pawadski/alertmanager-opsgenie-proxy`
2. `cd alertmanager-opsgenie-proxy`
3. `python3.5 proxy.py`

## configure Alertmanager

You will need to point Alertmanager at the proxy instead of OpsGenie API:

```
receivers:
- name: opsgenie
  opsgenie_configs:
  - api_key: "put_api_key_here"
    api_url: "http://127.0.0.1:9095"
    send_resolved: true
```

## configure alerts

tl;dr - all annotation fields that begin with "opsgenie_" are converted to actually be sent to opsgenie, so an annotation `opsgenie_alias` is sent to OpsGenie as `alias`

Example:

```
groups:
- name: monitoring
  interval: 5s
  rules:
  - alert: IOWait5minAvgOver35
    expr: monitoring_stat_cpu_current_iowait_percent >= 0
    labels:
      service: monitoring
      severity: critical
    annotations:
      opsgenie_description: '{{ $labels.instance }}: 5 minute average CPU IOWait is >35'
      opsgenie_alias: 'hello_this_is_an_alias'
```

In the above example, `opsgenie_description` and `opsgenie_alias` get passed to OpsGenie as themselves without the "opsgenie_" part.

# bugs

I don't know. Literally just made it.
