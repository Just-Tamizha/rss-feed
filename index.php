<?php
    header("Access-Control-Allow-Origin:*");
    // Check if the 'url' query parameter is set
    if(isset($_GET['url'])) {
        // Get the URL of the XML feed from the 'url' query parameter
        $xmlFeedUrl = $_GET['url'];

        // Load the XML feed with the SimpleXML extension
        $xmlFeed = simplexml_load_file($xmlFeedUrl);

        // Convert the XML feed to JSON
        $json = json_encode($xmlFeed);

        // Set the Content-Type header to application/json
        header('Content-Type: application/json');

        // Output the JSON
        echo $json;
    } else {
        // If the 'url' query parameter is not set, return an error message
        echo 'Error: No URL specified';
    }
?>
