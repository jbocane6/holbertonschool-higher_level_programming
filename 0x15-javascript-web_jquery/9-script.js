const url = "https://fourtonfish.com/hellosalut/?lang=fr";
$.get(url, (data, status) => {
  if (status === "success") {
    $("#hello").text(data.hello);
  }
});
