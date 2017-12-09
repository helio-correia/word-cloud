$(document).ready(function() {
  $.each($('span.top-words'), function () {
    var size = parseInt($(this).data('size')) + 10;
    $(this).css('font-size', size + 'px');
  });

  $('form.login-form').on('submit', function (e) {
    var errorField = $('.non_field_errors');

    e.preventDefault();

    $.post('/api-token-auth/', $(this).serializeArray())
        .done(function (data) {
          localStorage.token = data.token;
          window.location.replace("/admin/");
        })
        .fail(function(response) {
          errorField.empty().hide();
          $('.form-error').remove();

          $.each(JSON.parse(response.responseText), function(field, message) {
            if (field === 'non_field_errors') {
              $('<p></p>', {text: message}).appendTo(errorField);
              errorField.show();
            } else {
              $('<span></span>', {
                class: 'form-error is-visible',
                text: message
              }).insertAfter($('input[name="' + field + '"]'));
            }
          });
        });
  });

  $('.button-logout').on('click', function () {
    localStorage.clear();
    window.location.replace("/login/");
  })

  if ($('.admin-page').length) {
    $.ajax({
      type: 'GET',
      url: '/words/',
      beforeSend: function (xhr) {
        if (localStorage.token) {
          xhr.setRequestHeader("Authorization", "Bearer " + localStorage.token);
        } else {
          window.location.replace("/login/");
        }
      },
      success: function (data) {
        $('.admin-page').removeClass('hide');
        data.map(function(item) {
          var content = "<tr><td>" + item.name + "</td><td>" + item.count + "</td></tr>"
          $('tbody.words-list').append(content);
        })
      },
      error: function () {
        window.location.replace("/login/");
      }
    });
  }
})