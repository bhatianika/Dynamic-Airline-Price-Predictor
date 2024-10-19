// When the form is submitted, prevent default submission and handle with AJAX
/*$(document).ready(function () {
    $('#pricingForm').on('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting the default way

        // Serialize the form data
        var formData = $(this).serialize();

        // AJAX request to send form data to Flask's predict route
        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            success: function (response) {
                // Update the result div with the predicted price
                $('#result').html('<h2>Predicted Ticket Price: $' + response.predicted_price + '</h2>');
            },
            error: function () {
                // Handle error and display an error message
                $('#result').html('<h2>Error predicting the price. Please try again.</h2>');
            }
        });
    });
});

$(document).ready(function () {
    // Function to fetch prediction based on current form values
    function fetchPrediction() {
        var formData = $('#pricingForm').serialize(); // Serialize form data

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            success: function (response) {
                // Update the result div with the predicted price
                $('#result').html('<h2>Predicted Ticket Price: $' + response.predicted_price + '</h2>');
            },
            error: function () {
                $('#result').html('<h2>Error predicting the price. Please try again.</h2>');
            }
        });
    }

    // Attach event listeners to form inputs to update the prediction in real-time
    $('#days_left, #seasonality, #base_price').on('input', function () {
        fetchPrediction(); // Call the prediction function every time an input changes
    });
});

$('#days_left').on('input', function() {
    var daysLeft = $(this).val();
    if (daysLeft <= 0) {
        alert("Days left must be a positive number.");
        $(this).val(''); // Clear invalid input
    }
});

$('#seasonality').on('input', function() {
    var seasonality = $(this).val();
    if (seasonality < 0 || seasonality > 2) {
        alert("Seasonality must be between 0 and 2.");
        $(this).val(''); // Clear invalid input
    }
});*/

$(document).ready(function () {
    // Function to fetch prediction based on current form values
    function fetchPrediction() {
        var formData = $('#pricingForm').serialize(); // Serialize form data

        $.ajax({
            url: '/predict',
            type: 'POST',
            data: formData,
            success: function (response) {
                // Update the result div with the predicted price
                $('#result').html('<h2>Predicted Ticket Price: $' + response.predicted_price + '</h2>');
            },
            error: function () {
                $('#result').html('<h2>Error predicting the price. Please try again.</h2>');
            }
        });
    }

    // When the form is submitted, prevent default submission and handle with AJAX
    $('#pricingForm').on('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting the default way

        fetchPrediction(); // Fetch prediction on form submission
    });

    // Attach event listeners to form inputs to update the prediction in real-time
    $('#days_left, #seasonality, #base_price').on('input', function () {
        fetchPrediction(); // Call the prediction function every time an input changes
    });

    // Input validation for days_left
    $('#days_left').on('input', function() {
        var daysLeft = $(this).val();
        if (daysLeft <= 0) {
            alert("Days left must be a positive number.");
            $(this).val(''); // Clear invalid input
        }
    });

    // Input validation for seasonality
    $('#seasonality').on('input', function() {
        var seasonality = $(this).val();
        if (seasonality < 0 || seasonality > 2) {
            alert("Seasonality must be between 0 and 2.");
            $(this).val(''); // Clear invalid input
        }
    });
});
