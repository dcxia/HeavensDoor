$initialFilePath  = "C:\Users\Daniel Lu\desktop\stand hack\reddit\airlines.csv"
$initial = Import-Csv -Path $initialFilePath | select id,title, body
$directory = "C:\Users\Daniel Lu\desktop\stand hack\Reddit\Seperate"



get-childitem -path $directory -force|forEach-object {
    write-host($_)
    $q = Import-CSV -Path "$directory\$_" | select id,title, body
    $initial = $initial + $q
}
$initial|export-csv -path "C:\Users\Daniel Lu\desktop\stand hack\reddit\reddit.csv" -delimiter "|"