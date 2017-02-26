<?php
	exec('python ../../cgi-bin/trackReport.cgi',$output);
	$data = json_decode($output[0],true);
	if(empty($data)){
		echo '';
		return;
	}
	$html = '<table><tr><th>TrackingId</th><th>Location</th><th>From</th><th>To</th></tr>';
	foreach($data as $record){
		$html .= '<tr><td>'.$record['TransactionId'].'</td><td>'.$record['CurrentLocation'].'</td><td>'.$record['From'].'</td><td>'.$record['To'].'</td></tr>';
	}
	$html .='</table>';
	echo $html;
?>