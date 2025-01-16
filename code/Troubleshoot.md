## Finding changes in plan2.json
```
cat plan2.json | jq '. | select(.change.action=="update")'
```
```
cat plan2.json | jq '. | select(.change.action=="update")."@message"'
```

## Errors:

```
cat plan2.json | jq '. | select(."@level"=="error")'
```