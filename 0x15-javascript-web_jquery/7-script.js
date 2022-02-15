const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
$.get(url, (data, status) => {
  if (status === "success") {
    $("#character").text(data.name);
  }
});
