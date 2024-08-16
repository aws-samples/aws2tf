mydir=$(pwd)
mydir=$(echo $mydir | rev | cut -f-2 -d'/' | rev)
which jq &>/dev/null
if [[ $? -eq 0 ]]; then
    which trivy &>/dev/null
    if [[ $? -eq 0 ]]; then
        ver=$(trivy version | head -1 | cut -f2 -d':' | tr -d ' |.')
        ver=$(expr $ver + 0)
        if [[ $ver -ge 480 ]]; then
            echo "Generating trivy security report ...."
            echo "trivy security report" >security-report.txt
            echo "CRITICAL:" >>security-report.txt
            trivy fs --scanners misconfig . -s CRITICAL --format json -q | jq '.Results[].Misconfigurations' | grep -v null | jq '.[] | [.CauseMetadata.Resource, .Description, .References]' 2>/dev/null >>security-report.txt
            echo "HIGH:" >>security-report.txt
            trivy fs --scanners misconfig . -s HIGH --format json -q | jq '.Results[].Misconfigurations' | grep -v null | jq '.[] | [.CauseMetadata.Resource, .Description, .References]' 2>/dev/null >>security-report.txt
            echo "Trivy security report: $mydir/security-report.txt"
        else
            echo "Please upgrade trivy to version v0.48.0 or higher"
        fi
    else
        echo "trivy is not installed. skipping security report"
    fi
else
    echo "jq is not installed. skipping security report"
fi
