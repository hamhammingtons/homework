$systemObject = Get-ChildItem -Path "C:\" -Filter "hiberfil.sys" -Force

$systemObject.DirectoryName # or we can do .Directory for full name 