<?php
$servername = "mariadb103.websupport.sk;port=3313";
$username = "drinks";
$password = "ADD_PASS";

try {
    $conn = new PDO("mysql:host=$servername;dbname=drinks;charset=UTF8", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    // echo "Connected successfully";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

if (is_numeric($_GET["recommender"])) {
    $id = pg_escape_string(($_GET["recommender"]));
    $query = $conn->prepare("UPDATE recommenders SET points = points + 1 WHERE recommender_id = {$id}");
    $query->execute();

    $query = $conn->prepare('SELECT recommender_name, points FROM recommenders');
    $query->execute();
    $result = $query->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode(($result));
}

?>