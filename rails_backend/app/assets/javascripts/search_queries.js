function status() {
  $('.badge').each(function(i, ele) {
    let val = $(ele).text();
    if (val === "ошибка") {
      $(ele).addClass('badge-danger');
    }
    else if (val === "готово") {
      $(ele).addClass('badge-success');
    }
    else if (val === "в обработке") {
      $(ele).addClass('badge-warning');
    }
    let result = val.split('/');
    if (result[0] === result[1]) {
      $(ele).addClass('badge-success');
    } else if (val.match(/\d+\/\d+/ig)) {
      $(ele).addClass('badge-warning');
    }
  })
}

$(status);
$(document).on("turbolinks:load", status);
