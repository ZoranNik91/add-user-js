<?php


if(count($argv)<4){
    die("Invalid number of arguments. Three expected (username, email, password)");
}

$user = "admin";
$password = "admin";
$db = new PDO('mysql:host=localhost;dbname=jpp-sql',$user,$password);

$data = [
    'username' => $argv[1],
    'email' => $argv[2],
    'password' => $argv[3],
];
$sql = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
$stmt= $db->prepare($sql);
$stmt->execute($data);
$stmt->closeCursor();
$db = null;
