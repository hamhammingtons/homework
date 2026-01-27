# Forces errors to be "Terminating" so the catch block actually triggers
$ErrorActionPreference = "Stop"

try {
    Write-Host "--- Attempting Task ---" -ForegroundColor Cyan
    
    $path = "C:\NonExistentFolder\data.txt"
    # This will fail and jump immediately to 'catch'
    $content = Get-Content -Path $path 

    Write-Host "This line will NEVER run if the command above fails."
} 
catch [System.IO.FileNotFoundException] {
    # You can catch SPECIFIC types of errors (Optional)
    Write-Host "Error: The specific file was not found!" -ForegroundColor Red
}
catch {
    # The 'catch-all' block (Like 'except Exception:')
    # $_ represents the current Error Object
    Write-Host "An unexpected error occurred: $($_.Exception.Message)" -ForegroundColor Red
} 
finally {
    # This runs no matter what (Like 'finally' in Python)
    Write-Host "--- Cleaning up resources ---" -ForegroundColor Gray
}
