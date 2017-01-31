<?php

require __DIR__ . '/vendor/autoload.php';
require __DIR__ . '/NextpertiseAPI/init.php';

class MyZipcode {
    
    private $client = null;
    private $provider_mapper = array(
        'KPNWBA' => 'KPN (wba)',
        'KPNWEAS' => 'KPN (weas)',
        'EUROFIBER' => 'EuroFiber',
        'TELE2' => 'Tele2',
    );
    private $technology_mapper = array(
        'ADSL' => 'Zakelijke ADSL',
        'VDSL' => 'Zakelijke VDSL',
        'SDSL' => 'Zakelijke SDSL',
        'SDSL.bis' => 'Zakelijke SDSL.bis',
        'Fiber' => 'Zakelijke Glasvezel',
    );
    
    function __construct($username, $password, $testing = false) {
        $this->client = new NextpertiseAPI\BasicBroadband($username, $password, $testing);
    }
    
    function zipcode($zipcode, $housenr, $housenrext = '') {
        $ret = $this->client->zipcode($zipcode, $housenr, $housenrext);
        foreach($ret['available'] as $provider => $technologies) {
            foreach($ret['available'][$provider] as $technology => $attributes) {
                // Add max_upload_str/max_download_str in readable string format
                $ret['available'][$provider][$technology]['max_upload_str'] = $this->_Kb2Str($ret['available'][$provider][$technology]['max_upload']);
                $ret['available'][$provider][$technology]['max_download_str'] = $this->_Kb2Str($ret['available'][$provider][$technology]['max_download']);
                // Update technology type with mapped technology type
                if(isset($this->technology_mapper[$technology])) {
                    $ret['available'][$provider] = $this->_change_key($ret['available'][$provider], $technology, $this->technology_mapper[$technology]);   
                }
            }
            // Update provider with mapped provider
            if(isset($this->provider_mapper[$provider])) {            
                $ret['available'] = $this->_change_key($ret['available'], $provider, $this->provider_mapper[$provider]);
            }
        }
        return $ret;   
    }
    
    function _change_key($array, $old_key, $new_key) {
        if( ! array_key_exists( $old_key, $array ) )
            return $array;
    
        $keys = array_keys($array);
        $keys[array_search($old_key, $keys)] = $new_key;
    
        return array_combine($keys, $array);
    }
    
    function _Kb2Str($val) {
        if($val < 1024)
            return sprintf('%d Kb', $val);
        if($val < 1000000)
            return sprintf('%d Mb', round($val / 1024) );
        return sprintf('%d Gb', round($val / 1024 / 1024) );
    }
}

$zipcodeHandler = new MyZipcode('USERNAME HERE', 'PASSWORD HERE');
$result = $zipcodeHandler->zipcode('1000AA', 1);
print_r($result);