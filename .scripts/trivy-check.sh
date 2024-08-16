mydir=`pwd`
mydir=`echo $mydir | rev | cut -f-2 -d'/' | rev`
which trivy &> /dev/null
if [[ $? -eq 0 ]]; then
    ver=$(trivy version | head -1 | cut -f2 -d':' | tr -d ' |.')
    ver=$(expr $ver + 0)
    if [[ $ver -ge 480 ]]; then
        echo "trivy security report" >security-report.txt
        echo "CRITICAL:" >>security-report.txt
        trivy fs --scanners misconfig . -s CRITICAL --format json -q | jq '.Results[].Misconfigurations' | grep -v null | jq '.[] | [.CauseMetadata.Resource, .Description, .References]' 2>/dev/null >>security-report.txt
        echo "HIGH:" >>security-report.txt
        trivy fs --scanners misconfig . -s HIGH --format json -q | jq '.Results[].Misconfigurations' | grep -v null | jq '.[] | [.CauseMetadata.Resource, .Description, .References]' 2>/dev/null >>security-report.txt
        echo "Trivy security report: $mydir/security-report.txt"
    else
        echo "Please upgrade trivy to version v0.48.0 or higher"
    fi
fi