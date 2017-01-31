<?php 

namespace NextpertiseAPI;

use JsonRPC\Client;

class ApiBase {
    
    private $client = NULL;
    private $username = NULL;
    private $password = NULL;
    private $endpoint = NULL;
    private $prod_url = 'https://api.nextpertise.nl';
    private $test_url = 'https://api.nextpertise.nl/test';
    private $testing = NULL;

    function __construct($endpoint, $username, $password, $testing = false) {
        $this->endpoint = $endpoint;
        $this->username = $username;
        $this->password = $password;
        $this->testing = $testing;
        $this->connect();
    }
    
    function connect() {
        $url = $this->testing ? $this->test_url : $this->prod_url;
        $this->client = new Client($url . '/' . $this->endpoint);
        $this->client->getHttpClient()
            ->withUsername($this->username)
            ->withPassword($this->password)
            ->withTimeout(360);
    }
    
    function __call($name, $arguments) {
        set_time_limit(360);
        if(isset($arguments) && is_array($arguments)) {
            if(isset($arguments[0]) && is_array($arguments[0])) {
                return $this->client->execute($name, $arguments[0]);       
            }
        }
        throw new Exception('Invalid argument');
    }
}