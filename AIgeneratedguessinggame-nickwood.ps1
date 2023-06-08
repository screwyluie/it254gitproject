$min = 0
$max = 100
$attempts = 0
Write-Host "Guess a random number from 0 to 99"
while ($true) {
  $guess = Read-Host "Enter your guess:"
  if ([int]$guess -eq $max) {
    Write-Host "Congratulations! You win!"
    exit
  } elseif([int]$guess -ge $min && [int]$guess -lt $max) {
    Write-Host "Your guess is too high."
  } else {
    Write-Host "Your guess is too low."
  }
  $attempts++
}