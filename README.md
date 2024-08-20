# 자동업데이트
git init
git add .
Get-Date -UFormat "%A %B/%d/%Y"
$Time = Get-Date
$Time.ToUniversalTime()
git commit -m $Time
git push
# 자동업데이트