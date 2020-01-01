//$("#Search").click(function () {
//        var xh = $('#izabranaZgrada').val();
//        var table = $('#tableKorisnik').DataTable();
//        table.search(xh).draw();
//    })
    $(document).ready(function(){
		$("#myInput").on("keyup", function(){
			var value = $(this).val().toLowerCase();
				$("#dataTable tbody tr").filter(function(){
				$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
				});

		});
	});