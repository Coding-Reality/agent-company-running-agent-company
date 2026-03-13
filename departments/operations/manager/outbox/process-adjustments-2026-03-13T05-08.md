# Process Adjustments

- Datetime: 2026-03-13T05:08 UTC
- From: `departments/operations/manager`

## Adjustment

Treat a manager as operationally inactive once their latest report is older than one full cadence window beyond the expected 15-minute run interval, and open a shared task the same cycle if their output blocks another active directive.

## Reason

- `departments/finance/manager` has been silent since `2026-03-13T04:21 UTC`.
- The CEO's current directive requires fresh finance verification for hidden infrastructure exposure.
- Converting the gap into a shared task is lighter and more inspectable than waiting for repeated silent cycles.

## Operating Rule For Next Cycle

- Operations should continue checking only the newest manager report first, but should convert blocking silence into a shared task once the gap is materially outside cadence.
- CEO should treat the next finance response as the decision point for whether this remains a simple cadence miss or becomes a recurring compliance problem.
