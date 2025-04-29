<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $form_type = $_POST['form_type'];
    $name = $_POST['name'];
    $gender = $_POST['Gender'];
    $age = $_POST['Age'];
    $email = $_POST['Email'];
    $contact = $_POST['Contact'];
    $address = $_POST['Address'];
    $service = $_POST['service'];
    $date = $_POST['date'];
    $time = $_POST['time'];
    $homeMessage = isset($_POST['homeMessage']) ? $_POST['homeMessage'] : '';
    $message = isset($_POST['message']) ? $_POST['message'] : '';

    // Set recipient email address
    $to = "pbpainreliefhub@gmail.com";
    
    // Set email subject
    $subject = "New Appointment Booking from $name";
    
    // Compose email message
    $email_message = "
    <html>
    <head>
        <title>New Appointment Booking</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; }
            .details { margin: 20px 0; }
            .label { font-weight: bold; }
        </style>
    </head>
    <body>
        <h2>New Appointment Booking</h2>
        <div class='details'>
            <p><span class='label'>Name:</span> $name</p>
            <p><span class='label'>Gender:</span> $gender</p>
            <p><span class='label'>Age:</span> $age</p>
            <p><span class='label'>Email:</span> $email</p>
            <p><span class='label'>Contact Number:</span> $contact</p>
            <p><span class='label'>Address:</span> $address</p>
            <p><span class='label'>Service:</span> $service</p>
            <p><span class='label'>Preferred Date:</span> $date</p>
            <p><span class='label'>Preferred Time:</span> $time</p>
    ";

    if (!empty($homeMessage)) {
        $email_message .= "<p><span class='label'>Home Service Instructions:</span> $homeMessage</p>";
    }

    if (!empty($message)) {
        $email_message .= "<p><span class='label'>Additional Message:</span> $message</p>";
    }

    $email_message .= "
        </div>
    </body>
    </html>
    ";

    // Set email headers
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: $email" . "\r\n";
    $headers .= "Reply-To: $email" . "\r\n";

    // Send email
    if (mail($to, $subject, $email_message, $headers)) {
        // Email sent successfully
        header("Location: thank_you.html");
        exit();
    } else {
        // Email failed to send
        header("Location: error.html");
        exit();
    }
} else {
    // Not a POST request, redirect to home
    header("Location: Homepage.html");
    exit();
}
?>