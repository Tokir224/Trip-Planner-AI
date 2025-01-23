var submitButton;

$(document).ready(function () {

    submitButton = $('#location-form').find('button[type="submit"]')

    $(window).on('pageshow', function () {
        if (submitButton.prop('disabled')) {
            submitButton.prop('disabled', false);
            submitButton.html('Generate');
        }
    });

    $('#location-form').on('submit', function () {
        submitButton = $(this).find('button[type="submit"]');
        submitButton.prop('disabled', true);
        submitButton.html('<span class="loader"></span>');
    });

    $('.marquee-link').on('click', function (e) {
        e.preventDefault();
        const selectedLocation = $(this).text();
        $('#location').val(selectedLocation);
    });

    var dateToday = new Date();
    var dates = $("#start_date, #end_date").datepicker({
        defaultDate: "",
        changeMonth: true,
        numberOfMonths: 1,
        minDate: dateToday,
        onSelect: function (selectedDate) {
            var option = this.id == "start_date" ? "minDate" : "maxDate",
                instance = $(this).data("datepicker"),
                date = $.datepicker.parseDate(instance.settings.dateFormat || $.datepicker._defaults.dateFormat, selectedDate, instance.settings);

            dates.not(this).datepicker("option", option, date);
        }
    });


});