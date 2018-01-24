$(function () {


  $("#notifications").click(function () {
    if ($(".popover").is(":visible")) {
      $("#notifications").popover('hide');
    }
    else {
      $("#notifications").popover('show');
      $.ajax({
        url: '/notifications/last/',
        beforeSend: function () {
          $(".popover-content").html("<div style='text-align:center'><img src='/static/img/loading.gif' /></div>");
          $("#notifications").removeClass("new-notifications");
        },
        success: function (data) {
          $(".popover-content").html(data);
        }
      });
    }
    return false;
  });
});
