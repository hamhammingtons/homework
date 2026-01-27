Set-StrictMode -Version latest

$fileNames = "C:\Users\Admin\OneDrive\Рабочий стол\Python, tasks done by me\howework_for_itstep\libraries\powershel_lol\FolderNames.txt"
$folderPath = "C:\Users\Admin\OneDrive\Рабочий стол\Python, tasks done by me\howework_for_itstep\libraries\powershel_lol\Share"

$data = Get-Content -Path $fileNames

#New-Item -Path $folderPath -Name $data[0] -ItemType Directory
#New-Item -Path $folderPath -Name $data[1] -ItemType Directory
# Manual way ^ 

# if you want to check if a path exists 

#if((Test-Path -Path "$folderPath[0]/$($data)") -eq $false){
    #add item... 
# }else{
    #Write-Output "Already exists"
# }


foreach($name in $data){ 
    if(-not(Test-Path -Path "$folderPath/$name")){
        New-Item -Path $folderPath -Name $name -ItemType Directory
    } else {
        Write-Host "Folder '$name' already exists!" -ForegroundColor Yellow
    }
}

# like a for loop but the syntax is different
# python: for i in ... but here we do foreach($iter in $...)

$fileNames | ForEach-Object -Process {
    if(-not(Test-Path -Path "$folderPath/$_")){
        New-Item -Path $folderPath -Name $_ -ItemType Directory
    } else {
        Write-Host "Folder '$name' already exists!" -ForegroundColor Yellow
    }
}

$data.ForEach( # BEST METHOD!!!
    {
        if(-not(Test-Path -Path "$folderPath/$_")){
            New-Item -Path $folderPath -Name $_ -ItemType Directory
        } else {
            Write-Host "Folder '$name' already exists!" -ForegroundColor Yellow
        }
    }
)


$filtered = $data | ? { $_ -like "k*" }
# ? == where object
$filtered