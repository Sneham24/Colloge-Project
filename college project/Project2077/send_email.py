from __future__ import annotations

import html
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from flask import Flask, redirect, request, send_from_directory

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)


@app.get("/")
def home() -> object:
    return send_from_directory(BASE_DIR, "Homepage.html")


@app.get("/<path:filename>")
def serve_static(filename: str) -> object:
    return send_from_directory(BASE_DIR, filename)


@app.post("/send_email")
def send_email() -> object:
    form = request.form

    form_type = form.get("form_type", "")
    name = form.get("name", "")
    gender = form.get("Gender", "")
    age = form.get("Age", "")
    email = form.get("Email", "")
    contact = form.get("Contact", "")
    address = form.get("Address", "")
    service = form.get("service", "")
    date = form.get("date", "")
    time = form.get("time", "")
    home_message = form.get("homeMessage", "")
    message = form.get("message", "")

    recipient = "pbpainreliefhub@gmail.com"
    subject = f"New Appointment Booking from {name}"

    def esc(value: str) -> str:
        return html.escape(value or "")

    html_message = f"""
    <html>
    <head>
        <title>New Appointment Booking</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
            .details {{ margin: 20px 0; }}
            .label {{ font-weight: bold; }}
        </style>
    </head>
    <body>
        <h2>New Appointment Booking</h2>
        <div class='details'>
            <p><span class='label'>Form Type:</span> {esc(form_type)}</p>
            <p><span class='label'>Name:</span> {esc(name)}</p>
            <p><span class='label'>Gender:</span> {esc(gender)}</p>
            <p><span class='label'>Age:</span> {esc(age)}</p>
            <p><span class='label'>Email:</span> {esc(email)}</p>
            <p><span class='label'>Contact Number:</span> {esc(contact)}</p>
            <p><span class='label'>Address:</span> {esc(address)}</p>
            <p><span class='label'>Service:</span> {esc(service)}</p>
            <p><span class='label'>Preferred Date:</span> {esc(date)}</p>
            <p><span class='label'>Preferred Time:</span> {esc(time)}</p>
    """

    if home_message:
        html_message += f"<p><span class='label'>Home Service Instructions:</span> {esc(home_message)}</p>"

    if message:
        html_message += f"<p><span class='label'>Additional Message:</span> {esc(message)}</p>"

    html_message += """
        </div>
    </body>
    </html>
    """

    text_message = (
        "New Appointment Booking\n"
        f"Form Type: {form_type}\n"
        f"Name: {name}\n"
        f"Gender: {gender}\n"
        f"Age: {age}\n"
        f"Email: {email}\n"
        f"Contact Number: {contact}\n"
        f"Address: {address}\n"
        f"Service: {service}\n"
        f"Preferred Date: {date}\n"
        f"Preferred Time: {time}\n"
        f"Home Service Instructions: {home_message}\n"
        f"Additional Message: {message}\n"
    )

    smtp_host = os.getenv("SMTP_HOST", "")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    smtp_from = os.getenv("SMTP_FROM", "") or smtp_user or email

    if not smtp_host or not smtp_from:
        return redirect("/error.html")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_from
    msg["To"] = recipient
    if email:
        msg["Reply-To"] = email
    msg.set_content(text_message)
    msg.add_alternative(html_message, subtype="html")

    try:
        if smtp_port == 465:
            server: smtplib.SMTP = smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=20)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port, timeout=20)
        with server:
            server.ehlo()
            if smtp_port != 465:
                server.starttls()
                server.ehlo()
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        return redirect("/thank_you.html")
    except Exception:
        return redirect("/error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
