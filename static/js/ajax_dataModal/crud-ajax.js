$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType: 'json',

			beforeSend: function(){
			    $('#dataModal').modal('show');
			},
			success: function(data, jqXHR){
				$('#dataModal .modal-content').html(data.html_form);

			}
			
		});
	};


	var SaveForm =  function(){
		var form = $(this);

		var fd = new FormData(this);
		$.ajax({
			url: form.attr('data-url'),

			//data: form.serialize(),
            data: fd,
			type: form.attr('method'),
			dataType: 'json',
			enctype: 'multipart/form-data',

            //cache: false,
            processData: false,
            contentType: false,

			success: function(data, jqXHR){
				if(data.form_is_valid){
				    $('#dataTable tbody').html(data.data_list);
					$('#dataModal').modal('hide');
                    $('#dataTable tbody').html(data.data_list);
					//$('#dataModal').ajax.reload();
				} else {
					$('#dataModal .modal-content').html(data.html_form)
				}
			}

		});
		return false;
		
	};


// create 
$(".show-form").click(ShowForm);
$("#dataModal").on("submit",".create-form",SaveForm);

//update
$('#dataTable').on("click",".show-form-update",ShowForm);
$('#dataModal').on("submit",".update-form",SaveForm)

//delete
$('#dataTable').on("click",".show-form-delete",ShowForm);
$('#dataModal').on("submit",".delete-form",SaveForm)
});