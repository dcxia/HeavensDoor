$folder = "delta\delta monthly analysis"

$initialFilePath  = "C:\Users\Daniel Lu\Desktop\STAND HACK\Twitter\delta\deltaair-2014-1.csv"
$directory = "C:\Users\Daniel Lu\desktop\stand hack\twitter\$folder"
$initial = Import-Csv -Path $initialFilePath | select tweet_ID,timestamp, text



get-childitem -path $directory -force|forEach-object {
    write-host($_)
    $q = Import-CSV -Path "$directory\$_" | select tweet_ID,timestamp, text
    $initial = $initial + $q
}
$initial|export-csv -path "C:\Users\Daniel Lu\desktop\stand hack\twitter\RedditDelta.csv" -delimiter "|"