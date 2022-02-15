function translate(lang) {
  const url = "https://www.fourtonfish.com/hellosalut/?lang=";
  $.get(`${url}${lang}`, (data, status) => {
    $("#hello").text(data.hello);
  });
}

$(document).ready(() => {
  $("#btn_translate").on("click", () => {
    const lang = $("#language_code").val();
    translate(lang);
  });
});
