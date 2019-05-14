<?php

include_once('./php_python.php');

class complex {
	var $real;
	var $imag;	
}

for($i=1;$i<=3;$i++){
  for($j = 1;$j<=3;$j++){
     for($k = 1;$k<=3;$k++){
        $ary = [1,$i,$j,$k,$j,$i];

        $res= ppython("essay::sfft",$ary);
		echo implode(',',$ary)." ".json_encode($res)."\n";

     }
  }

}

?>
