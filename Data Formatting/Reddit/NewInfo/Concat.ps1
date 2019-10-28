$folderName = "del"
$FilePath  = "C:\Users\Daniel Lu\desktop\stand hack\reddit\NewInfo\$folderName"
$initialFilePath = "$FilePath\airlines.csv"
$initial = Import-Csv -Path $initialFilePath | select created,title, body
$directory = "$FilePath\Delta"


get-childitem -path $directory -force|forEach-object {
    write-host($_)
    $q = Import-CSV -Path "$directory\$_" | select created,title, body
    $initial = $initial + $q
}
$initial|export-csv -path "C:\Users\Daniel Lu\desktop\stand hack\reddit\NewInfo\DeltaReddit.csv" -delimiter "|"