<html>
	<head>
		<title>
			Team Apex - Make Commerce Happen
		</title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	</head>
	<body>
		<h1>
			Client Interface - Query for a new delivery
		</h1>
		<table>
			<tr>
				<td> Client Id : </td>
				<td> <input name="clientId" type="text" /> </td>
			</tr>
			<tr>
				<td> Source : </td>
				<td> <input name="sourceCity" type="text" /></td>
			</tr>
			<tr>
				<td> Destination : </td>
				<td> <input name="destinationCity" type="text"/></td>
			</tr>
		</table>
		<input id="querySubmit" type="button" value="Query" />
		<hr/>
		<h1>
			Track All Active Items
		</h1>
		<input id="getTrackReport" type="button" value="Get Report"/>
		<div id="reportData"></div>
		<hr/>
		<h1>
			Mark Item Recieved
		</h1>
		<table>
			<tr>
				<td> Transaction ID : </td>
				<td> <input name="recievedTransactionId" type="text"/></td>
			</tr>
			<tr>
				<td> Recieved Location : </td>
				<td> <input name="recievedLocation" type="text"/></td>
			</tr>
		</table>
		<input type="button" value="Mark Recieved" id="recievedButton" />
	</body>
</html>
<script type="text/javascript">
	$("#querySubmit").on("click",function(){
		var sourceCity = $("[name='sourceCity']").val();
		var destinationCity = $("[name='destinationCity']").val();
		$.ajax({
			url : 'queryCalculator.php',
			method : 'POST',
			data : {'sourceCity' : sourceCity, 'destinationCity' : destinationCity},
			success : function(response){
				response = JSON.parse(response);
				var check = confirm("The cost of this delivery is : "+response.cost);
				if(check){
					$.ajax({
						url : 'confirmBooking.php',
						method : 'POST',
						data : {'ClientID' : $("[name='clientId']").val(), 'src' : sourceCity, 'dst' : destinationCity,'cost':response.cost},
						success : function(response){
							response = JSON.parse(response);
							if(response.status == "success"){
								alert("Booking Confirmed.");
							}else{
								alert("Booking Failed. Reason : "+response.errorMsg);
							}
						}
					});
				}
			}
		});
	});
	$("#getTrackReport").on("click",function(){
		$.ajax({
			url : 'trackReport.php',
			method : 'GET',
			success: function(response){
				$("#reportData").html(response);
			}
		})
	});
	$("#recievedButton").on("click",function(){
		$.ajax({
			url : 'packageRecieved.php',
			method:'POST',
			data : {'transactionId':$("[name='recievedTransactionId']").val(),'location':$("[name='recievedLocation']").val()},
			success: function(response){
				response = JSON.parse(response);
				if(response.status=="success"){
					alert("Item Reception Noted!");
				}else{
					alert("Item Reception Failed! Reason : "+response.errorMsg);
				}
			}
		});
	});
</script>