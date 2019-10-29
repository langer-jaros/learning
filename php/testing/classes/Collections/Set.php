<?php

class Set extends Bag {

    public function add($item) {
        if (!parent::contains($item))
            parent::add($item);
    }
}
