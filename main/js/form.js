$(document).ready(function () {
    $("form").submit(function (event) {
      var formData = {
        name: $("#name").val(),
        email: $("#email").val(),
        superheroAlias: $("#superheroAlias").val(),
      };
      console.log("a")
      $.ajax({
        type: "GET",
        url: "http://127.0.0.1:2901/home",
        data: formData,
        contentType : "application/json",
        dataType: "json",
        encode: true,
      }).done(function(data) {
        console.log(data);
      });
  
      event.preventDefault();
    });
  });