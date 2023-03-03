<?php
// Set the API endpoint URL and API key
$url = 'https://pokemon-go1.p.rapidapi.com/pokemon_types.json';
$api_key = 'f2d5a52a87msh1e4c81a743db401p10c2b8jsn0f0035f00a93';

// Set up the CURL request
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'X-RapidAPI-Host: pokemon-go1.p.rapidapi.com',
    'X-RapidAPI-Key: ' . $api_key
]);

// Execute the request and decode the JSON response
$response = curl_exec($ch);
$data = json_decode($response, true);

// Output the data as an HTML table
echo '<table>';
echo '<thead><tr><th>Name</th><th>Type</th></tr></thead>';
echo '<tbody>';
for ($i = 0; $i < 10; $i++) {
    $pokemon = $data[$i];
    echo '<tr><td>' . $pokemon['pokemon_name'] . '</td><td>' . $pokemon['type'] . '</td></tr>';
}
echo '</tbody>';
echo '</table>';

// Close the CURL request
curl_close($ch);
?>