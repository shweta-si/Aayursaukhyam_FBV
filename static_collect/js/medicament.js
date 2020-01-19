$(document).ready(function() {
	
	/* FOR MEDICAMENT */
	$('#id_drug_form').on('change', function(event) {
		var drug_form = $('#id_drug_form').val();
		console.log("ssss000"+drug_form);
        $.ajax({
	        	type : "GET",
	            url : "/get_dose_unit",
	            datType : "JSON",
	            data : {
	              	drug_form : drug_form,
	              	},
        		cache : false,
				}).done(function(data) {
        	     $('#id_dose_unit').empty();
	             	var opt = $('<option />');
	            	opt.attr('selected');
	            	opt.val('');
	            	opt.text('---------');
	            	$('#id_dose_unit').append(opt);
	
	            	$.each(data, function(key, value) {
	                	var opt = $('<option />');
	                	// here we're creating a new select option for each group
	               		opt.val(value.id);
	                	opt.text(value.name);
	                	$('#id_dose_unit').append(opt);
	            	});
        		});// done closes here
	});
	
	
});//document.ready close