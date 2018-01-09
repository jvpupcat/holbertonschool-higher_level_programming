#!/usr/bin/node
ajaxSetup({
  type: "GET",
  dataType: "jsonp",
  error: function(xhr) {
    if (xhr.status == "200") {
      alert("code: " + xhr.status);
    } else if (xhr.status == "404") {
      alert("code: " + xhr.status);
    } else {
      console.log("")
    }
  }
});
