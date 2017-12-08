$(document).ready(function() {
  $.each($('span.top-words'), function () {
    var size = parseInt($(this).data('size')) + 10;
    $(this).css('font-size', size + 'px');
  });
})