<?php
	exec("python ../../cgi-bin/getCostMatrix.cgi",$output);
	$costMatrix = json_decode($output[0],true);
	$source = $_POST['sourceCity'];
	$destination = $_POST['destinationCity'];
	$cost = $costMatrix[$source][$destination];
	echo json_encode(array('cost'=>$cost));
?>