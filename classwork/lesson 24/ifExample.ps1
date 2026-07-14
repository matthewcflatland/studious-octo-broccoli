Set-Location C:\temp

if (Test-Path -Path new_folder) {
    <# Action to perform if the condition is true #>
    mkdir if_folder
}
if(Test-Path -Path if_folder){
    mkdir hyperionDev
}
else{
    mkdir new-projects
}