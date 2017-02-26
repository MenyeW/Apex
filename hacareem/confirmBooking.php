<?php
	exec('python ../../cgi-bin/insertTransaction.cgi '.$_POST['ClientID'].' '.$_POST['src'].' '.$_POST['dst'].' '.$_POST['cost'],$output);
	echo json_encode(array('status'=>'success'));
?>