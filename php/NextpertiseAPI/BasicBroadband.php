<?php
    
namespace NextpertiseAPI;

class BasicBroadband {
    
    private $client = null;
    
    function __construct($username, $password, $testing = false) {
        $this->client = new ApiBase('/broadband/basic/v1', $username, $password, $testing);
    }
    
    function zipcode($zipcode, $housenr, $housenrext = '') {
        return $this->client->zipcode(['zipcode' => $zipcode, 'housenr' => (int)$housenr, 'housenrext' => $housenrext]);
    }
}