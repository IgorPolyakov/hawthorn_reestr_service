function status() {
  $('.badge').each(function(i, ele) {
    var val = $(ele).text();
    if (val === "ошибка") {
      $(ele).addClass('badge-danger');
    }
    if (val === "готово") {
      $(ele).addClass('badge-success');
    }
    if (val === "в обработке") {
      $(ele).addClass('badge-warning');
    }
  })
}

$(status);
$(document).on("turbolinks:load", status);
