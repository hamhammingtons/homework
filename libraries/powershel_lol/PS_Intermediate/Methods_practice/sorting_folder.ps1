function Sort-Folder {
    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    begin {
        Write-Host "Beginning script." -ForegroundColor Cyan
        # DONT FORGET
        $FileNaming = @{ # USE @ BEFORE {} BECAUSE IF YOU DONT DO THAT IT WILL ASSIGN IT AS A CODE BLOCK!!!!
            ".pdf"  = "documents"
            ".jpeg" = "images"
            ".jpg"  = "images"
        }
    }

    process {
        if (-not (Test-Path -Path $Path)) {
            Write-Warning "Incorrect path: $Path"
            return
        }

        $items = Get-ChildItem -Path $Path -File  # an array!!

        foreach ($_ in $items) {
            # Your index logic (This works!)
            $dotPart = $_.Name.LastIndexOf(".")
            
            if ($dotPart -ne -1) {
                $Extension = $_.Name.Substring($dotPart).ToLower()

                if ($Extension -in $FileNaming.Keys) {
                    $folderName = $FileNaming[$Extension]
                    
                    # Construct paths safely
                    $targetFolder = Join-Path -Path $Path -ChildPath $folderName
                    
                    # Create folder if it's missing!
                    if (-not (Test-Path $targetFolder)) {
                        New-Item -ItemType Directory -Path $targetFolder | Out-Null
                    }

                    # Move the actual file ($_) to the target folder
                    Move-Item -Path $_.FullName -Destination $targetFolder -Verbose
                } 
            }
            else {
                Write-Host "Extension not found for: $($_.Name)" -ForegroundColor Yellow
            }
        }
    }

    end {
        Write-Host "Completed script" -ForegroundColor Green
    }
}

$desktop = [System.Environment]::GetFolderPath('Desktop')
$myPath = Join-Path -Path $desktop -ChildPath # INSERT FILE HERE.

Sort-Folder -Path $myPath