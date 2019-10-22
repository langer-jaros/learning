<?php

class Bag {
    private $list = [];

    public function add($item) {
        $this->list[$item] = (isset($this->list[$item]))? ++$this->list[$item]: 1;
    }

    public function clear() {
        $this->list = [];
    }

    public function contains($item) {
        return array_key_exists($item, $this->list); 
    }

    public function elementSize($item) {
        return (isset($this->list[$item]))? $this->list[$item]: 0;
    }

    public function isEmpty() {
        return empty($this->list);
    }

    public function remove($item) {
        if (isset($this->list[$item]) && $this->list[$item] > 0)
            $this->list[$item]--;
        else
            unset($this->list[$item]);
    }

    public function size() {
        return array_sum($this->list);
    }
    public function pBag() {
        var_dump($this->list);
    }
}