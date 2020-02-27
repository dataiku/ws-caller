# ws-caller

Tool to connect N client(s) to a websocket endpoint behaving according to a predefined scenario.

## Quick start

```
pipenv sync
pipenv run ws-caller -c 1 --path "/websocket" -p 8000 --scenario PRINT_RECEIVED_MESSAGES
```

## Use case

This tool has been successfully used to reproduce the Jetty bug https://bugs.eclipse.org/bugs/show_bug.cgi?id=433262 using the scenario *CLOSE_IMMEDIATELY*.
