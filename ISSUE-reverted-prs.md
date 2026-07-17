# Reverted PRs requiring rework: #155 and #158

## Summary




PR 170
The kept literal leaves the account id and region inline, exactly as the existing Resource guard does - the lambda branch returns before reaching the account/region format(...) substitution that other arn types get. Letting these fall through to that substitution would be the nicer end state, but it would also change the Resource, wildcard and cross-region cases, so I've kept it out of this fix. Happy to follow up if you want it.


