<?php
	$command = 'python ../../cgi-bin/packageRecieved.cgi '.$_POST['transactionId'].' '.$_POST['location'];
	exec($command,$out);
	echo json_encode(array('status'=>'success'));
?>