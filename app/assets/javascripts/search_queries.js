function status() {
  $('.badge').each(function(i, ele) {
    let val = $(ele).text();

    // if value like this - 0/0
    if (val.match(/\d+\/\d+/ig)) {
      let result = val.split('/');
      if (result[0] === result[1]) {
        $(ele).addClass('badge-success');
      } else {
        $(ele).addClass('badge-warning');
      }
    }
    // else color status
    else {
      if (val === "ошибка") {
        $(ele).addClass('badge-danger');
      }
      else if (val === "готово") {
        $(ele).addClass('badge-success');
      }
      else if (val === "в обработке") {
        $(ele).addClass('badge-warning');
      }
      else   {
        $(ele).addClass('badge-danger');
      }
    }
  })
}

$(status);
$(document).on("turbolinks:load", status);